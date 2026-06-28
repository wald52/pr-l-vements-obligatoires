"""Étage 1 — Téléchargement des sources vers data/raw/ avec cache et checksums.

- Chaque source activée de sources.yaml est téléchargée vers
  data/raw/<id>.<ext>.
- Un manifeste (data/raw/_manifest.json) enregistre URL, sha256, taille, date.
- `--offline` : n'effectue aucun appel réseau, réutilise le cache existant.
- Une source en échec (réseau bloqué, 403…) est signalée mais n'interrompt
  pas le pipeline : les parsers travailleront sur ce qui est disponible.
"""

from __future__ import annotations

import hashlib
import json
import time
from datetime import datetime, timezone
from typing import Any

from .config import enabled_sources, load_sources
from .paths import RAW_DIR, ensure_dirs

MANIFEST = "_manifest.json"
_RETRY_DELAYS = (2, 4, 8, 16)  # backoff exponentiel (secondes)


def _sha256(path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def _download(url: str, dest, timeout: int = 60) -> None:
    """Télécharge `url` vers `dest` avec retries sur erreurs réseau.

    Ne réessaie PAS sur 403/407 (déni de politique d'egress) : on lève
    immédiatement pour le signaler à l'appelant.
    """
    import requests  # import tardif : permet d'importer le module sans requests
    from requests.exceptions import ProxyError

    last_exc: Exception | None = None
    for attempt, delay in enumerate((0, *_RETRY_DELAYS)):
        if delay:
            time.sleep(delay)
        try:
            resp = requests.get(url, timeout=timeout, stream=True)
            if resp.status_code in (403, 407):
                raise PermissionError(
                    f"HTTP {resp.status_code} (déni de politique d'egress) sur {url}"
                )
            resp.raise_for_status()
            with open(dest, "wb") as f:
                for chunk in resp.iter_content(1 << 16):
                    f.write(chunk)
            return
        except PermissionError:
            raise  # ne pas retenter sur un déni de politique
        except ProxyError as exc:
            # CONNECT refusé par le proxy d'egress (403/407 niveau tunnel) :
            # c'est un déni de politique, inutile de retenter.
            raise PermissionError(f"Proxy a refusé l'accès à {url} : {exc}") from exc
        except Exception as exc:  # noqa: BLE001 - on retente les erreurs réseau
            last_exc = exc
            continue
    raise RuntimeError(f"Échec du téléchargement après retries : {url}") from last_exc


def _ext_for(stype: str) -> str:
    return {
        "xlsx": "xlsx", "xls": "xls", "pdf": "pdf", "json": "json",
        "csv": "csv", "datagouv_dataset": "json",
    }.get(stype, "bin")


def fetch(offline: bool = False) -> dict[str, Any]:
    """Télécharge toutes les sources activées. Retourne le manifeste."""
    ensure_dirs()
    cfg = load_sources()
    manifest: dict[str, Any] = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "reference_year": cfg.get("reference_year"),
        "entries": {},
    }

    for src in enabled_sources(cfg):
        sid = src["id"]
        dest = RAW_DIR / f"{sid}.{_ext_for(src.get('type', 'bin'))}"
        entry: dict[str, Any] = {
            "url": src.get("url", ""),
            "type": src.get("type"),
            "role": src.get("role"),
        }

        if offline:
            if dest.exists():
                entry.update(status="cached", path=str(dest), sha256=_sha256(dest))
            else:
                entry.update(status="missing",
                             error="mode hors-ligne et aucun cache disponible")
            manifest["entries"][sid] = entry
            print(f"[fetch] {sid}: {entry['status']}")
            continue

        try:
            _download(src["url"], dest)
            entry.update(status="ok", path=str(dest), sha256=_sha256(dest),
                         bytes=dest.stat().st_size)
        except PermissionError as exc:
            entry.update(status="blocked", error=str(exc))
        except Exception as exc:  # noqa: BLE001
            entry.update(status="error", error=str(exc))

        manifest["entries"][sid] = entry
        print(f"[fetch] {sid}: {entry['status']}"
              + (f" — {entry.get('error')}" if entry.get("error") else ""))

    with open(RAW_DIR / MANIFEST, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    return manifest


def load_manifest() -> dict[str, Any]:
    path = RAW_DIR / MANIFEST
    if not path.exists():
        return {"entries": {}}
    with open(path, encoding="utf-8") as f:
        return json.load(f)
