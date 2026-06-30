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
| Retenus (PRIS) | 320 |
| Rejetés (REJET) | 39 |
| À arbitrer | 0 |
| Somme des PRIS (socle curé) | 1326.1 Md€ |
| Somme des PRIS (itemisé, indicatif) | 1572.0 Md€ |
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

320 prélèvements retenus, regroupés par secteur bénéficiaire et triés par montant décroissant.

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

### Administrations publiques locales (APUL) — 25 lignes, 90.45 Md€

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
| Taxe pour la gestion des eaux pluviales urbaines |  | — | CGCT art. L2333-97 | supplement_cure (supplément curé (CGI/CIBS, V&M PLF 2026)) |
| Taxe sur les logements vacants | TLV | — | CGI art. 232 | readme_seed (README §4-§5) |

### Union européenne — 3 lignes, 6.20 Md€

| Prélèvement | Sigle | Montant (Md€) | Base légale | Sources |
|---|---|---:|---|---|
| Ressource propre fondée sur la TVA |  | 3.00 | Décision ressources propres UE | readme_seed (README §4-§5) |
| Droits de douane |  | 2.00 | Code des douanes de l'Union | readme_seed (README §4-§5) |
| Contribution sur les emballages plastiques non recyclés |  | 1.20 | Décision ressources propres UE | readme_seed (README §4-§5) |

### Secteur à préciser — 247 lignes, 245.85 Md€

| Prélèvement | Sigle | Montant (Md€) | Base légale | Sources |
|---|---|---:|---|---|
| Taxe intérieure de consommation des produits énergétiques |  | 29.55 |  | eurostat_ntl (FR:D214A/C06) |
| Droits d'enregistrement (y compris taxe additionnelle) |  | 14.66 |  | eurostat_ntl (FR:D214C/C01) |
| Autres prélèvements sociaux |  | 14.65 |  | eurostat_ntl (FR:D51M/C06) |
| Taxe départementale de publicité foncière sur les mutations à titres onéreux |  | 14.57 |  | taxes_affectees |
| Taxes sur les tabacs |  | 13.61 |  | eurostat_ntl (FR:D214A/C10) |
| Droits de consommation sur les tabacs |  | 13.56 |  | taxes_affectees |
| Contributions des entreprises à la formation professionnelle et à l'apprentissage |  | 11.36 |  | eurostat_ntl (FR:D29C/C02) |
| Contributions pour le remboursement de la dette sociale (CRDS) |  | 8.72 |  | taxes_affectees |
| Taxe de solidarité additionnelle |  | 6.21 |  | eurostat_ntl (FR:D214G/C01) |
| Taxe intérieure de consommation sur les produits énergétique (TICPE) - Fractions transférées en compensation du transfert du RMI/RSA et dans le cadre de l'acte II de la décentralisation |  | 5.10 |  | taxes_affectees |
| Accise sur l'électricité |  | 4.80 |  | eurostat_ntl (FR:D214A/C07) |
| Taxes sur les boissons |  | 4.75 |  | eurostat_ntl (FR:D214A/C09) |
| Taxe intérieure de consommation sur les produits énergétique (TICPE dont part modulable) |  | 4.66 |  | taxes_affectees |
| Produits de la loterie nationale et du loto |  | 3.99 |  | eurostat_ntl (FR:D214F/C01) |
| Taxe intérieure sur la consommation de gaz naturel |  | 3.18 |  | eurostat_ntl (FR:D214A/C02) |
| Taxe sur les certificats d'immatriculation des véhicules |  | 3.12 | LFR-I 2014 et de la LFI 2015 | eurostat_ntl (FR:D214D/C01); taxes_affectees |
| Taxe communale additionnelle à certains droits d'enregistrement |  | 3.09 |  | taxes_affectees |
| Cotisation patronale pour le FNAL (Fonds national d'aide au logement) |  | 2.94 |  | eurostat_ntl (FR:D29C/C06) |
| Cotisation des employeurs |  | 2.89 |  | taxes_affectees |
| Impôt de solidarité sur la fortune (jusque 2017) / Impôt sur la fortune immobilière (à partir de 2018) |  | 2.68 |  | eurostat_ntl (FR:D59A/C02) |
| Part sur les salaires |  | 2.63 |  | eurostat_ntl (FR:D29A/C08) |
| Droits d'importation |  | 2.60 |  | eurostat_ntl (FR:D2121/C02) |
| Contribution de solidarité pour l'autonomie |  | 2.47 |  | eurostat_ntl (FR:D29C/C05) |
| Taxe sur les certificats d'immatriculation des véhicules (cartes grises) |  | 2.44 |  | taxes_affectees |
| Contribution solidarité autonomie (CSA) |  | 2.38 |  | taxes_affectees |
| Droits de consommation sur les alcools |  | 2.29 |  | taxes_affectees |
| Redevance pour obstacle sur les cours d’eau, redevance pour stockage d’eau en période d’étiage, redevance pour la protection du milieu aquatique, redevance pour pollutions diffuses, redevances pour prélèvement sur la ressource en eau, redevances pour pollution de l’eau, redevances pour modernisation des réseaux de collecte, redevances cynégétiques, droit de validation du permis de chasse |  | 2.20 | LFR 2015 et de la LFI 2016 | taxes_affectees |
| Taxe sur les émissions de CO2 |  | 2.11 |  | eurostat_ntl (FR:D29F/C02) |
| Fraction affectée du produit du relèvement du tarif de taxe intérieure de consommation sur les produits énergétiques (TICPE) sur le carburant gazole |  | 1.91 | LFR-I 2014 et de la LFI 2015 | taxes_affectees |
| Taxes sur les transports |  | 1.86 |  | eurostat_ntl (FR:D214H/C10) |
| Taxes sur les paris hippiques |  | 1.80 |  | eurostat_ntl (FR:D214F/C03) |
| Taxes sur les services professionnels hors droits de mutations |  | 1.76 |  | eurostat_ntl (FR:D214H/C09) |
| Cotisations sur primes d'assurance |  | 1.73 |  | eurostat_ntl (FR:D214G/C02) |
| Contribution tarifaire d'acheminement (CTA) |  | 1.70 |  | taxes_affectees |
| Participation des employeurs à l'effort de construction |  | 1.50 |  | eurostat_ntl (FR:D29C/C13) |
| Taxes au profit de l'Association sur la garantie des salaires |  | 1.47 |  | eurostat_ntl (FR:D29C/C04) |
| Taxes sur les jeux des casinos |  | 1.44 |  | eurostat_ntl (FR:D214F/C02) |
| Droit d'octroi de mer et droit d'octroi de mer régional |  | 1.37 |  | taxes_affectees |
| Part sur la consommation |  | 1.33 |  | eurostat_ntl (FR:D59A/C05) |
| Taxe sur primes d'assurance automobile |  | 1.25 |  | eurostat_ntl (FR:D214G/C05) |
| Part sur le capital |  | 1.24 |  | eurostat_ntl (FR:D29A/C09) |
| Taxes sur la construction |  | 1.19 |  | eurostat_ntl (FR:D214H/C08) |
| Droit sur les bières et les boissons non alcoolisées |  | 1.18 |  | taxes_affectees |
| Contribution sociale sur les bénéfices des sociétés |  | 1.17 |  | eurostat_ntl (FR:D51O/C06) |
| Taxe spéciale sur les conventions d'assurance automobile |  | 1.14 |  | taxes_affectees |
| Taxe sur construction de bureaux et sur les locaux à usage de bureaux |  | 1.05 |  | eurostat_ntl (FR:D29A/C16) |
| Contribution patronale sur stock-options |  | 1.03 |  | eurostat_ntl (FR:D29C/C10) |
| Autres taxes sur la pollution |  | 1.01 |  | eurostat_ntl (FR:D214A/C03) |
| Taxe sur les véhicules de tourisme des sociétés |  | 0.99 |  | eurostat_ntl (FR:D29B/C04) |
| Prélèvements sur les revenus des capitaux mobiliers |  | 0.97 |  | eurostat_ntl (FR:D51M/C08) |
| Taxes pharmaceutiques (contribution grossistes répartiteurs, taxe sur les ventes de médicaments et de cosmétiques) |  | 0.96 |  | eurostat_ntl (FR:D214I/C01) |
| Taxe d'aéroport |  | 0.93 |  | taxes_affectees |
| Contributions patronales et salariales sur les attributions d’options (stock-options) de souscription ou d’achat des actions et sur les attributions gratuites |  | 0.92 |  | taxes_affectees |
| Contribution additionnelle de solidarité autonomie (CASA) |  | 0.86 |  | taxes_affectees |
| Redevances sur les prélèvements de l'eau |  | 0.83 |  | eurostat_ntl (FR:D214H/C07) |
| Cotisation spéciale sur les boissons alcooliques |  | 0.76 |  | taxes_affectees |
| Taxe sur les véhicules de société (TVS) |  | 0.76 |  | taxes_affectees |
| Taxe départementale sur la consommation finale d'électricité (TCFE) |  | 0.72 |  | taxes_affectees |
| Cotisation des entreprises cinématographiques au profit du CNC (Centre national du cinéma) |  | 0.71 |  | eurostat_ntl (FR:D214E/C03) |
| Contribution de sécurité immobilière |  | 0.69 |  | eurostat_ntl (FR:D214B/C01) |
| Taxe due par les concessionnaires d'autoroutes |  | 0.68 | LFI 2012 | taxes_affectees |
| Retenue sur les bénéfices non commerciaux |  | 0.66 |  | eurostat_ntl (FR:D51O/C07) |
| Taxe annuelle sur les locaux à usage de bureaux, les locaux commerciaux, les locaux de stockage et les surfaces de stationnement annexées à ces catégories de locaux perçue dans la région Ile-de-France |  | 0.66 | LFI 2012 | taxes_affectees |
| Octroi de mer |  | 0.65 |  | eurostat_ntl (FR:D2121/C03) |
| Autres taxes sur l'énergie |  | 0.62 |  | eurostat_ntl (FR:D214A/C04) |
| Taxe sur les exploitants d'infrastructures de transports |  | 0.60 | LFI 2024 | taxes_affectees |
| Taxe sur les mises à disposition de produits pétroliers pour le stockage stratégique |  | 0.60 |  | eurostat_ntl (FR:D214A/C11) |
| Prélèvement sur les contrats d'assurance de biens |  | 0.58 |  | taxes_affectees |
| Taxe intérieure de consommation sur les produits énergétiques (TICPE) - part Grenelle |  | 0.56 |  | taxes_affectees |
| Taxe sur infrastructures de transport longues distances |  | 0.55 |  | eurostat_ntl (FR:D51O/C10) |
| Taxe spéciale de consommation sur les carburants |  | 0.55 |  | taxes_affectees |
| Produit de l'imposition chambre de commerce |  | 0.53 |  | eurostat_ntl (FR:D29A/C13) |
| Solde de la taxe d'apprentissage après prise en compte des versements directs des entreprises mentionnés au II de l'article L. 6241-2 |  | 0.52 |  | taxes_affectees |
| Contributions sur les loyers immobiliers |  | 0.51 |  | eurostat_ntl (FR:D214H/C04) |
| Contribution due par les entreprises exploitant des médicaments bénéficiant d'une AMM / Contribution sur le chiffre d'affaires des entreprises exploitant une ou plusieurs spécialités pharmaceutiques |  | 0.51 |  | taxes_affectees |
| Droits départementaux d'enregistrement sur les mutations à titre onéreux d'immeubles |  | 0.50 |  | taxes_affectees |
| Cotisation obligatoire |  | 0.49 |  | taxes_affectees |
| Taxe sur les boissons sucrées |  | 0.44 |  | taxes_affectees |
| Contribution des distributeurs d'énergie électrique basse tension |  | 0.38 |  | eurostat_ntl (FR:D214L/C02) |
| Droit de licence sur la rémunération des débitants de tabacs |  | 0.37 |  | taxes_affectees |
| Imposition sur les pylônes |  | 0.35 |  | eurostat_ntl (FR:D29A/C15) |
| Cotisation versée par les organismes HLM et les SEM |  | 0.34 |  | taxes_affectees |
| Fraction des droits de timbre sur les passeports sécurisés |  | 0.30 | LFI 2012 | taxes_affectees |
| Taxe additionnelle à la taxe foncière sur les propriétés non baties, pour frais de chambres d'agriculture (TCA-TFPNB) |  | 0.29 | LFI 2013 et de la LFR-III 2012 | taxes_affectees |
| TA-CFE - fraction CCI-R de la Taxe additionnelle à la cotisation foncière des entreprises pour frais de chambres de commerce et d’industrie de région |  | 0.28 | LFI 2013 et de la LFR-III 2012 | taxes_affectees |
| TA-CVAE - Taxe additionnelle à la cotisation sur la valeur ajoutée des entreprises pour frais de chambres de commerce et d'industrie de région |  | 0.27 | LFI 2013 et de la LFR-III 2012 | taxes_affectees |
| Prélèvement progressif sur le produit des jeux dans les casinos au profit des communes |  | 0.26 |  | taxes_affectees |
| Taxe sur les transactions financières - fraction affectée de la ressource État |  | 0.25 | LFI 2013 et de la LFR-III 2012 | taxes_affectees |
| Contribution due par les laboratoires et les grossistes répartiteurs sur les ventes en gros aux officines pharmaceutiques |  | 0.25 |  | taxes_affectees |
| Prélèvement sur les jeux exploités par la FdJ hors paris sportifs |  | 0.25 | LFI 2012 | taxes_affectees |
| TST - Taxe sur les éditeurs et distributeurs de services de télévision - Fraction Editeurs |  | 0.25 |  | taxes_affectees |
| TA-CFE - fraction CRMA de la Taxe additionnelle à la cotisation foncière des entreprises pour frais de chambre régionale de métiers et d'artisanat |  | 0.24 | LFR 2017 et LFI 2018 | taxes_affectees |
| Taxe due par les opérateurs de communications électroniques |  | 0.24 |  | eurostat_ntl (FR:D214H/C11) |
| Contribution supplémentaire à l'apprentissage |  | 0.23 |  | taxes_affectees |
| Chambre d'agriculture |  | 0.23 |  | eurostat_ntl (FR:D29A/C17) |
| Contributions pour frais de contrôle |  | 0.22 | LFI 2014 | taxes_affectees |
| Contribution sur les régimes de retraite conditionnant la constitution de droits à prestations à l’achèvement de la carrière du bénéficiaire dans l’entreprise |  | 0.22 |  | taxes_affectees |
| Taxe chambre métier |  | 0.21 |  | eurostat_ntl (FR:D29A/C14) |
| TST - Taxe sur les éditeurs et distributeurs de services de télévision - Fraction Distributeurs |  | 0.20 |  | taxes_affectees |
| Redevances perçues à l'occasion des procédures et formalités en matière de propriété industrielle ainsi que de registre du commerce et des sociétés, établies par divers textes |  | 0.18 | LFI 2021 | taxes_affectees |
| Prélèvement sur les paris sportifs en ligne de la FdJ et des nouveaux opérateurs agréés |  | 0.18 | LFI 2012 | taxes_affectees |
| Impôt sur les spectacles, jeux et divertissements |  | 0.16 |  | taxes_affectees |
| Taxe de séjour, taxe de séjour forfaitaire |  | 0.16 |  | taxes_affectees |
| Taxe spéciale sur les véhicules routiers (taxe à l'essieu) |  | 0.15 |  | eurostat_ntl (FR:D29B/C02) |
| Taxe départementale additionnelle à certains droits d'enregistrement |  | 0.15 |  | taxes_affectees |
| Autres taxes sur le revenu |  | 0.14 |  | eurostat_ntl (FR:D51E/C01) |
| Droit de consommation sur les tabacs dans les DOM |  | 0.14 |  | taxes_affectees |
| Droits de consommation sur les tabacs (DOM) |  | 0.14 |  | taxes_affectees |
| TSA - Taxe sur le prix des entrées aux séances organisées par les exploitants d’établissements de spectacles cinématographiques |  | 0.14 |  | taxes_affectees |
| Contribution due par les laboratoires sur leurs dépenses de publicité |  | 0.13 |  | taxes_affectees |
| Taxe sur les ventes et les locations de vidéogrammes destinés à l'usage privé du public (taxe vidéo et VOD ) |  | 0.13 |  | taxes_affectees |
| Cotisation BTP intempéries |  | 0.13 |  | taxes_affectees |
| Redevance hydraulique |  | 0.13 | LFI 2020 | taxes_affectees |
| Contribution sur les rentes infra marginales (électricité) |  | 0.13 |  | eurostat_ntl (FR:D29H/C05) |
| Contributions additionnelles aux primes ou cotisations afférentes à certaines conventions d'assurance |  | 0.12 | LFR 2015 et de la LFI 2016 | taxes_affectees |
| Droits et contributions pour frais de contrôle |  | 0.12 | LFI 2014 | taxes_affectees |
| Taxe de balayage |  | 0.11 |  | taxes_affectees |
| Contribution équivalente aux droits de plaidoirie |  | 0.11 |  | taxes_affectees |
| Droit de circulation sur les vins, cidres, poirés et hydromels |  | 0.11 |  | taxes_affectees |
| Contribution des assurés |  | 0.10 |  | taxes_affectees |
| Fraction des produits annuels de la vente de biens confisqués |  | 0.10 | LFI 2012 | taxes_affectees |
| Taxes sur les spectacles |  | 0.10 |  | eurostat_ntl (FR:D214E/C02) |
| Droits perçus au profit de la Caisse nationale de l'assurance maladie des travailleurs salariés (CNAMTS) en matière de produits de santé, taxe annuelle due par les laboratoires de biologie médicale |  | 0.09 |  | taxes_affectees |
| Contribution spéciale pour la gestion des déchets radioactifs - Conception |  | 0.08 |  | taxes_affectees |
| Contribution conventionnelle à la formation pour les entreprises de travail temporaire |  | 0.07 |  | taxes_affectees |
| Taxe spéciale d'équipement au profit de l'établissement public Société du Grand Paris |  | 0.07 | LFI 2012 | taxes_affectees |
| Taxe additionnelle à la taxe sur les installations nucléaires de base - Recherche |  | 0.07 | LFI 2012 | taxes_affectees |
| Contribution annuelle au profit de l'Institut de radioprotection et de sûreté nucléaire |  | 0.06 | LFR 2015 et de la LFI 2016 | taxes_affectees |
| Droit de consommation sur les produits intermédiaires |  | 0.06 |  | taxes_affectees |
| Contribution sur la cession à un service de télévision des droits de diffusion de manifestations ou de compétitions sportives |  | 0.06 | LFI 2012 | taxes_affectees |
| Redevance cynégétique (permis de chasse) |  | 0.06 |  | eurostat_ntl (FR:D59D/C04) |
| Contribution due par les entreprises fabriquant ou exploitant des dispositifs médicaux sur leurs dépenses de publicité |  | 0.05 |  | taxes_affectees |
| Contribution spécifique pour le développement de la formation professionnelle initiale et continue dans les métiers des professions du bâtiment et des travaux publics. |  | 0.05 |  | taxes_affectees |
| Contribution sur les avantages de préretraite d’entreprise |  | 0.05 |  | taxes_affectees |
| Taxe due par les entreprises de transport public aérien et maritime (Corse, DOM) |  | 0.05 |  | eurostat_ntl (FR:D29B/C05); taxes_affectees |
| Droit annuel de francisation et de navigation |  | 0.04 |  | eurostat_ntl (FR:D59D/C02) |
| Taxe sur les nuisances sonores aériennes |  | 0.04 | LFI 2014 | taxes_affectees |
| Taxe sur les boissons édulcorées |  | 0.04 |  | taxes_affectees |
| Droit départemental de passage sur les ouvrages d'art reliant le continent aux îles maritimes |  | 0.03 |  | taxes_affectees |
| Taxe due par les entreprises de transport public aérien et maritime sur les passagers embarqués |  | 0.03 |  | taxes_affectees |
| Participation au financement de la formation- Fraction affectée aux CMA pour leurs actions de formation |  | 0.03 |  | taxes_affectees |
| Taxe sur les spectacles de variétés |  | 0.03 | LFI 2012 | taxes_affectees |
| Contribution sur les indemnités de mise à la retraite |  | 0.03 |  | taxes_affectees |
| Redevances pour prélèvement sur la ressource en eau, pour pollution de l'eau, pour modernisation des réseaux de collecte, pour pollutions diffuses, pour stockage d'eau en période d'étiage, pour obstacle sur les cours d'eau et pour protection du milieu aquatique dans les DOM |  | 0.03 |  | taxes_affectees |
| Taxe de risque systémique |  | 0.03 |  | eurostat_ntl (FR:D59F/C02) |
| Droit affecté au fonds d’indemnisation de la profession d’avoués près les cours d’appel |  | 0.03 |  | taxes_affectees |
| Taxes locales d'équipement |  | 0.03 |  | taxes_affectees |
| Fraction des droits de timbre sur les cartes nationales d'identité |  | 0.02 | LFI 2012 | taxes_affectees |
| Taxe sur la cession à titre onéreux des terrains nus ou des droits relatifs à des terrains nus rendus constructibles du fait de leur classement |  | 0.02 | LFI 2013 et de la LFR-III 2012 | taxes_affectees |
| Surtaxe sur les eaux minérales |  | 0.02 |  | taxes_affectees |
| Taxe additionnelle régionale de 15% à la taxe de séjour IDF |  | 0.02 | LFI 2019 | taxes_affectees |
| Taxe communale sur la consommation finale d'électricité (TCFE) |  | 0.02 |  | taxes_affectees |
| Taxe additionnelle départementale à la taxe de séjour |  | 0.02 |  | taxes_affectees |
| Taxe sur les déchets réceptionnés dans une installation de stockage ou un incinérateur de déchets ménagers |  | 0.02 |  | taxes_affectees |
| Contribution annuelle acquittée par les personnes inscrites comme commissaires aux comptes, et droit fixe sur chaque rapport de certification des comptes, et contribution de la compagnie nationale des commissaires aux comptes |  | 0.02 | LFR 2017 et LFI 2018 | taxes_affectees |
| Taxe sur les Titres de séjour et de voyage electroniques |  | 0.02 | LFI 2012 | taxes_affectees |
| Redevances UMTS 2G et 3G |  | 0.01 |  | taxes_affectees |
| Cotisation versée par les organismes HLM |  | 0.01 | LFR-I 2014 et de la LFI 2015 | taxes_affectees |
| Fraction du Prélèvement sur les mises de jeux de cercle en ligne affectée aux communes dans le ressort territorial desquelles sont ouverts au public un ou plusieurs casinos |  | 0.01 |  | taxes_affectees |
| Fraction du Prélèvement sur les paris hippiques affectée aux EPCI sur le territoire desquelles sont ouverts au public un ou plusieurs hippodromes (affectée jusqu'aux mises 2012 versées en 2013 aux Communes concernées) |  | 0.01 |  | taxes_affectees |
| Redevances communale et départementale des mines |  | 0.01 |  | taxes_affectees |
| Cotisations (normale et supplémentaire) des entreprises cinématographiques |  | 0.01 |  | taxes_affectees |
| Droit de timbre pour la délivrance du permis de conduire en cas de perte ou de vol |  | 0.01 | LFI 2012 | taxes_affectees |
| Autres taxes |  | 0.01 |  | eurostat_ntl (FR:D2122C/C01); vm_tome1 (ligne 1799) |
| Taxe relative à la mise sur le marché des produits phytopharmaceutiques et de leurs adjuvants, des matières fertilisantes et de leurs adjuvants et des supports de culture |  | 0.01 | LFR 2016 et LFI 2017 | taxes_affectees |
| Prélèvement sur la participation des employeurs à l'effort de construction (PEEC) |  | 0.01 | LFR-I 2014 et de la LFI 2015 | taxes_affectees |
| Droit sur les produits bénéficiant d'une appellation d'origine ou d'une indication géographique protégée (INAO) |  | 0.01 | LFI 2012 | taxes_affectees |
| Taxe sur les remontées mécaniques |  | 0.01 |  | taxes_affectees |
| Fraction des Prélèvements sociaux sur les jeux prévus aux art. L137-20 à L137-22 du Code de la sécurité sociale |  | 0.01 | LFI 2012 | taxes_affectees |
| Droits de plaidoirie |  | 0.00 |  | taxes_affectees |
| Droit annuel de francisation et de navigation en Corse; droit de passeport en Corse |  | 0.00 |  | taxes_affectees |
| Taxe liée aux dossiers de demande concernant les médicaments vétérinaires ou leur publicité |  | 0.00 | LFR 2016 et LFI 2017 | taxes_affectees |
| Taxe annuelle sur la vente des produits phytopharmaceutiques |  | 0.00 | LFR-I 2014 et de la LFI 2015 | taxes_affectees |
| Taxe annuelle portant sur les autorisations de médicaments vétérinaires et les autorisations d’établissements pharmaceutiques vétérinaires |  | 0.00 | LFR 2016 et LFI 2017 | taxes_affectees |
| Taxe annuelle sur les engins maritimes à usage personnel (TAEMUP) |  | 0.00 | LFR 2017 et LFI 2018 | taxes_affectees |
| Droits assimilés au droit d'octroi de mer sur les rhums et spiritueux à base d'alcool de cru |  | 0.00 |  | taxes_affectees |
| Contribution forfaitaire des organismes assureurs et contribution forfaitaire des organismes participant à la gestion du régime prévu par la loi n° 2001-1128 du 30 novembre 2001 |  | 0.00 |  | taxes_affectees |
| Redevance due par les titulaires de titres d'exploitation de mines d'hydrocarbures liquides ou gazeux |  | 0.00 |  | taxes_affectees |
| Taxe sur les passagers maritimes embarqués à destination d'espaces naturels protégés |  | 0.00 |  | taxes_affectees |
| TA-TINB - Taxe additionnelle à la taxe sur les installations nucléaires de base dite "de stockage" |  | 0.00 |  | taxes_affectees |
| Taxe de ski de fond |  | 0.00 |  | taxes_affectees |
| Taxe exceptionnelle de solidarité sur les hautes rémunérations |  | 0.00 |  | eurostat_ntl (FR:D29C/C11) |
| Taxe sur les exploitants de plateformes de mises en relation par voie électronique en vue de fournir certaines prestations de transport |  | 0.00 | LFI 2022 | taxes_affectees |
| Taxes spéciales d'équipement |  | 0.00 | LFR 2016 et LFI 2017 | taxes_affectees |
| Taxes dans le domaine funéraire |  | 0.00 |  | taxes_affectees |
| Redevance pour délivrance initiale du permis de chasse |  | 0.00 |  | taxes_affectees |
| Redevance perçue à l’occasion de l’introduction des familles étrangères en France |  | 0.00 |  | taxes_affectees |
| Redevance proportionnelle sur l'énergie hydraulique |  | 0.00 |  | taxes_affectees |
| Taxe due par les concessionnaires de mines d'or, les amodiataires des concessions de mines d'or et les titulaires de permis et d'autorisations d'exploitation de mines d'or exploitées en Guyane (taxe additionnelle aurifère) |  | 0.00 |  | taxes_affectees |
| Droit d'examen du permis de chasse |  | 0.00 |  | taxes_affectees |
| Taxe pour non-raccordement à l'égout - Participation pour le financement de l'assainissement collectif (PAC) |  | 0.00 |  | taxes_affectees |
| Contribution spécifique à la formation professionnelle pour Saint Pierre et Miquelon |  | 0.00 |  | taxes_affectees |
| Versement pour sous-densité |  | 0.00 |  | taxes_affectees |
| Taxe annuelle sur les engins maritimes à usage personnel (TAEMUP) – Fraction perçue sur les engins ne battant pas pavillon français |  | 0.00 | LFR 2017 et LFI 2018 | taxes_affectees |
| Taxe sur les permis de conduire |  | 0.00 |  | taxes_affectees |
| 3% dividendes |  | — |  | eurostat_ntl (FR:D51O/C08) |
| Accises sur les énergies (ex-TICFE) |  | — |  | vm_tome1 (ligne 1503) |
| Accises sur les énergies (ex-TICGN) |  | — |  | vm_tome1 (ligne 1502) |
| Achats d'énergies renouvelables à prix contractuels |  | — |  | eurostat_ntl (FR:D29H/C06) |
| Avoir fiscal distribué (négatif) |  | — |  | eurostat_ntl (FR:D51O/C02) |
| Avoir fiscal utilisé (positif) |  | — |  | eurostat_ntl (FR:D51M/C02) |
| Contribution au SRF (single resolution fund) |  | — |  | eurostat_ntl (FR:D29H/C04) |
| Contribution différentielle applicable à certains contribuables titulaires de très hauts revenus |  | — |  | vm_tome1 (ligne 1440) |
| Contribution exceptionnelle des organismes complémentaires en santé aux dépenses liées à la gestion de l'épidémie de Covid-19 |  | — |  | taxes_affectees |
| Contribution exceptionnelle sur les bénéfices des grandes entreprises |  | — |  | vm_tome1 (ligne 1441) |
| Contribution sociale à la charge des fournisseurs agréés de produits de tabac |  | — |  | taxes_affectees |
| Contribution sur la rente infra-marginale de la production d'électricité |  | — |  | vm_tome1 (ligne 1752) |
| Contribution temporaire de solidarité |  | — |  | eurostat_ntl (FR:D51O/C09) |
| Cotisation additionnelle versée par les organismes HLM et les SEM |  | — |  | taxes_affectees |
| Cotisation au profit des caisses d’assurances d’accidents agricoles d’Alsace-Moselle |  | — |  | taxes_affectees |
| Cotisation minimale de taxe professionnelle |  | — |  | eurostat_ntl (FR:D29A/C02) |
| Fonds de solidarité contribution des fonctionnaires |  | — |  | eurostat_ntl (FR:D51M/C05) |
| Fraction de Taxe de solidarité additionnelle (TSA) |  | — |  | taxes_affectees |
| Impôt forfaitaire annuel |  | — |  | eurostat_ntl (FR:D51O/C05) |
| Impôt sur les opérations traitées dans les bourses de valeurs |  | — |  | eurostat_ntl (FR:D214C/C02) |
| Produits des jeux exploités par la Française des jeux (hors paris sportifs) |  | — |  | vm_tome1 (ligne 1785) |
| Prélèvement sur le produit brut des paris hippiques |  | — |  | vm_tome1 (ligne 1787) |
| Prélèvement sur les jeux de cercle en ligne |  | — |  | vm_tome1 (ligne 1789) |
| Prélèvement sur les paris sportifs |  | — |  | vm_tome1 (ligne 1788) |
| Prélèvements de solidarité |  | — |  | vm_tome1 (ligne 1427) |
| Prélèvements et taxes compensatoires à l'importation |  | — |  | eurostat_ntl (FR:D2122B/C01) |
| Prélèvements sur le produit des jeux dans les casinos |  | — |  | vm_tome1 (ligne 1786) |
| Recettes diverses |  | — |  | vm_tome1 (ligne 1499) |
| Redevance pour création de bureaux ou de locaux de recherche en région Ile-de-France |  | — |  | taxes_affectees |
| Retenues à la source et prélèvements sur les revenus de capitaux mobiliers et le prélèvement sur les bons anonymes |  | — |  | vm_tome1 (ligne 1402) |
| Retenues à la source sur certains bénéfices non commerciaux et de l'impôt sur le revenu |  | — |  | vm_tome1 (ligne 1401) |
| TVA sur subventions |  | — |  | eurostat_ntl (FR:D29H/C03) |
| Taxe additionnelle sur les assurances automobile |  | — |  | eurostat_ntl (FR:D214G/C03) |
| Taxe annuelle sur les logements vacants |  | — |  | taxes_affectees |
| Taxe d'habitation |  | — |  | eurostat_ntl (FR:D59A/C03) |
| Taxe départementale des espaces naturels sensibles |  | — |  | taxes_affectees |
| Taxe exceptionnelle sur la réserve de capitalisation (exit-tax) |  | — |  | taxes_affectees |
| Taxe professionnelle |  | — |  | eurostat_ntl (FR:D29A/C05) |
| Taxe sur l'utilisation des voies navigables (dont taxe hydraulique) |  | — |  | eurostat_ntl (FR:D29A/C11) |
| Taxe sur le patrimoine financier |  | — |  | vm_tome1 (ligne 1439) |
| Taxe sur les déclarations et notifications de produit du tabac |  | — |  | taxes_affectees |
| Taxe sur les installations de production d'électricité utilisant l'énergie mécanique du vent situées dans les eaux intérieures ou la mer territoriale |  | — |  | taxes_affectees |
| Taxe sur les petits colis |  | — |  | vm_tome1 (ligne 1442) |
| Taxe sur les plus-values immobilières (PVI) autres que terrains à bâtir |  | — |  | taxes_affectees |
| Taxe sur les produits de tabac |  | — |  | taxes_affectees |
| Taxe sur les rachats d'actions |  | — |  | vm_tome1 (ligne 1796) |
| Taxe sur les véhicules (partie ménages) |  | — |  | eurostat_ntl (FR:D59D/C01) |
| Taxes au profit de l'ADEME (Agence de l'environnement et de la maîtrise de l'énergie) |  | — |  | eurostat_ntl (FR:D214A/C08) |
| Taxes au profit du FNDMA (Financement National de Développement et de Modernisation de l'Apprentissage) |  | — |  | eurostat_ntl (FR:D29C/C08) |
| Taxes sur les friches commerciales |  | — |  | taxes_affectees |
| Taxes sur les véhicules à moteur payées par les producteurs |  | — |  | eurostat_ntl (FR:D29B/C03) |
| Versement transport dû par les entreprises de plus de 9 salariés implantées en province |  | — |  | taxes_affectees |

## 3. Candidats rejetés (REJET)

39 candidats écartés, avec le critère en échec (C1 versement effectif, C2 bénéficiaire APU/UE, C3 obligatoire et sans contrepartie).

| Candidat | Critère | Note | Sources |
|---|---|---|---|
| Cotisations sociales imputées (fonctionnaires d'État) | C1 | Pas de versement effectif (employeur fictif). | readme_seed (README §4-§5) |
| Contribution des employeurs à l'association pour la gestion du régime d'assurance des créances des salariés (AGS) | C2 | Bénéficiaire hors périmètre APU (organisme de droit privé) — échec C2 (README §5). | taxes_affectees |
| Contribution annuelle au fonds de développement pour l'insertion professionnelle des handicapés (FIPH) | C2 | Bénéficiaire hors périmètre APU (organisme de droit privé) — échec C2 (README §5). | taxes_affectees |
| Contribution patronale au dialogue social (0,016%) | C2 | Bénéficiaire hors périmètre APU (organisme de droit privé) — échec C2 (README §5). | taxes_affectees |
| Taxe pour le développement des industries de la mécanique et de la construction métallique, des matériels et consommables de soudage et produits du décolletage, de construction métallique et des matériels aérauliques et thermiques | C2 | Bénéficiaire hors périmètre APU (organisme de droit privé) — échec C2 (README §5). | taxes_affectees |
| Redevances sur les paris hippiques | C2 | Bénéficiaire hors périmètre APU (organisme de droit privé) — échec C2 (README §5). | taxes_affectees |
| Taxe destinée à financer le développement des actions de formation professionnelle dans les transports routiers | C2 | Bénéficiaire hors périmètre APU (organisme de droit privé) — échec C2 (README §5). | taxes_affectees |
| Taxe pour le développement de la formation professionnelle dans les métiers de la réparation de l'automobile, du cycle et du motocycle | C2 | Bénéficiaire hors périmètre APU (organisme de droit privé) — échec C2 (README §5). | taxes_affectees |
| Fraction du prélèvement sur les jeux de loterie correspondant aux jeux dédiés au patrimoine | C2 | Bénéficiaire hors périmètre APU (organisme de droit privé) — échec C2 (README §5). | taxes_affectees |
| Taxe pour le développement des industries du cuir, de la maroquinerie, de la ganterie et de la chaussure | C2 | Bénéficiaire hors périmètre APU (organisme de droit privé) — échec C2 (README §5). | taxes_affectees |
| Taxe pour le développement des industries de l'ameublement ainsi que des industries du bois | C2 | Bénéficiaire hors périmètre APU (organisme de droit privé) — échec C2 (README §5). | taxes_affectees |
| Taxe pour le développement des industries des matériaux de construction regroupant les industries du béton, de la terre cuite et des roches ornementales et de construction | C2 | Bénéficiaire hors périmètre APU (organisme de droit privé) — échec C2 (README §5). | taxes_affectees |
| Taxe pour le développement des industries de l'horlogerie, bijouterie, joaillerie, orfèvrerie et arts de la table | C2 | Bénéficiaire hors périmètre APU (organisme de droit privé) — échec C2 (README §5). | taxes_affectees |
| Taxe pour le développement des industries de l'habillement | C2 | Bénéficiaire hors périmètre APU (organisme de droit privé) — échec C2 (README §5). | taxes_affectees |
| Taxe affectée au financement d’un nouveau Centre Technique Industriel de la plasturgie et des composites | C2 | Bénéficiaire hors périmètre APU (organisme de droit privé) — échec C2 (README §5). | taxes_affectees |
| Taxe sur les spectacles perçue au profit de l'Association pour le soutien du théâtre privé | C2 | Bénéficiaire hors périmètre APU (organisme de droit privé) — échec C2 (README §5). | taxes_affectees |
| Taxe sur les produits de la fonderie | C2 | Bénéficiaire hors périmètre APU (organisme de droit privé) — échec C2 (README §5). | taxes_affectees |
| Taxe pour le développement de l'industrie de la conservation des produits agricoles (CTCPA) | C2 | Bénéficiaire hors périmètre APU (organisme de droit privé) — échec C2 (README §5). | taxes_affectees |
| Taxe pour le développement des industries de fabrication du papier, du carton et de la pâte de cellulose. | C2 | Bénéficiaire hors périmètre APU (organisme de droit privé) — échec C2 (README §5). | taxes_affectees |
| Taxe affectée au financement de l'institut des corps gras | C2 | Bénéficiaire hors périmètre APU (organisme de droit privé) — échec C2 (README §5). | taxes_affectees |
| Cotisations aux ordres professionnels et syndicats | C2 | Bénéficiaire hors périmètre APU (organisme privé). | readme_seed (README §4-§5) |
| Fraction du produit des successions en déshérence | C2 | Bénéficiaire hors périmètre APU (organisme de droit privé) — échec C2 (README §5). | taxes_affectees |
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

0 lignes restent à classer. Elles sont pré-triées ci-dessous pour faciliter l'instruction.

### 4.1 Doublons probables d'un prélèvement déjà retenu

0 lignes ressemblent fortement à un PRIS existant (rapprochement automatique) : à **fusionner** (ajuster un libellé dans le socle, ou un alias dans `reconcile`).

| Ligne à arbitrer | Montant (Md€) | Ressemble au PRIS | Score | Source |
|---|---:|---|---:|---|

### 4.2 Lignes Eurostat NTL à rattacher ou classer

0 taxes/contributions individuelles de la NTL (code ESA + montant officiel) sans correspondance directe : confirmer le statut et, le cas échéant, l'affecter à une rubrique.

| Ligne | ESA | Montant (Md€) | Réf. | 
|---|---|---:|---|

### 4.3 Taxes affectées à instruire

0 taxes affectées (V&M Tome I) à confirmer comme PO et rattacher à un bénéficiaire. Triées par bénéficiaire.

| Taxe affectée | Bénéficiaire | Montant (Md€) | Base légale |
|---|---|---:|---|

### 4.4 Nouvelles impositions du V&M Tome I (lignes 1xxx) à classer

0 impositions d'État détaillées au V&M, non encore présentes ailleurs : à qualifier (la plupart sont des PO d'État récents).

| Imposition | Ligne budgétaire |
|---|---|

## 5. Pistes et questions ouvertes

Chantiers identifiés pour la suite des recherches :

1. **Doublons** : les correspondances de même périmètre (« Foncier bâti » ↔ taxe foncière, « Mutations à titre gratuit » ↔ DMTG) sont désormais fusionnées via la colonne `alias` du socle. Les candidats résiduels du §4.1 sont des **composantes plus fines** (ex. accises ex-TICGN/TICFE) : à fusionner au cas par cas ou à conserver comme détail.
2. **Classification ESA** : la correspondance par préfixe (D29→D2, D51→D5…) reclasse désormais automatiquement les lignes NTL ; les codes encore non couverts (cf. catégorie « indéterminée » au §1) restent à compléter dans `esa_defaults`.
3. **Montants manquants** : 82 PRIS sont sans montant ; les renseigner depuis la NTL fiabiliserait la couverture.
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
