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
make test              # 17 tests unitaires
```

Étapes individuelles : `make fetch|normalize|classify|reconcile|validate|report`.

## Le « socle curé » (toujours présent)

`seed/readme_inventory.csv` encode la liste déjà vérifiée du README (§4 PRIS,
§5 REJET) comme source à part entière (`readme_seed`). Il garantit un jeu de
données significatif **même sans réseau** ; les sources officielles l'étendent
ensuite à l'exhaustivité ligne à ligne et remplacent les montants approximatifs
(« ordre de grandeur ») par les montants officiels.

## Atteindre l'exhaustivité ligne à ligne

1. Vérifier/actualiser les URLs de `config/sources.yaml` (le n° du PDF V&M et le
   millésime OpenDataSoft changent à chaque PLF).
2. `make all` avec accès réseau aux domaines sources (`ec.europa.eu`,
   `budget.gouv.fr`, `data.economie.gouv.fr`, `data.gouv.fr`).
3. Inspecter la section « Lignes à arbitrer » de `docs/RAPPORT.md` et compléter
   `config/decision_rules.yaml` pour les cas nouveaux.

> ⚠️ Dans l'environnement Claude Code on the web utilisé pour construire ce
> pipeline, l'egress vers `ec.europa.eu` et `data.economie.gouv.fr` est **bloqué
> par la politique réseau** (403). La génération live nécessite d'élargir cette
> politique ou d'exécuter le pipeline en local.

## Ajouter une source

1. Ajouter une entrée dans `config/sources.yaml`.
2. Écrire un parser `src/po_pipeline/parse_<x>.py` exposant
   `parse(path, reference_year) -> list[Prelevement]`.
3. L'enregistrer dans `PARSERS` de `src/po_pipeline/normalize.py`.
4. Ajouter une fixture + un test dans `tests/`.
