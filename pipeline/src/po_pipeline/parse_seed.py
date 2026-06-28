"""Parser du socle curé issu du README (pipeline/seed/readme_inventory.csv).

Ce socle rend la connaissance déjà vérifiée du README (§4 PRIS, §5 REJET)
directement exploitable par le pipeline. Il garantit un jeu de données
significatif et vérifié même hors-ligne ; les sources officielles
(Eurostat NTL, V&M Tome I…) l'étendent ensuite à l'exhaustivité ligne à ligne.
"""

from __future__ import annotations

import csv

from .paths import PIPELINE_DIR
from .schema import Prelevement, Source, slugify

SEED_PATH = PIPELINE_DIR / "seed" / "readme_inventory.csv"


def parse(path=None, reference_year: int | None = None) -> list[Prelevement]:
    path = path or SEED_PATH
    if not path.exists():
        return []
    records: list[Prelevement] = []
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            nom = (row.get("nom") or "").strip()
            if not nom:
                continue
            records.append(Prelevement(
                id=slugify(f"seed-{nom}"),
                nom=nom,
                sigle=_clean(row.get("sigle")),
                categorie=(row.get("categorie") or "indéterminée").strip() or "indéterminée",
                secteur=_clean(row.get("secteur")),
                base_legale=_clean(row.get("base_legale")),
                montant_eur=_mdeur_to_eur(row.get("montant_mdeur")),
                annee=(reference_year if _clean(row.get("montant_mdeur")) else None),
                statut=(row.get("statut") or "A_ARBITRER").strip() or "A_ARBITRER",
                critere_echec=_clean(row.get("critere_echec")),
                notes=_clean(row.get("notes")),
                sources=[Source("readme_seed", ref="README §4-§5")],
            ))
    return records


def _clean(value):
    if value is None:
        return None
    v = str(value).strip()
    return v or None


def _mdeur_to_eur(value):
    v = _clean(value)
    if not v:
        return None
    try:
        return float(v.replace(",", ".")) * 1_000_000_000
    except ValueError:
        return None
