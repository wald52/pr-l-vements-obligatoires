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


# ---------------------------------------------------------------------------
# Contrôle plus fin : le rapprochement par enregistrement
# ---------------------------------------------------------------------------
# Le test ci-dessus compare les mots du libellé au *corpus entier* du jeu de
# données. Il laisse donc passer un prélèvement dont les mots existent, mais
# éparpillés sur plusieurs enregistrements différents. C'est exactement ce qui
# est arrivé à la « contribution spécifique sur les indemnités de rupture
# conventionnelle » : « indemnités » venait de la contribution sur les
# indemnités de mise à la retraite, « conventionnelle » de la contribution
# conventionnelle à la formation, et la ligne était absente du jeu de données
# tout en obtenant un score de 0,80. Un prélèvement de 774 M€ manquait sans que
# rien ne le signale.
#
# Le contrôle qui suit exige que les mots se retrouvent dans **un seul et même**
# enregistrement. Les libellés qui restent en dessous du seuil sont ceux que le
# jeu de données porte sous un autre nom ; ils sont listés nommément avec leur
# contrepartie, ce qui documente la divergence au lieu de la masquer.

SEUIL_PAR_ENREGISTREMENT = 0.5

VARIANTES = {
    "Prélèvement forfaitaire unique (PFU / « flat tax »)":
        "Prélèvements sur les revenus des capitaux mobiliers",
    "Contribution sur les eaux minérales naturelles":
        "Surtaxe sur les eaux minérales",
    "Cotisations aux caisses de prévoyance et de retraite du personnel ferroviaire":
        "Cotisations des régimes spéciaux",
    "Cotisations des organismes HLM et des SEM à la CGLLS":
        "Cotisation versée par les organismes HLM et les SEM",
    "Recettes de la mise aux enchères des quotas carbone affectées à l'ANAH":
        "Produit de la mise aux enchères des quotas d'émission",
    "Taxe sur les installations nucléaires de base relevant du secteur énergétique (TINB-E)":
        "Taxe sur les installations nucléaires de base - tarif de reconversion",
    "Fractions d'accise sur les énergies affectées aux opérateurs de service public de l'électricité et du gaz":
        "Fraction affectée du produit du relèvement du tarif de taxe intérieure de consommation",
    "Taxe sur les biens des industries mécaniques (TBIC)":
        "Taxes sur les biens des industries mécaniques, de la fonderie, de la soudure…",
    "Taxe sur les biens des industries des corps gras (TICG)":
        "Taxe sur les biens des industries des corps gras",
    "Cotisations assises sur les honoraires des commissaires aux comptes":
        "Contributions des commissaires aux comptes et des organismes de contrôle",
    "Produit de la vente des biens confisqués ; successions en déshérence ; contrats d'assurance-vie en déshérence":
        "Fraction des produits annuels de la vente de biens confisqués",
}


def _dataset_documents() -> list[str]:
    records = json.loads(
        (ROOT / "data" / "prelevements_obligatoires.json").read_text(encoding="utf-8")
    )
    return [
        _norm(" ".join([rec["nom"], rec.get("sigle") or ""] + (rec.get("aliases") or [])))
        for rec in records
    ]


def _meilleur_score(label: str, documents: list[str]) -> float | None:
    tokens = [t for t in _norm(label).split() if len(t) > 4 and t not in STOPWORDS]
    if len(tokens) < 2:
        return None
    return max(sum(1 for t in tokens if t in doc) / len(tokens) for doc in documents)


def _libelles_readme() -> list[tuple[str, str]]:
    entrees = [(f"§{n}", label) for n, label in _readme_entries()]
    return entrees + [("§5", label) for label in _readme_rejets()]


def test_chaque_prelevement_se_retrouve_dans_un_seul_enregistrement():
    documents = _dataset_documents()
    manquants = []
    for origine, label in _libelles_readme():
        plat = " ".join(label.split())
        if _norm(label).strip() in CHAPEAUX or plat in VARIANTES:
            continue
        score = _meilleur_score(label, documents)
        if score is not None and score < SEUIL_PAR_ENREGISTREMENT:
            manquants.append(f"{origine} — {plat} (score {score:.2f})")
    assert not manquants, (
        "Prélèvements du README dont les mots ne se retrouvent dans aucun "
        "enregistrement unique de data/ :\n  - " + "\n  - ".join(manquants)
        + "\n\nSoit la ligne manque (l'ajouter à pipeline/seed/supplement.csv), "
          "soit le jeu de données la porte sous un autre nom (la déclarer dans "
          "VARIANTES avec sa contrepartie)."
    )


def test_les_variantes_declarees_sont_toujours_utiles():
    """Une variante dont le libellé a été aligné doit sortir de la liste."""
    documents = _dataset_documents()
    libelles = {" ".join(label.split()) for _, label in _libelles_readme()}
    inutiles = []
    for readme_label in VARIANTES:
        if readme_label not in libelles:
            inutiles.append(f"{readme_label} — absent du README")
            continue
        score = _meilleur_score(readme_label, documents)
        if score is not None and score >= SEUIL_PAR_ENREGISTREMENT:
            inutiles.append(f"{readme_label} — passe désormais le contrôle")
    assert not inutiles, "Entrées de VARIANTES devenues inutiles :\n  - " + "\n  - ".join(inutiles)
