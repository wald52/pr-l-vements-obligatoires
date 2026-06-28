"""Lecture/écriture des artefacts interim et processed."""

from __future__ import annotations

import json
from typing import Iterable

from .paths import INTERIM_DIR
from .schema import Prelevement, Source


def write_interim(source_id: str, records: Iterable[Prelevement]) -> int:
    INTERIM_DIR.mkdir(parents=True, exist_ok=True)
    items = [r.to_dict() for r in records]
    path = INTERIM_DIR / f"{source_id}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
    return len(items)


def read_interim(source_id: str) -> list[Prelevement]:
    path = INTERIM_DIR / f"{source_id}.json"
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        items = json.load(f)
    return [_from_dict(d) for d in items]


def read_all_interim() -> list[Prelevement]:
    out: list[Prelevement] = []
    for path in sorted(INTERIM_DIR.glob("*.json")):
        with open(path, encoding="utf-8") as f:
            for d in json.load(f):
                out.append(_from_dict(d))
    return out


def _from_dict(d: dict) -> Prelevement:
    sources = [Source(**s) for s in d.get("sources", [])]
    d = {**d, "sources": sources}
    return Prelevement(**d)
