"""Le jeu de données ne doit pas contenir de doublon franc.

Signal retenu : deux libellés très proches **et** un montant identique. C'est
ce qui a fait apparaître la double comptabilisation du droit de consommation
sur les tabacs dans les DOM (143,8 M€ comptés deux fois).

Les doublons connus et assumés — parce qu'ils viennent d'une même énumération
officielle qu'on ne réécrit pas — sont listés dans TOLERES, avec leur raison.
"""

from __future__ import annotations

from po_pipeline.doublons import _cle, doublons_suspects

# Paires tolérées : libellé A, libellé B (normalisés), et pourquoi.
TOLERES = {
    (
        "droit de consommation sur les tabacs dans les dom",
        "droits de consommation sur les tabacs dom",
    ): "Doublon interne à la liste officielle des taxes affectées : le même "
       "tarif ultramarin y figure sous deux libellés. Non fusionné parce que "
       "la déduplication ne rapproche pas deux lignes d'une même source.",
}


def test_pas_de_doublon_franc_non_tolere(dataset_records):
    francs = [
        d for d in doublons_suspects(dataset_records)
        if d["montants_egaux"]
        and tuple(sorted((_cle(d["a"]), _cle(d["b"])))) not in
        {tuple(sorted(k)) for k in TOLERES}
    ]
    assert not francs, "Doublons francs (libellés proches, montants égaux) :\n  - " + \
        "\n  - ".join(f"{d['a']} || {d['b']}" for d in francs)


def test_les_doublons_toleres_existent_toujours(dataset_records):
    """Un doublon corrigé en amont doit sortir de la liste des tolérés."""
    presents = {
        tuple(sorted((_cle(d["a"]), _cle(d["b"]))))
        for d in doublons_suspects(dataset_records)
    }
    obsoletes = [k for k in TOLERES if tuple(sorted(k)) not in presents]
    assert not obsoletes, f"Tolérances devenues inutiles : {obsoletes}"
