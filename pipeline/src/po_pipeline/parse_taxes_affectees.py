"""Parser de la liste des taxes affectées (export JSON OpenDataSoft).

Deux structures sont gérées :

1. **Structure « propre »** (nos fixtures, et certains millésimes) : chaque
   objet porte des clés explicites (``intitule_de_la_taxe``, ``affectataire``,
   ``rendement_2022``…). Les montants y sont exprimés en **millions d'euros**.

2. **Structure « OpenDataSoft désalignée »** du jeu officiel
   ``plf2024-v-and-m-t1-liste-des-taxes-affectees`` : l'en-tête du fichier
   source a décalé les colonnes, qui se retrouvent nommées ``empty``,
   ``empty0``… L'intitulé de la taxe est en ``empty4``, le bénéficiaire en
   ``empty3``, la nature juridique du bénéficiaire dans
   ``nature_juridique_du_beneficiaire`` et les montants (en **euros**) dans
   ``empty5``/``empty8``/``empty11``.

On détecte la structure et on mappe en conséquence. Le secteur n'est
volontairement PAS renseigné pour ces lignes : faute de code ESA, elles
restent ``A_ARBITRER`` (arbitrage ligne à ligne), sauf si un override de
``decision_rules.yaml`` reconnaît leur libellé.
"""

from __future__ import annotations

import json
import re
from typing import Any

from .schema import Prelevement, Source, slugify

_NOM_KEYS = ["intitule", "libelle", "nom", "imposition", "denomination"]
_BENEF_KEYS = ["affectataire", "beneficiaire", "organisme", "operateur"]
_MONTANT_KEYS = ["rendement", "montant", "produit", "evaluation", "recette"]
_LEGAL_KEYS = ["texte", "reference", "article", "base_legale", "fondement"]

# Mots-clés permettant de reconnaître un intitulé de prélèvement (filtre anti-bruit
# pour la structure désalignée, où certaines lignes sont des totaux/agrégats).
_TAX_KW = re.compile(
    r"taxe|redevance|contribution|droit|imp[oô]t|pr[ée]l[èe]vement|cotisation|"
    r"accise|fraction|surtaxe|prime|versement",
    re.I,
)


def parse(path, reference_year: int | None = None) -> list[Prelevement]:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    rows = data["results"] if isinstance(data, dict) and "results" in data else data
    if not isinstance(rows, list) or not rows:
        return []

    misaligned = _is_misaligned(rows)
    records: list[Prelevement] = []
    seen: set[str] = set()
    for row in rows:
        fields = row.get("fields", row) if isinstance(row, dict) else {}
        rec = _from_misaligned(fields) if misaligned else _from_clean(fields)
        if rec is None:
            continue
        key = slugify(rec.nom)
        if key in seen:
            continue
        seen.add(key)
        rec.annee = reference_year
        records.append(rec)
    return records


def _is_misaligned(rows: list[Any]) -> bool:
    """Détecte la structure OpenDataSoft désalignée (présence de colonnes empty*)."""
    sample = rows[0] if isinstance(rows[0], dict) else {}
    fields = sample.get("fields", sample)
    return "empty4" in fields or sum(1 for k in fields if str(k).startswith("empty")) >= 5


# --- structure propre (fixtures, millésimes bien formés) ---------------------

def _from_clean(fields: dict[str, Any]) -> Prelevement | None:
    nom = _pick_str(fields, _NOM_KEYS)
    if not nom:
        return None
    return Prelevement(
        id=slugify(f"ta-{nom}"),
        nom=nom,
        categorie="taxe affectée",
        beneficiaire=_pick_str(fields, _BENEF_KEYS),
        base_legale=_pick_str(fields, _LEGAL_KEYS),
        montant_eur=_to_eur_millions(_pick(fields, _MONTANT_KEYS)),
        sources=[Source("taxes_affectees")],
    )


# --- structure OpenDataSoft désalignée (plf2024 V&M T1) ----------------------

def _from_misaligned(fields: dict[str, Any]) -> Prelevement | None:
    nom = fields.get("empty4")
    if not isinstance(nom, str) or len(nom.strip()) < 4 or not _TAX_KW.search(nom):
        return None
    nom = nom.strip()
    benef = fields.get("empty3")
    montant = next(
        (fields[k] for k in ("empty8", "empty5", "empty11")
         if isinstance(fields.get(k), (int, float)) and fields[k] > 0),
        None,
    )
    return Prelevement(
        id=slugify(f"ta-{nom}"),
        nom=nom,
        categorie="taxe affectée",
        beneficiaire=benef.strip() if isinstance(benef, str) else None,
        base_legale=_clean_str(fields.get("reference_juridique")),
        montant_eur=float(montant) if montant is not None else None,  # déjà en euros
        sources=[Source("taxes_affectees")],
    )


# --- helpers -----------------------------------------------------------------

def _pick(fields: dict[str, Any], keys: list[str]) -> Any:
    for k, v in fields.items():
        kn = re.sub(r"[^a-z]", "", str(k).lower())
        if any(key in kn for key in keys) and v not in (None, ""):
            return v
    return None


def _pick_str(fields: dict[str, Any], keys: list[str]) -> str | None:
    """Comme _pick mais n'accepte qu'une valeur textuelle (évite les indices numériques)."""
    for k, v in fields.items():
        kn = re.sub(r"[^a-z]", "", str(k).lower())
        if any(key in kn for key in keys) and isinstance(v, str) and v.strip():
            return v.strip()
    return None


def _clean_str(value: Any) -> str | None:
    return value.strip() if isinstance(value, str) and value.strip() else None


def _to_eur_millions(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        # Rendements exprimés en M€ dans la structure propre.
        return float(str(value).replace(" ", "").replace(",", ".")) * 1_000_000
    except ValueError:
        return None
