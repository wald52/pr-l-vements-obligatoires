"""Parser de la liste des taxes affectées (export JSON OpenDataSoft).

L'export v2.1 `/exports/json` renvoie une liste d'objets (un par taxe) ;
l'API `/records` renvoie {"results": [...]}. On gère les deux formes et on
repère les champs par mots-clés car les noms de colonnes varient.
"""

from __future__ import annotations

import json
import re
from typing import Any

from .schema import Prelevement, Source, slugify

_NOM_KEYS = ["intitule", "libelle", "nom", "imposition", "taxe", "denomination"]
_BENEF_KEYS = ["affectataire", "beneficiaire", "organisme", "operateur"]
_MONTANT_KEYS = ["rendement", "montant", "produit", "evaluation", "recette"]
_LEGAL_KEYS = ["texte", "reference", "article", "base_legale", "fondement"]


def parse(path, reference_year: int | None = None) -> list[Prelevement]:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    rows = data["results"] if isinstance(data, dict) and "results" in data else data
    if not isinstance(rows, list):
        return []

    records: list[Prelevement] = []
    for row in rows:
        fields = row.get("fields", row) if isinstance(row, dict) else {}
        nom = _pick(fields, _NOM_KEYS)
        if not nom:
            continue
        records.append(Prelevement(
            id=slugify(f"ta-{nom}"),
            nom=str(nom).strip(),
            categorie="taxe affectée",
            beneficiaire=_pick(fields, _BENEF_KEYS),
            base_legale=_pick(fields, _LEGAL_KEYS),
            montant_eur=_to_eur(_pick(fields, _MONTANT_KEYS)),
            annee=reference_year,
            sources=[Source("taxes_affectees")],
        ))
    return records


def _pick(fields: dict[str, Any], keys: list[str]) -> Any:
    for k, v in fields.items():
        kn = re.sub(r"[^a-z]", "", str(k).lower())
        if any(key in kn for key in keys) and v not in (None, ""):
            return v
    return None


def _to_eur(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        # Les rendements des taxes affectées sont usuellement en M€.
        return float(str(value).replace(" ", "").replace(",", ".")) * 1_000_000
    except ValueError:
        return None
