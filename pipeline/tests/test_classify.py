"""Teste la couche de décision sur les cas-limites du README §4-§5."""

from po_pipeline.classify import classify_records
from po_pipeline.config import load_rules
from po_pipeline.schema import Prelevement


def _rec(nom, esa=None, secteur=None):
    return Prelevement(id="x", nom=nom, esa_code=esa, secteur=secteur)


def _classify_one(rec):
    return classify_records([rec], load_rules())[0]


def test_esa_default_impot_pris():
    assert _classify_one(_rec("Impôt sur le revenu", esa="D5")).statut == "PRIS"


def test_cotisation_imputee_rejetee_c1():
    r = _classify_one(_rec("Cotisations imputées des fonctionnaires", esa="D612"))
    assert r.statut == "REJET" and r.critere_echec == "C1"


def test_teom_prise_mais_reom_rejetee():
    teom = _classify_one(_rec("Taxe d'enlèvement des ordures ménagères", esa="D2"))
    reom = _classify_one(_rec("Redevance d'enlèvement des ordures ménagères"))
    assert teom.statut == "PRIS"
    assert reom.statut == "REJET" and reom.critere_echec == "C3"


def test_amende_rejetee_sanction():
    r = _classify_one(_rec("Amendes et pénalités de stationnement"))
    assert r.statut == "REJET" and r.critere_echec == "sanction"


def test_redevance_agence_eau_prise():
    r = _classify_one(_rec("Redevance pollution des agences de l'eau"))
    assert r.statut == "PRIS"


def test_cotisation_ordre_rejetee_c2():
    r = _classify_one(_rec("Cotisation à l'ordre professionnel des médecins"))
    assert r.statut == "REJET" and r.critere_echec == "C2"


def test_ligne_inconnue_a_arbitrer():
    r = _classify_one(_rec("Prélèvement mystère non documenté"))
    assert r.statut == "A_ARBITRER"


def test_secteur_hors_apu_declasse_c2():
    r = _classify_one(_rec("Contribution à un organisme privé", esa="D61", secteur="S11"))
    assert r.statut == "REJET" and r.critere_echec == "C2"
