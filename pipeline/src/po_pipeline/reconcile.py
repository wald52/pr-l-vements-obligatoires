"""Étage 4 — Réconciliation : fusion multi-sources + mesure de couverture.

- Rapproche un même prélèvement présent dans plusieurs sources (libellé
  normalisé + similarité floue rapidfuzz), fusionne leurs provenances et
  retient le montant le plus fiable.
- Calcule la couverture : somme des montants PRIS vs enveloppe INSEE
  (control_envelope de sources.yaml). C'est la *preuve mesurée* d'exhaustivité.
- Écrit les sorties finales versionnées : data/prelevements_obligatoires.{json,csv}
  et data/processed/coverage.json.
"""

from __future__ import annotations

import csv
import json
from typing import Any

from rapidfuzz import fuzz

from .config import load_rules, load_sources
from .paths import DATASET_DIR, PROCESSED_DIR, ensure_dirs
from .schema import CSV_COLUMNS, Prelevement, Source, normalize_label

# Priorité de source pour choisir le montant de référence en cas de conflit.
_SOURCE_PRIORITY = ["eurostat_ntl", "vm_tome1", "taxes_affectees", "rei_local"]


def _compatible(a: Prelevement, b: Prelevement) -> bool:
    """Deux enregistrements peuvent fusionner s'ils ne se contredisent pas.

    On ne dédoublonne PAS deux lignes issues d'une même source unique : une
    énumération officielle/curée liste des lignes distinctes à dessein (ex.
    taxe foncière bâtie vs non bâtie). La fusion ne vise que les doublons
    *entre* sources différentes.
    """
    if a.esa_code and b.esa_code and a.esa_code != b.esa_code:
        return False
    sa = {s.source_id for s in a.sources}
    sb = {s.source_id for s in b.sources}
    if len(sa) == 1 and sa == sb:
        return False
    return True


def _match_labels(rec: Prelevement) -> list[str]:
    """Libellés normalisés servant au rapprochement : intitulé ET sigle.

    Une source peut nommer un prélèvement par son sigle (NTL Eurostat : « TVA »)
    et une autre par son intitulé complet (« Taxe sur la valeur ajoutée ») ;
    rapprocher aussi sur le sigle évite de double-compter ces lignes.
    """
    labels = [normalize_label(rec.nom)]
    if rec.sigle:
        sig = normalize_label(rec.sigle)
        if len(sig) >= 2:
            labels.append(sig)
    return [l for l in labels if l]


def reconcile_records(records: list[Prelevement], threshold: int) -> list[Prelevement]:
    clusters: list[list[Prelevement]] = []
    cluster_labels: list[list[str]] = []  # libellés (intitulé+sigle) du cluster

    for rec in records:
        labels = _match_labels(rec)
        placed = False
        for i, keys in enumerate(cluster_labels):
            if _compatible(rec, clusters[i][0]) and any(
                fuzz.token_sort_ratio(la, lb) >= threshold
                for la in labels for lb in keys
            ):
                clusters[i].append(rec)
                cluster_labels[i] = keys + [l for l in labels if l not in keys]
                placed = True
                break
        if not placed:
            clusters.append([rec])
            cluster_labels.append(labels)

    return [_merge(cluster) for cluster in clusters]


def _source_rank(sid: str) -> int:
    return _SOURCE_PRIORITY.index(sid) if sid in _SOURCE_PRIORITY else len(_SOURCE_PRIORITY)


def _merge(cluster: list[Prelevement]) -> Prelevement:
    # Représentant : la source la plus prioritaire fournit l'ossature.
    cluster = sorted(
        cluster,
        key=lambda r: _source_rank(r.sources[0].source_id if r.sources else "zzz"),
    )
    base = cluster[0]
    sources: list[Source] = []
    seen_src: set[tuple[str, str]] = set()
    for rec in cluster:
        for s in rec.sources:
            tag = (s.source_id, s.ref)
            if tag not in seen_src:
                seen_src.add(tag)
                sources.append(s)

    def first(attr: str) -> Any:
        for rec in cluster:
            val = getattr(rec, attr)
            if val not in (None, "", "indéterminée"):
                return val
        return getattr(base, attr)

    # Montant : celui de la source la plus prioritaire qui en fournit un.
    montant = next((r.montant_eur for r in cluster if r.montant_eur is not None), None)
    annee = next((r.annee for r in cluster if r.annee is not None), None)

    return Prelevement(
        id=base.id,
        nom=base.nom,
        sigle=first("sigle"),
        categorie=first("categorie"),
        esa_code=first("esa_code"),
        beneficiaire=first("beneficiaire"),
        secteur=first("secteur"),
        base_legale=first("base_legale"),
        montant_eur=montant,
        annee=annee,
        statut=_merge_statut(cluster),
        critere_echec=first("critere_echec") if _merge_statut(cluster) == "REJET" else None,
        sources=sources,
        notes=first("notes"),
    )


def _merge_statut(cluster: list[Prelevement]) -> str:
    statuts = {r.statut for r in cluster}
    if "PRIS" in statuts:
        return "PRIS"
    if "REJET" in statuts:
        return "REJET"
    return "A_ARBITRER"


def coverage(records: list[Prelevement], envelope: dict[str, Any]) -> dict[str, Any]:
    pris = [r for r in records if r.statut == "PRIS"]
    total_eur = sum(r.montant_eur or 0 for r in pris)
    total_mdeur = total_eur / 1e9
    target = envelope.get("total_po_mdeur")
    pct = (100 * total_mdeur / target) if target else None
    return {
        "year": envelope.get("year"),
        "n_records_total": len(records),
        "n_pris": len(pris),
        "n_rejet": sum(1 for r in records if r.statut == "REJET"),
        "n_a_arbitrer": sum(1 for r in records if r.statut == "A_ARBITRER"),
        "n_pris_sans_montant": sum(1 for r in pris if r.montant_eur is None),
        "somme_pris_mdeur": round(total_mdeur, 1),
        "enveloppe_insee_mdeur": target,
        "couverture_pct": round(pct, 1) if pct is not None else None,
        "source_enveloppe": envelope.get("source"),
    }


def _write_outputs(records: list[Prelevement], cov: dict[str, Any]) -> None:
    ensure_dirs()
    # JSON structuré (sorties finales versionnées).
    items = [r.to_dict() for r in records]
    with open(DATASET_DIR / "prelevements_obligatoires.json", "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

    # CSV à plat.
    with open(DATASET_DIR / "prelevements_obligatoires.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CSV_COLUMNS, extrasaction="ignore")
        w.writeheader()
        for r in records:
            row = r.to_dict()
            row["source_ids"] = ";".join(s.source_id for s in r.sources)
            w.writerow(row)

    with open(PROCESSED_DIR / "coverage.json", "w", encoding="utf-8") as f:
        json.dump(cov, f, ensure_ascii=False, indent=2)


def reconcile(records: list[Prelevement] | None = None) -> tuple[list[Prelevement], dict[str, Any]]:
    if records is None:
        from .classify import classify
        records = classify()

    rules = load_rules()
    threshold = int(rules.get("fuzzy_match_threshold", 88))
    merged = reconcile_records(records, threshold)
    merged.sort(key=lambda r: (r.statut != "PRIS", -(r.montant_eur or 0), r.nom))

    envelope = load_sources().get("control_envelope", {})
    cov = coverage(merged, envelope)
    _write_outputs(merged, cov)
    print(f"[reconcile] {len(merged)} prélèvements uniques "
          f"({cov['n_pris']} PRIS, {cov['n_rejet']} REJET, "
          f"{cov['n_a_arbitrer']} à arbitrer) — couverture {cov['couverture_pct']}%")
    return merged, cov
