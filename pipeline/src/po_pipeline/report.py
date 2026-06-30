"""Étage 5 — Rapport : génère docs/RAPPORT.md à partir des sorties.

Le rapport restitue le décompte, les montants par catégorie et par bénéficiaire,
la couverture (preuve d'exhaustivité) et la liste des lignes restant à arbitrer.
"""

from __future__ import annotations

import json
from collections import defaultdict
from datetime import date
from typing import Any

from .paths import DATASET_DIR, DOCS_DIR, PROCESSED_DIR, ensure_dirs
from .schema import Prelevement, Source


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


def _mdeur(eur: float | None) -> str:
    if not eur:
        return "—"
    return f"{eur / 1e9:,.1f}".replace(",", " ")


def _table_by(records: list[Prelevement], attr: str, title: str) -> str:
    sums: dict[str, float] = defaultdict(float)
    counts: dict[str, int] = defaultdict(int)
    for r in records:
        if r.statut != "PRIS":
            continue
        key = getattr(r, attr) or "(non renseigné)"
        sums[key] += r.montant_eur or 0
        counts[key] += 1
    if not sums:
        return ""
    lines = [f"### {title}\n", f"| {attr.capitalize()} | Nombre | Montant (Md€) |",
             "|---|---:|---:|"]
    for key in sorted(sums, key=lambda k: -sums[k]):
        lines.append(f"| {key} | {counts[key]} | {_mdeur(sums[key])} |")
    return "\n".join(lines) + "\n"


def build_markdown(records: list[Prelevement], cov: dict[str, Any]) -> str:
    pris = [r for r in records if r.statut == "PRIS"]
    a_arbitrer = [r for r in records if r.statut == "A_ARBITRER"]

    out: list[str] = []
    out.append("# Rapport — inventaire des prélèvements obligatoires en France\n")
    out.append(f"> Généré le {date.today().isoformat()} par le pipeline "
               "(`po-pipeline report`). Ne pas éditer à la main.\n")

    out.append("## Synthèse\n")
    out.append("| Indicateur | Valeur |")
    out.append("|---|---:|")
    out.append(f"| Prélèvements retenus (PRIS) | {cov.get('n_pris', len(pris))} |")
    out.append(f"| Candidats rejetés (REJET) | {cov.get('n_rejet', 0)} |")
    out.append(f"| Lignes à arbitrer | {cov.get('n_a_arbitrer', len(a_arbitrer))} |")
    out.append(f"| Somme des PRIS (socle curé) | {cov.get('somme_pris_socle_mdeur', '—')} Md€ |")
    out.append(f"| Somme des PRIS (itemisé, indicatif) | {cov.get('somme_pris_itemise_mdeur', '—')} Md€ |")
    out.append(f"| Enveloppe INSEE ({cov.get('year', '—')}) | "
               f"{cov.get('enveloppe_insee_mdeur', '—')} Md€ |")
    out.append(f"| **Couverture (socle)** | **{cov.get('couverture_pct', '—')} %** |")
    out.append(f"| PRIS sans montant | {cov.get('n_pris_sans_montant', '—')} |\n")
    out.append("> La couverture rapporte la somme des PRIS du **socle curé** "
               "(non chevauchant) à l'enveloppe INSEE. La somme « itemisée » "
               "ajoute les composantes fines de la NTL et des taxes affectées : "
               "indicative, elle mêle agrégats et composantes et n'est pas une "
               "mesure de couverture.\n")

    by_cat = _table_by(records, "categorie", "Montants par catégorie")
    if by_cat:
        out.append(by_cat)
    by_benef = _table_by(records, "secteur", "Montants par secteur bénéficiaire")
    if by_benef:
        out.append(by_benef)

    out.append("## Prélèvements retenus (top 40 par montant)\n")
    out.append("| Prélèvement | Catégorie | Montant (Md€) | Sources |")
    out.append("|---|---|---:|---|")
    for r in pris[:40]:
        src = ", ".join(sorted({s.source_id for s in r.sources}))
        out.append(f"| {r.nom} | {r.categorie} | {_mdeur(r.montant_eur)} | {src} |")
    out.append("")

    if a_arbitrer:
        out.append("## Lignes à arbitrer (classement incertain)\n")
        out.append("Ces lignes n'ont pu être classées automatiquement "
                   "(ni code ESA, ni règle). À expertiser manuellement.\n")
        out.append("| Libellé | Sources |")
        out.append("|---|---|")
        for r in a_arbitrer[:50]:
            src = ", ".join(sorted({s.source_id for s in r.sources}))
            out.append(f"| {r.nom} | {src} |")
        out.append("")

    out.append("## Méthodologie\n")
    out.append("Classement par application de la règle de décision C1–C3 "
               "(voir `README.md` §2-§3 et `pipeline/config/decision_rules.yaml`). "
               "Sources et provenance : `pipeline/config/sources.yaml` et le champ "
               "`sources` de chaque ligne du jeu de données.\n")
    return "\n".join(out)


def report() -> str:
    ensure_dirs()
    records, cov = _load()
    md = build_markdown(records, cov)
    path = DOCS_DIR / "RAPPORT.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"[report] écrit {path}")
    return md
