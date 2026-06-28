"""Étage 2 — Normalisation : exécute les parsers et produit data/interim/.

Chaque source brute disponible est confiée au parser adapté, qui produit des
enregistrements au schéma canonique (partiels) écrits dans interim/<id>.json.
Une source absente/bloquée est simplement ignorée avec un avertissement.
"""

from __future__ import annotations

from pathlib import Path

from . import parse_eurostat, parse_seed, parse_taxes_affectees, parse_vm_tome1
from .config import enabled_sources, load_sources
from .fetch import load_manifest
from .io_utils import write_interim
from .paths import RAW_DIR

# Dispatch : id de source -> fonction parse(path, reference_year).
PARSERS = {
    "eurostat_ntl": parse_eurostat.parse,
    "vm_tome1": parse_vm_tome1.parse,
    "taxes_affectees": parse_taxes_affectees.parse,
}


def _raw_path(sid: str, manifest: dict) -> Path | None:
    entry = manifest.get("entries", {}).get(sid, {})
    if entry.get("path") and Path(entry["path"]).exists():
        return Path(entry["path"])
    # repli : cherche un fichier raw/<id>.* (utile pour fixtures/tests)
    matches = sorted(RAW_DIR.glob(f"{sid}.*"))
    return matches[0] if matches else None


def normalize() -> dict[str, int]:
    cfg = load_sources()
    ref_year = cfg.get("reference_year")
    manifest = load_manifest()
    counts: dict[str, int] = {}

    # Le socle curé du README est toujours intégré (indépendant du réseau).
    seed_records = parse_seed.parse(reference_year=ref_year)
    if seed_records:
        counts["readme_seed"] = write_interim("readme_seed", seed_records)
        print(f"[normalize] readme_seed: {counts['readme_seed']} enregistrements")

    for src in enabled_sources(cfg):
        sid = src["id"]
        parser = PARSERS.get(sid)
        if parser is None:
            continue  # source de contrôle (ex. eurostat_taxag) : pas de parser
        path = _raw_path(sid, manifest)
        if path is None:
            print(f"[normalize] {sid}: source brute absente — ignorée")
            continue
        try:
            records = parser(path, ref_year)
        except Exception as exc:  # noqa: BLE001
            print(f"[normalize] {sid}: erreur de parsing — {exc}")
            continue
        counts[sid] = write_interim(sid, records)
        print(f"[normalize] {sid}: {counts[sid]} enregistrements")

    return counts
