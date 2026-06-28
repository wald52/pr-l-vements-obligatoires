"""Parser du Voies & Moyens Tome I (PDF) — énumération des impositions.

Le PDF contient des tableaux « numéro de ligne / intitulé de la recette /
évaluation ». On extrait, page par page, les tableaux via pdfplumber et on
retient les lignes ayant un intitulé non vide et, idéalement, un montant.

L'extraction PDF est intrinsèquement fragile : ce parser est défensif et
journalise ce qu'il ne sait pas exploiter plutôt que d'échouer.
"""

from __future__ import annotations

import re
from typing import Any

from .schema import Prelevement, Source, slugify

# Une ligne ressemble souvent à : "1101  Taxe sur la valeur ajoutée  204 000"
_AMOUNT_RE = re.compile(r"(-?\d[\d   ]*[\d])(?:\s*(?:M€|€|k€)?)?$")
_LINENO_RE = re.compile(r"^\d{3,4}$")


def parse(path, reference_year: int | None = None) -> list[Prelevement]:
    import pdfplumber

    records: list[Prelevement] = []
    seen: set[str] = set()

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            for table in page.extract_tables() or []:
                records.extend(_rows_from_table(table, reference_year, seen))
    return records


def _rows_from_table(table: list[list[Any]], year: int | None,
                     seen: set[str]) -> list[Prelevement]:
    out: list[Prelevement] = []
    for row in table:
        cells = [(_clean(c)) for c in row if c is not None]
        cells = [c for c in cells if c]
        if not cells:
            continue
        nom, lineno, montant = _interpret(cells)
        if not nom or len(nom) < 4:
            continue
        key = slugify(nom)
        if key in seen:
            continue
        seen.add(key)
        out.append(Prelevement(
            id=slugify(f"vm-{nom}"),
            nom=nom,
            montant_eur=montant,
            annee=(year if montant is not None else None),
            sources=[Source("vm_tome1", ref=(lineno or ""))],
        ))
    return out


def _interpret(cells: list[str]) -> tuple[str | None, str | None, float | None]:
    """Devine (intitulé, n° de ligne, montant) à partir des cellules."""
    lineno = None
    montant = None
    label_parts: list[str] = []

    for c in cells:
        if _LINENO_RE.fullmatch(c):
            lineno = c
            continue
        amt = _parse_amount(c)
        if amt is not None and not re.search(r"[a-zA-Zéèà]", c):
            montant = amt
            continue
        label_parts.append(c)

    nom = " ".join(label_parts).strip(" .-—") or None
    return nom, lineno, montant


def _clean(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value).replace("\n", " ")).strip()


def _parse_amount(text: str) -> float | None:
    t = text.strip()
    m = _AMOUNT_RE.search(t)
    if not m:
        return None
    digits = re.sub(r"[   ]", "", m.group(1))
    try:
        # Le V&M est exprimé en millions d'euros.
        return float(digits) * 1_000_000
    except ValueError:
        return None
