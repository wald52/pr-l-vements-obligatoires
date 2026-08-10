"""Audit des doublons résiduels du jeu de données.

Le rapprochement de `reconcile.py` ne fusionne **jamais** deux lignes issues
d'une même source : une énumération officielle liste des lignes distinctes à
dessein (taxe foncière bâtie / non bâtie, fractions éditeurs / distributeurs de
la TST…). La contrepartie est qu'un doublon *interne* à une source y survit.

Ce module les fait remonter au lieu de les laisser invisibles. Il est appelé
par `report.py` et alimente une section de `docs/RAPPORT.md`.
"""

from __future__ import annotations

import itertools
import re
import unicodedata

from rapidfuzz import fuzz

# Qualificatifs qui distinguent deux prélèvements aux libellés voisins : si l'un
# les porte et pas l'autre, ce ne sont pas des doublons.
_DISTINCTIFS = re.compile(
    r"\b(non|additionnel|additionnelle|forfaitaire|regional|regionale|"
    r"departemental|departementale|communal|communale|incineres|decharge|"
    r"editeurs|distributeurs|bis|ter)\b"
)


def _cle(nom: str) -> str:
    text = unicodedata.normalize("NFD", nom.lower())
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", text)).strip()


def doublons_suspects(records, seuil: int = 90) -> list[dict]:
    """Paires de libellés très proches que la déduplication n'a pas fusionnées."""
    items = [(r, _cle(r.nom)) for r in records]
    suspects = []
    for (a, ka), (b, kb) in itertools.combinations(items, 2):
        score = fuzz.token_sort_ratio(ka, kb)
        if score < seuil:
            continue
        if set(_DISTINCTIFS.findall(ka)) ^ set(_DISTINCTIFS.findall(kb)):
            continue  # qualificatif distinctif présent d'un seul côté
        sources_a = {s.source_id for s in a.sources}
        sources_b = {s.source_id for s in b.sources}
        suspects.append({
            "score": score,
            "a": a.nom,
            "b": b.nom,
            "sources": sorted(sources_a | sources_b),
            "meme_source": sources_a == sources_b,
            "montants_egaux": (
                a.montant_eur is not None and a.montant_eur == b.montant_eur
            ),
        })
    suspects.sort(key=lambda d: (-d["montants_egaux"], -d["score"]))
    return suspects
