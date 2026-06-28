"""Parser de la National Tax List Eurostat (épine dorsale, impôt par impôt).

La NTL détaillée est un classeur Excel où chaque ligne est une taxe ou une
cotisation, avec : un code ESA (D2/D5/D91/D61), un libellé, le secteur
bénéficiaire et un montant par année. Les en-têtes variant selon le millésime,
le parser repère les colonnes par mots-clés plutôt que par position fixe.
"""

from __future__ import annotations

import re
from typing import Any

from .schema import ESA_CODES, Prelevement, Source, slugify

# Mots-clés d'en-tête -> rôle logique de colonne.
_HEADER_HINTS = {
    "esa": ["esa", "sec", "code"],
    "nom": ["tax", "name", "title", "libell", "denomination", "list"],
    "secteur": ["sector", "secteur", "subsector", "receiving", "beneficiaire"],
}


def _norm(s: Any) -> str:
    return re.sub(r"\s+", " ", str(s or "").strip().lower())


def _canon_esa(value: Any) -> str | None:
    raw = re.sub(r"[^A-Za-z0-9]", "", str(value or "")).upper()
    if not raw:
        return None
    m = re.match(r"(D\d{1,3})", raw)
    code = m.group(1) if m else raw
    return code if code in {c for c in ESA_CODES if c} else (code or None)


def _find_columns(header: list[Any]) -> dict[str, int]:
    cols: dict[str, int] = {}
    for idx, cell in enumerate(header):
        h = _norm(cell)
        for role, hints in _HEADER_HINTS.items():
            if role in cols:
                continue
            if any(hint in h for hint in hints):
                cols[role] = idx
    return cols


def _year_columns(header: list[Any]) -> dict[int, int]:
    """Repère les colonnes dont l'en-tête est une année (ex. 2024)."""
    out: dict[int, int] = {}
    for idx, cell in enumerate(header):
        m = re.fullmatch(r"(19|20)\d{2}", str(cell).strip())
        if m:
            out[int(m.group(0))] = idx
    return out


def parse(path, reference_year: int | None = None) -> list[Prelevement]:
    """Parse l'Excel NTL. Tolérant : ignore les lignes non exploitables."""
    import openpyxl

    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    records: list[Prelevement] = []

    for ws in wb.worksheets:
        rows = list(ws.iter_rows(values_only=True))
        if not rows:
            continue
        # Cherche la ligne d'en-tête (celle qui contient le plus d'indices).
        header_idx, cols = _best_header(rows)
        if "nom" not in cols:
            continue
        years = _year_columns(list(rows[header_idx]))
        year_col = _pick_year_col(years, reference_year)

        for raw in rows[header_idx + 1:]:
            nom = raw[cols["nom"]] if cols["nom"] < len(raw) else None
            if not nom or not str(nom).strip():
                continue
            esa = _canon_esa(raw[cols["esa"]]) if "esa" in cols and cols["esa"] < len(raw) else None
            secteur = (str(raw[cols["secteur"]]).strip()
                       if "secteur" in cols and cols["secteur"] < len(raw)
                       and raw[cols["secteur"]] else None)
            montant = _to_eur(raw[year_col]) if year_col is not None and year_col < len(raw) else None

            records.append(Prelevement(
                id=slugify(f"eurostat-{nom}"),
                nom=str(nom).strip(),
                esa_code=esa,
                secteur=secteur,
                montant_eur=montant,
                annee=(reference_year if montant is not None else None),
                sources=[Source("eurostat_ntl", ref=f"{ws.title}")],
            ))
    wb.close()
    return records


def _best_header(rows: list[tuple]) -> tuple[int, dict[str, int]]:
    best_idx, best_cols = 0, {}
    for idx, row in enumerate(rows[:25]):  # l'en-tête est dans les 1res lignes
        cols = _find_columns(list(row))
        if len(cols) > len(best_cols):
            best_idx, best_cols = idx, cols
    return best_idx, best_cols


def _pick_year_col(years: dict[int, int], reference_year: int | None) -> int | None:
    if not years:
        return None
    if reference_year in years:
        return years[reference_year]
    return years[max(years)]  # année la plus récente disponible


def _to_eur(value: Any) -> float | None:
    """Convertit un montant Eurostat (millions d'euros) en euros."""
    if value is None or value == "":
        return None
    try:
        return float(str(value).replace(" ", "").replace(",", ".")) * 1_000_000
    except ValueError:
        return None
