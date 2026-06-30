"""Étage 6 — Document de travail consolidé (docs/INVENTAIRE_TRAVAIL.md).

À partir du jeu de données réconcilié, génère un document *de travail* — par
opposition au RAPPORT.md synthétique — pensé pour poursuivre les recherches :

  * les prélèvements retenus, regroupés par secteur bénéficiaire ;
  * les candidats rejetés et leur motif ;
  * surtout, les lignes « à arbitrer » triées par source et par thème, avec
    repérage automatique des doublons probables d'un prélèvement déjà retenu
    (p. ex. « Foncier bâti » de la NTL ↔ « Taxe foncière… » du socle) ;
  * une liste de pistes et questions ouvertes pour la suite ;
  * le registre des sources et la commande de régénération.

C'est volontairement exhaustif (toutes les lignes y figurent) : le but est de
servir de plan de travail navigable, pas de résumé.
"""

from __future__ import annotations

import json
from collections import defaultdict
from datetime import date
from typing import Any

from rapidfuzz import fuzz

from .config import load_sources
from .paths import DATASET_DIR, DOCS_DIR, PROCESSED_DIR, ensure_dirs
from .schema import Prelevement, Source, normalize_label

OUT = "INVENTAIRE_TRAVAIL.md"

# Libellés lisibles + ordre d'affichage des secteurs bénéficiaires.
_SECTEURS = [
    ("ASSO", "Administrations de sécurité sociale (ASSO)"),
    ("APUC", "État et administrations centrales (APUC)"),
    ("ODAC", "Organismes divers d'administration centrale (ODAC)"),
    ("APUL", "Administrations publiques locales (APUL)"),
    ("UE", "Union européenne"),
    (None, "Secteur à préciser"),
]
_DUP_THRESHOLD = 82  # score rapidfuzz au-delà duquel on signale un doublon probable


# --------------------------------------------------------------------------- #
# Chargement
# --------------------------------------------------------------------------- #

def _load() -> tuple[list[Prelevement], dict[str, Any]]:
    with open(DATASET_DIR / "prelevements_obligatoires.json", encoding="utf-8") as f:
        items = json.load(f)
    records = [
        Prelevement(**{**d, "sources": [Source(**s) for s in d.get("sources", [])]})
        for d in items
    ]
    cov_path = PROCESSED_DIR / "coverage.json"
    cov = json.load(open(cov_path, encoding="utf-8")) if cov_path.exists() else {}
    return records, cov


# --------------------------------------------------------------------------- #
# Helpers de mise en forme
# --------------------------------------------------------------------------- #

def _md(eur: float | None) -> str:
    if not eur:
        return "—"
    return f"{eur / 1e9:,.2f}".replace(",", " ")


def _srcs(r: Prelevement) -> str:
    parts = []
    for s in r.sources:
        parts.append(f"{s.source_id}" + (f" ({s.ref})" if s.ref else ""))
    return "; ".join(parts)


def _esc(text: str | None) -> str:
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


def _anchor(label: str) -> str:
    return "".join(c for c in label.lower().replace(" ", "-") if c.isalnum() or c == "-")


# --------------------------------------------------------------------------- #
# Sections
# --------------------------------------------------------------------------- #

def _header(cov: dict[str, Any], n: int, ref_year: int | None) -> list[str]:
    return [
        "# Inventaire des prélèvements obligatoires — document de travail",
        "",
        f"> Généré le {date.today().isoformat()} par le pipeline "
        "(`po-pipeline workdoc`). **Ne pas éditer à la main** : relancer "
        "`make all` régénère ce document depuis les sources.",
        "",
        f"Ce document regroupe les **{n} prélèvements** de l'inventaire réconcilié "
        f"(année de référence {ref_year}). Il est conçu comme un **plan de travail** "
        "pour poursuivre les recherches : chaque ligne porte sa **provenance**, et "
        "les candidats incertains sont isolés et pré-triés.",
        "",
        "**Comment l'utiliser.** Traiter en priorité le §4 (« à arbitrer ») : "
        "commencer par le §4.1 (doublons probables à fusionner), puis instruire "
        "les taxes affectées (§4.3) et les nouvelles impositions (§4.4). Le §5 "
        "liste les questions ouvertes.",
        "",
    ]


def _toc() -> list[str]:
    items = [
        "1. [Synthèse](#1-synthèse)",
        "2. [Prélèvements retenus (PRIS)](#2-prélèvements-retenus-pris)",
        "3. [Candidats rejetés (REJET)](#3-candidats-rejetés-rejet)",
        "4. [À arbitrer — front de recherche](#4-à-arbitrer--front-de-recherche)",
        "5. [Pistes et questions ouvertes](#5-pistes-et-questions-ouvertes)",
        "6. [Registre des sources et régénération](#6-registre-des-sources-et-régénération)",
    ]
    return ["## Sommaire", "", *[f"{it}" for it in items], ""]


def _synthese(records: list[Prelevement], cov: dict[str, Any]) -> list[str]:
    by_stat = defaultdict(int)
    for r in records:
        by_stat[r.statut] += 1
    out = ["## 1. Synthèse", "",
           "| Indicateur | Valeur |", "|---|---:|",
           f"| Prélèvements au total | {len(records)} |",
           f"| Retenus (PRIS) | {by_stat['PRIS']} |",
           f"| Rejetés (REJET) | {by_stat['REJET']} |",
           f"| À arbitrer | {by_stat['A_ARBITRER']} |",
           f"| Somme des PRIS (socle curé) | {cov.get('somme_pris_socle_mdeur', '—')} Md€ |",
           f"| Somme des PRIS (itemisé, indicatif) | {cov.get('somme_pris_itemise_mdeur', '—')} Md€ |",
           f"| Enveloppe INSEE {cov.get('year', '')} | {cov.get('enveloppe_insee_mdeur', '—')} Md€ |",
           f"| Couverture (socle / INSEE) | {cov.get('couverture_pct', '—')} % |", ""]
    # Répartition par catégorie et par source.
    cat = defaultdict(int)
    src = defaultdict(int)
    for r in records:
        cat[r.categorie or "indéterminée"] += 1
        for s in r.sources:
            src[s.source_id] += 1
    out += ["### Répartition par catégorie", "", "| Catégorie | Nombre |", "|---|---:|"]
    out += [f"| {_esc(k)} | {v} |" for k, v in sorted(cat.items(), key=lambda x: -x[1])]
    out += ["", "### Présence par source (une ligne peut avoir plusieurs sources)", "",
            "| Source | Lignes |", "|---|---:|"]
    out += [f"| {k} | {v} |" for k, v in sorted(src.items(), key=lambda x: -x[1])]
    out += [""]
    return out


def _retenus(records: list[Prelevement]) -> list[str]:
    pris = [r for r in records if r.statut == "PRIS"]
    out = ["## 2. Prélèvements retenus (PRIS)", "",
           f"{len(pris)} prélèvements retenus, regroupés par secteur bénéficiaire "
           "et triés par montant décroissant.", ""]
    by_sec: dict[Any, list[Prelevement]] = defaultdict(list)
    for r in pris:
        by_sec[r.secteur if r.secteur in {s for s, _ in _SECTEURS} else None].append(r)
    for code, label in _SECTEURS:
        grp = by_sec.get(code, [])
        if not grp:
            continue
        total = sum(r.montant_eur or 0 for r in grp)
        out += [f"### {label} — {len(grp)} lignes, {_md(total)} Md€", "",
                "| Prélèvement | Sigle | Montant (Md€) | Base légale | Sources |",
                "|---|---|---:|---|---|"]
        for r in sorted(grp, key=lambda r: -(r.montant_eur or 0)):
            out.append(f"| {_esc(r.nom)} | {_esc(r.sigle)} | {_md(r.montant_eur)} "
                       f"| {_esc(r.base_legale)} | {_esc(_srcs(r))} |")
        out += [""]
    return out


def _rejetes(records: list[Prelevement]) -> list[str]:
    rej = [r for r in records if r.statut == "REJET"]
    out = ["## 3. Candidats rejetés (REJET)", "",
           f"{len(rej)} candidats écartés, avec le critère en échec "
           "(C1 versement effectif, C2 bénéficiaire APU/UE, C3 obligatoire et sans "
           "contrepartie).", "",
           "| Candidat | Critère | Note | Sources |", "|---|---|---|---|"]
    for r in sorted(rej, key=lambda r: (r.critere_echec or "")):
        out.append(f"| {_esc(r.nom)} | {_esc(r.critere_echec)} | {_esc(r.notes)} "
                   f"| {_esc(_srcs(r))} |")
    out += [""]
    return out


def _best_pris_match(rec: Prelevement, pris_keys: list[tuple[str, str]]) -> tuple[str, int]:
    """Renvoie (nom du PRIS le plus proche, score) pour repérer un doublon."""
    labels = [normalize_label(rec.nom)]
    if rec.sigle:
        labels.append(normalize_label(rec.sigle))
    best_nom, best = "", 0
    for nom, key in pris_keys:
        sc = max(int(fuzz.token_sort_ratio(l, key)) for l in labels)
        if sc > best:
            best_nom, best = nom, sc
    return best_nom, best


def _a_arbitrer(records: list[Prelevement]) -> list[str]:
    arb = [r for r in records if r.statut == "A_ARBITRER"]
    pris = [r for r in records if r.statut == "PRIS"]
    pris_keys = [(r.nom, normalize_label(r.nom)) for r in pris]
    pris_keys += [(r.nom, normalize_label(r.sigle)) for r in pris if r.sigle]

    # Repérage des doublons probables.
    dups, residual = [], []
    for r in arb:
        nom, score = _best_pris_match(r, pris_keys)
        if score >= _DUP_THRESHOLD:
            dups.append((r, nom, score))
        else:
            residual.append(r)

    out = ["## 4. À arbitrer — front de recherche", "",
           f"{len(arb)} lignes restent à classer. Elles sont pré-triées ci-dessous "
           "pour faciliter l'instruction.", ""]

    # 4.1 doublons probables
    out += ["### 4.1 Doublons probables d'un prélèvement déjà retenu", "",
            f"{len(dups)} lignes ressemblent fortement à un PRIS existant "
            "(rapprochement automatique) : à **fusionner** (ajuster un libellé "
            "dans le socle, ou un alias dans `reconcile`).", "",
            "| Ligne à arbitrer | Montant (Md€) | Ressemble au PRIS | Score | Source |",
            "|---|---:|---|---:|---|"]
    for r, nom, score in sorted(dups, key=lambda t: -t[2]):
        out.append(f"| {_esc(r.nom)} | {_md(r.montant_eur)} | {_esc(nom)} | {score} "
                   f"| {_esc(_srcs(r))} |")
    out += [""]

    # Le reste, par source dominante.
    def src_of(r: Prelevement) -> str:
        ids = [s.source_id for s in r.sources]
        for pref in ("vm_tome1", "eurostat_ntl", "taxes_affectees"):
            if pref in ids:
                return pref
        return ids[0] if ids else "?"

    buckets: dict[str, list[Prelevement]] = defaultdict(list)
    for r in residual:
        buckets[src_of(r)].append(r)

    # 4.2 NTL
    ntl = buckets.get("eurostat_ntl", [])
    out += ["### 4.2 Lignes Eurostat NTL à rattacher ou classer", "",
            f"{len(ntl)} taxes/contributions individuelles de la NTL (code ESA + "
            "montant officiel) sans correspondance directe : confirmer le statut "
            "et, le cas échéant, l'affecter à une rubrique.", "",
            "| Ligne | ESA | Montant (Md€) | Réf. | "]
    out += ["|---|---|---:|---|"]
    for r in sorted(ntl, key=lambda r: -(r.montant_eur or 0)):
        ref = r.sources[0].ref if r.sources else ""
        out.append(f"| {_esc(r.nom)} | {_esc(r.esa_code)} | {_md(r.montant_eur)} | {_esc(ref)} |")
    out += [""]

    # 4.3 taxes affectées
    ta = buckets.get("taxes_affectees", [])
    out += ["### 4.3 Taxes affectées à instruire", "",
            f"{len(ta)} taxes affectées (V&M Tome I) à confirmer comme PO et "
            "rattacher à un bénéficiaire. Triées par bénéficiaire.", "",
            "| Taxe affectée | Bénéficiaire | Montant (Md€) | Base légale |",
            "|---|---|---:|---|"]
    for r in sorted(ta, key=lambda r: ((r.beneficiaire or "~").lower(), -(r.montant_eur or 0))):
        out.append(f"| {_esc(r.nom)} | {_esc(r.beneficiaire)} | {_md(r.montant_eur)} "
                   f"| {_esc(r.base_legale)} |")
    out += [""]

    # 4.4 V&M
    vm = buckets.get("vm_tome1", [])
    out += ["### 4.4 Nouvelles impositions du V&M Tome I (lignes 1xxx) à classer", "",
            f"{len(vm)} impositions d'État détaillées au V&M, non encore présentes "
            "ailleurs : à qualifier (la plupart sont des PO d'État récents).", "",
            "| Imposition | Ligne budgétaire |", "|---|---|"]
    for r in sorted(vm, key=lambda r: (r.sources[0].ref if r.sources else "")):
        ref = r.sources[0].ref if r.sources else ""
        out.append(f"| {_esc(r.nom)} | {_esc(ref)} |")
    out += [""]
    return out


def _pistes(records: list[Prelevement], cov: dict[str, Any]) -> list[str]:
    n_dup = "voir §4.1"
    n_sans_montant = sum(1 for r in records if r.statut == "PRIS" and not r.montant_eur)
    return [
        "## 5. Pistes et questions ouvertes", "",
        "Chantiers identifiés pour la suite des recherches :", "",
        "1. **Doublons** : les correspondances de même périmètre (« Foncier bâti » "
        "↔ taxe foncière, « Mutations à titre gratuit » ↔ DMTG) sont désormais "
        "fusionnées via la colonne `alias` du socle. Les candidats résiduels du "
        "§4.1 sont des **composantes plus fines** (ex. accises ex-TICGN/TICFE) : à "
        "fusionner au cas par cas ou à conserver comme détail.",
        "2. **Classification ESA** : la correspondance par préfixe (D29→D2, "
        "D51→D5…) reclasse désormais automatiquement les lignes NTL ; les codes "
        "encore non couverts (cf. catégorie « indéterminée » au §1) restent à "
        "compléter dans `esa_defaults`.",
        f"3. **Montants manquants** : {n_sans_montant} PRIS sont sans montant ; les "
        "renseigner depuis la NTL fiabiliserait la couverture.",
        "4. **Base de mesure** : la couverture "
        f"({cov.get('couverture_pct', '—')} %) dépasse 100 % car les montants NTL "
        "sont en base Eurostat (~45,3 % du PIB) alors que l'enveloppe de contrôle "
        "est INSEE (42,7 %). Décider d'une base de référence unique pour le suivi.",
        "5. **Exhaustivité de l'État A** : le volume narratif du V&M ne détaille que "
        "les ~24 principaux impôts d'État ; les lignes mineures (1101→1799) sont "
        "agrégées (« Autres taxes », « Recettes diverses »). Si besoin, parser la "
        "table récapitulative formelle (État A) pour les ~300 lignes complètes.",
        "6. **Taxes affectées** (§4.3) : confirmer le périmètre PO de chacune "
        "(certaines redevances pour service rendu sont à exclure au titre de C3).",
        "",
    ]


def _sources_registre(cfg: dict[str, Any]) -> list[str]:
    out = ["## 6. Registre des sources et régénération", "",
           "| Source | Rôle | Activée | URL |", "|---|---|:--:|---|"]
    for s in cfg.get("sources", []):
        out.append(f"| {_esc(s.get('title', s.get('id')))} | {_esc(s.get('role'))} "
                   f"| {'✅' if s.get('enabled') else '—'} | {_esc(s.get('url'))} |")
    out += ["", "**Socle curé** : `pipeline/seed/readme_inventory.csv` (issu du "
            "README racine, toujours intégré).",
            "**Supplément curé** : `pipeline/seed/supplement.csv` — long tail de "
            "PO non détaillés par le README (composantes IFER/TGAP, taxes "
            "récentes du PLF 2026…), attestés par le CGI/CIBS et le V&M.", "",
            "**Régénérer ce document :**", "", "```bash",
            "cd pipeline && make all      # fetch → … → report → workdoc", "```", ""]
    return out


# --------------------------------------------------------------------------- #
# Point d'entrée
# --------------------------------------------------------------------------- #

def build() -> str:
    ensure_dirs()
    records, cov = _load()
    cfg = load_sources()
    ref_year = cfg.get("reference_year")

    lines: list[str] = []
    lines += _header(cov, len(records), ref_year)
    lines += _toc()
    lines += _synthese(records, cov)
    lines += _retenus(records)
    lines += _rejetes(records)
    lines += _a_arbitrer(records)
    lines += _pistes(records, cov)
    lines += _sources_registre(cfg)

    path = DOCS_DIR / OUT
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"[workdoc] écrit {path}")
    return str(path)
