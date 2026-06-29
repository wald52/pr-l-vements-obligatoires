# Rapport — inventaire des prélèvements obligatoires en France

> Généré le 2026-06-29 par le pipeline (`po-pipeline report`). Ne pas éditer à la main.

## Synthèse

| Indicateur | Valeur |
|---|---:|
| Prélèvements retenus (PRIS) | 56 |
| Candidats rejetés (REJET) | 19 |
| Lignes à arbitrer | 251 |
| Somme des PRIS | 1337.2 Md€ |
| Enveloppe INSEE (2024) | 1254.0 Md€ |
| **Couverture** | **106.6 %** |
| PRIS sans montant | 12 |

> La couverture rapporte la somme des montants retenus à l'enveloppe INSEE des prélèvements obligatoires. Un écart s'explique par les lignes sans montant, les écarts de périmètre/millésime entre sources et les doublons résiduels.

### Montants par catégorie

| Categorie | Nombre | Montant (Md€) |
|---|---:|---:|
| cotisation sociale | 6 | 570.0 |
| impôt d'État | 15 | 433.1 |
| taxe affectée | 14 | 199.5 |
| impôt local | 12 | 82.1 |
| fiscalité sociale | 5 | 25.4 |
| impôt en capital | 1 | 20.8 |
| ressource UE | 3 | 6.2 |

### Montants par secteur bénéficiaire

| Secteur | Nombre | Montant (Md€) |
|---|---:|---:|
| ASSO | 14 | 771.1 |
| APUC | 17 | 443.2 |
| APUL | 15 | 83.5 |
| (non renseigné) | 1 | 20.8 |
| ODAC | 6 | 12.4 |
| UE | 3 | 6.2 |

## Prélèvements retenus (top 40 par montant)

| Prélèvement | Catégorie | Montant (Md€) | Sources |
|---|---|---:|---|
| Cotisations du régime général (maladie, vieillesse, famille, AT-MP, CSA) | cotisation sociale | 420.0 | readme_seed |
| TVA | impôt d'État | 206.3 | eurostat_ntl, readme_seed |
| Contribution sociale généralisée | taxe affectée | 153.1 | eurostat_ntl, readme_seed, taxes_affectees |
| Impôt sur le revenu | impôt d'État | 96.2 | eurostat_ntl, readme_seed |
| Cotisations de retraite complémentaire obligatoire | cotisation sociale | 90.0 | readme_seed |
| Impôt sur les sociétés | impôt d'État | 60.0 | readme_seed |
| Cotisations d'assurance chômage (part employeur) | cotisation sociale | 40.0 | readme_seed |
| Taxe foncière sur les propriétés bâties | impôt local | 35.0 | readme_seed |
| Accise sur les énergies (ex-TICPE) | impôt d'État | 30.0 | readme_seed |
| Mutations à titre gratuit | impôt en capital | 20.8 | eurostat_ntl |
| Accises sur les alcools, tabacs et boissons | impôt d'État | 18.0 | readme_seed |
| Droits d'enregistrement et de mutation à titre gratuit | impôt d'État | 18.0 | readme_seed |
| Taxes sur les salaires | taxe affectée | 17.3 | eurostat_ntl, readme_seed, taxes_affectees |
| Cotisations des travailleurs indépendants | cotisation sociale | 15.0 | readme_seed |
| Droits de mutation à titre onéreux | impôt local | 15.0 | readme_seed |
| Versement mobilité | impôt local | 12.2 | eurostat_ntl, readme_seed |
| Taxe spéciale sur les conventions d'assurance | taxe affectée | 10.0 | eurostat_ntl, readme_seed, taxes_affectees |
| Contribution unique à la formation professionnelle et à l'alternance | taxe affectée | 9.8 | readme_seed, taxes_affectees |
| Contribution au remboursement de la dette sociale | fiscalité sociale | 9.1 | eurostat_ntl, readme_seed |
| Cotisation foncière des entreprises | impôt local | 7.7 | eurostat_ntl, readme_seed |
| Forfait social | fiscalité sociale | 6.3 | eurostat_ntl, readme_seed |
| Contribution sociale de solidarité des sociétés | taxe affectée | 5.2 | eurostat_ntl, readme_seed, taxes_affectees |
| Cotisation sur la valeur ajoutée des entreprises | impôt local | 5.0 | eurostat_ntl, readme_seed |
| Cotisations agricoles | cotisation sociale | 5.0 | readme_seed |
| Prélèvement de solidarité sur les revenus du capital | fiscalité sociale | 5.0 | readme_seed |
| Taxe de solidarité additionnelle (complémentaire santé) | fiscalité sociale | 5.0 | readme_seed |
| Ressource propre fondée sur la TVA | ressource UE | 3.0 | readme_seed |
| Taxe d'habitation sur les résidences secondaires | impôt local | 2.5 | readme_seed |
| Redevances des agences de l'eau | taxe affectée | 2.2 | readme_seed |
| Droits de douane | ressource UE | 2.0 | readme_seed |
| Impôt sur la fortune immobilière | impôt d'État | 2.0 | readme_seed |
| Impositions forfaitaires sur les entreprises de réseaux | impôt local | 1.9 | eurostat_ntl, readme_seed |
| Taxe sur les transactions financières | impôt d'État | 1.9 | eurostat_ntl, readme_seed |
| Taxe sur les surfaces commerciales | impôt local | 1.3 | eurostat_ntl, readme_seed |
| Contribution sur les emballages plastiques non recyclés | ressource UE | 1.2 | readme_seed |
| Taxe foncière sur les propriétés non bâties | impôt local | 1.0 | readme_seed |
| Taxe sur les services numériques | impôt d'État | 0.8 | eurostat_ntl, readme_seed |
| Taxes d'enlèvement des ordures ménagères | taxe affectée | 0.6 | readme_seed, taxes_affectees |
| Taxe d’aménagement | taxe affectée | 0.6 | readme_seed, taxes_affectees |
| Taxe GEMAPI | impôt local | 0.5 | eurostat_ntl, readme_seed |

## Lignes à arbitrer (classement incertain)

Ces lignes n'ont pu être classées automatiquement (ni code ESA, ni règle). À expertiser manuellement.

| Libellé | Sources |
|---|---|
| Foncier bâti | eurostat_ntl |
| Taxe intérieure de consommation des produits énergétiques | eurostat_ntl |
| Droits d'enregistrement (y compris taxe additionnelle) | eurostat_ntl |
| Autres prélèvements sociaux | eurostat_ntl |
| Taxe départementale de publicité foncière sur les mutations à titres onéreux | taxes_affectees |
| Taxes sur les tabacs | eurostat_ntl |
| Droits de consommation sur les tabacs | taxes_affectees |
| Contributions des entreprises à la formation professionnelle et à l'apprentissage | eurostat_ntl |
| Contributions pour le remboursement de la dette sociale (CRDS) | taxes_affectees |
| Taxe de solidarité additionnelle | eurostat_ntl |
| Taxe intérieure de consommation sur les produits énergétique (TICPE) - Fractions transférées en compensation du transfert du RMI/RSA et dans le cadre de l'acte II de la décentralisation | taxes_affectees |
| Accise sur l'électricité | eurostat_ntl |
| Taxes sur les boissons | eurostat_ntl |
| Taxe intérieure de consommation sur les produits énergétique (TICPE dont part modulable) | taxes_affectees |
| Produits de la loterie nationale et du loto | eurostat_ntl |
| Taxe intérieure sur la consommation de gaz naturel | eurostat_ntl |
| Taxe sur les certificats d'immatriculation des véhicules | eurostat_ntl, taxes_affectees |
| Taxe communale additionnelle à certains droits d'enregistrement | taxes_affectees |
| Cotisation patronale pour le FNAL (Fonds national d'aide au logement) | eurostat_ntl |
| Cotisation des employeurs | taxes_affectees |
| Impôt de solidarité sur la fortune (jusque 2017) / Impôt sur la fortune immobilière (à partir de 2018) | eurostat_ntl |
| Part sur les salaires | eurostat_ntl |
| Droits d'importation | eurostat_ntl |
| Contribution de solidarité pour l'autonomie | eurostat_ntl |
| Taxe sur les certificats d'immatriculation des véhicules (cartes grises) | taxes_affectees |
| Contribution solidarité autonomie (CSA) | taxes_affectees |
| Droits de consommation sur les alcools | taxes_affectees |
| Redevance pour obstacle sur les cours d’eau, redevance pour stockage d’eau en période d’étiage, redevance pour la protection du milieu aquatique, redevance pour pollutions diffuses, redevances pour prélèvement sur la ressource en eau, redevances pour pollution de l’eau, redevances pour modernisation des réseaux de collecte, redevances cynégétiques, droit de validation du permis de chasse | taxes_affectees |
| Taxe sur les émissions de CO2 | eurostat_ntl |
| Fraction affectée du produit du relèvement du tarif de taxe intérieure de consommation sur les produits énergétiques (TICPE) sur le carburant gazole | taxes_affectees |
| Taxes sur les transports | eurostat_ntl |
| Taxes sur les paris hippiques | eurostat_ntl |
| Taxes sur les services professionnels hors droits de mutations | eurostat_ntl |
| Cotisations sur primes d'assurance | eurostat_ntl |
| Contribution tarifaire d'acheminement (CTA) | taxes_affectees |
| Participation des employeurs à l'effort de construction | eurostat_ntl |
| Taxes au profit de l'Association sur la garantie des salaires | eurostat_ntl |
| Taxes sur les jeux des casinos | eurostat_ntl |
| Droit d'octroi de mer et droit d'octroi de mer régional | taxes_affectees |
| Part sur la consommation | eurostat_ntl |
| Taxe sur primes d'assurance automobile | eurostat_ntl |
| Part sur le capital | eurostat_ntl |
| Taxes sur la construction | eurostat_ntl |
| Droit sur les bières et les boissons non alcoolisées | taxes_affectees |
| Contribution sociale sur les bénéfices des sociétés | eurostat_ntl |
| Taxe sur construction de bureaux et sur les locaux à usage de bureaux | eurostat_ntl |
| Contribution patronale sur stock-options | eurostat_ntl |
| Autres taxes sur la pollution | eurostat_ntl |
| Taxe sur les véhicules de tourisme des sociétés | eurostat_ntl |
| Prélèvements sur les revenus des capitaux mobiliers | eurostat_ntl |

## Méthodologie

Classement par application de la règle de décision C1–C3 (voir `README.md` §2-§3 et `pipeline/config/decision_rules.yaml`). Sources et provenance : `pipeline/config/sources.yaml` et le champ `sources` de chaque ligne du jeu de données.
