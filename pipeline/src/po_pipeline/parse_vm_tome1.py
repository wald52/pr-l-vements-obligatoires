"""Parser du Voies & Moyens Tome I (PDF) — énumération des impositions.

Le volume « Évaluation des recettes » présente chaque recette sous forme d'un
paragraphe dont le **titre porte le numéro de ligne budgétaire** entre
parenthèses, p. ex. :

    Cotisation sur la valeur ajoutée des entreprises (ligne 1497)
    Taxe sur les petits colis (ligne 1442)

On extrait ces titres : ils constituent l'énumération officielle, ligne à
ligne, des impositions. On ne retient que les **recettes fiscales** (lignes
1xxx) — les impositions de toutes natures de l'État —, à l'exclusion des
recettes non fiscales (2xxx : dividendes, domaine, redevances pour service) et
des prélèvements sur recettes (3xxx : reversements aux collectivités et à l'UE).

Le numéro de ligne sert d'identifiant stable ; le libellé, parfois réparti sur
deux lignes de texte, est reconstruit en remontant les lignes précédentes. Les
montants ne sont volontairement pas extraits ici (ils figurent en clair dans la
prose, de façon trop ambiguë pour être fiables) : la valeur ajoutée de cette
source est l'**exhaustivité des intitulés**, les montants venant de la NTL
Eurostat et du socle curé.
"""

from __future__ import annotations

import re
from typing import Any

from .schema import Prelevement, Source, slugify

_HEAD_RE = re.compile(r"\(lignes?\s*(\d{3,4})\)")
_AMOUNT_RE = re.compile(r"(-?\d[\d   ]*[\d])(?:\s*(?:M€|€|k€)?)?$")
_LINENO_RE = re.compile(r"^\d{3,4}$")

# Lignes de texte à ne jamais agréger dans un libellé (en-têtes, intertitres).
_SECTION_RE = re.compile(
    r"^(annexe au plf|retour sur|la r[ée]vision|l[' ]?[ée]valuation|"
    r"analyse |pr[ée]vision |partie |chapitre |encadr[ée])",
    re.I,
)
_PAGEHDR_RE = re.compile(r"^\d{1,3}\s+annexe au plf", re.I)


def parse(path, reference_year: int | None = None) -> list[Prelevement]:
    import pdfplumber

    lines: list[str] = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            for ln in (page.extract_text() or "").split("\n"):
                lines.append(ln.strip())

    records: list[Prelevement] = []
    seen: set[str] = set()
    for i, ln in enumerate(lines):
        m = _HEAD_RE.search(ln)
        if not m:
            continue
        lineno = m.group(1)
        # On ne garde que les recettes fiscales (1xxx) : les impositions d'État.
        if not lineno.startswith("1"):
            continue
        if lineno in seen:
            continue
        nom = _reconstruct_name(lines, i, m.start())
        if not nom or len(nom) < 4:
            continue
        seen.add(lineno)
        records.append(Prelevement(
            id=slugify(f"vm-{lineno}-{nom}"),
            nom=nom,
            categorie="recette fiscale (État)",
            sources=[Source("vm_tome1", ref=f"ligne {lineno}")],
        ))
    return records


def _reconstruct_name(lines: list[str], i: int, start: int) -> str:
    """Reconstitue le libellé précédant « (ligne NNNN) », titre éventuellement
    réparti sur la ligne courante et la/les ligne(s) précédente(s)."""
    head = _strip_bullet(lines[i][:start].strip())
    parts: list[str] = [head] if head else []

    j = i - 1
    # Tant que le début du libellé semble incomplet (vide ou commençant en
    # minuscule), on remonte la ligne précédente, sauf si c'est un intertitre.
    while j >= 0 and _needs_more(parts):
        prev = lines[j].strip()
        if not prev or _is_section(prev):
            break
        parts.insert(0, _strip_bullet(prev))
        if prev[:1].isupper():  # une ligne commençant par une majuscule amorce le titre
            break
        j -= 1

    name = re.sub(r"\s+", " ", " ".join(p for p in parts if p)).strip(" .-—•")
    # Recolle les césures de fin de ligne (« reve- nus » -> « revenus ») sans
    # toucher aux traits d'union légitimes (« ex-TICPE », « infra-marginale »),
    # qui ne sont jamais suivis d'une espace.
    name = re.sub(r"(\w)-\s+(\w)", r"\1\2", name)
    return name


def _needs_more(parts: list[str]) -> bool:
    if not parts:
        return True
    first = parts[0]
    return not first or first[:1].islower() or len(" ".join(parts)) < 12


def _is_section(line: str) -> bool:
    if _SECTION_RE.match(line) or _PAGEHDR_RE.match(line):
        return True
    letters = [c for c in line if c.isalpha()]
    # Intertitre en capitales (ex. « RETOUR SUR 2024 »).
    return bool(letters) and sum(c.isupper() for c in letters) / len(letters) > 0.8


def _strip_bullet(text: str) -> str:
    return re.sub(r"^[•\-–—\s]+", "", text).strip()


# --- helpers conservés (compat. tests / usage tabulaire éventuel) ------------

def _interpret(cells: list[str]) -> tuple[str | None, str | None, float | None]:
    """Devine (intitulé, n° de ligne, montant) à partir de cellules tabulaires."""
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
    digits = re.sub(r"[   ]", "", m.group(1))
    try:
        return float(digits) * 1_000_000  # le V&M est exprimé en millions d'euros
    except ValueError:
        return None
