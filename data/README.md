# Jeux de données — prélèvements obligatoires

Fichiers **générés** par le pipeline (`pipeline/`). Ne pas éditer à la main :
les regénérer via `cd pipeline && make all` (ou `make offline`).

| Fichier | Description |
|---|---|
| `prelevements_obligatoires.json` | Registre complet (PRIS + REJET) avec provenance par ligne. |
| `prelevements_obligatoires.csv` | Même contenu, format tabulaire. |

## Colonnes

`id`, `nom`, `sigle`, `categorie`, `esa_code`, `beneficiaire`, `secteur`,
`base_legale`, `montant_eur`, `annee`, `statut` (PRIS/REJET/A_ARBITRER),
`critere_echec` (∅/C1/C2/C3/sanction/supprime), `sources`, `notes`.

## Provenance

État actuel : produit par un **`make all` complet**, les quatre sources ayant été
récupérées en direct. Cinq contributeurs :

| Source | Rôle | Enregistrements |
|---|---|---:|
| `eurostat_ntl` | National Tax List, onglet France — épine dorsale, codes SEC et montants | 103 |
| `taxes_affectees` | Liste des taxes affectées (data.economie.gouv.fr) | 184 |
| `readme_seed` | Socle curé du README (§4 PRIS, §5 REJET) | 69 |
| `supplement_cure` | Ajouts curés à la main (`pipeline/seed/supplement.csv`) | 147 |
| `vm_tome1` | Voies & Moyens Tome I — énumération des lignes budgétaires | 24 |

Après déduplication : **450 prélèvements uniques**.

## Ce que ce jeu de données ne contient pas

- Les prélèvements des **collectivités à autonomie fiscale** (Nouvelle-Calédonie,
  Polynésie française, Wallis-et-Futuna, Saint-Pierre-et-Miquelon,
  Saint-Barthélemy). Ils sont réels et documentés au **README §4.7**, mais ils
  sont hors du **territoire économique des comptes nationaux** : les inclure
  fausserait la mesure de couverture. Saint-Martin, rattaché statistiquement à la
  Guadeloupe, est en revanche dans le champ — ses 13 prélèvements propres (TGCA,
  patentes, taxes foncières locales, taxe de consommation sur les produits
  pétroliers…) y figurent donc.
- Les **prélèvements supprimés** y figurent en `REJET` / `critere_echec=supprime`,
  volontairement : c'est ce qui évite de les réintroduire par erreur.
