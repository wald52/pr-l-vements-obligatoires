# Inventaire des prélèvements obligatoires — document de travail

> Généré le 2026-06-30 par le pipeline (`po-pipeline workdoc`). **Ne pas éditer à la main** : relancer `make all` régénère ce document depuis les sources.

Ce document regroupe les **359 prélèvements** de l'inventaire réconcilié (année de référence 2024). Il est conçu comme un **plan de travail** pour poursuivre les recherches : chaque ligne porte sa **provenance**, et les candidats incertains sont isolés et pré-triés.

**Comment l'utiliser.** Traiter en priorité le §4 (« à arbitrer ») : commencer par le §4.1 (doublons probables à fusionner), puis instruire les taxes affectées (§4.3) et les nouvelles impositions (§4.4). Le §5 liste les questions ouvertes.

## Sommaire

1. [Synthèse](#1-synthèse)
2. [Prélèvements retenus (PRIS)](#2-prélèvements-retenus-pris)
3. [Candidats rejetés (REJET)](#3-candidats-rejetés-rejet)
4. [À arbitrer — front de recherche](#4-à-arbitrer--front-de-recherche)
5. [Pistes et questions ouvertes](#5-pistes-et-questions-ouvertes)
6. [Registre des sources et régénération](#6-registre-des-sources-et-régénération)

## 1. Synthèse

| Indicateur | Valeur |
|---|---:|
| Prélèvements au total | 359 |
| Retenus (PRIS) | 152 |
| Rejetés (REJET) | 19 |
| À arbitrer | 188 |
| Somme des PRIS (socle curé) | 1326.1 Md€ |
| Somme des PRIS (itemisé, indicatif) | 1483.6 Md€ |
| Enveloppe INSEE 2024 | 1254.0 Md€ |
| Couverture (socle / INSEE) | 105.8 % |

### Répartition par catégorie

| Catégorie | Nombre |
|---|---:|
| taxe affectée | 178 |
| impôt sur la production/importation | 62 |
| impôt local | 25 |
| impôt d'État | 24 |
| impôt courant sur le revenu/patrimoine | 21 |
| recette fiscale (État) | 17 |
| indéterminée | 13 |
| fiscalité sociale | 8 |
| cotisation sociale | 6 |
| ressource UE | 3 |
| impôt en capital | 1 |
| cotisation sociale imputée | 1 |

### Présence par source (une ligne peut avoir plusieurs sources)

| Source | Lignes |
|---|---:|
| taxes_affectees | 184 |
| eurostat_ntl | 103 |
| readme_seed | 69 |
| vm_tome1 | 24 |
| supplement_cure | 18 |

## 2. Prélèvements retenus (PRIS)

152 prélèvements retenus, regroupés par secteur bénéficiaire et triés par montant décroissant.

### Administrations de sécurité sociale (ASSO) — 14 lignes, 771.06 Md€

| Prélèvement | Sigle | Montant (Md€) | Base légale | Sources |
|---|---|---:|---|---|
| Cotisations du régime général (maladie, vieillesse, famille, AT-MP, CSA) |  | 420.00 | Code de la sécurité sociale | readme_seed (README §4-§5) |
| Contribution sociale généralisée | CSG | 153.13 | CSS art. L136-1 s. | eurostat_ntl (FR:D51M/C04); taxes_affectees; readme_seed (README §4-§5) |
| Cotisations de retraite complémentaire obligatoire | AGIRC-ARRCO | 90.00 | ANI / Code de la sécurité sociale | readme_seed (README §4-§5) |
| Cotisations d'assurance chômage (part employeur) |  | 40.00 | Code du travail | readme_seed (README §4-§5) |
| Taxe sur les salaires |  | 17.32 | CGI art. 231 | eurostat_ntl (FR:D29C/C03); taxes_affectees; readme_seed (README §4-§5) |
| Cotisations des travailleurs indépendants |  | 15.00 | Code de la sécurité sociale | readme_seed (README §4-§5) |
| Contribution au remboursement de la dette sociale | CRDS | 9.08 | Ordonnance 96-50 | eurostat_ntl (FR:D51M/C03); readme_seed (README §4-§5) |
| Forfait social |  | 6.30 | CSS art. L137-15 | eurostat_ntl (FR:D29C/C09); readme_seed (README §4-§5) |
| Contribution sociale de solidarité des sociétés | C3S | 5.23 | CSS art. L651-1 | eurostat_ntl (FR:D29H/C02); taxes_affectees; readme_seed (README §4-§5) |
| Cotisations agricoles |  | 5.00 | Code rural | readme_seed (README §4-§5) |
| Prélèvement de solidarité sur les revenus du capital |  | 5.00 | CSS | readme_seed (README §4-§5) |
| Taxe de solidarité additionnelle (complémentaire santé) | TSA | 5.00 | CSS art. L862-4 | readme_seed (README §4-§5) |
| Contributions de l'industrie pharmaceutique (clause de sauvegarde M) |  | — | CSS | readme_seed (README §4-§5) |
| Cotisations des régimes spéciaux |  | — | Code de la sécurité sociale | readme_seed (README §4-§5) |

### État et administrations centrales (APUC) — 24 lignes, 446.00 Md€

| Prélèvement | Sigle | Montant (Md€) | Base légale | Sources |
|---|---|---:|---|---|
| Taxe sur la valeur ajoutée | TVA | 206.33 | CGI art. 256 s. | eurostat_ntl (FR:D211/C01); readme_seed (README §4-§5) |
| Impôt sur le revenu | IR | 96.16 | CGI art. 1 A s. | eurostat_ntl (FR:D51M/C07); readme_seed (README §4-§5) |
| Impôt sur les sociétés | IS | 60.00 | CGI art. 205 s. | readme_seed (README §4-§5) |
| Accise sur les énergies (ex-TICPE) | TICPE | 30.00 | CIBS | vm_tome1 (ligne 1501); readme_seed (README §4-§5) |
| Droits d'enregistrement et de mutation à titre gratuit |  | 20.82 | CGI | eurostat_ntl (FR:D91A/C01); readme_seed (README §4-§5) |
| Accises sur les alcools, tabacs et boissons |  | 18.00 | CIBS | readme_seed (README §4-§5) |
| Taxe spéciale sur les conventions d'assurance | TSCA | 10.03 | CGI art. 991 s. | eurostat_ntl (FR:D214G/C04); taxes_affectees; readme_seed (README §4-§5) |
| Impôt sur la fortune immobilière | IFI | 2.00 | CGI art. 964 s. | vm_tome1 (ligne 1406); readme_seed (README §4-§5) |
| Taxe sur les transactions financières | TTF | 1.85 | CGI art. 235 ter ZD | eurostat_ntl (FR:D214C/C03); vm_tome1 (ligne 1797); readme_seed (README §4-§5) |
| Taxe sur les services numériques |  | 0.79 | CGI art. 299 s. | eurostat_ntl (FR:D214I/C02); vm_tome1 (ligne 1430); readme_seed (README §4-§5) |
| Taxe sur les surfaces de stationnement |  | 0.01 | CGI | taxes_affectees; readme_seed (README §4-§5) |
| Contribution exceptionnelle sur les hauts revenus | CEHR | — | CGI art. 223 sexies | readme_seed (README §4-§5) |
| Droit de timbre sur les procédures civiles en première instance et prud'homales |  | — | CGI | supplement_cure (supplément curé (CGI/CIBS, V&M PLF 2026)) |
| Droits de timbre |  | — | CGI | readme_seed (README §4-§5) |
| Malus automobile (CO2 et masse) |  | — | CIBS | readme_seed (README §4-§5) |
| Taxe générale sur les activités polluantes | TGAP | — | CIBS | vm_tome1 (ligne 1756); readme_seed (README §4-§5) |
| Taxe générale sur les activités polluantes — composante déchets | TGAP déchets | — | CIBS (ex-CGI 266 sexies) | supplement_cure (supplément curé (CGI/CIBS, V&M PLF 2026)) |
| Taxe générale sur les activités polluantes — composante lessives | TGAP lessives | — | CIBS | supplement_cure (supplément curé (CGI/CIBS, V&M PLF 2026)) |
| Taxe générale sur les activités polluantes — composante matériaux d'extraction | TGAP matériaux | — | CIBS | supplement_cure (supplément curé (CGI/CIBS, V&M PLF 2026)) |
| Taxe générale sur les activités polluantes — composante émissions polluantes | TGAP émissions | — | CIBS | supplement_cure (supplément curé (CGI/CIBS, V&M PLF 2026)) |
| Taxe sur l'affectation des véhicules à des fins économiques | ex-TVS | — | CIBS | readme_seed (README §4-§5) |
| Taxe sur l'exploitation des infrastructures de transport de longue distance | TEILD | — | CGI art. 235 ter ZE bis | supplement_cure (supplément curé (CGI/CIBS, V&M PLF 2026)) |
| Taxe sur le transport aérien de passagers — tarif de solidarité | TSBA solidarité | — | CIBS (ex-taxe de solidarité « Chirac ») | supplement_cure (supplément curé (CGI/CIBS, V&M PLF 2026)) |
| Taxe sur les bureaux et locaux en Île-de-France |  | — | CGI | readme_seed (README §4-§5) |

### Organismes divers d'administration centrale (ODAC) — 7 lignes, 12.41 Md€

| Prélèvement | Sigle | Montant (Md€) | Base légale | Sources |
|---|---|---:|---|---|
| Contribution unique à la formation professionnelle et à l'alternance | CUFPA | 9.83 | Code du travail L6131-1 | taxes_affectees; readme_seed (README §4-§5) |
| Redevances des agences de l'eau |  | 2.20 | Code de l'environnement L213-10 | readme_seed (README §4-§5) |
| Taxe de solidarité sur les billets d'avion |  | 0.21 | CGI art. 302 bis K | taxes_affectees; readme_seed (README §4-§5) |
| Contribution de vie étudiante et de campus | CVEC | 0.17 | Code de l'éducation L841-5 | taxes_affectees; readme_seed (README §4-§5) |
| Contribution spéciale et taxe additionnelle d'accompagnement (stockage de déchets radioactifs, Cigéo) |  | — | Loi de finances 2000 art. 43 | supplement_cure (supplément curé (CGI/CIBS, V&M PLF 2026)) |
| Taxes affectées au CNC |  | — | Code du cinéma | readme_seed (README §4-§5) |
| Taxes pour frais de chambres consulaires |  | — | CGI | readme_seed (README §4-§5) |

### Administrations publiques locales (APUL) — 24 lignes, 90.45 Md€

| Prélèvement | Sigle | Montant (Md€) | Base légale | Sources |
|---|---|---:|---|---|
| Taxe foncière sur les propriétés bâties | TFPB | 42.06 | CGI art. 1380 s. | eurostat_ntl (FR:D29A/C03); readme_seed (README §4-§5) |
| Droits de mutation à titre onéreux | DMTO | 15.00 | CGI art. 1594 A s. | readme_seed (README §4-§5) |
| Versement mobilité |  | 12.23 | Code des transports L2333-64 | eurostat_ntl (FR:D29C/C07); readme_seed (README §4-§5) |
| Cotisation foncière des entreprises | CFE | 7.71 | CGI art. 1447 s. | eurostat_ntl (FR:D29A/C06); readme_seed (README §4-§5) |
| Cotisation sur la valeur ajoutée des entreprises | CVAE | 5.00 | CGI art. 1586 ter | eurostat_ntl (FR:D29A/C07); vm_tome1 (ligne 1497); readme_seed (README §4-§5) |
| Taxe d'habitation sur les résidences secondaires | THRS | 2.50 | CGI art. 1407 s. | readme_seed (README §4-§5) |
| Impositions forfaitaires sur les entreprises de réseaux | IFER | 1.86 | CGI art. 1635-0 quinquies | eurostat_ntl (FR:D29A/C10); readme_seed (README §4-§5) |
| Taxe sur les surfaces commerciales | TASCOM | 1.27 | CGI | eurostat_ntl (FR:D29A/C12); readme_seed (README §4-§5) |
| Taxe foncière sur les propriétés non bâties | TFPNB | 0.88 | CGI art. 1393 s. | eurostat_ntl (FR:D29A/C04); readme_seed (README §4-§5) |
| Taxe d'enlèvement des ordures ménagères | TEOM | 0.63 | CGI art. 1520 s. | taxes_affectees; readme_seed (README §4-§5) |
| Taxe d'aménagement |  | 0.58 | CGI art. 1635 quater A | taxes_affectees; readme_seed (README §4-§5) |
| Taxe GEMAPI |  | 0.53 | CGI art. 1530 bis | eurostat_ntl (FR:D29A/C18); readme_seed (README §4-§5) |
| Taxe locale sur la publicité extérieure | TLPE | 0.19 | CGCT L2333-6 s. | taxes_affectees; readme_seed (README §4-§5) |
| Imposition forfaitaire sur le matériel ferroviaire roulant | IFER ferroviaire | — | CGI art. 1599 quater A | supplement_cure (supplément curé (CGI/CIBS, V&M PLF 2026)) |
| Imposition forfaitaire sur les centrales photovoltaïques et hydrauliques | IFER photovoltaïque | — | CGI art. 1519 F | supplement_cure (supplément curé (CGI/CIBS, V&M PLF 2026)) |
| Imposition forfaitaire sur les installations de production d'électricité nucléaire ou thermique à flamme | IFER nucléaire | — | CGI art. 1519 E | supplement_cure (supplément curé (CGI/CIBS, V&M PLF 2026)) |
| Imposition forfaitaire sur les installations gazières et canalisations de transport | IFER gaz | — | CGI art. 1519 HA | supplement_cure (supplément curé (CGI/CIBS, V&M PLF 2026)) |
| Imposition forfaitaire sur les répartiteurs principaux et équipements de boucle locale cuivre | IFER cuivre | — | CGI art. 1599 quater B | supplement_cure (supplément curé (CGI/CIBS, V&M PLF 2026)) |
| Imposition forfaitaire sur les stations radioélectriques | IFER antennes | — | CGI art. 1519 H | supplement_cure (supplément curé (CGI/CIBS, V&M PLF 2026)) |
| Imposition forfaitaire sur les transformateurs électriques | IFER transformateurs | — | CGI art. 1519 G | supplement_cure (supplément curé (CGI/CIBS, V&M PLF 2026)) |
| Imposition forfaitaire sur les éoliennes terrestres et hydroliennes | IFER éolien | — | CGI art. 1519 D | supplement_cure (supplément curé (CGI/CIBS, V&M PLF 2026)) |
| Taxe d'habitation sur les logements vacants | THLV | — | CGI art. 1407 bis | supplement_cure (supplément curé (CGI/CIBS, V&M PLF 2026)) |
| Taxe de séjour |  | — | CGCT L2333-26 s. | readme_seed (README §4-§5) |
| Taxe sur les logements vacants | TLV | — | CGI art. 232 | readme_seed (README §4-§5) |

### Union européenne — 3 lignes, 6.20 Md€

| Prélèvement | Sigle | Montant (Md€) | Base légale | Sources |
|---|---|---:|---|---|
| Ressource propre fondée sur la TVA |  | 3.00 | Décision ressources propres UE | readme_seed (README §4-§5) |
| Droits de douane |  | 2.00 | Code des douanes de l'Union | readme_seed (README §4-§5) |
| Contribution sur les emballages plastiques non recyclés |  | 1.20 | Décision ressources propres UE | readme_seed (README §4-§5) |

### Secteur à préciser — 80 lignes, 157.50 Md€

| Prélèvement | Sigle | Montant (Md€) | Base légale | Sources |
|---|---|---:|---|---|
| Taxe intérieure de consommation des produits énergétiques |  | 29.55 |  | eurostat_ntl (FR:D214A/C06) |
| Droits d'enregistrement (y compris taxe additionnelle) |  | 14.66 |  | eurostat_ntl (FR:D214C/C01) |
| Autres prélèvements sociaux |  | 14.65 |  | eurostat_ntl (FR:D51M/C06) |
| Taxes sur les tabacs |  | 13.61 |  | eurostat_ntl (FR:D214A/C10) |
| Contributions des entreprises à la formation professionnelle et à l'apprentissage |  | 11.36 |  | eurostat_ntl (FR:D29C/C02) |
| Taxe de solidarité additionnelle |  | 6.21 |  | eurostat_ntl (FR:D214G/C01) |
| Accise sur l'électricité |  | 4.80 |  | eurostat_ntl (FR:D214A/C07) |
| Taxes sur les boissons |  | 4.75 |  | eurostat_ntl (FR:D214A/C09) |
| Produits de la loterie nationale et du loto |  | 3.99 |  | eurostat_ntl (FR:D214F/C01) |
| Taxe intérieure sur la consommation de gaz naturel |  | 3.18 |  | eurostat_ntl (FR:D214A/C02) |
| Taxe sur les certificats d'immatriculation des véhicules |  | 3.12 | LFR-I 2014 et de la LFI 2015 | eurostat_ntl (FR:D214D/C01); taxes_affectees |
| Cotisation patronale pour le FNAL (Fonds national d'aide au logement) |  | 2.94 |  | eurostat_ntl (FR:D29C/C06) |
| Impôt de solidarité sur la fortune (jusque 2017) / Impôt sur la fortune immobilière (à partir de 2018) |  | 2.68 |  | eurostat_ntl (FR:D59A/C02) |
| Part sur les salaires |  | 2.63 |  | eurostat_ntl (FR:D29A/C08) |
| Droits d'importation |  | 2.60 |  | eurostat_ntl (FR:D2121/C02) |
| Contribution de solidarité pour l'autonomie |  | 2.47 |  | eurostat_ntl (FR:D29C/C05) |
| Taxe sur les émissions de CO2 |  | 2.11 |  | eurostat_ntl (FR:D29F/C02) |
| Taxes sur les transports |  | 1.86 |  | eurostat_ntl (FR:D214H/C10) |
| Taxes sur les paris hippiques |  | 1.80 |  | eurostat_ntl (FR:D214F/C03) |
| Taxes sur les services professionnels hors droits de mutations |  | 1.76 |  | eurostat_ntl (FR:D214H/C09) |
| Cotisations sur primes d'assurance |  | 1.73 |  | eurostat_ntl (FR:D214G/C02) |
| Participation des employeurs à l'effort de construction |  | 1.50 |  | eurostat_ntl (FR:D29C/C13) |
| Taxes au profit de l'Association sur la garantie des salaires |  | 1.47 |  | eurostat_ntl (FR:D29C/C04) |
| Taxes sur les jeux des casinos |  | 1.44 |  | eurostat_ntl (FR:D214F/C02) |
| Part sur la consommation |  | 1.33 |  | eurostat_ntl (FR:D59A/C05) |
| Taxe sur primes d'assurance automobile |  | 1.25 |  | eurostat_ntl (FR:D214G/C05) |
| Part sur le capital |  | 1.24 |  | eurostat_ntl (FR:D29A/C09) |
| Taxes sur la construction |  | 1.19 |  | eurostat_ntl (FR:D214H/C08) |
| Contribution sociale sur les bénéfices des sociétés |  | 1.17 |  | eurostat_ntl (FR:D51O/C06) |
| Taxe sur construction de bureaux et sur les locaux à usage de bureaux |  | 1.05 |  | eurostat_ntl (FR:D29A/C16) |
| Contribution patronale sur stock-options |  | 1.03 |  | eurostat_ntl (FR:D29C/C10) |
| Autres taxes sur la pollution |  | 1.01 |  | eurostat_ntl (FR:D214A/C03) |
| Taxe sur les véhicules de tourisme des sociétés |  | 0.99 |  | eurostat_ntl (FR:D29B/C04) |
| Prélèvements sur les revenus des capitaux mobiliers |  | 0.97 |  | eurostat_ntl (FR:D51M/C08) |
| Taxes pharmaceutiques (contribution grossistes répartiteurs, taxe sur les ventes de médicaments et de cosmétiques) |  | 0.96 |  | eurostat_ntl (FR:D214I/C01) |
| Redevances sur les prélèvements de l'eau |  | 0.83 |  | eurostat_ntl (FR:D214H/C07) |
| Cotisation des entreprises cinématographiques au profit du CNC (Centre national du cinéma) |  | 0.71 |  | eurostat_ntl (FR:D214E/C03) |
| Contribution de sécurité immobilière |  | 0.69 |  | eurostat_ntl (FR:D214B/C01) |
| Retenue sur les bénéfices non commerciaux |  | 0.66 |  | eurostat_ntl (FR:D51O/C07) |
| Octroi de mer |  | 0.65 |  | eurostat_ntl (FR:D2121/C03) |
| Autres taxes sur l'énergie |  | 0.62 |  | eurostat_ntl (FR:D214A/C04) |
| Taxe sur les mises à disposition de produits pétroliers pour le stockage stratégique |  | 0.60 |  | eurostat_ntl (FR:D214A/C11) |
| Taxe sur infrastructures de transport longues distances |  | 0.55 |  | eurostat_ntl (FR:D51O/C10) |
| Produit de l'imposition chambre de commerce |  | 0.53 |  | eurostat_ntl (FR:D29A/C13) |
| Contributions sur les loyers immobiliers |  | 0.51 |  | eurostat_ntl (FR:D214H/C04) |
| Contribution des distributeurs d'énergie électrique basse tension |  | 0.38 |  | eurostat_ntl (FR:D214L/C02) |
| Imposition sur les pylônes |  | 0.35 |  | eurostat_ntl (FR:D29A/C15) |
| Taxe due par les opérateurs de communications électroniques |  | 0.24 |  | eurostat_ntl (FR:D214H/C11) |
| Chambre d'agriculture |  | 0.23 |  | eurostat_ntl (FR:D29A/C17) |
| Taxe chambre métier |  | 0.21 |  | eurostat_ntl (FR:D29A/C14) |
| Taxe spéciale sur les véhicules routiers (taxe à l'essieu) |  | 0.15 |  | eurostat_ntl (FR:D29B/C02) |
| Autres taxes sur le revenu |  | 0.14 |  | eurostat_ntl (FR:D51E/C01) |
| Contribution sur les rentes infra marginales (électricité) |  | 0.13 |  | eurostat_ntl (FR:D29H/C05) |
| Taxes sur les spectacles |  | 0.10 |  | eurostat_ntl (FR:D214E/C02) |
| Redevance cynégétique (permis de chasse) |  | 0.06 |  | eurostat_ntl (FR:D59D/C04) |
| Taxe due par les entreprises de transport public aérien et maritime (Corse, DOM) |  | 0.05 |  | eurostat_ntl (FR:D29B/C05); taxes_affectees |
| Droit annuel de francisation et de navigation |  | 0.04 |  | eurostat_ntl (FR:D59D/C02) |
| Taxe de risque systémique |  | 0.03 |  | eurostat_ntl (FR:D59F/C02) |
| Autres taxes |  | 0.01 |  | eurostat_ntl (FR:D2122C/C01); vm_tome1 (ligne 1799) |
| Taxe exceptionnelle de solidarité sur les hautes rémunérations |  | 0.00 |  | eurostat_ntl (FR:D29C/C11) |
| 3% dividendes |  | — |  | eurostat_ntl (FR:D51O/C08) |
| Achats d'énergies renouvelables à prix contractuels |  | — |  | eurostat_ntl (FR:D29H/C06) |
| Avoir fiscal distribué (négatif) |  | — |  | eurostat_ntl (FR:D51O/C02) |
| Avoir fiscal utilisé (positif) |  | — |  | eurostat_ntl (FR:D51M/C02) |
| Contribution au SRF (single resolution fund) |  | — |  | eurostat_ntl (FR:D29H/C04) |
| Contribution temporaire de solidarité |  | — |  | eurostat_ntl (FR:D51O/C09) |
| Cotisation minimale de taxe professionnelle |  | — |  | eurostat_ntl (FR:D29A/C02) |
| Fonds de solidarité contribution des fonctionnaires |  | — |  | eurostat_ntl (FR:D51M/C05) |
| Impôt forfaitaire annuel |  | — |  | eurostat_ntl (FR:D51O/C05) |
| Impôt sur les opérations traitées dans les bourses de valeurs |  | — |  | eurostat_ntl (FR:D214C/C02) |
| Prélèvements et taxes compensatoires à l'importation |  | — |  | eurostat_ntl (FR:D2122B/C01) |
| TVA sur subventions |  | — |  | eurostat_ntl (FR:D29H/C03) |
| Taxe additionnelle sur les assurances automobile |  | — |  | eurostat_ntl (FR:D214G/C03) |
| Taxe d'habitation |  | — |  | eurostat_ntl (FR:D59A/C03) |
| Taxe professionnelle |  | — |  | eurostat_ntl (FR:D29A/C05) |
| Taxe sur l'utilisation des voies navigables (dont taxe hydraulique) |  | — |  | eurostat_ntl (FR:D29A/C11) |
| Taxe sur les véhicules (partie ménages) |  | — |  | eurostat_ntl (FR:D59D/C01) |
| Taxes au profit de l'ADEME (Agence de l'environnement et de la maîtrise de l'énergie) |  | — |  | eurostat_ntl (FR:D214A/C08) |
| Taxes au profit du FNDMA (Financement National de Développement et de Modernisation de l'Apprentissage) |  | — |  | eurostat_ntl (FR:D29C/C08) |
| Taxes sur les véhicules à moteur payées par les producteurs |  | — |  | eurostat_ntl (FR:D29B/C03) |

## 3. Candidats rejetés (REJET)

19 candidats écartés, avec le critère en échec (C1 versement effectif, C2 bénéficiaire APU/UE, C3 obligatoire et sans contrepartie).

| Candidat | Critère | Note | Sources |
|---|---|---|---|
| Cotisations sociales imputées (fonctionnaires d'État) | C1 | Pas de versement effectif (employeur fictif). | readme_seed (README §4-§5) |
| Cotisations aux ordres professionnels et syndicats | C2 | Bénéficiaire hors périmètre APU (organisme privé). | readme_seed (README §4-§5) |
| Prélèvement sur les contrats d'assurance-vie en deshérence; 'Prélèvement sur les contrats participation et intéressement en déshérence | C3 | Versement non obligatoire (libre choix). | taxes_affectees |
| Cotisations facultatives (PER, assurance-vie, prévoyance facultative) | C3 | Versement non obligatoire (libre choix). | readme_seed (README §4-§5) |
| Dons et legs aux administrations | C3 | Volontaires. | readme_seed (README §4-§5) |
| Emprunts et produits de la dette | C3 | Ressource remboursable, librement souscrite. | readme_seed (README §4-§5) |
| Factures d'eau et d'assainissement (part exploitant) | C3 | Contrepartie directe. | readme_seed (README §4-§5) |
| Forfait de post-stationnement | C3 | Contrepartie directe (occupation du domaine public) depuis 2018. | readme_seed (README §4-§5) |
| Péages autoroutiers et d'ouvrages d'art | C3 | Paiement d'un service rendu (usage de l'infrastructure). | readme_seed (README §4-§5) |
| Redevance d'enlèvement des ordures ménagères | C3 | Tarifée selon le service rendu => contrepartie directe (README §5). | readme_seed (README §4-§5) |
| Redevances domaniales | C3 | Contrepartie : droit d'occupation du domaine public. | readme_seed (README §4-§5) |
| Revenus du domaine, dividendes, loyers | C3 | Recettes patrimoniales avec contrepartie. | readme_seed (README §4-§5) |
| Impôts sur les sociétés y compris majoration et frais de poursuite | sanction | Sanction, hors champ des prélèvements (README §5). | eurostat_ntl (FR:D51O/C04) |
| Recettes diverses et pénalités | sanction | Sanction, hors champ des prélèvements (README §5). | eurostat_ntl (FR:D91C/C01) |
| Amendes et confiscations | sanction | Sanction, hors champ des prélèvements (README §5). | eurostat_ntl (FR:D2121/C01) |
| Amendes, pénalités et majorations | sanction | Sanction, hors champ des prélèvements (README §5). | readme_seed (README §4-§5) |
| Contribution à l'audiovisuel public | supprime | Supprimée en 2022, remplacée par une fraction de TVA (mémoire, README §5). | eurostat_ntl (FR:D59D/C03) |
| Contribution à l'audiovisuel public (ex-redevance TV) | supprime | Supprimée en 2022, remplacée par une fraction de TVA (mémoire, README §5). | readme_seed (README §4-§5) |
| Part salariale de l'assurance chômage | supprime | Supprimée en 2018, remplacée par de la CSG. | readme_seed (README §4-§5) |

## 4. À arbitrer — front de recherche

188 lignes restent à classer. Elles sont pré-triées ci-dessous pour faciliter l'instruction.

### 4.1 Doublons probables d'un prélèvement déjà retenu

8 lignes ressemblent fortement à un PRIS existant (rapprochement automatique) : à **fusionner** (ajuster un libellé dans le socle, ou un alias dans `reconcile`).

| Ligne à arbitrer | Montant (Md€) | Ressemble au PRIS | Score | Source |
|---|---:|---|---:|---|
| Accises sur les énergies (ex-TICFE) | — | Accise sur les énergies (ex-TICPE) | 95 | vm_tome1 (ligne 1503) |
| Accises sur les énergies (ex-TICGN) | — | Accise sur les énergies (ex-TICPE) | 92 | vm_tome1 (ligne 1502) |
| Taxe spéciale sur les conventions d'assurance automobile | 1.14 | Taxe spéciale sur les conventions d'assurance | 89 | taxes_affectees |
| Taxe sur les certificats d'immatriculation des véhicules (cartes grises) | 2.44 | Taxe sur les certificats d'immatriculation des véhicules | 87 | taxes_affectees |
| Taxe annuelle sur les logements vacants | — | Taxe sur les logements vacants | 86 | taxes_affectees |
| Contributions pour le remboursement de la dette sociale (CRDS) | 8.72 | Contribution au remboursement de la dette sociale | 84 | taxes_affectees |
| Taxe communale additionnelle à certains droits d'enregistrement | 3.09 | Droits d'enregistrement (y compris taxe additionnelle) | 82 | taxes_affectees |
| Taxe sur les boissons sucrées | 0.44 | Taxes sur les boissons | 82 | taxes_affectees |

### 4.2 Lignes Eurostat NTL à rattacher ou classer

0 taxes/contributions individuelles de la NTL (code ESA + montant officiel) sans correspondance directe : confirmer le statut et, le cas échéant, l'affecter à une rubrique.

| Ligne | ESA | Montant (Md€) | Réf. | 
|---|---|---:|---|

### 4.3 Taxes affectées à instruire

164 taxes affectées (V&M Tome I) à confirmer comme PO et rattacher à un bénéficiaire. Triées par bénéficiaire.

| Taxe affectée | Bénéficiaire | Montant (Md€) | Base légale |
|---|---|---:|---|
| Contribution spécifique pour le développement de la formation professionnelle initiale et continue dans les métiers des professions du bâtiment et des travaux publics. | 3CABTP et OPCO Constructys | 0.05 |  |
| Contributions pour frais de contrôle | ACPR - Autorité de contrôle prudentiel et de résolution | 0.22 | LFI 2014 |
| Fraction affectée du produit du relèvement du tarif de taxe intérieure de consommation sur les produits énergétiques (TICPE) sur le carburant gazole | AFITF - Agence de financement des infrastructures de transport de France | 1.91 | LFR-I 2014 et de la LFI 2015 |
| Taxe due par les concessionnaires d'autoroutes | AFITF - Agence de financement des infrastructures de transport de France | 0.68 | LFI 2012 |
| Taxe sur les exploitants d'infrastructures de transports | AFITF - Agence de financement des infrastructures de transport de France | 0.60 | LFI 2024 |
| Taxe destinée à financer le développement des actions de formation professionnelle dans les transports routiers | AFT - Association pour le développement de la formation professionnelle dans les transports | 0.06 |  |
| Redevance pour obstacle sur les cours d’eau, redevance pour stockage d’eau en période d’étiage, redevance pour la protection du milieu aquatique, redevance pour pollutions diffuses, redevances pour prélèvement sur la ressource en eau, redevances pour pollution de l’eau, redevances pour modernisation des réseaux de collecte, redevances cynégétiques, droit de validation du permis de chasse | Agences de l'eau | 2.20 | LFR 2015 et de la LFI 2016 |
| Contribution patronale au dialogue social (0,016%) | AGFPN - Association de Gestion du Fonds Paritaire National – AGFPN. | 0.10 |  |
| Fraction des produits annuels de la vente de biens confisqués | AGRASC - Agence de gestion et de recouvrement des avoirs saisis et confisqués | 0.10 | LFI 2012 |
| Contribution des employeurs à l'association pour la gestion du régime d'assurance des créances des salariés (AGS) | AGS - Association pour la gestion du régime d'assurance des créances des salariés | 0.91 |  |
| Droits et contributions pour frais de contrôle | AMF - Autorité des marchés financiers | 0.12 | LFI 2014 |
| Cotisation versée par les organismes HLM | ANCOLS - Agence nationale de contrôle du logement social | 0.01 | LFR-I 2014 et de la LFI 2015 |
| Prélèvement sur la participation des employeurs à l'effort de construction (PEEC) | ANCOLS - Agence nationale de contrôle du logement social | 0.01 | LFR-I 2014 et de la LFI 2015 |
| Contribution spéciale pour la gestion des déchets radioactifs - Conception | ANDRA - Agence nationale pour la gestion des déchets radioactifs | 0.08 |  |
| Taxe additionnelle à la taxe sur les installations nucléaires de base - Recherche | ANDRA - Agence nationale pour la gestion des déchets radioactifs | 0.07 | LFI 2012 |
| Taxe pour le développement de la formation professionnelle dans les métiers de la réparation de l'automobile, du cycle et du motocycle | ANFA - Association nationale pour la formation automobile | 0.03 |  |
| Prélèvement sur les jeux exploités par la FdJ hors paris sportifs | ANS - Agence nationale du sport | 0.25 | LFI 2012 |
| Prélèvement sur les paris sportifs en ligne de la FdJ et des nouveaux opérateurs agréés | ANS - Agence nationale du sport | 0.18 | LFI 2012 |
| Contribution sur la cession à un service de télévision des droits de diffusion de manifestations ou de compétitions sportives | ANS - Agence nationale du sport | 0.06 | LFI 2012 |
| Fraction des Prélèvements sociaux sur les jeux prévus aux art. L137-20 à L137-22 du Code de la sécurité sociale | ANSP - Agence nationale de santé publique | 0.01 | LFI 2012 |
| Taxe relative à la mise sur le marché des produits phytopharmaceutiques et de leurs adjuvants, des matières fertilisantes et de leurs adjuvants et des supports de culture | ANSéS - Agence nationale de sécurité sanitaire, de l'alimentation, de l'environnement et du travail | 0.01 | LFR 2016 et LFI 2017 |
| Taxe liée aux dossiers de demande concernant les médicaments vétérinaires ou leur publicité | ANSéS - Agence nationale de sécurité sanitaire, de l'alimentation, de l'environnement et du travail | 0.00 | LFR 2016 et LFI 2017 |
| Taxe annuelle sur la vente des produits phytopharmaceutiques | ANSéS - Agence nationale de sécurité sanitaire, de l'alimentation, de l'environnement et du travail | 0.00 | LFR-I 2014 et de la LFI 2015 |
| Taxe annuelle portant sur les autorisations de médicaments vétérinaires et les autorisations d’établissements pharmaceutiques vétérinaires | ANSéS - Agence nationale de sécurité sanitaire, de l'alimentation, de l'environnement et du travail | 0.00 | LFR 2016 et LFI 2017 |
| Taxe sur les déclarations et notifications de produit du tabac | ANSéS - Agence nationale de sécurité sanitaire, de l'alimentation, de l'environnement et du travail | — |  |
| Taxe sur les produits de tabac | ANSéS - Agence nationale de sécurité sanitaire, de l'alimentation, de l'environnement et du travail | — |  |
| Fraction des droits de timbre sur les passeports sécurisés | ANTS - Agence nationale des titres sécurisés | 0.30 | LFI 2012 |
| Fraction des droits de timbre sur les cartes nationales d'identité | ANTS - Agence nationale des titres sécurisés | 0.02 | LFI 2012 |
| Taxe sur les Titres de séjour et de voyage electroniques | ANTS - Agence nationale des titres sécurisés | 0.02 | LFI 2012 |
| Droit de timbre pour la délivrance du permis de conduire en cas de perte ou de vol | ANTS - Agence nationale des titres sécurisés | 0.01 | LFI 2012 |
| Taxe sur les exploitants de plateformes de mises en relation par voie électronique en vue de fournir certaines prestations de transport | ARPE - Autorité des relations sociales des plateformes d'emploi | 0.00 | LFI 2022 |
| Taxe sur la cession à titre onéreux des terrains nus ou des droits relatifs à des terrains nus rendus constructibles du fait de leur classement | ASP - Agence de services et de paiement | 0.02 | LFI 2013 et de la LFR-III 2012 |
| Contribution annuelle au fonds de développement pour l'insertion professionnelle des handicapés (FIPH) | Association de gestion du fonds de développement pour l'insertion professionnelle des handicapés (AGEFIPH) | 0.44 |  |
| Taxe sur les spectacles perçue au profit de l'Association pour le soutien du théâtre privé | Association pour le soutien du théâtre privé | 0.01 | LFI 2012 |
| Versement transport dû par les entreprises de plus de 9 salariés implantées en province | Autorités organisatrices des transports urbains | — |  |
| Cotisation au profit des caisses d’assurances d’accidents agricoles d’Alsace-Moselle | CAAA - Caisses d'assurances d'accidents agricoles d'Alsace-Moselle | — |  |
| Solde de la taxe d'apprentissage après prise en compte des versements directs des entreprises mentionnés au II de l'article L. 6241-2 | Caisse des dépôts et des consignations | 0.52 |  |
| Contribution tarifaire d'acheminement (CTA) | Caisse nationale de retraite des industries électriques et gazières | 1.70 |  |
| Taxe sur les boissons édulcorées | CCMSA (non salariés-maladie) | 0.04 |  |
| Droits de consommation sur les tabacs | CCMSA (non salariés-maladie, non salariés-RCO et salariés), CNAMTS, CNAF, autres régimes de sécurité sociale, CNSA, FCAATA, Fonds CMU-C jusqu'en 2016; CNAMTS et RAVGDT en 2017 | 13.56 |  |
| Droits de consommation sur les alcools | CCMSA (non salariés-vieillesse et maladie) jusqu'en 2016; CCMSA (non salariés-vieillesse, maladie et RCO) en 2017 | 2.29 |  |
| Droit sur les bières et les boissons non alcoolisées | CCMSA - non salariés branche vieillesse | 1.18 |  |
| Cotisation spéciale sur les boissons alcooliques | CCMSA - non salariés branche vieillesse | 0.76 |  |
| Droit de circulation sur les vins, cidres, poirés et hydromels | CCMSA - non salariés branche vieillesse | 0.11 |  |
| Droit de consommation sur les produits intermédiaires | CCMSA - non salariés branche vieillesse | 0.06 |  |
| Cotisation obligatoire | Centre national de la fonction publique territoriale (CNFPT) | 0.49 |  |
| Taxe pour le développement des industries de fabrication du papier, du carton et de la pâte de cellulose. | Centre technique de l’industrie des papiers, cartons et celluloses | 0.00 |  |
| Taxe affectée au financement d’un nouveau Centre Technique Industriel de la plasturgie et des composites | Centres techniques industriels de la plasturgie et des composites | 0.01 |  |
| Cotisation versée par les organismes HLM et les SEM | CGLLS - Caisse de garantie du logement locatif social | 0.34 |  |
| TA-CFE - fraction CCI-R de la Taxe additionnelle à la cotisation foncière des entreprises pour frais de chambres de commerce et d’industrie de région | Chambres de commerce et d'industrie de région (CCI-R) | 0.28 | LFI 2013 et de la LFR-III 2012 |
| TA-CVAE - Taxe additionnelle à la cotisation sur la valeur ajoutée des entreprises pour frais de chambres de commerce et d'industrie de région | Chambres de commerce et d'industrie de région (CCI-R) | 0.27 | LFI 2013 et de la LFR-III 2012 |
| Taxe additionnelle à la taxe foncière sur les propriétés non baties, pour frais de chambres d'agriculture (TCA-TFPNB) | Chambres départementales d'agriculture | 0.29 | LFI 2013 et de la LFR-III 2012 |
| Contributions patronales et salariales sur les attributions d’options (stock-options) de souscription ou d’achat des actions et sur les attributions gratuites | CNAF | 0.92 |  |
| Taxe sur les véhicules de société (TVS) | CNAF | 0.76 |  |
| Taxe exceptionnelle sur la réserve de capitalisation (exit-tax) | CNAF | — |  |
| Contribution due par les entreprises exploitant des médicaments bénéficiant d'une AMM / Contribution sur le chiffre d'affaires des entreprises exploitant une ou plusieurs spécialités pharmaceutiques | CNAMTS | 0.51 |  |
| Droit de licence sur la rémunération des débitants de tabacs | CNAMTS | 0.37 |  |
| Contribution due par les laboratoires et les grossistes répartiteurs sur les ventes en gros aux officines pharmaceutiques | CNAMTS | 0.25 |  |
| Contribution due par les laboratoires sur leurs dépenses de publicité | CNAMTS | 0.13 |  |
| Droits perçus au profit de la Caisse nationale de l'assurance maladie des travailleurs salariés (CNAMTS) en matière de produits de santé, taxe annuelle due par les laboratoires de biologie médicale | CNAMTS | 0.09 |  |
| Contribution due par les entreprises fabriquant ou exploitant des dispositifs médicaux sur leurs dépenses de publicité | CNAMTS | 0.05 |  |
| Contribution exceptionnelle des organismes complémentaires en santé aux dépenses liées à la gestion de l'épidémie de Covid-19 | CNAMTS | — |  |
| Contribution sociale à la charge des fournisseurs agréés de produits de tabac | CNAMTS - Fonds tabacs | — |  |
| Contribution sur les régimes de retraite conditionnant la constitution de droits à prestations à l’achèvement de la carrière du bénéficiaire dans l’entreprise | CNAMTS, CNAVTS, CCMSA (non salariés-maladie) en 2016; CNAVTS dès 2017 | 0.22 |  |
| Contribution sur les avantages de préretraite d’entreprise | CNAMTS, CNAVTS, CCMSA (non salariés-maladie) en 2016; CNAVTS dès 2017 | 0.05 |  |
| Contribution sur les indemnités de mise à la retraite | CNAMTS, CNAVTS, CCMSA (non salariés-maladie) en 2016; CNAVTS dès 2017 | 0.03 |  |
| Redevances UMTS 2G et 3G | CNAMTS, CNAVTS, CCMSA (non salariés-maladie) en 2016; CNAVTS dès 2017 | 0.01 |  |
| Redevance due par les titulaires de titres d'exploitation de mines d'hydrocarbures liquides ou gazeux | CNAMTS, CNAVTS, CCMSA (non salariés-maladie) en 2016; CNAVTS dès 2017 | 0.00 |  |
| Contribution équivalente aux droits de plaidoirie | CNBF - Caisse nationale des barreaux français | 0.11 |  |
| Droits de plaidoirie | CNBF - Caisse nationale des barreaux français | 0.00 |  |
| TST - Taxe sur les éditeurs et distributeurs de services de télévision - Fraction Editeurs | CNC - Centre national du cinéma et de l'image animée | 0.25 |  |
| TST - Taxe sur les éditeurs et distributeurs de services de télévision - Fraction Distributeurs | CNC - Centre national du cinéma et de l'image animée | 0.20 |  |
| TSA - Taxe sur le prix des entrées aux séances organisées par les exploitants d’établissements de spectacles cinématographiques | CNC - Centre national du cinéma et de l'image animée | 0.14 |  |
| Taxe sur les ventes et les locations de vidéogrammes destinés à l'usage privé du public (taxe vidéo et VOD ) | CNC - Centre national du cinéma et de l'image animée | 0.13 |  |
| Cotisations (normale et supplémentaire) des entreprises cinématographiques | CNC - Centre national du cinéma et de l'image animée | 0.01 |  |
| Taxe sur les spectacles de variétés | CNM - Centre national de la musique | 0.03 | LFI 2012 |
| Contribution solidarité autonomie (CSA) | CNSA | 2.38 |  |
| Contribution additionnelle de solidarité autonomie (CASA) | CNSA | 0.86 |  |
| Droit de consommation sur les tabacs dans les DOM | Collectivité territoriale de Corse et Conservatoire de l'espace littoral, de 2007 à 2011 | 0.14 |  |
| Droit annuel de francisation et de navigation en Corse; droit de passeport en Corse | Collectivité territoriale de Corse et Conservatoire de l'espace littoral, de 2007 à 2011 | 0.00 |  |
| Droit d'octroi de mer et droit d'octroi de mer régional | Collectivités territoriales des DOM | 1.37 |  |
| Taxe pour le développement des industries de l'habillement | Comité de développement et de promotion de l'habillement - DEFI | 0.01 |  |
| Taxe sur les installations de production d'électricité utilisant l'énergie mécanique du vent situées dans les eaux intérieures ou la mer territoriale | Comités départementaux et interdépartementaux des pêches maritimes et des élevages marins | — |  |
| Impôt sur les spectacles, jeux et divertissements | Communes | 0.16 |  |
| Taxe de balayage | Communes | 0.11 |  |
| Surtaxe sur les eaux minérales | Communes | 0.02 |  |
| Taxe sur les déchets réceptionnés dans une installation de stockage ou un incinérateur de déchets ménagers | Communes | 0.02 |  |
| Taxe pour non-raccordement à l'égout - Participation pour le financement de l'assainissement collectif (PAC) | Communes | 0.00 |  |
| Fraction du Prélèvement sur les mises de jeux de cercle en ligne affectée aux communes dans le ressort territorial desquelles sont ouverts au public un ou plusieurs casinos | Communes concernées | 0.01 |  |
| Redevance proportionnelle sur l'énergie hydraulique | Communes et départements (part départementale) | 0.00 |  |
| TA-TINB - Taxe additionnelle à la taxe sur les installations nucléaires de base dite "de stockage" | Communes et EPCI (établissements publics de coopération intercommunale) situés dans un rayon maximal autour de l'accès principal aux installations de stockage | 0.00 |  |
| Prélèvement progressif sur le produit des jeux dans les casinos au profit des communes | Communes ou EPCI (établissements publics de coopération intercommunale à fiscalité propre) - part communale | 0.26 |  |
| Taxe de séjour, taxe de séjour forfaitaire | Communes ou EPCI (établissements publics de coopération intercommunale à fiscalité propre) - part communale | 0.16 |  |
| Taxes sur les friches commerciales | Communes ou EPCI (établissements publics de coopération intercommunale à fiscalité propre) - part communale | — |  |
| Taxe de ski de fond | Communes ou EPCI (établissements publics de coopération intercommunale à fiscalité propre) - part intercommunale | 0.00 |  |
| Taxes dans le domaine funéraire | Communes ou EPCI (établissements publics de coopération intercommunale) à fiscalité propre | 0.00 |  |
| Versement pour sous-densité | Communes ou EPCI (établissements publics de coopération intercommunale) à fiscalité propre et Départements | 0.00 |  |
| Taxe sur les remontées mécaniques | Communes ou EPCI (établissements publics de coopération intercommunale) à fiscalité propre et Départements - part communale | 0.01 |  |
| Redevances communale et départementale des mines | Communes ou EPCI (établissements publics de coopération intercommunale) à fiscalité propre et Départements - part départementale | 0.01 |  |
| Taxe communale sur la consommation finale d'électricité (TCFE) | Communes ou EPCI (établissements publics de coopération intercommunale) à fiscalité propre et Départements - part intercommunale | 0.02 |  |
| Taxes locales d'équipement | Communes ou Groupements de communes (parts communale et intercommunale) | 0.03 |  |
| TA-CFE - fraction CRMA de la Taxe additionnelle à la cotisation foncière des entreprises pour frais de chambre régionale de métiers et d'artisanat | CRMA (incl. Alsace et Moselle) | 0.24 | LFR 2017 et LFI 2018 |
| Participation au financement de la formation- Fraction affectée aux CMA pour leurs actions de formation | CRMA (incl. Alsace et Moselle) | 0.03 |  |
| Taxe pour le développement des industries du cuir, de la maroquinerie, de la ganterie et de la chaussure | CTC - Comité professionnel de développement Cuir, Chaussure, Maroquinerie | 0.02 |  |
| Taxe pour le développement de l'industrie de la conservation des produits agricoles (CTCPA) | CTCPA - Centre technique de la conservation des produits agricoles | 0.00 | LFI 2012 |
| Taxe pour le développement des industries de la mécanique et de la construction métallique, des matériels et consommables de soudage et produits du décolletage, de construction métallique et des matériels aérauliques et thermiques | CTI de l'Industrie : CT des indus. mécaniques (CETIM), CT de l'industrie du décolletage (CTDEC), CTI de la construction métallique (CTICM), CT des indus. aérauliques et thermiques (CETIAT), et Institut de Soudure | 0.10 |  |
| Taxe pour le développement des industries de l'ameublement ainsi que des industries du bois | CTI de la filière Bois - Comité professionnel de développement des industries françaises de l'ameublement et du bois (CODIFAB); Institut technologique FCBA (Filière cellulose, bois, ameublement); Centre technique de la mécanique (CETIM) | 0.02 |  |
| Taxe pour le développement des industries des matériaux de construction regroupant les industries du béton, de la terre cuite et des roches ornementales et de construction | CTI des matériaux : Centre d'étude et de recherche de l'industrie du béton (CERIB); Centre technique de matériaux naturels de construction (CTMNC) | 0.01 |  |
| Taxe sur les produits de la fonderie | CTIF - Centre technique des industries de la fonderie | 0.01 |  |
| Taxe départementale de publicité foncière sur les mutations à titres onéreux | Départements (part départementale) | 14.57 |  |
| Taxe intérieure de consommation sur les produits énergétique (TICPE) - Fractions transférées en compensation du transfert du RMI/RSA et dans le cadre de l'acte II de la décentralisation | Départements (part départementale) | 5.10 |  |
| Droits départementaux d'enregistrement sur les mutations à titre onéreux d'immeubles | Départements (part départementale) | 0.50 |  |
| Taxe départementale additionnelle à certains droits d'enregistrement | Départements (part départementale) | 0.15 |  |
| Droit départemental de passage sur les ouvrages d'art reliant le continent aux îles maritimes | Départements (part départementale) | 0.03 |  |
| Taxe additionnelle départementale à la taxe de séjour | Départements (part départementale) | 0.02 |  |
| Taxe départementale des espaces naturels sensibles | Départements (part départementale) | — |  |
| Droits de consommation sur les tabacs (DOM) | Départements d'Outre-mer | 0.14 |  |
| Taxe départementale sur la consommation finale d'électricité (TCFE) | Départements et métropole de Lyon | 0.72 |  |
| Fraction du Prélèvement sur les paris hippiques affectée aux EPCI sur le territoire desquelles sont ouverts au public un ou plusieurs hippodromes (affectée jusqu'aux mises 2012 versées en 2013 aux Communes concernées) | EPCI concernés - Etablissements publics de coopération intercommunale à fiscalité propre (Communes concernées jusqu'en 2012) | 0.01 |  |
| Taxes spéciales d'équipement | Etablissement public foncier de Mayotte | 0.00 | LFR 2016 et LFI 2017 |
| Contribution forfaitaire des organismes assureurs et contribution forfaitaire des organismes participant à la gestion du régime prévu par la loi n° 2001-1128 du 30 novembre 2001 | FCATA (Fonds commun des accidents du travail agricole) jusqu'en 2016; CCMSA en 2017 | 0.00 |  |
| Contribution des assurés | FGAO - Fonds de garantie des assurances obligatoires de dommages | 0.10 |  |
| Prélèvement sur les contrats d'assurance de biens | FGTI - Fonds de garantie des victimes d'actes terroristes et autres infractions | 0.58 |  |
| Cotisation des employeurs | FNAL - Fonds national d'aide au logement | 2.89 |  |
| Taxe sur les plus-values immobilières (PVI) autres que terrains à bâtir | FNAL - Fonds national d'aide au logement | — |  |
| Cotisation additionnelle versée par les organismes HLM et les SEM | FNAVDL - Fonds national d’accompagnement vers et dans le logement | — |  |
| Contributions additionnelles aux primes ou cotisations afférentes à certaines conventions d'assurance | FNGRA - Fonds national de gestion des risques en agriculture et fonds de calamités agricoles dans les départements d'outre-mer | 0.12 | LFR 2015 et de la LFI 2016 |
| Fraction du prélèvement sur les jeux de loterie correspondant aux jeux dédiés au patrimoine | Fondation du patrimoine | 0.03 |  |
| Fraction du produit des successions en déshérence | Fondation du patrimoine | — |  |
| Fraction de Taxe de solidarité additionnelle (TSA) | Fonds CMU - Fonds de financement de la protection complémentaire de la couverture universelle du risque maladie | — |  |
| Droit affecté au fonds d’indemnisation de la profession d’avoués près les cours d’appel | Fonds d'indemnisation de la profession d'avoués près les cours d'appel | 0.03 |  |
| Contribution conventionnelle à la formation pour les entreprises de travail temporaire | Fonds pour l'emploi du travail temporaire | 0.07 |  |
| Contribution supplémentaire à l'apprentissage | France Compétences | 0.23 |  |
| Contribution spécifique à la formation professionnelle pour Saint Pierre et Miquelon | France Compétences | 0.00 |  |
| Redevances sur les paris hippiques | France Galop et la société d’encouragement à l’élevage du cheval français (SECF) | 0.08 |  |
| Taxe pour le développement des industries de l'horlogerie, bijouterie, joaillerie, orfèvrerie et arts de la table | Francéclat | 0.01 |  |
| Taxe sur les transactions financières - fraction affectée de la ressource État | FSD - Fonds de solidarité pour le développement géré par l'Agence française de développement (AFD) - suivi MEF | 0.25 | LFI 2013 et de la LFR-III 2012 |
| Contribution annuelle acquittée par les personnes inscrites comme commissaires aux comptes, et droit fixe sur chaque rapport de certification des comptes, et contribution de la compagnie nationale des commissaires aux comptes | H3C - Haut conseil du commissariat aux comptes | 0.02 | LFR 2017 et LFI 2018 |
| Droit sur les produits bénéficiant d'une appellation d'origine ou d'une indication géographique protégée (INAO) | INAO - Institut national de l'origine et de la qualité | 0.01 | LFI 2012 |
| Redevances perçues à l'occasion des procédures et formalités en matière de propriété industrielle ainsi que de registre du commerce et des sociétés, établies par divers textes | INPI - Institut national de la propriété industrielle | 0.18 | LFI 2021 |
| Contribution annuelle au profit de l'Institut de radioprotection et de sûreté nucléaire | IRSN - Institut de radioprotection et de sûreté nucléaire | 0.06 | LFR 2015 et de la LFI 2016 |
| Taxe affectée au financement de l'institut des corps gras | ITERG - Institut des corps gras | 0.00 |  |
| Redevance pour délivrance initiale du permis de chasse | OFB - Office français de la biodiversité | 0.00 |  |
| Droit d'examen du permis de chasse | OFB - Office français de la biodiversité | 0.00 |  |
| Redevances pour prélèvement sur la ressource en eau, pour pollution de l'eau, pour modernisation des réseaux de collecte, pour pollutions diffuses, pour stockage d'eau en période d'étiage, pour obstacle sur les cours d'eau et pour protection du milieu aquatique dans les DOM | Offices de l'eau (dans les DOM) | 0.03 |  |
| Redevance perçue à l’occasion de l’introduction des familles étrangères en France | OFII - Office français de l'immigration et de l'intégration | 0.00 |  |
| Taxe annuelle sur les engins maritimes à usage personnel (TAEMUP) | Organismes de secours et de sauvetage en mer agréés (art. L742-9 code de la sécurité intérieure) | 0.00 | LFR 2017 et LFI 2018 |
| Taxe annuelle sur les engins maritimes à usage personnel (TAEMUP) – Fraction perçue sur les engins ne battant pas pavillon français | Organismes de secours et de sauvetage en mer agréés (art. L742-9 code de la sécurité intérieure) | 0.00 | LFR 2017 et LFI 2018 |
| Taxe sur les passagers maritimes embarqués à destination d'espaces naturels protégés | Personne publique assurant la gestion de l'espace naturel protégé concerné ou la commune d'implantation de l'espace naturel protégé | 0.00 |  |
| Taxe d'aéroport | Personnes publiques ou privées exploitant des aérodromes dont le trafic embarqué ou débarqué s'élève au cours de la dernière année civile connue à plus de 5000 unités de trafic (UDT) | 0.93 |  |
| Taxe sur les nuisances sonores aériennes | Personnes publiques ou privées exploitant des aérodromes pour lesquels : - le nombre annuel des mouvements d'aéronefs de masse maximale au décollage supérieure ou égale à 20 tonnes a dépassé 20 000 lors de l'une des cinq années civiles précédentes, - ou le nombre annuel des mouvements d'aéronef de masse maximale au décollage supérieure ou égale à 2 tonnes a dépassé 50 000 lors de l'une des 5 années civiles précédentes, si les plans d'exposition au bruit ou de gêne sonore de cet aérodrome possèdent un domaine d'intersection avec les plans d'exposition au bruit ou de gêne sonore d'un aérodrome présentant les caractéristiques définies au tiret précédent. | 0.04 | LFI 2014 |
| Taxe due par les concessionnaires de mines d'or, les amodiataires des concessions de mines d'or et les titulaires de permis et d'autorisations d'exploitation de mines d'or exploitées en Guyane (taxe additionnelle aurifère) | Région de la Guyane | 0.00 |  |
| Redevance pour création de bureaux ou de locaux de recherche en région Ile-de-France | Région Ile-de-France | — |  |
| Taxe intérieure de consommation sur les produits énergétique (TICPE dont part modulable) | Régions | 4.66 |  |
| Taxe intérieure de consommation sur les produits énergétiques (TICPE) - part Grenelle | Régions | 0.56 |  |
| Taxe sur les permis de conduire | Régions | 0.00 |  |
| Taxe spéciale de consommation sur les carburants | Régions de la Guadeloupe, de la Martinique, de la Guyane et de la Réunion | 0.55 |  |
| Taxe due par les entreprises de transport public aérien et maritime sur les passagers embarqués | Régions de la Guadeloupe, de la Martinique, de la Guyane et de la Réunion | 0.03 |  |
| Droits assimilés au droit d'octroi de mer sur les rhums et spiritueux à base d'alcool de cru | Régions de la Guadeloupe, de la Martinique, de la Guyane et de la Réunion | 0.00 |  |
| Taxe annuelle sur les locaux à usage de bureaux, les locaux commerciaux, les locaux de stockage et les surfaces de stationnement annexées à ces catégories de locaux perçue dans la région Ile-de-France | SGP - Société du Grand Paris | 0.66 | LFI 2012 |
| Taxe spéciale d'équipement au profit de l'établissement public Société du Grand Paris | SGP - Société du Grand Paris | 0.07 | LFI 2012 |
| Taxe additionnelle régionale de 15% à la taxe de séjour IDF | SGP - Société du Grand Paris | 0.02 | LFI 2019 |
| Cotisation BTP intempéries | UCF CIBTP - Union des caisses de France | 0.13 |  |
| Redevance hydraulique | VNF - Voies navigables de France | 0.13 | LFI 2020 |

### 4.4 Nouvelles impositions du V&M Tome I (lignes 1xxx) à classer

15 impositions d'État détaillées au V&M, non encore présentes ailleurs : à qualifier (la plupart sont des PO d'État récents).

| Imposition | Ligne budgétaire |
|---|---|
| Retenues à la source sur certains bénéfices non commerciaux et de l'impôt sur le revenu | ligne 1401 |
| Retenues à la source et prélèvements sur les revenus de capitaux mobiliers et le prélèvement sur les bons anonymes | ligne 1402 |
| Prélèvements de solidarité | ligne 1427 |
| Taxe sur le patrimoine financier | ligne 1439 |
| Contribution différentielle applicable à certains contribuables titulaires de très hauts revenus | ligne 1440 |
| Contribution exceptionnelle sur les bénéfices des grandes entreprises | ligne 1441 |
| Taxe sur les petits colis | ligne 1442 |
| Recettes diverses | ligne 1499 |
| Contribution sur la rente infra-marginale de la production d'électricité | ligne 1752 |
| Produits des jeux exploités par la Française des jeux (hors paris sportifs) | ligne 1785 |
| Prélèvements sur le produit des jeux dans les casinos | ligne 1786 |
| Prélèvement sur le produit brut des paris hippiques | ligne 1787 |
| Prélèvement sur les paris sportifs | ligne 1788 |
| Prélèvement sur les jeux de cercle en ligne | ligne 1789 |
| Taxe sur les rachats d'actions | ligne 1796 |

## 5. Pistes et questions ouvertes

Chantiers identifiés pour la suite des recherches :

1. **Doublons** : les correspondances de même périmètre (« Foncier bâti » ↔ taxe foncière, « Mutations à titre gratuit » ↔ DMTG) sont désormais fusionnées via la colonne `alias` du socle. Les candidats résiduels du §4.1 sont des **composantes plus fines** (ex. accises ex-TICGN/TICFE) : à fusionner au cas par cas ou à conserver comme détail.
2. **Classification ESA** : la correspondance par préfixe (D29→D2, D51→D5…) reclasse désormais automatiquement les lignes NTL ; les codes encore non couverts (cf. catégorie « indéterminée » au §1) restent à compléter dans `esa_defaults`.
3. **Montants manquants** : 49 PRIS sont sans montant ; les renseigner depuis la NTL fiabiliserait la couverture.
4. **Base de mesure** : la couverture (105.8 %) dépasse 100 % car les montants NTL sont en base Eurostat (~45,3 % du PIB) alors que l'enveloppe de contrôle est INSEE (42,7 %). Décider d'une base de référence unique pour le suivi.
5. **Exhaustivité de l'État A** : le volume narratif du V&M ne détaille que les ~24 principaux impôts d'État ; les lignes mineures (1101→1799) sont agrégées (« Autres taxes », « Recettes diverses »). Si besoin, parser la table récapitulative formelle (État A) pour les ~300 lignes complètes.
6. **Taxes affectées** (§4.3) : confirmer le périmètre PO de chacune (certaines redevances pour service rendu sont à exclure au titre de C3).

## 6. Registre des sources et régénération

| Source | Rôle | Activée | URL |
|---|---|:--:|---|
| Eurostat — National Tax List (liste détaillée des impôts et cotisations, FR) | backbone | ✅ | https://ec.europa.eu/eurostat/statistics-explained/images/e/ef/National_tax_lists_2025_2026-04-22.xlsx |
| Évaluation des Voies et Moyens, Tome I — annexe au PLF 2026 | backbone | ✅ | https://www.assemblee-nationale.fr/dyn/dyn/contenu/visualisation/1087930/file/PLF%202026%20-%20V&M%20TI%20-%20Evaluations%20des%20recettes.pdf |
| V&M Tome I — liste des taxes affectées (data.economie.gouv.fr) | enrich | ✅ | https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/plf2024-v-and-m-t1-liste-des-taxes-affectees/exports/json |
| CPO — cartographie de la fiscalité affectée | control | — | https://www.data.gouv.fr/api/1/datasets/cartographie-de-la-fiscalite-affectee-selon-le-perimetre-retenu-pour-le-rapport-du-conseil-des-prele/ |
| REI — recensement des éléments d'imposition à la fiscalité directe locale | enrich | — | https://www.data.gouv.fr/api/1/datasets/impots-locaux-fichier-de-recensement-des-elements-dimposition-a-la-fiscalite-directe-locale-rei-4/ |
| Eurostat — Main national accounts tax aggregates (gov_10a_taxag) | control | ✅ | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/gov_10a_taxag?format=JSON&lang=EN&geo=FR&unit=MIO_EUR&sector=S13&na_item=D2&na_item=D5&na_item=D91&na_item=D61 |

**Socle curé** : `pipeline/seed/readme_inventory.csv` (issu du README racine, toujours intégré).
**Supplément curé** : `pipeline/seed/supplement.csv` — long tail de PO non détaillés par le README (composantes IFER/TGAP, taxes récentes du PLF 2026…), attestés par le CGI/CIBS et le V&M.

**Régénérer ce document :**

```bash
cd pipeline && make all      # fetch → … → report → workdoc
```
