"""Réconciliation du socle avec les agrégats de comptabilité nationale.

Le socle curé sert au calcul de la couverture : sa somme doit rester cohérente
avec les agrégats de la National Tax List d'Eurostat, bloc par bloc. Un total
global juste peut masquer deux erreurs qui se compensent — d'où le découpage.

Ce test est né de deux incidents :

* le socle a compté les cotisations sociales **deux fois** (une ligne agrégée
  plus quatre familles empilées), soit 140 Md€ de trop, ce qui gonflait la
  couverture à 106,5 % ;
* le bloc fiscal était au contraire **court de 77 Md€**, dont trois
  sous-évaluations concentrées (IS, prélèvement de solidarité, surtaxes sur les
  bénéfices) que l'on avait d'abord mises au compte d'une « longue traîne ».

Les valeurs de référence sont figées ici parce que `pipeline/data/raw/` n'est
pas versionné (cf. `.gitignore`). Elles proviennent de la NTL, onglet France,
millésime 2024. **À réviser en même temps que `reference_year`.**
"""

from __future__ import annotations

from collections import defaultdict

# National Tax List d'Eurostat, onglet France, exercice 2024, en Md€.
NTL_2024 = {
    # Cotisations sociales effectives obligatoires : D.611C employeurs
    # (293,1) + D.613C ménages (136,9). Les cotisations imputées (D.612,
    # 51,2 Md€) en sont exclues : elles échouent au critère C1.
    "cotisations": 430.1,
    # Impôts : D.2 (456,3) + D.5 (366,0) + D.91 (21,5).
    "impots": 843.8,
}

# Tolérances. Le bloc social doit tomber juste : il est porté par une ligne
# agrégée unique, alignée sur la NTL. Le bloc fiscal admet un manque, borné :
# le socle n'énumère pas les lignes NTL inférieures au milliard.
TOL_COTISATIONS = 1.0
MANQUE_FISCAL_MAX = 15.0


def _socle_par_bloc(records) -> dict[str, float]:
    sommes = defaultdict(float)
    for rec in records:
        if rec.statut != "PRIS":
            continue
        if not any(s.source_id == "readme_seed" for s in rec.sources):
            continue
        bloc = "cotisations" if rec.categorie == "cotisation sociale" else "impots"
        sommes[bloc] += (rec.montant_eur or 0) / 1e9
    return sommes


def test_bloc_social_aligne_sur_la_ntl(dataset_records):
    socle = _socle_par_bloc(dataset_records)["cotisations"]
    ecart = socle - NTL_2024["cotisations"]
    assert abs(ecart) <= TOL_COTISATIONS, (
        f"Cotisations sociales du socle : {socle:.1f} Md€ contre "
        f"{NTL_2024['cotisations']:.1f} attendus (écart {ecart:+.1f}).\n"
        "Un excédent signale un double compte : vérifier qu'aucune famille "
        "(chômage, complémentaires, indépendants, agricoles, régimes spéciaux) "
        "n'est valorisée en plus de la ligne agrégée."
    )


def test_bloc_fiscal_sans_exces_ni_manque_excessif(dataset_records):
    socle = _socle_par_bloc(dataset_records)["impots"]
    ecart = socle - NTL_2024["impots"]
    assert ecart <= TOL_COTISATIONS, (
        f"Impôts du socle : {socle:.1f} Md€, soit {ecart:+.1f} au-dessus de "
        f"l'agrégat NTL. Un excédent est un double compte, pas une exhaustivité."
    )
    assert -ecart <= MANQUE_FISCAL_MAX, (
        f"Impôts du socle : {socle:.1f} Md€ contre {NTL_2024['impots']:.1f} "
        f"attendus, soit {ecart:+.1f}. Au-delà de {MANQUE_FISCAL_MAX:.0f} Md€, "
        "l'écart n'est plus imputable aux lignes NTL inférieures au milliard : "
        "chercher une famille non valorisée ou une valeur approchée."
    )
