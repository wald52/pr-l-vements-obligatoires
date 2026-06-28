"""Schéma canonique d'un prélèvement candidat + utilitaires de normalisation.

Une ligne du jeu de données final = un *candidat* prélèvement, qu'il soit
retenu (PRIS) ou rejeté (REJET) après application de la règle de décision.
Conserver les rejets est volontaire : c'est la trace auditable du raisonnement
(README §5).
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import asdict, dataclass, field
from typing import Any

# Catégories admises (cf. README §4).
CATEGORIES = {
    "impôt sur la production/importation",
    "impôt courant sur le revenu/patrimoine",
    "impôt en capital",
    "cotisation sociale",
    "cotisation sociale imputée",
    "fiscalité sociale",
    "impôt d'État",
    "impôt local",
    "taxe affectée",
    "ressource UE",
    "indéterminée",
}

STATUTS = {"PRIS", "REJET", "A_ARBITRER"}

# Codes ESA (SEC 2010) utilisés par la comptabilité nationale.
ESA_CODES = {"D2", "D5", "D91", "D61", "D611", "D612", "D613", "D2_D5", None}


@dataclass
class Source:
    """Provenance d'une donnée (traçabilité)."""

    source_id: str
    url: str = ""
    ref: str = ""  # référence interne à la source (n° de ligne, code, page…)


@dataclass
class Prelevement:
    """Enregistrement canonique d'un prélèvement candidat."""

    id: str
    nom: str
    sigle: str | None = None
    categorie: str = "indéterminée"
    esa_code: str | None = None
    beneficiaire: str | None = None  # entité (ex. URSSAF, communes, UE)
    secteur: str | None = None       # APUC / ODAC / APUL / ASSO / UE
    base_legale: str | None = None
    montant_eur: float | None = None  # en euros (pas en millions)
    annee: int | None = None
    statut: str = "A_ARBITRER"
    critere_echec: str | None = None  # None / C1 / C2 / C3 / sanction / supprime
    sources: list[Source] = field(default_factory=list)
    notes: str | None = None

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        return d


# --- Normalisation des libellés --------------------------------------------

def strip_accents(text: str) -> str:
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def normalize_label(text: str | None) -> str:
    """Minuscule, sans accents, espaces compactés — pour le matching."""
    if not text:
        return ""
    t = strip_accents(str(text)).lower()
    t = re.sub(r"[’`]", "'", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def slugify(text: str) -> str:
    """Identifiant stable à partir d'un libellé."""
    t = normalize_label(text)
    t = re.sub(r"[^a-z0-9]+", "-", t)
    return t.strip("-")[:80] or "sans-nom"


# --- Schéma JSON pour validation des sorties --------------------------------

JSON_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "array",
    "items": {
        "type": "object",
        "required": ["id", "nom", "categorie", "statut"],
        "properties": {
            "id": {"type": "string", "minLength": 1},
            "nom": {"type": "string", "minLength": 1},
            "sigle": {"type": ["string", "null"]},
            "categorie": {"type": "string", "enum": sorted(CATEGORIES)},
            "esa_code": {"type": ["string", "null"]},
            "beneficiaire": {"type": ["string", "null"]},
            "secteur": {"type": ["string", "null"]},
            "base_legale": {"type": ["string", "null"]},
            "montant_eur": {"type": ["number", "null"]},
            "annee": {"type": ["integer", "null"]},
            "statut": {"type": "string", "enum": sorted(STATUTS)},
            "critere_echec": {"type": ["string", "null"]},
            "sources": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["source_id"],
                    "properties": {
                        "source_id": {"type": "string"},
                        "url": {"type": "string"},
                        "ref": {"type": "string"},
                    },
                },
            },
            "notes": {"type": ["string", "null"]},
        },
    },
}

# Ordre des colonnes pour l'export CSV.
CSV_COLUMNS = [
    "id", "nom", "sigle", "categorie", "esa_code", "beneficiaire", "secteur",
    "base_legale", "montant_eur", "annee", "statut", "critere_echec", "notes",
    "source_ids",
]
