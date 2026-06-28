"""Étage 3 — Classification : applique la règle de décision (README §2-§3).

Pour chaque enregistrement :
  1. classement par défaut selon le code ESA (esa_defaults) ;
  2. ajustement du secteur/critère C2 si le bénéficiaire est hors APU ;
  3. application du premier `override` dont les mots-clés matchent le libellé
     (priorité sur le défaut) — cas-limites du README §4-§5.

Un enregistrement sans code ESA ni override reste `A_ARBITRER` : il apparaîtra
dans la liste des lignes à arbitrer du rapport (transparence sur l'incertitude).
"""

from __future__ import annotations

from typing import Any

from .config import load_rules
from .io_utils import read_all_interim
from .schema import Prelevement, normalize_label


def _matches(label: str, rule: dict[str, Any]) -> bool:
    """Vrai si le libellé satisfait les conditions de l'override."""
    if "not_match" in rule and any(normalize_label(t) in label for t in rule["not_match"]):
        return False
    if "any" in rule and not any(normalize_label(t) in label for t in rule["any"]):
        return False
    if "match" in rule and not all(normalize_label(t) in label for t in rule["match"]):
        return False
    return "any" in rule or "match" in rule


def _apply_esa_default(rec: Prelevement, defaults: dict[str, Any]) -> None:
    code = rec.esa_code
    rule = defaults.get(code) if code else None
    if rule is None and code and code.startswith("D612"):
        rule = defaults.get("D612")
    if rule:
        rec.statut = rule.get("statut", rec.statut)
        if rule.get("critere_echec"):
            rec.critere_echec = rule["critere_echec"]
        if rec.categorie in (None, "indéterminée") and rule.get("categorie"):
            rec.categorie = rule["categorie"]


def _apply_sector_c2(rec: Prelevement, secteurs_apu: list[str]) -> None:
    """Si un secteur est renseigné et hors APU/UE => échec C2."""
    if not rec.secteur:
        return
    sect = rec.secteur.strip().upper()
    known = {s.upper() for s in secteurs_apu}
    # On ne déclasse que si le secteur est explicite et non reconnu.
    if sect and not any(k in sect or sect in k for k in known):
        if rec.statut == "PRIS":
            rec.statut, rec.critere_echec = "REJET", "C2"


def classify_records(records: list[Prelevement], rules: dict[str, Any]) -> list[Prelevement]:
    defaults = rules.get("esa_defaults", {})
    secteurs_apu = rules.get("secteurs_apu", [])
    overrides = rules.get("overrides", [])

    for rec in records:
        _apply_esa_default(rec, defaults)
        _apply_sector_c2(rec, secteurs_apu)

        label = normalize_label(rec.nom)
        for rule in overrides:
            if _matches(label, rule):
                rec.statut = rule.get("statut", rec.statut)
                rec.critere_echec = rule.get("critere_echec")
                if rule.get("note"):
                    rec.notes = rule["note"]
                break
    return records


def classify() -> list[Prelevement]:
    rules = load_rules()
    records = read_all_interim()
    return classify_records(records, rules)
