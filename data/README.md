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

> État actuel : produit à partir du **socle curé du README** (source
> `readme_seed`). Les montants sont des ordres de grandeur tant que les sources
> officielles (Eurostat NTL, Voies & Moyens Tome I…) n'ont pas été récupérées
> en exécution réseau. Voir `pipeline/README.md`.
