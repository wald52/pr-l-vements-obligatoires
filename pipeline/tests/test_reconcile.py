"""Teste la fusion multi-sources et le calcul de couverture."""

from po_pipeline.reconcile import coverage, reconcile_records
from po_pipeline.schema import Prelevement, Source


def test_merge_same_tax_across_sources():
    a = Prelevement(id="a", nom="Taxe sur la valeur ajoutée", esa_code="D2",
                    montant_eur=200e9, statut="PRIS",
                    sources=[Source("eurostat_ntl")])
    b = Prelevement(id="b", nom="Taxe sur la valeur ajoutee (TVA)",
                    statut="PRIS", sources=[Source("vm_tome1", ref="1101")])
    merged = reconcile_records([a, b], threshold=80)
    assert len(merged) == 1
    assert {s.source_id for s in merged[0].sources} == {"eurostat_ntl", "vm_tome1"}
    assert merged[0].montant_eur == 200e9  # montant de la source prioritaire


def test_distinct_taxes_not_merged():
    a = Prelevement(id="a", nom="Impôt sur le revenu", esa_code="D5", statut="PRIS",
                    sources=[Source("eurostat_ntl")])
    b = Prelevement(id="b", nom="Impôt sur les sociétés", esa_code="D5", statut="PRIS",
                    sources=[Source("eurostat_ntl")])
    assert len(reconcile_records([a, b], threshold=88)) == 2


def test_coverage_computation():
    recs = [
        Prelevement(id="a", nom="A", montant_eur=600e9, statut="PRIS"),
        Prelevement(id="b", nom="B", montant_eur=500e9, statut="PRIS"),
        Prelevement(id="c", nom="C", statut="REJET", critere_echec="C3"),
    ]
    cov = coverage(recs, {"year": 2024, "total_po_mdeur": 1254.0})
    assert cov["n_pris"] == 2
    assert cov["n_rejet"] == 1
    assert cov["somme_pris_mdeur"] == 1100.0
    assert cov["couverture_pct"] == round(100 * 1100 / 1254, 1)
