import json
from pathlib import Path

import pytest

from po_pipeline.schema import Prelevement, Source

ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture(scope="session")
def dataset_records() -> list[Prelevement]:
    """Le jeu de données versionné, relu tel qu'il est publié."""
    raw = json.loads(
        (ROOT / "data" / "prelevements_obligatoires.json").read_text(encoding="utf-8")
    )
    records = []
    for row in raw:
        row = dict(row)
        row["sources"] = [Source(**s) for s in row.get("sources", [])]
        records.append(Prelevement(**row))
    return records
