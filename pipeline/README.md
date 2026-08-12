# Pipeline — inventaire exhaustif des prélèvements obligatoires (PO)

Pipeline reproductible qui produit, à partir des sources officielles, un
**jeu de données exhaustif et tracé** des prélèvements obligatoires en France,
en appliquant la règle de décision du [`README.md`](../README.md) racine
(définition INSEE/OCDE + 3 critères C1–C3).

## Principe

```
fetch ──▶ normalize ──▶ classify ──▶ reconcile ──▶ report
(raw/)     (interim/)   (statut PO)   (dédup +      (docs/RAPPORT.md)
                                       couverture)
```

- **fetch** : télécharge les sources de `config/sources.yaml` vers `data/raw/`
  (cache + sha256 + manifeste). `--offline` réutilise le cache sans réseau.
- **normalize** : exécute les parsers (Eurostat NTL, Voies & Moyens Tome I PDF,
  taxes affectées OpenDataSoft, **socle curé du README**) → `data/interim/`.
- **classify** : applique la règle de décision (`config/decision_rules.yaml`)
  → `statut` ∈ {PRIS, REJET, A_ARBITRER} + `critere_echec`.
- **reconcile** : fusionne les doublons *entre* sources, calcule la
  **couverture** (Σ des PO retenus vs enveloppe INSEE), écrit les sorties.
- **report** : génère [`docs/RAPPORT.md`](../docs/RAPPORT.md).

## Sorties (versionnées)

| Fichier | Contenu |
|---|---|
| `../data/prelevements_obligatoires.json` | registre complet + provenance |
| `../data/prelevements_obligatoires.csv` | même contenu, à plat |
| `data/processed/coverage.json` | métriques de couverture |
| `../docs/RAPPORT.md` | rapport lisible auto-généré |

## Installation & exécution

```bash
cd pipeline
python -m venv .venv && source .venv/bin/activate
make install           # dépendances (PyPI)

make all               # fetch -> ... -> report (réseau requis)
# ou, hors-ligne, sur le socle curé + cache éventuel :
make offline
make test              # 30 tests unitaires
```

Étapes individuelles : `make fetch|normalize|classify|reconcile|validate|report`.

## Le « socle curé » (toujours présent)

Deux fichiers, tous deux lus par `parse_seed.py` :

| Fichier | Rôle |
|---|---|
| `seed/readme_inventory.csv` | La liste déjà vérifiée du README (§4 PRIS, §5 REJET), source `readme_seed`. |
| `seed/supplement.csv` | **Le fichier à éditer** pour ajouter un prélèvement à la main : entrées issues du dépouillement documentaire (V&M Tome I, état A et article 36 du PLF 2026, liste INSEE des ODAC, NTL Eurostat), source `supplement_cure`. |

Ils garantissent un jeu de données significatif **même sans réseau** ; les
sources officielles l'étendent ensuite à l'exhaustivité ligne à ligne et
remplacent les montants approximatifs par les montants officiels.

Colonnes de `supplement.csv` :
`nom;sigle;categorie;secteur;base_legale;montant_mdeur;statut;critere_echec;notes;alias`

Deux pièges à connaître :

- **Pas de point-virgule dans les champs** : le fichier est en `;` sans
  échappement systématique ; un `;` dans les notes décale toutes les colonnes.
- **Renseigner `alias`** (séparateur `|`) quand le prélèvement existe déjà sous
  un autre libellé dans une source officielle — typiquement l'appellation CIBS
  moderne face à l'appellation historique du tableau des taxes affectées. Sans
  alias, la déduplication échoue et la même taxe apparaît deux fois, parfois
  avec deux statuts contradictoires.

## Atteindre l'exhaustivité ligne à ligne

1. Vérifier/actualiser les URLs de `config/sources.yaml` (le n° du PDF V&M et le
   millésime OpenDataSoft changent à chaque PLF).
2. `make all` avec accès réseau aux domaines sources (`ec.europa.eu`,
   `budget.gouv.fr`, `data.economie.gouv.fr`, `data.gouv.fr`).
3. Inspecter la section « Lignes à arbitrer » de `docs/RAPPORT.md` et compléter
   `config/decision_rules.yaml` pour les cas nouveaux.

> ℹ️ L'egress vers `ec.europa.eu` et `data.economie.gouv.fr` était bloqué (403)
> dans l'environnement où ce pipeline a été construit. **Ce n'est plus le cas** :
> les quatre sources ont été récupérées en direct et le jeu de données versionné
> est désormais produit par un `make all` complet (Eurostat NTL, V&M Tome I,
> taxes affectées, agrégats de contrôle). Si `make all` échoue sur un 403,
> l'environnement d'exécution est en cause, pas la configuration : `make offline`
> reste disponible et retombe sur le socle curé.

## Ajouter une source

1. Ajouter une entrée dans `config/sources.yaml`.
2. Écrire un parser `src/po_pipeline/parse_<x>.py` exposant
   `parse(path, reference_year) -> list[Prelevement]`.
3. L'enregistrer dans `PARSERS` de `src/po_pipeline/normalize.py`.
4. Ajouter une fixture + un test dans `tests/`.
