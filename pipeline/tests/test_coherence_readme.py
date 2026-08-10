"""Cohérence entre les deux formats du dépôt (règle n° 1 de CLAUDE.md).

Tout prélèvement nommé au §4 (retenus) **ou au §5** (rejetés) du README doit se
retrouver dans le jeu de données. Conserver les rejets est volontaire : c'est la
trace auditable du raisonnement, et un rejet absent des données est aussi
gênant qu'un prélèvement manquant — il laisse croire que le candidat n'a jamais
été examiné. Sans ce contrôle, les deux formats divergent silencieusement : c'est
exactement ce qui s'était produit sur treize entrées (quotas d'émission,
contribution FIPHFP, taxes de l'ANSM…).

Deux exceptions, explicites et justifiées :

* le **§4.7** recense les collectivités à autonomie fiscale, hors du territoire
  économique des comptes nationaux ; les y inclure fausserait la couverture
  (cf. `data/README.md`) — Saint-Martin, qui est dans le champ, y figure bien ;
* quelques entrées sont des **intitulés de rubrique** introduisant une
  sous-liste, et non des prélèvements : ils sont listés ci-dessous.
"""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Intitulés qui coiffent une sous-liste sans désigner eux-mêmes un prélèvement.
CHAPEAUX = {
    "taxes sur les navigations maritimes et fluviales",
    "taxes affectees a l anses",
    "ressources de l afitf",
}

STOPWORDS = set(
    "de la le les des du et en a au aux pour sur par ou d l dans une un "
    "taxe taxes autres nouvelle entree".split()
)


def _norm(value: str) -> str:
    text = unicodedata.normalize("NFD", str(value).lower())
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9 ]", " ", text)


def _dataset_corpus() -> str:
    records = json.loads(
        (ROOT / "data" / "prelevements_obligatoires.json").read_text(encoding="utf-8")
    )
    parts = []
    for rec in records:
        parts.append(rec["nom"])
        parts.append(rec.get("sigle") or "")
        parts.extend(rec.get("aliases") or [])
    return _norm(" | ".join(parts))


def _readme_rejets() -> list[str]:
    """Candidats rejetés du §5 : première cellule en gras de chaque ligne."""
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    section = text[text.index("## 5. Candidats"): text.index("## 6. Cas limites")]
    return [
        re.sub(r"\s*\(.*?\)\s*", " ", m.group(1)).strip()
        for m in re.finditer(r"^\| \*\*([^*]{8,120})\*\*", section, re.M)
    ]


def _readme_entries() -> list[tuple[str, str]]:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    section = text[text.index("## 4. Les prélèvements"): text.index("## 5. Candidats")]
    entries = []
    for block in re.split(r"\n### ", section)[1:]:
        number = block.split("\n")[0].split()[0]
        if number.startswith("4.7"):  # hors territoire économique
            continue
        for match in re.finditer(r"^- \*\*([^*]{8,110})\*\*", block, re.M):
            entries.append((number, match.group(1).strip()))
    return entries


def test_chaque_prelevement_du_readme_est_dans_le_jeu_de_donnees():
    corpus = _dataset_corpus()
    manquants = []
    for number, label in _readme_entries():
        if _norm(label).strip() in CHAPEAUX:
            continue
        tokens = [t for t in _norm(label).split() if len(t) > 4 and t not in STOPWORDS]
        if len(tokens) < 2:
            continue
        if sum(1 for t in tokens if t in corpus) / len(tokens) < 0.55:
            manquants.append(f"§{number} — {label}")
    assert not manquants, (
        "Prélèvements nommés au README §4 mais absents de data/ :\n  - "
        + "\n  - ".join(manquants)
        + "\n\nAjouter la ligne à pipeline/seed/supplement.csv puis régénérer "
          "(cf. CLAUDE.md, règle n° 1)."
    )


def test_les_chapeaux_declares_existent_toujours():
    """Garde-fou : un chapeau retiré du README doit sortir de la liste."""
    labels = {_norm(label).strip() for _, label in _readme_entries()}
    obsoletes = sorted(CHAPEAUX - labels)
    assert not obsoletes, f"Chapeaux déclarés mais absents du README : {obsoletes}"


def test_chaque_rejet_du_readme_est_dans_le_jeu_de_donnees():
    corpus = _dataset_corpus()
    manquants = []
    for label in _readme_rejets():
        tokens = [t for t in _norm(label).split() if len(t) > 4 and t not in STOPWORDS]
        if len(tokens) < 2:
            continue
        if sum(1 for t in tokens if t in corpus) / len(tokens) < 0.55:
            manquants.append(label)
    assert not manquants, (
        "Candidats rejetés au README §5 mais absents de data/ :\n  - "
        + "\n  - ".join(manquants)
        + "\n\nLes ajouter à pipeline/seed/supplement.csv avec statut REJET et le "
          "critère en échec (cf. CLAUDE.md, règle n° 1)."
    )
