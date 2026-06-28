# Rapport — inventaire des prélèvements obligatoires en France

> Généré le 2026-06-28 par le pipeline (`po-pipeline report`). Ne pas éditer à la main.

## Synthèse

| Indicateur | Valeur |
|---|---:|
| Prélèvements retenus (PRIS) | 55 |
| Candidats rejetés (REJET) | 14 |
| Lignes à arbitrer | 0 |
| Somme des PRIS | 1278.8 Md€ |
| Enveloppe INSEE (2024) | 1254.0 Md€ |
| **Couverture** | **102.0 %** |
| PRIS sans montant | 20 |

> La couverture rapporte la somme des montants retenus à l'enveloppe INSEE des prélèvements obligatoires. Un écart s'explique par les lignes sans montant, les écarts de périmètre/millésime entre sources et les doublons résiduels.

### Montants par catégorie

| Categorie | Nombre | Montant (Md€) |
|---|---:|---:|
| cotisation sociale | 6 | 570.0 |
| impôt d'État | 17 | 429.2 |
| fiscalité sociale | 8 | 178.0 |
| impôt local | 15 | 83.5 |
| taxe affectée | 6 | 11.9 |
| ressource UE | 3 | 6.2 |

### Montants par secteur bénéficiaire

| Secteur | Nombre | Montant (Md€) |
|---|---:|---:|
| ASSO | 14 | 748.0 |
| APUC | 17 | 429.2 |
| APUL | 15 | 83.5 |
| ODAC | 6 | 11.9 |
| UE | 3 | 6.2 |

## Prélèvements retenus (top 40 par montant)

| Prélèvement | Catégorie | Montant (Md€) | Sources |
|---|---|---:|---|
| Cotisations du régime général (maladie, vieillesse, famille, AT-MP, CSA) | cotisation sociale | 420.0 | readme_seed |
| Taxe sur la valeur ajoutée | impôt d'État | 200.0 | readme_seed |
| Contribution sociale généralisée | fiscalité sociale | 140.0 | readme_seed |
| Cotisations de retraite complémentaire obligatoire | cotisation sociale | 90.0 | readme_seed |
| Impôt sur le revenu | impôt d'État | 90.0 | readme_seed |
| Impôt sur les sociétés | impôt d'État | 60.0 | readme_seed |
| Cotisations d'assurance chômage (part employeur) | cotisation sociale | 40.0 | readme_seed |
| Taxe foncière sur les propriétés bâties | impôt local | 35.0 | readme_seed |
| Accise sur les énergies (ex-TICPE) | impôt d'État | 30.0 | readme_seed |
| Accises sur les alcools, tabacs et boissons | impôt d'État | 18.0 | readme_seed |
| Droits d'enregistrement et de mutation à titre gratuit | impôt d'État | 18.0 | readme_seed |
| Taxe sur les salaires | fiscalité sociale | 16.0 | readme_seed |
| Cotisations des travailleurs indépendants | cotisation sociale | 15.0 | readme_seed |
| Droits de mutation à titre onéreux | impôt local | 15.0 | readme_seed |
| Contribution unique à la formation professionnelle et à l'alternance | taxe affectée | 9.5 | readme_seed |
| Versement mobilité | impôt local | 9.0 | readme_seed |
| Contribution au remboursement de la dette sociale | fiscalité sociale | 8.0 | readme_seed |
| Cotisation foncière des entreprises | impôt local | 8.0 | readme_seed |
| Taxe d'enlèvement des ordures ménagères | impôt local | 8.0 | readme_seed |
| Taxe spéciale sur les conventions d'assurance | impôt d'État | 8.0 | readme_seed |
| Cotisation sur la valeur ajoutée des entreprises | impôt local | 5.0 | readme_seed |
| Cotisations agricoles | cotisation sociale | 5.0 | readme_seed |
| Prélèvement de solidarité sur les revenus du capital | fiscalité sociale | 5.0 | readme_seed |
| Taxe de solidarité additionnelle (complémentaire santé) | fiscalité sociale | 5.0 | readme_seed |
| Contribution sociale de solidarité des sociétés | fiscalité sociale | 4.0 | readme_seed |
| Ressource propre fondée sur la TVA | ressource UE | 3.0 | readme_seed |
| Taxe d'habitation sur les résidences secondaires | impôt local | 2.5 | readme_seed |
| Taxe sur les transactions financières | impôt d'État | 2.5 | readme_seed |
| Redevances des agences de l'eau | taxe affectée | 2.2 | readme_seed |
| Droits de douane | ressource UE | 2.0 | readme_seed |
| Impôt sur la fortune immobilière | impôt d'État | 2.0 | readme_seed |
| Contribution sur les emballages plastiques non recyclés | ressource UE | 1.2 | readme_seed |
| Taxe foncière sur les propriétés non bâties | impôt local | 1.0 | readme_seed |
| Taxe sur les services numériques | impôt d'État | 0.7 | readme_seed |
| Contribution de vie étudiante et de campus | taxe affectée | 0.2 | readme_seed |
| Contribution exceptionnelle sur les hauts revenus | impôt d'État | — | readme_seed |
| Contributions de l'industrie pharmaceutique (clause de sauvegarde M) | fiscalité sociale | — | readme_seed |
| Cotisations des régimes spéciaux | cotisation sociale | — | readme_seed |
| Droits de timbre | impôt d'État | — | readme_seed |
| Forfait social | fiscalité sociale | — | readme_seed |

## Méthodologie

Classement par application de la règle de décision C1–C3 (voir `README.md` §2-§3 et `pipeline/config/decision_rules.yaml`). Sources et provenance : `pipeline/config/sources.yaml` et le champ `sources` de chaque ligne du jeu de données.
