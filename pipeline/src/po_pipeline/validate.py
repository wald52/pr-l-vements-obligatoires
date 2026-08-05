"""Validation du jeu de données final contre le schéma JSON."""

from __future__ import annotations

import json

from jsonschema import validate

from .paths import DATASET_DIR
from .schema import JSON_SCHEMA


def validate_dataset() -> int:
    path = DATASET_DIR / "prelevements_obligatoires.json"
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    validate(instance=data, schema=JSON_SCHEMA)
    print(f"[validate] OK — {len(data)} enregistrements conformes au schéma")
    return len(data)
