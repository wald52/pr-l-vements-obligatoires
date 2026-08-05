# Les prélèvements obligatoires en France — recensement raisonné

> **Objet.** Ce document recense, de façon aussi exhaustive que possible, les
> prélèvements obligatoires (PO) en France. Conformément à la démarche demandée,
> il commence par **définir clairement ce qu'est un prélèvement obligatoire**,
> en tire une **règle de décision** (prendre / rejeter), puis applique cette
> règle à chaque candidat (impôt, taxe, cotisation, redevance, amende…).
>
> **Année de référence.** Montants 2024 (comptes nationaux INSEE
> semi-définitifs) ; liste des dispositifs reflétant le droit en vigueur mi-2026
> (loi de finances et loi de financement de la sécurité sociale pour 2026
> incluses). À titre indicatif, l'INSEE estime le taux **2025 (provisoire) à
> 43,6 % du PIB**.
>
> **Contenu.** 261 entrées retenues (§4), 44 candidats rejetés avec le critère qui
> les disqualifie (§5), 8 cas limites (§6) et une liste des prélèvements récemment
> supprimés (§7), pour ne pas les recompter. Les sources primaires — Voies et
> moyens tome I, état A et article 36 du PLF 2026, liste INSEE des ODAC, National
> Tax List d'Eurostat — ont été dépouillées ligne à ligne ; le contrôle de
> couverture est publié au §10. Le **jeu de données ligne à ligne** correspondant
> est dans [`data/`](data/) (437 prélèvements), produit par le
> [`pipeline/`](pipeline/) — voir §8.

---

## Sommaire

1. [Combien, et pour qui ?](#1-combien-et-pour-qui-)
2. [Définition : qu'est-ce qu'un prélèvement obligatoire ?](#2-définition--quest-ce-quun-prélèvement-obligatoire-)
3. [Règle de décision (prendre / rejeter)](#3-règle-de-décision-prendre--rejeter)
4. [Les prélèvements obligatoires retenus (PRIS)](#4-les-prélèvements-obligatoires-retenus-pris)
5. [Candidats examinés puis REJETÉS](#5-candidats-examinés-puis-rejetés)
6. [Cas limites et points de vigilance](#6-cas-limites-et-points-de-vigilance)
7. [Prélèvements récemment supprimés (mémoire)](#7-prélèvements-récemment-supprimés-mémoire)
8. [Du raisonnement au pipeline reproductible](#8-du-raisonnement-au-pipeline-reproductible)
9. [Sources](#9-sources)
10. [Pistes encore ouvertes](#10-pistes-encore-ouvertes)

Le raisonnement est dans ce document ; le **jeu de données ligne à ligne** est
dans [`data/`](data/), produit par le [`pipeline/`](pipeline/) — voir §8.

---

## 1. Combien, et pour qui ?

En 2024, les prélèvements obligatoires représentent **1 254 Md€, soit 42,7 % du
PIB** selon l'INSEE (45,3 % selon la mesure Eurostat, qui retraite différemment
les crédits d'impôt). La France reste le pays au taux le plus élevé de la zone
euro.

Répartition par sous-secteur d'administration bénéficiaire (en points de PIB,
2024) :

| Bénéficiaire | Poids (pts de PIB) | Exemples emblématiques |
|---|---|---|
| Administrations de sécurité sociale (ASSO) | ≈ 24,1 | Cotisations sociales, CSG, CRDS |
| État + organismes divers d'administration centrale (ODAC) | ≈ 14,2 | TVA, IR, IS, accises |
| Administrations publiques locales (APUL) | ≈ 6,4 | Taxe foncière, CFE, DMTO |
| Institutions de l'Union européenne | ≈ 0,2 | Droits de douane |

> La Sécurité sociale capte donc plus de la moitié des prélèvements obligatoires,
> l'État un petit tiers, les collectivités le reste.

> *Lecture du tableau.* La somme des poids par bénéficiaire (≈ 45 pts) dépasse
> légèrement le taux INSEE (42,7 %) : la ventilation est présentée **avant
> déduction des crédits d'impôt restituables**, sur une base proche de la mesure
> Eurostat (cf. §5.4, dernière ligne). L'ordre de grandeur et la hiérarchie des
> bénéficiaires restent inchangés.

**Et combien de prélèvements distincts ?** Il n'existe **aucun décompte officiel
unique**, et les ordres de grandeur publiés divergent d'un facteur cinq :

| Source | Décompte | Champ retenu |
|---|---|---|
| Ministère des Finances (2013) | ≈ 180 impôts | Hors petites taxes affectées à des agences |
| Inspection générale des finances (2014) | 192 taxes | **À faible rendement seulement** (< 150 M€) |
| Conseil des prélèvements obligatoires | ≈ 238 ressources affectées | Taxes affectées à des tiers (≈ 352 Md€ en 2022) |
| Fondation IFRAP (2015) | ≈ 360 taxes et impôts | Décompte large |
| Gilles Carrez, président de la commission des finances (2015) | « un millier » | Décompte maximaliste |
| Wikipédia, *Liste des impôts et taxes français* | 430 entrées : 3 européennes, ≈ 337 nationales et locales, 82 supprimées, 8 temporaires | Inclut des doublons et des dispositifs abrogés à tort ou à raison (cf. §7) |

L'écart n'est pas un désaccord factuel mais un **désaccord de découpage** : la
CSG compte-t-elle pour un prélèvement ou pour cinq (une par assiette) ? les
quatre fractions de l'accise sur les énergies pour une ou pour quatre ? La Cour
des comptes recommande depuis 2019 l'établissement d'un **inventaire annuel
exhaustif** des impôts et taxes à faible rendement ; il n'existe toujours pas.
Le présent document ne prétend donc pas à un décompte, mais à une **couverture
par famille**.

---

## 2. Définition : qu'est-ce qu'un prélèvement obligatoire ?

La notion est une convention de **comptabilité nationale**, harmonisée par
l'**OCDE** et appliquée en France par l'**INSEE**. Les prélèvements obligatoires
sont *« les impôts et cotisations sociales effectives reçus par les
administrations publiques et les institutions européennes, sans contrepartie
directe et immédiate »*.

Trois **critères cumulatifs** doivent être réunis. C'est l'absence de **l'un
seul** d'entre eux qui suffit à écarter un candidat.

| # | Critère | Ce qu'il exige | Ce qu'il exclut |
|---|---|---|---|
| **C1** | **Versement effectif** | Un flux monétaire réel est décaissé | Les cotisations « **imputées** » (employeur fictif, ex. pensions des fonctionnaires d'État) |
| **C2** | **Au profit des administrations publiques (APU) ou de l'UE** | Le bénéficiaire appartient au périmètre des APU (État, ODAC, APUL, ASSO) ou est une institution européenne | Les versements à des organismes **privés hors APU** (ordres professionnels, mutuelles facultatives, syndicats) |
| **C3** | **Obligatoire ET sans contrepartie directe** | Le redevable ne choisit ni le principe, ni le montant, ni les modalités ; il ne reçoit pas en échange un service individualisé et proportionnel | Les versements **facultatifs** et les **redevances pour service rendu** (contrepartie directe) |

**Point clef : le nom ne fait pas la nature.** Une « redevance » peut être un
prélèvement obligatoire (ex. les *redevances des agences de l'eau*, qualifiées
d'« impositions de toutes natures » par le Conseil constitutionnel), tandis
qu'une « contribution » peut ne pas en être un. C'est l'analyse des trois
critères qui tranche, pas l'étiquette.

**Second point clef : « taxe affectée » au sens de la LOLF ≠ prélèvement
obligatoire.** L'annexe budgétaire *Liste des taxes affectées* et le mécanisme
de plafonnement des ressources affectées (68 taxes plafonnées, 20,6 Md€ en LFI
2025 ; 21,4 Md€ proposés en PLF 2026) recensent des ressources selon un critère
**budgétaire** (recette affectée à un tiers autre que l'État), pas selon les
trois critères ci-dessus. On y trouve ainsi les **redevances de l'INPI**, qui
sont des paiements pour service rendu et donc **pas** des PO. La coïncidence est
large, l'identité n'existe pas.

### 2.1 Le périmètre géographique (souvent oublié)

Le taux de 42,7 % du PIB est calculé sur le **territoire économique** des comptes
nationaux français : France métropolitaine et **régions ultrapériphériques**
(Guadeloupe — Saint-Martin y étant rattaché —, Martinique, Guyane, La Réunion,
Mayotte), plus le territoire extra-régional (ambassades, bases).

En sont **hors champ** les collectivités dotées de l'**autonomie fiscale** et
d'un système statistique propre : Nouvelle-Calédonie, Polynésie française,
Wallis-et-Futuna, Saint-Pierre-et-Miquelon, Saint-Barthélemy. Leurs
prélèvements sont pourtant, sur leur territoire, aussi obligatoires que les
autres. Ils sont donc recensés ici (§4.7) mais **explicitement signalés comme
n'entrant pas dans le ratio national** : les additionner au 42,7 % serait une
faute de méthode.

> Sources de la définition : INSEE (définition c1571), OCDE (Statistiques des
> recettes publiques / guide d'interprétation), FIPECO. Voir §9.

---

## 3. Règle de décision (prendre / rejeter)

On applique à chaque candidat l'arbre suivant. On **rejette** dès qu'une réponse
est « non ».

```
Candidat
  │
  ├─ Donne-t-il lieu à un versement monétaire effectif ?        ── non ─▶ REJET (échec C1 : cotisation imputée)
  │        oui
  ├─ Le bénéficiaire est-il une APU ou une institution UE ?     ── non ─▶ REJET (échec C2 : organisme privé hors APU)
  │        oui
  ├─ Le versement est-il obligatoire (pas de libre choix) ?     ── non ─▶ REJET (échec C3 : versement facultatif)
  │        oui
  ├─ Est-il SANS contrepartie directe et proportionnelle ?      ── non ─▶ REJET (échec C3 : redevance pour service rendu)
  │        oui
  └─ Est-ce une sanction (amende, pénalité) ?                   ── oui ─▶ REJET (hors champ : sanction, pas un prélèvement)
           non
        ▶ PRIS : c'est un prélèvement obligatoire
```

Les §4 (candidats **pris**), §5 (candidats **rejetés**) et §6 (cas **limites**)
appliquent cette règle.

**Comment on tranche C2 en pratique.** Le critère du bénéficiaire est le plus
piégeux, et il ne se déduit pas du nom de l'organisme. Deux instruments le
tranchent :

- la **liste INSEE des ODAC** (édition mai 2025, situation 2023) pour
  l'administration centrale — c'est elle qui sépare le **FIPHFP** (ODAC, donc
  PO) de l'**AGEFIPH** (hors liste, donc pas de PO), ou qui fait entrer le
  **FGTI**, le **FGDR**, la **CGLLS**, l'**AMF**, l'**OFII**, les **OPCO** et
  **Action Logement Services** dans le champ des APU ;
- le classement en **ODAL** (organismes divers d'administration locale) pour les
  organismes à compétence territoriale : c'est le cas des **agences de l'eau**,
  qui ne figurent pas dans la liste ODAC non parce qu'elles seraient privées,
  mais parce qu'elles relèvent des **APUL**. C2 est satisfait dans les deux cas.

---

## 4. Les prélèvements obligatoires retenus (PRIS)

> L'énumération de référence des impôts et taxes figure dans l'annexe
> **« Évaluation des voies et moyens, tome I »** du projet de loi de finances et
> dans son annexe **« Liste des taxes affectées »**, qui recensent l'ensemble des
> *impositions de toutes natures*. Les rubriques ci-dessous en organisent
> l'essentiel ; les documents budgétaires font foi pour l'exhaustivité ligne à
> ligne.
>
> **État de la recherche.** Ce recensement est incrémental. La dernière passe a
> été conduite à partir de quatre sources primaires dépouillées directement — le
> **Voies et moyens tome I du PLF 2026** (102 pages, lignes de recettes et
> tableaux de plafonnement), l'**article 36 du PLF 2026** (tableau de 135
> ressources affectées), la **liste INSEE des ODAC** (≈ 700 organismes) et la
> liste encyclopédique des impôts français (≈ 430 entrées) — et a ajouté une
> dizaine de familles entières absentes de la version précédente : la **taxonomie
> du CIBS** (§4.2), les **taxes de l'urbanisme et de l'aménagement**, les
> **collectivités à autonomie fiscale** (§4.7), les **régimes sociaux
> particuliers** (§4.8), les **taxes des centres techniques industriels** et les
> **taxes de régulation économique et sectorielle** (§4.10), ainsi que deux
> **corrections d'erreurs** signalées en §7. Les pistes non encore dépouillées
> sont au §10.

**Ce que contient ce recensement.** Le §4 compte **261 entrées**, réparties comme
suit. Une entrée n'est pas toujours un prélèvement : certaines en regroupent
plusieurs (« cinq taxes affectées à l'ANSES », « sept redevances des agences de
l'eau »), d'autres décrivent une même taxe vue depuis un affectataire différent.
Le tableau donne donc un ordre de grandeur de la couverture, pas un décompte —
pour les raisons exposées au §1.

| Section | Entrées | Bénéficiaire |
|---|---:|---|
| 4.1 Revenu, bénéfices, patrimoine | 21 | État |
| 4.2 Accises et impositions sur les biens et services (CIBS) | 34 | État, collectivités, ASSO |
| 4.3 Enregistrement, timbre, mutations, transactions | 18 | État |
| 4.4 Jeux d'argent et de hasard | 7 | État, ASSO, communes, ANS |
| 4.5 Impôts locaux | 33 | APUL |
| 4.6 DROM et Corse | 8 | Collectivités ultramarines |
| 4.7 Collectivités à autonomie fiscale | 35 | *hors champ du ratio national* |
| 4.8 Cotisations sociales effectives | 14 | ASSO |
| 4.9 Fiscalité sociale | 18 | ASSO |
| 4.10 Taxes affectées aux opérateurs et agences | 68 | ODAC, ODAL, organismes divers |
| 4.11 Union européenne | 5 | Institutions de l'UE |

S'y ajoutent **44 candidats examinés puis rejetés** (§5) et **8 cas limites**
(§6), dont trois restent délibérément non tranchés.

Le jeu de données [`data/`](data/), qui découpe plus finement et intègre les
sources officielles ligne à ligne, compte de son côté **437 prélèvements
uniques** (380 PRIS, 56 REJET, 1 à arbitrer) — voir §8 pour l'articulation entre
les deux.

### 4.1 Impôts d'État sur le revenu, les bénéfices et le patrimoine

Satisfont C1-C2-C3 : versés à l'État, obligatoires, sans contrepartie.

> **Sur la nomenclature des lignes.** Les numéros cités (1101, 1406, 1442…) sont
> ceux de l'**état A** annexé à la loi de finances, qui énumère nommément
> **toutes** les recettes du budget général. C'est la seule liste officielle
> exhaustive des impositions perçues par l'État. Elle a été dépouillée
> intégralement pour cette version, ce qui explique l'apparition de plusieurs
> lignes de faible rendement ci-dessous. Deux avertissements : l'état A conserve
> des **lignes dormantes** à rendement nul (précompte, cotisation minimale de
> taxe professionnelle, taxe d'habitation sur les résidences principales, IFER
> à affectation temporaire de 2010…), vestiges d'impôts éteints qu'il ne faut pas
> compter comme prélèvements en vigueur ; et il mêle **recettes fiscales** (série
> 1xxx) et **recettes non fiscales** (série 2xxx), dont aucune n'est un PO (§5.5).

**Imposition des revenus des personnes physiques**
- **Impôt sur le revenu (IR)**, prélevé à la source.
- **Prélèvement forfaitaire unique (PFU / « flat tax »)** sur les revenus du
  capital — la LF 2026 portant les prélèvements sociaux sur le capital à 18,6 %,
  le PFU atteint **31,4 %**.
- **Contribution exceptionnelle sur les hauts revenus (CEHR)**.
- **Contribution différentielle sur les hauts revenus (CDHR)** — imposition
  minimale des très hauts revenus, créée pour les revenus 2025, **prorogée par la
  LF 2026** (1,7 Md€ attendus en 2026) jusqu'à ce que le déficit public repasse
  sous 3 % du PIB.
- **Retenues à la source sur certains bénéfices non commerciaux** (ligne 1401)
  et **retenues à la source sur les revenus de capitaux mobiliers** (ligne 1402),
  y compris le **prélèvement sur les bons anonymes**.
- **Retenues à la source sur les revenus versés à des non-résidents** (salaires,
  dividendes, redevances).
- **Taxe forfaitaire sur les métaux précieux, bijoux, objets d'art, de
  collection et d'antiquité** — imposition libératoire sur la cession.
- **Prélèvement sur les sommes versées par les organismes d'assurance à raison
  des contrats d'assurance en cas de décès** (art. 990 I et 990 I bis du CGI) —
  478 M€ ; c'est le régime successoral propre à l'assurance-vie. **Nouvelle
  entrée.**
- **Autres impôts directs perçus par voie d'émission de rôles** (ligne 1201) —
  ligne résiduelle qui recueille les impositions établies par rôle hors barème.

**Imposition des bénéfices des sociétés**
- **Impôt sur les sociétés (IS)** et **contribution sociale sur l'IS**.
- **Contribution exceptionnelle sur les bénéfices des grandes entreprises**
  (CA > 1 Md€) — 8 Md€ en 2025, **prorogée pour un an à taux moitié moindre**
  par la LF 2026 (≈ 4 Md€).
- **Impôt minimum mondial à 15 % (« pilier 2 » / imposition mondiale des groupes,
  IMG)** — transposition de la directive UE 2022/2523 ; ligne de recette propre
  au Voies et moyens depuis le PLF 2026. Nouvelle entrée par rapport à la
  version précédente de ce document.
- **Contribution sur les revenus locatifs (CRL)** — personnes morales, immeubles
  achevés depuis plus de quinze ans.
- **Taxe sur les excédents de provisions des entreprises d'assurances de
  dommages** et **prélèvements sur les entreprises d'assurance** (ligne 1408).
- **Contribution de la Caisse des dépôts et consignations représentative de
  l'impôt sur les sociétés** (ligne 1303) — la CDC n'étant pas assujettie à l'IS,
  elle acquitte une contribution qui en tient lieu. **Nouvelle entrée.**
- **Contribution des institutions financières** (ligne 1415).
- **Prélèvement exceptionnel de 25 % sur les distributions de bénéfices**
  (ligne 1405) et **précompte dû par les sociétés** (ligne 1404) — lignes
  résiduelles, en extinction.
- **Taxe sur les gestionnaires d'infrastructures de transport** (ligne 1429,
  écrêtement au profit de l'État).

**Patrimoine et détention**
- **Impôt sur la fortune immobilière (IFI)** — 2,7 Md€ en 2024.
- **Taxe sur la valeur vénale des immeubles des entités juridiques** (« taxe de
  3 % ») — frappe les entités détenant des immeubles en France sans révéler
  leurs bénéficiaires.
- **Taxe sur le patrimoine financier / sur les actifs non affectés à une
  activité opérationnelle des holdings patrimoniales** — annoncée dans le PLF
  2026 (ligne 1439, 1 Md€ attendus), **adoptée sous une forme resserrée** :
  20 %, holdings contrôlées par des personnes physiques détenant au moins 5 M€,
  assiette limitée aux actifs somptuaires non affectés (yachts, voitures de
  collection, chevaux de course, bijoux), pour les **exercices clos à compter du
  31 décembre 2026**. Droit voté, rendement encore nul à la date du document.

### 4.2 Accises et impositions sur les biens et services (code du CIBS)

Depuis l'ordonnance n° 2021-1843 du 22 décembre 2021, l'essentiel des taxes
indirectes est refondu dans le **code des impositions sur les biens et services
(CIBS)**, qui les organise en grandes familles. Cette taxonomie est un outil de
recensement puissant : elle **garantit la couverture** d'une zone où les listes
historiques laissaient des trous.

**Taxe sur la valeur ajoutée**
- **TVA** — premier impôt par le rendement (210,7 Md€ nets en 2024, tous
  affectataires confondus). Des fractions sont affectées à la Sécurité sociale
  (57,9 Md€ en 2024), aux collectivités (52,1 Md€) et à l'audiovisuel public
  (4,0 Md€) ; ce sont des transferts, pas des prélèvements distincts.

**Accise sur les énergies** (une seule accise, quatre fractions budgétaires
depuis le 1ᵉʳ janvier 2026)
- fraction perçue sur les **produits énergétiques** (ex-**TICPE**, ligne 1501) ;
- fraction perçue sur les **gaz naturels** (ex-TICGN, ligne 1502) ;
- fraction perçue sur l'**électricité** (ex-TICFE / ex-CSPE, ligne 1503) ;
- fraction perçue sur les **charbons et autres** (ex-TICC, ex-**TICHLC** sur les
  houilles, lignites et cokes, ligne 1504).

> Les anciennes **taxes communales et départementales sur la consommation finale
> d'électricité (TCCFE / TDCFE)** ont été absorbées par cette accise : les
> collectivités en reçoivent désormais une **part**, elles ne lèvent plus un
> impôt distinct.

**Accises sur les alcools et les boissons**
- **Droits de consommation sur les alcools** ; **droit de consommation sur les
  produits intermédiaires** ; **droit de circulation sur les vins, cidres, poirés
  et hydromels** ; **droit sur les bières**.
- **Cotisation spéciale sur les boissons alcooliques** (« cotisation sécurité
  sociale » sur les boissons titrant plus de 18°).
- **Taxe sur les boissons « prémix »**.
- **Contributions sur les boissons non alcooliques** : composante **sucres
  ajoutés**, composante **édulcorants**.
- **Contribution sur les eaux minérales naturelles** (au profit des communes
  d'implantation des sources).

**Accises sur les tabacs**
- **Droit de consommation sur les tabacs manufacturés** et **taxe additionnelle
  à l'accise sur les tabacs**.
- **Droits de consommation sur les tabacs propres à la Corse et aux DROM**
  (tarifs dérogatoires).

**Taxes sur les mobilités (CIBS, section « AIS-MOB »)**
- **Taxes sur l'affectation des véhicules à des fins économiques** (ex-TVS) :
  **taxe annuelle sur les émissions de CO₂** et **taxe annuelle sur les émissions
  de polluants atmosphériques**.
- **Malus à l'immatriculation** : **taxe sur les émissions de CO₂** et **taxe sur
  la masse en ordre de marche**.
- **Taxe spéciale sur certains véhicules routiers** (« taxe à l'essieu »).
- **Taxe sur la distance parcourue sur le réseau autoroutier concédé**.
- **Taxe sur l'exploitation des infrastructures de transport de longue
  distance** — créée par la LF 2024 (art. 100) ; 4,6 % du chiffre d'affaires
  au-delà de 120 M€ pour les exploitants dont la rentabilité moyenne dépasse
  10 % ; vise les sociétés concessionnaires d'autoroutes et les grands aéroports
  (Roissy, Orly, Marseille, Lyon, Nice, Toulouse) ; ≈ 600 M€ attendus, dont
  ≈ 450 M€ des autoroutes. **Nouvelle entrée.**
- **Taxes sur le transport aérien** : **taxe d'aéroport**, **taxe sur le
  transport aérien de passagers** (dont le **tarif de solidarité**, « taxe
  Chirac »), **taxe sur les nuisances sonores aériennes (TNSA)**.
- **Taxes sur les navigations maritimes et fluviales** : **taxe annuelle sur les
  engins maritimes à usage personnel (TAEMUP**, ex-droit de francisation et de
  navigation), **droit de passeport** (navires sous pavillon étranger de
  résidents français), **taxe sur les passagers maritimes embarqués à destination
  d'espaces naturels protégés**.
- **Taxes sur le transport guidé** (ferroviaire et guidé).
- **Taxe sur les certificats d'immatriculation** — voir §4.5 (régions).

**Taxes sur les communications et l'économie numérique (« AIS-CCN »)**
- **Taxe sur les services fournis par les opérateurs de communications
  électroniques (TOCE)**.
- **Taxe sur les services de télévision** — volet **éditeurs** (TST-E) et volet
  **distributeurs** (TST-D).
- **Taxe sur les services d'accès à des contenus audiovisuels à la demande**
  (SMAD / « taxe streaming vidéo »).
- **Taxe sur la mise en relation par voie électronique en vue de fournir
  certaines prestations de transport** (plateformes VTC/livraison).
- **Taxe sur certains services numériques** (dite « taxe GAFA ») — 785 M€ en
  2024, 882 M€ attendus en 2026.
- **Taxe sur les locations de phonogrammes et vidéomusiques en ligne** (« taxe
  streaming musical », au profit du CNM).

**Autres taxes sur les biens et services**
- **Taxe générale sur les activités polluantes (TGAP)** — composantes
  **déchets**, **émissions polluantes**, **lessives**, **matériaux
  d'extraction** ; 1,15 Md€ en 2024, 1,36 Md€ attendus en 2026.
- **Taxe sur les petits colis** — 2 € par article sur les envois de moins de
  150 € en provenance de pays tiers, applicable au **1ᵉʳ mars 2026** ; 500 M€
  attendus (ligne 1442). **Nouvelle entrée.**
- **Taxe sur certaines dépenses de publicité** (ligne 1777) et **taxe spéciale
  sur la publicité télévisée** (ligne 1774) ; **taxe sur les surfaces
  commerciales (TASCOM)** et sa **taxe additionnelle**.
- **Taxe sur les achats de viande** (ligne 1773) et **redevances sanitaires
  d'abattage et de découpage** (ligne 1776).
- **Cotisation à la production sur les sucres** (ligne 1757).
- **Taxe de l'aviation civile** (ligne 1780).
- **Taxe sur les installations nucléaires de base** (ligne 1781) — volet État,
  distinct des tarifs affectés au CEA, à l'ANDRA et aux GIP (§4.10).
- **Taxes sur les stations et liaisons radioélectriques privées** (ligne 1782).
- **Redevance sur les paris hippiques en ligne** (ligne 1790).
- **Droits d'importation** (ligne 1751) — part nationale des recettes douanières,
  distincte des droits de douane reversés à l'UE (§4.11).
- **Produit de la mise aux enchères des quotas d'émission (SEQE-UE)** — bien
  qu'il prenne la forme d'un marché, il est enregistré en comptabilité nationale
  comme un **impôt sur la production (D.29)** au sens du SEC 2010 : c'est donc un
  PO. Le manuel du déficit et de la dette (MGDD) prescrit un enregistrement
  décalé d'une année civile ; une partie du produit est affectée à l'ANAH
  (0,9 Md€ écrêtés en 2024).

### 4.3 Enregistrement, timbre, mutations et transactions

- **Droits de mutation à titre gratuit** : **successions** (16,0 Md€ en 2024,
  17,0 Md€ attendus en 2026) et **donations** (4,9 Md€ en 2024).
- **Droits de mutation à titre onéreux (DMTO)** — voir §4.5 pour la part locale ;
  **taxe de publicité foncière** ; **droits d'enregistrement sur les mutations de
  fonds de commerce**, de **créances, rentes et prix d'offices**, et sur les
  **mutations de jouissance (baux)**.
- **Droits d'apport des sociétés** ; **droit fixe pour l'établissement d'un
  contrat de mariage** ; **droits sur les autres conventions et actes civils**
  (ligne 1711) et sur les **actes judiciaires et extrajudiciaires** (ligne 1712).
- **Droit de partage** — 1,1 % de l'actif net partagé, dû lors du partage de
  biens indivis : sortie d'indivision successorale, liquidation de communauté
  après divorce, partage de société. ≈ 0,7 Md€. Souvent oublié des recensements
  parce qu'il se confond avec les droits d'enregistrement, alors qu'il a son
  fait générateur propre — le partage, non la mutation.
- **Contribution de sécurité immobilière** (ligne 1707) — perçue à l'occasion des
  formalités de publicité foncière ; a succédé en 2013 au « salaire du
  conservateur des hypothèques ». **Nouvelle entrée.**
- **Taxe additionnelle au droit de bail** (ligne 1715).
- **Timbre unique** (ligne 1721) et **droits sur les actes et écrits assujettis
  au timbre de dimension** (ligne 1723).
- **Droit d'examen et permis de chasser** (ligne 1725) ; **redevance pour
  délivrance initiale du permis de chasse** et **droit de validation** (OFB,
  §4.10).
- **Garantie des matières d'or et d'argent** (ligne 1766) — droits de
  poinçonnage. **Nouvelle entrée.**
- **Droit de licence sur la rémunération des débitants de tabac** (ligne 1758).
- **Droits de timbre** : **passeports sécurisés** (fraction affectée à l'ANTS),
  **cartes nationales d'identité**, **permis de conduire en cas de perte ou de
  vol**, **demandes de naturalisation, de réintégration et déclarations
  d'acquisition de la nationalité par mariage**.
- **Droit de timbre sur les procédures civiles en première instance et
  prud'homales** — **créé et plafonné pour la première fois en PLF 2026** (45 M€)
  au profit de l'**UNCARPA**. **Nouvelle entrée** ; à ne pas confondre avec
  l'ancienne *contribution pour l'aide juridique* (supprimée en 2014, cf. §7).
- **Taxes sur les titres de séjour et l'immigration**, au profit de l'**OFII**
  (ODAC) : taxe perçue à la délivrance du **premier titre de séjour**, taxe de
  **renouvellement**, **droit de visa de régularisation**, taxe sur les
  **documents de circulation pour étrangers mineurs**, **taxe due par les
  employeurs de main-d'œuvre étrangère**.
- **Taxe sur les transactions financières (TTF)** — 1,33 Md€ en 2024, 2,63 Md€
  attendus en 2026 après relèvement du taux à 0,4 % ; une fraction est écrêtée au
  profit du **Fonds de solidarité pour le développement** (ODAC, 0,8 Md€ en 2024).
  Deux taxes jumelles complètent le dispositif : **taxe sur les ordres annulés
  dans le cadre d'opérations à haute fréquence** et **taxe sur les contrats
  d'échange sur défaut d'un État** (CDS souverains « à nu »).
- **Taxe sur les rachats d'actions** — assise sur la réduction de capital
  consécutive au rachat par une grande entreprise de ses propres titres ; 400 M€
  en 2025, 200 M€ attendus en 2026 au titre de la composante pérenne.
- **Taxe spéciale sur les conventions d'assurance (TSCA)** — assise sur les
  primes, y compris celles des assurances **obligatoires** (dont la souscription,
  elle, n'est pas un PO : cf. §5). Ses taux varient par risque (art. 991 à 1004
  du CGI) et son produit est **éclaté entre plusieurs bénéficiaires** : le volet
  **véhicules terrestres à moteur** (18 %) alimente notamment les départements
  (services d'incendie et de secours) et la branche famille de la Sécurité
  sociale. Une seule taxe, plusieurs affectataires — d'où sa réapparition en
  §4.5 et §4.9.
- **Contribution au Fonds de résolution unique (FRU / SRF)** — versée par les
  établissements de crédit dans le cadre de l'Union bancaire. Figure nommément
  dans la National Tax List d'Eurostat pour la France, classée **D.29H** :
  c'est donc bien un prélèvement obligatoire, ce que le raisonnement seul ne
  permettait pas de trancher (§6). **Nouvelle entrée.**
- **Contributions additionnelles aux primes d'assurance** finançant des fonds :
  **Fonds de prévention des risques naturels majeurs** (« fonds Barnier ») et
  **Fonds de garantie des victimes des actes de terrorisme et d'autres
  infractions (FGTI)** — le FGTI figurant dans la liste INSEE des ODAC, C2 est
  satisfait. **Nouvelle entrée.**

### 4.4 Prélèvements sur les jeux d'argent et de hasard

Famille souvent oubliée des recensements, alors qu'elle satisfait pleinement
C1-C2-C3 : le joueur ne reçoit aucune contrepartie individualisée en échange du
prélèvement, qui est assis sur les mises ou sur le **produit brut des jeux
(PBJ)** et versé par l'opérateur. Produits d'État : **5,5 Md€ en 2024**.

- **Prélèvements sur les jeux de loterie et les jeux instantanés** (FDJ, hors
  paris sportifs) — 3,03 Md€ en 2024 (ligne 1785).
- **Prélèvements sur le produit brut des jeux des casinos** — 948 M€ (ligne 1786).
- **Prélèvement sur le produit brut des paris hippiques** — 416 M€ (ligne 1787).
- **Prélèvement sur les paris sportifs** — 996 M€ (ligne 1788) ; **7,6 %** du PBJ
  en réseau physique et **15 %** en ligne.
- **Prélèvement sur les jeux de cercle en ligne (poker)** — 120 M€ (ligne 1789) ;
  porté de 0,2 % à **1 % des mises**.
- **Impôt sur les cercles et maisons de jeux**.
- **Contribution sur la cession à un service de télévision des droits de
  diffusion de manifestations sportives** (« taxe Buffet ») — affectée à
  l'**Agence nationale du sport**, qui perçoit avec le prélèvement sur les paris
  sportifs en ligne ≈ 240 M€ de taxes affectées en 2026.

> Environ **23 %** du produit de ces prélèvements est reversé à des affectataires
> autres que l'État : Sécurité sociale, bloc communal, Agence nationale du sport,
> sociétés de courses. Leur volet social figure en §4.9 et leur volet communal en
> §4.5 — c'est le **même** prélèvement vu par bénéficiaire, non un doublon. Deux
> fractions locales méritent d'être citées nommément : la part du prélèvement sur
> les **jeux de cercle en ligne** revenant aux communes accueillant un casino, et
> la part du prélèvement sur les **paris hippiques** revenant aux EPCI accueillant
> un hippodrome.

### 4.5 Impôts locaux (APUL)

Versés aux communes, EPCI, départements et régions ; obligatoires ; sans
contrepartie individualisée.

**Fiscalité foncière et d'habitation**
- **Taxe foncière sur les propriétés bâties (TFPB)** et **sur les propriétés non
  bâties (TFPNB)**, plus la **taxe additionnelle à la TFPNB**.
- **Taxe d'habitation sur les résidences secondaires (THRS)** (la TH sur les
  résidences principales a été supprimée en 2023).
- **Taxe sur les logements vacants (TLV)** en zone tendue — produit affecté à
  l'ANAH — et **taxe d'habitation sur les logements vacants (THLV)**, instituée
  par les communes hors zone tendue.
- **Taxe d'enlèvement des ordures ménagères (TEOM)** — adossée au foncier, sans
  lien avec le service effectivement rendu → **PO** (à distinguer de la REOM,
  cf. §5).
- **Taxe de balayage** — imposition de toute nature, transférée de l'article 1528
  du CGI à l'article **L. 2333-97 du CGCT** au 1ᵉʳ janvier 2019 ; toujours en
  vigueur (Paris notamment). Son produit ne peut excéder le coût du balayage, ce
  qui en fait un cas limite discuté au §6.

**Fiscalité économique locale**
- **Cotisation foncière des entreprises (CFE)**.
- **Cotisation sur la valeur ajoutée des entreprises (CVAE)** — en extinction
  progressive ; la part État tombe de 4,07 Md€ (2025) à 2,74 Md€ (2026).
- **Impositions forfaitaires sur les entreprises de réseaux (IFER)** — neuf
  composantes, dont : éoliennes et hydroliennes, centrales photovoltaïques et
  hydrauliques, centrales nucléaires et thermiques, transformateurs
  électriques, stations radioélectriques, réseaux de gaz naturel et canalisations
  d'hydrocarbures, répartiteurs principaux de téléphonie, matériel roulant
  ferroviaire, et **IFER-STIF sur le matériel roulant de la RATP** (affectée à la
  Société des grands projets).
- **Taxe sur les surfaces commerciales (TASCOM)**.
- **Cotisation foncière minimum** et **taxes pour frais de chambres consulaires**
  (cf. §4.10).
- **Taxe sur les friches commerciales**.
- **Taxe sur les activités commerciales saisonnières non salariées**.
- **Imposition forfaitaire sur les pylônes électriques**.
- **Redevances communale et départementale des mines** — malgré leur nom, des
  impositions et non des redevances pour service rendu.
- **Taxe sur les remontées mécaniques** (communes et départements de montagne).
- **Taxe sur les éoliennes maritimes** (« taxe sur les éoliennes en mer »).

**Mutations et transactions locales**
- **Droits de mutation à titre onéreux (DMTO)** — « frais de notaire » pour la
  part fiscale : **droits départementaux d'enregistrement**, **taxe communale
  additionnelle**, **taxe départementale additionnelle**.
- **Taxe forfaitaire sur la cession de terrains nus devenus constructibles** —
  deux versions coexistent : la **taxe communale facultative** et la **taxe
  nationale** perçue au profit de l'Agence de services et de paiement (ASP).

**Urbanisme et aménagement**
- **Taxe d'aménagement** — a absorbé depuis 2012 l'ancienne *taxe locale
  d'équipement*, la *taxe départementale des espaces naturels sensibles* et la
  *taxe départementale CAUE*, qui n'existent donc plus en tant que telles.
- **Taxe d'archéologie préventive (TAP, ex-redevance RAP)** — qualifiée
  d'« imposition de toute nature », adossée depuis 2022 au recouvrement de la
  taxe d'aménagement ; finance l'INRAP (ODAC), les services archéologiques des
  collectivités et le Fonds national pour l'archéologie préventive.
- **Redevance pour création de bureaux, locaux commerciaux et de stockage en
  Île-de-France (RCBCE)** — imposition due à la construction, distincte de la
  taxe annuelle ci-dessous.
- **Taxe annuelle sur les bureaux et locaux** en Île-de-France (et, depuis 2023,
  en Provence-Alpes-Côte d'Azur) ; **taxe annuelle sur les surfaces de
  stationnement** annexées.
- **Taxes spéciales d'équipement (TSE)** — additionnelles aux impôts directs
  locaux, au profit des **établissements publics fonciers** d'État et locaux
  (Bretagne, Grand-Est, Hauts-de-France, Normandie, Nouvelle-Aquitaine,
  Occitanie, Ouest Rhône-Alpes, PACA, Vendée…), de l'**office foncier de Corse**,
  des **EPF de Guyane et de Mayotte**, des **agences des cinquante pas
  géométriques** de Guadeloupe et de Martinique, de la **Société des grands
  projets** et de la **Société du Grand Projet du Sud-Ouest**.

**Tourisme, transports et environnement locaux**
- **Versement mobilité** (ex-versement transport), dû par les employeurs.
- **Taxe de séjour**, sa **taxe additionnelle départementale** (10 %) et la
  **taxe additionnelle régionale d'Île-de-France** (15 %, au profit de la Société
  des grands projets).
- **Taxe GEMAPI** (gestion des milieux aquatiques et prévention des inondations).
- **Taxe locale sur la publicité extérieure (TLPE)**.
- **Taxe sur les déchets réceptionnés dans une installation de stockage ou un
  incinérateur de déchets ménagers** (taxe communale).
- **Taxe sur les certificats d'immatriculation des véhicules** (« carte grise »)
  — au profit des **régions** ; s'y ajoutent la **taxe fixe** et la **taxe pour
  la gestion des certificats d'immatriculation** (ANTS).
- **Taxe additionnelle spéciale annuelle** au profit de la région Île-de-France.
- **Droit départemental de passage sur les ouvrages d'art reliant le continent
  aux îles maritimes** (pont de Ré, pont d'Oléron…).
- **Taxe dans le domaine funéraire** (convois, inhumations, crémations).
- **Frais de gestion de la fiscalité directe locale** — majorations (de 1 % à
  8 % selon les impôts) prélevées par l'**État** sur le contribuable local au
  titre de l'assiette, du recouvrement, des frais de dégrèvement et de
  non-valeurs. Pour le redevable, c'est un supplément d'imposition de plein
  exercice, quel que soit le compte budgétaire où il atterrit. **Nouvelle
  entrée.**

> Beaucoup de ces taxes sont **facultatives** : elles n'existent que si la
> collectivité les institue par délibération. Elles n'en sont pas moins des
> prélèvements obligatoires **pour le redevable** — le caractère facultatif porte
> sur l'institution du prélèvement, pas sur son acquittement. C'est aussi ce qui
> rend un décompte national exhaustif impraticable (§10).

### 4.6 Fiscalité des départements et régions d'outre-mer et de la Corse

Régime juridique distinct — l'octroi de mer bénéficie d'une **dérogation de
l'Union européenne**, aujourd'hui accordée jusqu'à fin 2027 — mais des
prélèvements obligatoires de plein exercice : obligatoires, sans contrepartie,
au profit des collectivités, et **dans le champ des comptes nationaux** (§2.1).

- **Octroi de mer** — frappe les importations **et** les productions locales
  dans les départements et régions d'outre-mer ; l'un des plus anciens impôts
  français (perçu en Martinique dès 1670). Plus de **1,6 Md€** de recettes en
  2022, soit en moyenne près du **tiers des ressources des communes**
  ultramarines ; réformé dans le cadre de la LF 2025.
- **Octroi de mer régional (OMR)** — part additionnelle au profit des régions.
- **Droits assimilés au droit d'octroi de mer sur les rhums et spiritueux à base
  d'alcool de cru**.
- **Taxe spéciale de consommation (TSC)** sur les carburants — équivalent
  ultramarin de l'accise sur les énergies, au profit des régions et départements
  d'outre-mer.
- **Droits de consommation sur les tabacs** propres aux DROM.
- **Taxe due par les entreprises de transport public aérien et maritime**
  (versions outre-mer et Corse) ; **taxe d'embarquement sur les passagers** et
  **taxe d'atterrissage** dans les territoires d'outre-mer.
- **Redevances de l'eau dans les départements d'outre-mer** (régime propre).
- **Corse** : **droits de consommation sur les tabacs** et **sur les alcools** à
  tarifs spécifiques, **droit de francisation et droit de passeport** à régime
  corse, **taxe due par les entreprises de transport public aérien et maritime**.

> À noter, symétriquement : la **TVA n'est pas applicable** en Guyane ni à
> Mayotte, et s'applique à taux réduits en Guadeloupe, en Martinique et à La
> Réunion. Une moindre imposition n'est évidemment pas un prélèvement.

### 4.7 Collectivités à autonomie fiscale (hors champ du ratio national)

**Nouvelle section.** Six collectivités disposent du pouvoir de créer, modifier
ou supprimer leurs propres impôts : Nouvelle-Calédonie, Polynésie française,
Wallis-et-Futuna, Saint-Pierre-et-Miquelon, Saint-Barthélemy et Saint-Martin.
Chacune a son propre corpus : **code des impôts** calédonien, fiscalité
polynésienne, **code général des impôts** de Saint-Martin, **code local des
impôts** de Saint-Pierre-et-Miquelon, **code des contributions** de
Saint-Barthélemy.

Ces prélèvements satisfont C1-C2-C3 sur leur territoire. Ils sont **exclus du
ratio de 42,7 % du PIB** parce qu'ils sont hors du territoire économique des
comptes nationaux français (sauf Saint-Martin, rattaché statistiquement à la
Guadeloupe). Les recenser sans le dire produirait un double langage ; les taire
laisserait un trou.

**Nouvelle-Calédonie** — système fiscal complet, le plus dense des six

- **Taxe générale sur la consommation (TGC)** — équivalent local de la TVA,
  introduite en 2018 ; frappe la consommation finale sur le territoire.
- **Impôt sur le revenu des personnes physiques** et déclarations catégorielles.
- **Impôt sur les sociétés**, **contribution additionnelle à l'IS (CAIS)** et
  **contribution sociale additionnelle à l'IS (CSA)**.
- **Contribution calédonienne de solidarité (CCS)** — créée au 1ᵉʳ janvier 2015
  pour financer durablement les régimes sociaux (retraite, personnes âgées,
  logement, handicap et dépendance) ; assise dès le premier franc et sans
  plafond, au taux de référence de **4 %** sur les revenus professionnels des
  indépendants, **2 %** sur les revenus d'activité et **1,3 %** sur les revenus
  de remplacement et de solidarité.
- **Impôt sur le revenu des valeurs mobilières (IRVM)** ; **contribution des
  patentes** ; **contribution foncière**.
- **Taxes sur les plus-values immobilières** et **mobilières** ; **taxe sur le
  produit net bancaire** — issues de la réforme fiscale récente.
- **Taxe sur les opérations financières (TOF)** ; **taxe sur les contrats
  d'assurance (TCA)**.
- **Taxes sur les alcools et les tabacs (TAT3S, TCI)** ; **taxe sur les produits
  alimentaires contenant du sucre**.
- **Taxe sur les produits des jeux**.
- **Redevance sur l'extraction des produits miniers** et **taxe sur l'exportation
  des produits miniers** — assises sur le nickel, ressource centrale du
  territoire.
- **Taxe hypothécaire** et **contribution de sécurité immobilière (CSI)**.

**Polynésie française** — fiscalité assise sur la consommation et l'activité,
sans impôt général sur le revenu

- **TVA polynésienne** ; **droits de douane** propres.
- **Contribution de solidarité territoriale (CST)** — **CST-S**, retenue à la
  source sur les salaires et revenus assimilés, et **CST-NS**, sur les professions
  et activités non salariées. C'est ce qui tient lieu d'imposition des revenus.
- **Impôt sur les transactions** (régime alternatif à l'IS pour les petites
  structures) et **impôt sur les sociétés**.
- **Contribution des patentes** (art. 211-1 à 219-2 du code des impôts) et
  **contribution des licences** (art. 231-1 à 236-1) — pour les débits de
  boissons.
- **Impôt foncier sur les propriétés bâties** (art. 221-1 à 228-3) et **régime
  des revenus locatifs**.
- **Centimes additionnels communaux** — surtaxes adossées à l'impôt foncier, à la
  contribution des patentes et à la contribution des licences, perçues au profit
  des communes et de leurs sections. Mécanisme sans équivalent métropolitain
  depuis la disparition des centimes additionnels en France continentale.

**Saint-Pierre-et-Miquelon** — **code local des impôts** voté par le conseil
territorial ; le corpus le plus proche du modèle métropolitain

- **Impôt sur le revenu** (barème progressif propre) et **impôt sur les
  sociétés**.
- **Taxe sur les salaires** ; **taxe sur les spectacles**.
- **Taxe de réhabilitation des sites**.
- **Taxes sur les pétroles**, **taxes spéciales sur les pétroles** et **redevance
  sur les pétroles** — trois prélèvements distincts sur les produits pétroliers.
- **Droits de mutation**, **taxes successorales**, **droits d'apport**, **taxe de
  publicité foncière** et **contribution de sécurité immobilière**.
- **Impôt foncier**, **droit de bail** et **taxes communales**.
- **Patente** et **droits de licence**.
- **Impôt sur la fortune**.
- S'y ajoute, prévue par le droit national, la **redevance due par les titulaires
  de titres d'exploitation de mines d'hydrocarbures au large de
  Saint-Pierre-et-Miquelon**.

**Saint-Barthélemy** — **code des contributions** ; taux de prélèvements
obligatoires d'environ **20 % du PIB**, moins de la moitié du niveau
métropolitain

- **Droit de quai** — droit d'importation de **5 %** de la valeur des
  marchandises (taux majoré pour les véhicules), qui tient lieu de TVA :
  ≈ **25 %** des recettes fiscales. Institué par un arrêté municipal du 24 mai
  1879, base légale confirmée par la loi de finances pour 1974.
- **Droits sur les mutations immobilières** — 4,8 % : ≈ **25 %** des recettes.
- **Taxe de séjour** (5 % du prix des nuitées) et **taxes portuaires et
  aéroportuaires** : ≈ **20 %** des recettes.
- **Taxes sur les carburants** et autres consommations spécifiques.
- **Contribution forfaitaire annuelle des entreprises** — part fixe de 350 € et
  part variable de 100 € par salarié ; **seul prélèvement direct sur les
  entreprises**, moins de 10 % des recettes.
- **Prélèvements sociaux identiques à ceux des DOM** (cotisations sociales, CSG,
  CRDS) : l'autonomie fiscale ne s'étend pas au champ social, qui reste régi par
  le droit national.

**Saint-Martin** — **code général des impôts** propre, largement décalqué du CGI
métropolitain (impôt sur le revenu, impôt sur les sociétés, droits
d'enregistrement, fiscalité foncière), avec des taux et abattements distincts.
Contrairement aux cinq autres collectivités de cette section, Saint-Martin est
**rattaché statistiquement à la Guadeloupe** et donc **inclus** dans le
territoire économique des comptes nationaux (§2.1).

**Wallis-et-Futuna** — le régime le plus atypique de la République

- **Pas d'impôt sur le revenu, pas d'impôt sur les sociétés au sens classique,
  pas de TVA, pas d'impôt sur la fortune, ni CSG ni CRDS.**
- **Droits de douane et taxes à l'importation** — l'essentiel des recettes ;
  ≈ 2,5 Md F CFP (≈ 208 M€) par an de fiscalité indirecte.
- **Droit proportionnel** sur toutes les marchandises dédouanées et mises à la
  consommation — première imposition directe du territoire, la moitié du total.
- **Patente** — droit fixe annuel variant selon l'activité (≈ 84 € à 7 542 €),
  **droit additionnel sur le commerce des alcools** (≈ 126 € à 838 €) et **taxe
  additionnelle de 30 % au profit de la chambre de commerce**.

> Le rapport public thématique de la Cour des comptes **« L'autonomie fiscale en
> outre-mer »** couvre les six collectivités. Le détail article par article des
> codes locaux — le seul code de Saint-Pierre-et-Miquelon fait 172 pages —
> dépasse le format de ce document ; les rubriques ci-dessus en donnent la
> structure et les principaux prélèvements, pas l'exhaustivité (§10).

### 4.8 Cotisations sociales effectives (ASSO)

Versements effectifs (C1), à des organismes classés dans les ASSO (C2),
obligatoires et sans contrepartie strictement proportionnelle (C3). La part
salariale **et** la part patronale sont incluses dès lors qu'elles sont
effectivement versées.

**Régimes de base**
- **Cotisations du régime général**, recouvrées par les **URSSAF** : maladie-
  maternité, vieillesse de base (plafonnée et déplafonnée), allocations
  familiales, accidents du travail – maladies professionnelles (AT-MP),
  contribution solidarité autonomie (CSA employeurs, 0,3 %).
- **Cotisations des travailleurs indépendants** (URSSAF, ex-RSI).
- **Cotisations agricoles** recouvrées par la **MSA** (exploitants et salariés
  agricoles).
- **Cotisations des régimes spéciaux** effectivement versées : **CNRACL**
  (fonction publique territoriale et hospitalière), régimes SNCF, RATP, marins
  (ENIM), Banque de France, Opéra de Paris, Comédie-Française, clercs de notaires
  (CRPCEN), mines.
- **Cotisations des régimes de base des professions libérales** — **CNAVPL** et
  ses sections professionnelles (CIPAV, CARMF, CARPIMKO, CAVEC, CARCDSF,
  CAVP, CARPV, CAVOM, CAVAMAC…), **CNBF** pour les avocats, **CAVIMAC** pour les
  ministres des cultes.

**Régimes complémentaires et de garantie obligatoires**
- **Cotisations de retraite complémentaire obligatoire** **AGIRC-ARRCO**
  (salariés du privé), **IRCANTEC** (agents non titulaires du public), **RAFP**
  (retraite additionnelle de la fonction publique), régimes complémentaires
  obligatoires des indépendants et des professions libérales.
- **Cotisations d'assurance chômage** (régime **Unédic**) — part employeur (la
  part salariale a été supprimée en 2018 et remplacée par de la CSG).
- **Contribution AGS** — contribution patronale recouvrée par l'URSSAF avec les
  contributions chômage, finançant le régime de garantie des salaires en cas de
  défaillance de l'employeur. L'AGS figure nommément dans la **liste INSEE des
  ODAC** (fonction « protection sociale »), ce qui règle C2 sans discussion.

**Régimes territoriaux et professionnels particuliers** — *nouvelle rubrique*
- **Cotisation du régime local d'assurance maladie d'Alsace-Moselle** — 1,30 %
  du salaire, **exclusivement à la charge des salariés** des trois départements
  (Bas-Rhin, Haut-Rhin, Moselle), taux maintenu pour 2026. Régime obligatoire
  régi par les articles L. 325-1 à L. 325-3 du code de la sécurité sociale,
  héritage de la législation allemande de 1883 ; ≈ 3 millions d'assurés.
- **Cotisations aux caisses d'assurance-accidents agricoles d'Alsace-Moselle**
  (régime AT-MP agricole local).
- **Contribution tarifaire d'acheminement (CTA)** — prélevée sur la part fixe de
  l'acheminement des factures d'électricité et de gaz, au profit de la **Caisse
  nationale des industries électriques et gazières (CNIEG)**, qu'elle finance
  pour l'essentiel. Obligatoire, sans contrepartie individualisée, au profit d'un
  organisme de sécurité sociale : PO caractérisé, alors qu'elle est perçue par le
  fournisseur d'énergie. **Nouvelle entrée.**
- **Droits de plaidoirie** — dus par l'avocat à chaque plaidoirie, au profit de
  la **CNBF** (caisse de retraite des avocats).

**Contributions assises sur la masse salariale**
- **Contribution au Fonds national d'aide au logement (FNAL)**.
- **Contribution au dialogue social** — *rejetée*, cf. §5.

> Les régimes complémentaires paritaires (AGIRC-ARRCO, Unédic) sont **inclus**
> bien que gérés en droit privé : ils relèvent du périmètre des ASSO et
> l'affiliation y est obligatoire.

### 4.9 Impôts et taxes affectés à la Sécurité sociale (« fiscalité sociale »)

Recettes fiscales fléchées vers les ASSO ; ce sont des PO comme les autres.

**Contributions assises sur les revenus**
- **CSG** — contribution sociale généralisée (revenus d'activité, de
  remplacement, du capital, des jeux).
- **CRDS** — contribution au remboursement de la dette sociale.
- **Prélèvement de solidarité** sur les revenus du capital — la **LF 2026**
  porte le taux global des prélèvements sociaux sur le capital à **18,6 %**.
- **Contribution additionnelle de solidarité pour l'autonomie (CASA)** — 0,3 %
  sur les pensions de retraite et d'invalidité imposables, au profit de la CNSA.

**Contributions assises sur la masse salariale et l'épargne salariale**
- **Taxe sur les salaires** (employeurs non assujettis à la TVA).
- **Forfait social**.
- **Contributions patronales et salariales sur les attributions gratuites
  d'actions et les stock-options**.
- **Contribution salariale sur les « carried interests »**. *Nouvelle entrée.*
- **Contribution sur les abondements des employeurs aux plans d'épargne retraite
  collectifs**. *Nouvelle entrée.*
- **Contributions sur les rentes de « retraites chapeau »**, sur les **avantages
  de préretraite d'entreprise** et sur les **indemnités de mise à la retraite**.
- **Contribution spécifique sur les indemnités de rupture conventionnelle**
  (ex-forfait social dédié, porté à 30 %).

**Contributions assises sur le chiffre d'affaires et l'activité**
- **Contribution sociale de solidarité des sociétés (C3S)**.
- **Taxe de solidarité additionnelle (TSA)** sur les contrats de complémentaire
  santé.
- **Contribution exceptionnelle à la charge des organismes complémentaires
  d'assurance maladie** — **2,05 %** de l'ensemble des cotisations perçues,
  instituée par la **LFSS 2026** (adoptée le 30 décembre 2025) et assortie d'une
  interdiction de répercussion directe sur les adhérents, en contrepartie d'un
  gel des cotisations 2026. **Nouvelle entrée.**
- **Contributions de l'industrie pharmaceutique** — un ensemble à part entière :
  **clause de sauvegarde « M »** (médicaments) et **clause « Z »** (dispositifs
  médicaux), **contribution sur le chiffre d'affaires** des laboratoires,
  **contribution sur les dépenses de promotion** des médicaments et des
  dispositifs médicaux, **contribution « vente en gros »** des
  grossistes-répartiteurs, **contributions au titre des tarifs Lv/Lh**,
  **contribution sur les premières ventes** de médicaments et de dispositifs
  médicaux.
- **Accises affectées** sur les tabacs, alcools et boissons sucrées.
- **Taxes sur l'affectation des véhicules à des fins économiques** (ex-TVS),
  affectées à la Sécurité sociale.

**Prélèvements sociaux sur les jeux**
- **CSG sur les jeux de loterie** portée de 6,2 % à **7,2 %**, **prélèvements
  sociaux sur les paris et les casinos** (art. L. 137-20 à L. 137-25 du code de
  la sécurité sociale). La réforme portée par la LFSS vise ≈ **1,6 Md€** pour la
  Sécurité sociale, au bénéfice principal des branches famille et maladie ; une
  fraction est affectée à l'Agence nationale de santé publique.

### 4.10 Taxes affectées à des opérateurs, agences et ODAC

Le Conseil des prélèvements obligatoires recense de l'ordre de **238 ressources
affectées** (≈ 352 Md€ en 2022) à des tiers autres que l'État. La grande
majorité sont des prélèvements obligatoires — mais pas toutes (cf. l'avertissement
du §2 et les cas limites du §6).

> **Source exploitée pour cette rubrique.** L'**article 36 du PLF 2026**
> (« Dispositions relatives à l'affectation de ressources à des tiers ») contient
> désormais un tableau unique de **135 lignes**, indiquant pour chacune la
> référence juridique, l'intitulé exact de la ressource, le bénéficiaire, le
> rendement prévisionnel 2026 et le plafond d'affectation. Il a été dépouillé
> intégralement pour cette version : c'est lui qui a fait apparaître les taxes des
> **centres techniques industriels**, les six taxes supplémentaires du **CNC**, les
> cinq taxes de l'**ANSES** ou la ventilation de la **taxe sur les éoliennes en
> mer**. Il confirme aussi, par la négative, trois rejets du §5 : l'**AGEFIPH**
> (ligne 37), la **contribution patronale au dialogue social** (ligne 10, versée à
> l'AGFPN) et les **contributions pour frais de contrôle** (ligne 39, versées à la
> **Banque de France – ACPR**) figurent dans ce tableau budgétaire **sans être des
> prélèvements obligatoires**, faute d'un bénéficiaire classé en APU.

Regroupement par domaine :

**Emploi, formation professionnelle et handicap**
- **Contribution unique à la formation professionnelle et à l'alternance
  (CUFPA)** = ex-**taxe d'apprentissage** + contribution à la formation
  professionnelle, au profit de **France compétences** (ODAC) — premier plafond
  relevé du PLF 2026 (+411 M€).
- **Contribution supplémentaire à l'apprentissage (CSA)**.
- **Contribution dédiée au financement du CPF des titulaires de CDD**.
- **Participations au financement de la formation des professions non salariées**
  — l'article 36 du PLF 2026 en distingue **sept** assiettes, toutes affectées à
  France compétences : artisans (0,29 % du PASS, micro-entrepreneurs inclus),
  autres non-salariés (0,25 % du PASS), agriculture et « entreprises du vivant »
  (0,30 % des revenus professionnels), pêche et cultures marines (≥ 0,15 % du
  PASS), particuliers employeurs (≥ 0,15 % du PASS), artistes-auteurs (≥ 0,1 % du
  PASS) et intermittents (≥ 2 % des rémunérations). **Nouvelles entrées.**
- **Contribution spécifique à la formation professionnelle pour
  Saint-Pierre-et-Miquelon**.
- **Solde de la taxe d'apprentissage** après versements directs des entreprises —
  affecté à la **Caisse des dépôts et consignations** (gestion de la plateforme
  SOLTéA).
- **Taxes de développement de la formation professionnelle** : **taxe sur
  l'immatriculation des véhicules de transport (TIVT)** au profit de l'**AFT**
  (transports routiers), **taxe pour le développement de la formation dans les
  métiers de la réparation de l'automobile, du cycle et du motocycle** au profit
  de l'**ANFA**, **contribution spécifique du bâtiment et des travaux publics**
  au profit du **3CABTP**, **contribution conventionnelle à la formation des
  entreprises de travail temporaire** au profit du **Fonds pour l'emploi du
  travail temporaire**. **Nouvelles entrées.**
- **Cotisation « BTP intempéries »** — versée par les employeurs du bâtiment aux
  **caisses de congés payés du BTP** (UCF CIBTP) pour financer l'indemnisation du
  chômage-intempéries. **Nouvelle entrée.**
- **Contribution FIPHFP** des employeurs publics au titre de l'obligation
  d'emploi des travailleurs handicapés — le FIPHFP figure dans la liste INSEE
  des ODAC (à la différence de l'AGEFIPH : cf. §5).

> **Réserve sur C2.** Quatre des affectataires ci-dessus (AFT, ANFA, 3CABTP, UCF
> CIBTP) sont des **organismes de droit privé** absents de la liste INSEE des
> ODAC. Les taxes qui les financent sont pourtant des **impositions de toutes
> natures** votées par le Parlement et recouvrées par l'administration fiscale.
> Leur qualification dépend donc d'une question technique de comptabilité
> nationale — le « réacheminement » (*rerouting*) du prélèvement à travers l'État
> — et non de l'analyse juridique. Même réserve pour les taxes des centres
> techniques industriels (rubrique « Industrie » ci-dessous). Cas limite consigné
> au §6.

**Logement**
- **Participation des employeurs à l'effort de construction (PEEC, « 1 %
  logement »)** — 0,45 % de la masse salariale, due par les entreprises d'au
  moins 50 salariés, et sa version **agricole (PEAEC)**. **Cas d'école du
  critère C2** : longtemps regardée comme un versement à un organisme privé, elle
  bascule dans le champ des PO depuis que l'**INSEE a reclassé Action Logement
  Services en ODAC** le 31 août 2022 — classement contesté sans succès par
  l'organisme, jusque devant le Conseil d'État (28 avril 2026). Le prélèvement n'a
  pas changé ; c'est la **nature de son bénéficiaire** qui a changé.
  **Confirmation par la source de référence** : la National Tax List d'Eurostat
  comporte pour la France une ligne « **Participation des employeurs à l'effort
  de construction** » classée **D.29C** (autres impôts sur la production, assis
  sur la masse salariale). Une version antérieure de ce document rejetait la
  PEEC au motif qu'elle serait un « investissement obligatoire » plutôt qu'un
  versement définitif ; cette lecture était défendable avant 2022, elle ne l'est
  plus depuis le reclassement d'Action Logement Services.
- **Cotisations des organismes HLM et des SEM à la CGLLS** (cotisation
  principale — 590 M€ en 2026 — et **cotisation additionnelle**, 38 M€) — la
  Caisse de garantie du logement locatif social figure dans la liste INSEE des
  ODAC. **Nouvelle entrée.**
- **Prélèvement sur la PEEC** et **cotisation versée par les organismes HLM** au
  profit de l'**ANCOLS** (Agence nationale de contrôle du logement social, ODAC).
  **Nouvelles entrées.**
- **Recettes de la mise aux enchères des quotas carbone affectées à l'ANAH** —
  1,46 Md€ attendus en 2026, plafonnés à 700 M€ (cf. §4.2 pour la qualification
  du produit des quotas en impôt sur la production).

**Eau, biodiversité et environnement**
- **Redevances des agences de l'eau** — sept familles : **pollution de l'eau**
  (domestique et non domestique), **modernisation des réseaux de collecte**,
  **consommation d'eau potable**, **performance des réseaux d'eau potable et des
  systèmes d'assainissement collectif**, **pollutions diffuses**, **prélèvement
  sur la ressource en eau**, **stockage d'eau en période d'étiage**. Qualifiées
  d'« impositions de toutes natures » par le Conseil constitutionnel ; les agences
  relevant des **ODAL**, C2 est satisfait par la voie locale (§3).
- **Redevances cynégétiques** et **droit de validation du permis de chasse**,
  **droit d'examen du permis de chasse**, **redevance pour protection du milieu
  aquatique**, **redevance pour obstacle sur les cours d'eau** — au profit de
  l'**Office français de la biodiversité** (ODAC). **Nouvelles entrées.**
- **Taxe annuelle sur les engins maritimes à usage personnel (TAEMUP)** — répartie
  entre le **Conservatoire du littoral** (ODAC), les **organismes de secours et de
  sauvetage en mer agréés** (SNSM) — y compris une fraction spécifique perçue sur
  les engins ne battant pas pavillon français — et la **filière REP des navires de
  plaisance hors d'usage**. Une même taxe, quatre affectataires de nature
  différente : les deux derniers relèvent de la réserve sur C2 énoncée plus haut.
- **Taxe sur les installations de production d'électricité utilisant l'énergie
  mécanique du vent en mer** (« taxe sur les éoliennes en mer ») — répartie entre
  le **Comité national des pêches maritimes et des élevages marins**, les
  **comités régionaux des pêches**, l'**OFB** et les **organismes de secours et de
  sauvetage en mer**. **Ventilation nouvelle.**
- **Taxes affectées à l'ANSES** — l'article 36 en distingue **cinq** : taxe sur
  les **dossiers de demande concernant les médicaments vétérinaires** ou leur
  publicité, **taxe annuelle sur les autorisations de médicaments vétérinaires et
  d'établissements pharmaceutiques vétérinaires**, **taxe relative à la mise sur
  le marché des produits phytopharmaceutiques**, adjuvants, matières fertilisantes
  et supports de culture, **taxe annuelle sur la vente des produits
  phytopharmaceutiques**, et **redevance sur les produits biocides**.
  **Nouvelles entrées.**
- **Indemnité de défrichement** (code forestier) — au profit de l'**ASP** ; malgré
  son nom, une imposition due à l'occasion d'une autorisation administrative.

**Énergie, nucléaire et réseaux**
- **Taxe sur les installations nucléaires de base relevant du secteur
  énergétique (TINB-E)** — une taxe, **quatre tarifs**, quatre affectataires :
  **tarif de base** au **CEA** (plafonné à 240 M€ depuis la LFI 2025), **tarif de
  recherche** et **tarif de conception** à l'**ANDRA** (gestion des déchets
  radioactifs), **tarif d'accompagnement** aux **GIP « Objectif Meuse » et
  « Haute-Marne »** et aux communes concernées (58 M€). **Nouvelles entrées.**
- **Fractions d'accise sur les énergies affectées aux opérateurs de service
  public de l'électricité et du gaz** — financement de la **péréquation tarifaire
  dans les zones non interconnectées (ZNI)** et de la **contribution au service
  public de l'électricité (CSPE)**, débudgétisées par les LF 2025 et 2026 (1,6 Md€
  en 2026). Le prélèvement reste une accise ; seul son circuit d'affectation
  change. **Nouvelle entrée.**
- **Taxe sur l'utilisation des bandes « 700 MHz » et « 800 MHz » du spectre
  radioélectrique** — au profit de l'**Agence nationale des fréquences** (ODAC).
  À distinguer des **redevances d'utilisation des fréquences**, rejetées au §5.2.
  **Nouvelle entrée.**
- **Contribution annuelle au profit de l'IRSN** (fonctions reprises par
  l'**ASNR** depuis 2025).
- **Redevance proportionnelle sur l'énergie hydraulique** et **taxe sur les
  titulaires d'ouvrages hydroélectriques concédés**.
- **Redevance hydraulique de Voies navigables de France** (ODAC).
- **Redevances dues par les titulaires de titres d'exploitation de mines
  d'hydrocarbures**, et **redevance d'exploitation de substances non énergétiques
  sur le plateau continental ou dans la ZEE**.
- **Rémunération pour services rendus au Comité professionnel des stocks
  stratégiques pétroliers (CPSSP)** — le CPSSP figure dans la liste INSEE des
  ODAC ; le prélèvement est la contrepartie monétaire de l'obligation de stockage
  stratégique, dont le volet **en nature** est rejeté au §5.4.

**Santé et produits de santé**
- **Taxes et droits affectés à l'ANSM** (droits d'enregistrement et taxes liées
  aux autorisations de mise sur le marché des médicaments).
- **Taxes affectées à l'ANSES** (produits phytopharmaceutiques, biocides,
  alimentation animale).
- **Redevances sanitaires** d'**abattage**, de **découpage**, de
  **transformation des produits de la pêche et de l'aquaculture**, de **contrôle
  de certaines substances et de leurs résidus**, et **redevance pour l'agrément
  des établissements du secteur de l'alimentation animale** — impositions
  recouvrées à l'occasion des contrôles, à distinguer des redevances de contrôle
  facturées à l'opérateur (cf. §6).

**Culture, audiovisuel, sport**
- **Taxes affectées au CNC** — l'article 36 en distingue **neuf**, contre trois
  dans la version précédente de ce document : **taxe sur les spectacles
  cinématographiques** (entrées en salles, 148 M€), **taxe sur les services de
  télévision** (252 M€), **taxe sur la publicité télévisuelle et autres ressources
  liées à la diffusion de services de télévision** (242 M€), **taxe sur les
  vidéogrammes**, **taxe sur les services d'accès à des contenus audiovisuels à la
  demande**, **taxe sur la publicité diffusée au moyen de ces mêmes services**,
  **taxe sur le visa d'exploitation cinématographique**, **taxe sur l'autorisation
  d'exercice de l'activité d'exploitant d'établissement**, **taxe sur la
  production et la distribution d'œuvres cinématographiques**. **Six nouvelles
  entrées.**
- **Taxe sur les spectacles vivants (TSV)** — une taxe, deux fractions et deux
  affectataires : fraction **spectacles de variétés** au **CNM** (59,9 M€,
  plafond porté à 58 M€ en 2026) et fraction **art dramatique, lyrique et
  chorégraphique** à l'**Association pour le soutien du théâtre privé** (ASTP),
  qui figure dans la liste INSEE des ODAC.
- **Taxe sur les locations de phonogrammes et vidéomusiques en ligne** (« taxe
  streaming ») — CNM.
- **Fraction du prélèvement sur les jeux de loterie dédiés au patrimoine** — au
  profit de la **Fondation du patrimoine** (« loto du patrimoine »). Bénéficiaire
  de droit privé : même réserve sur C2 que ci-dessus. **Nouvelle entrée.**
- **Contribution sur les droits de diffusion des manifestations sportives**
  (« taxe Buffet ») et **prélèvement sur les paris sportifs en ligne** — Agence
  nationale du sport (§4.4).

**Transports et infrastructures**
- **Taxe d'aéroport** — de **nature fiscale** : elle finance des missions
  régaliennes de sûreté et de sécurité, qui ne peuvent précisément pas être
  financées par des redevances ; à distinguer des **redevances aéroportuaires**
  (cf. §5).
- **Taxe de solidarité sur les billets d'avion** (« taxe Chirac ») et son
  **éco-contribution**, **taxe sur le transport aérien de passagers** — l'AFITF
  et le **Fonds de solidarité pour le développement** (ODAC) en sont
  affectataires.
- **Ressources de l'AFITF** — l'agence est financée par **quatre** impositions :
  fraction de l'**accise sur les énergies** (+398 M€ de plafond en PLF 2026),
  **tarif de solidarité de la taxe sur le transport aérien de passagers**
  (1,45 Md€ de rendement, plafonné à 271 M€), **taxe sur la distance parcourue sur
  le réseau autoroutier concédé** et **taxe sur l'exploitation des infrastructures
  de transport de longue distance (TEITLD)**.
- **Taxes affectées à l'ANTS** (Agence nationale des titres sécurisés, ODAC) :
  **taxe fixe sur l'immatriculation des véhicules (TFIV)**, **taxe sur le
  renouvellement et l'échange du permis de conduire (TREPC)**, fractions des
  **droits de timbre sur les passeports sécurisés**, sur les **cartes nationales
  d'identité** et sur les **titres de séjour**. **Nouvelles entrées.**
- **Taxe sur les exploitants de plateformes de mise en relation par voie
  électronique** fournissant des prestations de transport — au profit de
  l'**ARPE** (Autorité des relations sociales des plateformes d'emploi, ODAC).
  **Nouvelle entrée.**
- **Droit de sécurité ferroviaire** (EPSF) et **droit dû par les entreprises
  ferroviaires** au profit de l'**Autorité de régulation des transports** — l'ART
  et l'EPSF figurent dans la liste INSEE des ODAC.
- **Taxe sur les nuisances sonores aériennes (TNSA)**.

**Agriculture, alimentation et qualité**
- **Taxe sur le chiffre d'affaires des exploitants agricoles** (ex-taxe ADAR).
- **Droit sur les produits bénéficiant d'une AOP, d'une IGP ou d'un label
  rouge** — au profit de l'**INAO** (ODAC). **Nouvelle entrée.**
- **Contribution additionnelle des exploitants agricoles et des conchyliculteurs
  au Fonds national de gestion des risques en agriculture (FNGRA)**, assise sur
  les primes d'assurance agricole.
- **Taxe additionnelle à la TFPNB pour frais de chambres d'agriculture**
  (335 M€ en 2026).
- **Redevance pour délivrance de certificats sanitaires et phytosanitaires** —
  FranceAgriMer (ODAC) ; la part de contrepartie individualisée en fait un cas
  discutable au regard de C3.
- **Redevance sur les paris hippiques** — versée aux **sociétés-mères de courses
  de chevaux** ; bénéficiaire de droit privé, d'où la réserve sur C2.
- **Taxe pour la protection des obtentions végétales** — due par les obtenteurs
  et détenteurs de certificats d'obtention ; même réserve sur C2, le bénéficiaire
  étant l'instance nationale des obtentions végétales.

**Industrie et branches professionnelles** — *nouvelle rubrique*

Famille entièrement absente de la version précédente. Le code des impositions
sur les biens et services a refondu en 2024 les anciennes « taxes pour le
développement des industries » en **taxes sur les biens** des filières
concernées, affectées à des **centres techniques industriels (CTI)** et à des
**comités professionnels de développement économique (CPDE)** :

- **Taxe sur les biens des industries mécaniques (TBIC)**, **de la fonderie
  (TBIF)**, **de la soudure (TBIS)**, **aérauliques et thermiques (TBIAT)** et
  **de la construction métallique (TBICC)** — CETIM, CTICM, CETIAT.
- **Taxe sur les biens des industries de l'ameublement (TBIA)** et **du bois
  (TBIB)** — CODIFAB, Institut technologique FCBA, CETIM.
- **Taxe sur les biens des industries du béton**, **des matériaux de
  construction en terre cuite (TBIMCT)** et **des roches ornementales et de
  construction (TBIROC)** — CERIB, CTMNC.
- **Taxe sur les biens des industries de l'habillement (TBIH)** — DEFI, Institut
  français du textile et de l'habillement.
- **Taxe sur les biens des industries du cuir, de la chaussure et de la
  maroquinerie (TBICCM)** — CTC.
- **Taxe sur les biens des industries de l'horlogerie, de la bijouterie-
  joaillerie, de l'orfèvrerie et des arts de la table (TBIHBJOAT)** — Comité
  Francéclat.
- **Taxe sur les biens des industries du papier (TBIP)** — Centre technique du
  papier.
- **Taxe sur les biens des industries de la plasturgie et des composites
  (TBIPC)** — CTIPC.
- **Taxe sur les biens des industries des corps gras (TICG)** — ITERG.
- **Taxe pour le développement de l'industrie de la conservation des produits
  agricoles** — CTCPA.

> **Décision retenue : REJET sur C2.** Ces dix rubriques (une quinzaine de taxes
> nommées) sont des impositions de toutes natures recouvrées par
> l'administration, mais leurs bénéficiaires — CTI et CPDE — **ne figurent pas**
> dans la liste INSEE des ODAC. La lecture stricte du critère C2 les écarte donc,
> exactement comme l'AGEFIPH et les CVO (§5.3), et c'est le classement appliqué
> dans le jeu de données. Elles sont décrites ici, et non au §5, parce qu'elles
> forment une **famille cohérente** qu'un recensement doit nommer : ce sont de
> vraies charges obligatoires pesant sur les entreprises, quelle que soit leur
> qualification statistique. La réserve — et ce qui pourrait la renverser — est
> au §6.

**Régulation économique, financière et professionnelle** — *nouvelle rubrique*
- **Droits et contributions pour frais de contrôle** au profit de l'**Autorité
  des marchés financiers** (ODAC) : contributions sur les opérations financières,
  sur les prestataires de services d'investissement, sur les OPC.
- **Cotisations assises sur les honoraires des commissaires aux comptes** et des
  **organismes tiers indépendants** certifiant les informations de durabilité,
  avec leurs **cotisations additionnelles** pour les entités d'intérêt public et
  la **contribution forfaitaire des commissaires aux comptes exerçant dans les
  pays tiers** ; s'y ajoutent, selon l'article 36 du PLF 2026, la **contribution
  annuelle acquittée par les personnes inscrites comme commissaires aux comptes**,
  un **droit fixe sur chaque rapport de certification des comptes** et une
  **contribution de la Compagnie nationale des commissaires aux comptes** — le
  tout au profit de la **Haute autorité de l'audit (H2A**, ex-H3C, ODAC).
  **Nouvelles entrées.**
- **Taxes pour frais de chambres consulaires** : **taxe additionnelle à la CFE**
  et **taxe additionnelle à la CVAE** pour les **chambres de commerce et
  d'industrie de région** (plafonds abaissés de 175 M€ en PLF 2026), **taxe
  additionnelle à la CFE** pour les **chambres de métiers et de l'artisanat**
  (−56,5 M€), régimes spécifiques d'**Alsace** et de **Moselle**.

**Enseignement supérieur et vie étudiante**
- **Contribution de vie étudiante et de campus (CVEC)** — plafond relevé de
  16 M€ en PLF 2026.

**Justice et sécurité**
- **Droit de timbre sur les procédures civiles et prud'homales** (UNCARPA, 2026)
  — cf. §4.3.
- **Contributions additionnelles aux primes d'assurance** au profit du **FGTI**
  et du **fonds Barnier** — cf. §4.3.
- **Droit affecté au fonds d'indemnisation de la profession d'avoués près les
  cours d'appel** — survivance de la réforme de 2011, toujours dans le tableau des
  ressources affectées.
- **Redevance perçue à l'occasion de l'introduction des familles étrangères en
  France** — OFII (ODAC), en complément des taxes sur les titres de séjour (§4.3).
- **Fraction des produits de la vente des biens confisqués** (AGRASC) et
  **fraction des successions en déshérence** — figurent dans le tableau des
  ressources affectées, mais sont **rejetées** au §5.5 : ce sont des dévolutions
  patrimoniales, pas des prélèvements.

### 4.11 Prélèvements au profit de l'Union européenne

Bénéficiaire = institutions de l'UE (C2 satisfait via le volet supranational).

- **Droits de douane** (ressources propres traditionnelles) — perçus pour le
  compte du budget de l'UE ; s'y ajoutent les **droits antidumping et
  compensateurs**.
- **Droits agricoles** et, historiquement, la **taxe à la production sur les
  quotas de sucre, d'isoglucose et de sirop d'inuline**.
- **Ressource propre fondée sur la TVA** (fraction d'assiette TVA).
- **Contribution fondée sur les déchets d'emballages plastiques non recyclés**.
- **Mécanisme d'ajustement carbone aux frontières (MACF / CBAM)** — entré en
  régime définitif le 1ᵉʳ janvier 2026, l'obligation d'achat de certificats ne
  produisant ses premiers versements qu'en 2027 : à surveiller, son
  rattachement (ressource propre de l'UE ou recette nationale) détermine la
  ligne où il sera comptabilisé.

> Nuance : la **contribution « ressource RNB »**, versée par l'État au budget de
> l'UE, est en comptabilité nationale un **transfert entre administrations**
> financé par les PO nationaux, et non un prélèvement supplémentaire sur les
> agents privés ; elle n'est donc pas recomptée comme PO distinct.

---

## 5. Candidats examinés puis REJETÉS

Pour chaque cas, on indique **le critère qui disqualifie**.

### 5.1 Sanctions et pénalités

| Candidat | Décision | Critère en échec / motif |
|---|---|---|
| **Amendes, pénalités et majorations** (routières, pénales, fiscales) | REJET | Hors champ : ce sont des **sanctions**, pas des prélèvements assis sur une capacité contributive. *Réserve* : la National Tax List d'Eurostat comporte une ligne « Amendes et confiscations » classée **D.2121**, c'est-à-dire parmi les droits à l'importation — les pénalités douanières y sont traitées comme l'accessoire du droit qu'elles sanctionnent. L'exception est étroite et ne remet pas en cause le rejet général. |
| **Contribution spéciale due par les employeurs d'étrangers sans autorisation de travail** | REJET | Hors champ : **sanction administrative** proportionnée au manquement, malgré le nom de « contribution ». |
| **Forfait de post-stationnement (FPS)** et stationnement payant | REJET | C3 — **contrepartie directe** (occupation du domaine public) ; ce n'est plus une amende depuis 2018. |

### 5.2 Contreparties directes (échec C3)

| Candidat | Décision | Critère en échec / motif |
|---|---|---|
| **Péages** autoroutiers et d'ouvrages d'art | REJET | C3 — paiement d'un **service rendu** (usage de l'infrastructure). |
| **Redevance d'enlèvement des ordures ménagères (REOM)** | REJET | C3 — tarifée **en fonction du service** rendu (à l'inverse de la TEOM, qui est un PO). |
| **Factures d'eau et d'assainissement** (part « exploitant ») et **participation pour le financement de l'assainissement collectif (PFAC)** | REJET | C3 — **contrepartie directe** (fourniture d'eau, raccordement, traitement). |
| **Redevances domaniales** (occupation du domaine public, terrasses, etc.) | REJET | C3 — contrepartie : droit d'occupation. |
| **Redevances aéroportuaires et redevances de navigation aérienne** | REJET | C3 — **service rendu** (usage des installations, contrôle aérien) ; à distinguer de la **taxe d'aéroport**, qui est un PO (§4.10). |
| **Redevances d'utilisation des fréquences radioélectriques** | REJET | C3 — contrepartie : droit d'usage d'une ressource rare du domaine public. |
| **Redevances de l'INPI** (procédures de propriété industrielle, registre du commerce) | REJET | C3 — **service rendu** individualisé, malgré leur inscription parmi les *taxes affectées plafonnées* du PLF 2026 (+45 M€). Illustration directe de l'avertissement du §2. |
| **Émoluments et débours des notaires, huissiers et greffiers** | REJET | C2 + C3 — rémunération d'un officier ministériel ; seuls les **DMTO** compris dans les « frais de notaire » sont des PO. |
| **Redevance pour frais d'envoi des certificats d'immatriculation** | REJET | C3 — coût d'acheminement d'un titre. |
| **Redevances perçues lors du lancement de certains matériels aéronautiques** | REJET | C3 — contrepartie d'une prestation de contrôle et d'homologation. |

### 5.3 Bénéficiaire hors APU (échec C2)

| Candidat | Décision | Critère en échec / motif |
|---|---|---|
| **Cotisations aux ordres professionnels** (médecins, avocats, experts-comptables…), **cotisations syndicales** | REJET | C2 — bénéficiaire **hors périmètre APU** (organismes privés). |
| **Contributions volontaires obligatoires (CVO / CVE)** des interprofessions agricoles | REJET | C2 — versées à des **interprofessions de droit privé** ; le Conseil constitutionnel juge qu'elles ne constituent pas des « impositions de toutes natures ». Obligatoires, mais hors APU. |
| **Éco-contributions REP** (emballages, textiles, meubles, bâtiment…) | REJET | C2 — perçues par des **éco-organismes agréés** de droit privé, non par une APU. |
| **Contribution AGEFIPH** (employeurs privés, obligation d'emploi des travailleurs handicapés) | REJET | C2 — l'AGEFIPH **ne figure pas** dans la liste INSEE des ODAC, à la différence du **FIPHFP** (§4.10). Asymétrie assumée : deux contributions jumelles, deux bénéficiaires de nature différente. |
| **Primes d'assurances obligatoires** (RC automobile, décennale) | REJET | C2 + C3 — versées à un **assureur privé** en échange d'une couverture. La **TSCA** assise sur ces primes est, elle, un PO (§4.3). |
| **Contribution des assurés au Fonds de garantie des assurances obligatoires de dommages (FGAO)** | REJET | C2 — personne morale de droit privé, absente de la liste ODAC — contrairement au **FGTI**, qui y figure et dont le prélèvement sur les contrats d'assurance de biens est donc un PO. Les deux figurent côte à côte dans le tableau des ressources affectées du PLF 2026 (lignes 90 et 91) : illustration parfaite de l'avertissement du §2. |
| **Contributions additionnelles aux primes d'assurance au profit de la Caisse centrale de réassurance (CCR)** — surprime « catastrophes naturelles » (120 M€) — et **contribution forfaitaire annuelle à la charge des professionnels de santé** (8,3 M€, fonds de garantie des dommages liés aux actes de soins) | REJET | C2 — la CCR est une **société anonyme d'assurance** détenue par l'État, classée parmi les sociétés financières et non parmi les APU. Le prélèvement est obligatoire, son bénéficiaire ne l'est pas. |
| **Cotisations aux services de prévention et de santé au travail (SPSTI)** | REJET | C2 + C3 — organisme privé, en contrepartie d'un service de suivi médical. |
| **Contribution patronale au dialogue social** (0,016 % de la masse salariale) | REJET | C2 — versée à l'**AGFPN**, association de gestion du fonds paritaire national, **hors périmètre APU**. Elle figure pourtant en ligne 10 du tableau des ressources affectées du PLF 2026. |
| **Redevance pour copie privée** | REJET | C2 — perçue par des **sociétés de gestion collective** de droit privé et reversée aux ayants droit ; c'est une rémunération, non un impôt. |
| **Majoration de la taxe sur les assurances de protection juridique au profit du Conseil national des barreaux** | REJET | C2 — le CNB est un établissement d'**utilité publique de droit privé**. |
| **Contribution pour frais de contrôle de l'ACPR** | REJET | C2 — l'ACPR est **adossée à la Banque de France**, classée dans les sociétés financières (S.121), et non dans les APU — à la différence de l'**AMF**, qui est un ODAC. Cas limite discuté au §6. |

### 5.4 Absence de versement effectif ou de flux (échec C1)

| Candidat | Décision | Critère en échec / motif |
|---|---|---|
| **Cotisations sociales imputées** (employeur fictif, pensions des fonctionnaires d'État) | REJET | C1 — **pas de versement effectif**. |
| **Certificats d'économies d'énergie (CEE)** | REJET | C1 + C2 — obligation **en nature** (obtenir des certificats) et non versement monétaire à une APU, quoique le coût soit répercuté sur les factures. |
| **Obligations d'achat d'électricité renouvelable à prix contractuels** | REJET *avec réserve forte* | Aucun versement à une APU : l'opérateur achète de l'énergie à un prix administré. Mais la National Tax List d'Eurostat comporte pour la France une ligne « **Achats d'énergies renouvelables à prix contractuels** » classée **D.29H** : la comptabilité nationale y voit un impôt sur la production, imputé au titre du surcoût imposé. Cas limite recensé au §6. |
| **Obligations d'investissement dans la production audiovisuelle** (éditeurs, SMAD) | REJET | C1 + C2 — obligation de **dépenser** dans un secteur, sans versement à une APU. |
| **Obligation de détention de stocks stratégiques pétroliers** (volet en nature) | REJET | C1 — obligation de stockage ; seule la **contribution monétaire au CPSSP** est un PO (§4.10). |
| **Franchises médicales et participation forfaitaire** | REJET | Non un prélèvement : un **moindre remboursement**, pas un flux versé à une APU. |
| **Crédits d'impôt restituables** (CICE historique, CIR…) | N/A | Non un prélèvement : ils **minorent** les PO ; leur traitement explique l'écart de taux INSEE / Eurostat. |

### 5.5 Versements facultatifs ou recettes non fiscales

| Candidat | Décision | Critère en échec / motif |
|---|---|---|
| **Cotisations facultatives** : épargne retraite individuelle (PER, ex-PERP), assurance-vie, mutuelles et prévoyance facultatives | REJET | C3 — versement **non obligatoire** (libre choix). |
| **Revenus du domaine, dividendes d'entreprises publiques, produits de cessions, loyers** | REJET | C3 — recettes patrimoniales **avec contrepartie**, non des prélèvements. |
| **Produit de la vente des biens confisqués ; successions en déshérence ; contrats d'assurance-vie en déshérence** | REJET | Non un prélèvement : **dévolution patrimoniale** au profit de l'État, sans fait générateur contributif. |
| **Emprunts et produits de la dette** | REJET | Non un prélèvement : ressource remboursable, librement souscrite. |
| **Dons et legs aux administrations** | REJET | C3 — **volontaires**. |
| **Part salariale de l'assurance chômage** | REJET (depuis 2018) | N'existe plus : supprimée et remplacée par de la CSG (incluse, elle). |
| **Contribution à l'audiovisuel public (ex-redevance TV)** | REJET *aujourd'hui* | Était un **PO jusqu'en 2022** ; supprimée et remplacée par une fraction de TVA (elle, comptée). Mentionnée pour mémoire. |

### 5.6 Flux internes au secteur public

| Candidat | Décision | Critère en échec / motif |
|---|---|---|
| **Cotisation des collectivités au CNFPT** (0,9 % de la masse salariale) et **cotisations aux centres de gestion** | REJET | **Transfert entre APU** : payé par des APUL à une APUL. Obligatoire, mais consolidé en comptabilité nationale, donc pas un prélèvement supplémentaire sur les agents privés. La cotisation CNFPT figure pourtant en ligne 47 du tableau des ressources affectées du PLF 2026. |
| **Cotisation obligatoire au Comité de gestion des œuvres sociales des personnels hospitaliers (CGOS)** | REJET | Double motif : payée par des **hôpitaux publics** (APU) à une **association de droit privé** — ni prélèvement sur un agent privé, ni bénéficiaire APU. Figure en ligne 66 du même tableau. |
| **Prélèvement SRU** sur les communes déficitaires en logement social | REJET | Idem — et par ailleurs de nature **sanctionnatrice**. |
| **Contribution « ressource RNB » de la France au budget de l'UE** | REJET | **Transfert entre administrations** financé par les PO nationaux (cf. §4.11). |
| **Prélèvements sur les recettes de l'État au profit des collectivités** (DGF, FCTVA…) | REJET | Dotations : dépense de l'État, pas prélèvement sur un redevable. |

---

## 6. Cas limites et points de vigilance

**Nouvelle section.** Sept dossiers où la qualification est disputée, mal
stabilisée ou susceptible de basculer. Les signaler vaut mieux que de trancher à
tort.

| Cas | Difficulté | Position retenue ici |
|---|---|---|
| **Taxe de balayage** | Imposition de toute nature, mais **produit plafonné au coût du service** balayé — ce qui est le critère usuel de la redevance. | **PRIS** (§4.5) : le Conseil d'État et la doctrine administrative la qualifient d'imposition ; le plafonnement encadre le rendement, il ne crée pas de contrepartie individualisée. |
| **Contribution ACPR** | Imposition de toutes natures au sens constitutionnel, mais bénéficiaire hors APU (Banque de France). | **REJET** sur C2 (§5.3), avec réserve : un reclassement sectoriel la ferait basculer. |
| **Contributions au FGDR** (fonds de garantie des dépôts et de résolution) | Le FGDR **est** un ODAC, donc C2 est satisfait ; mais une part des contributions prend la forme de **dépôts de garantie restituables** (certificats d'associé), ce qui contredit C3. | **Non tranché.** À qualifier contribution par contribution. |
| ~~**Contributions au Fonds de résolution unique (FRU)**~~ | *Cas tranché.* | **PRIS** — la National Tax List d'Eurostat comporte une ligne « **Contribution au SRF (single resolution fund)** » classée **D.29H** pour la France. Le cas est donc résolu par la source de référence, non par déduction ; entrée reportée au §4.3. |
| **Contributions conventionnelles aux OPCO** | Les OPCO figurent dans la liste INSEE des ODAC, ce qui satisfait C2 ; mais ces contributions sont créées par **accord de branche**, non par la loi. | **Non tranché** : obligatoires par extension de l'accord, elles occupent une zone grise de C3. |
| **Taxes affectées à des organismes de droit privé** *(tranché : REJET C2)* : une quinzaine de **taxes sur les biens** des filières industrielles (CTI et CPDE), taxes de formation sectorielle (AFT, ANFA, 3CABTP), **cotisation BTP intempéries**, **redevance sur les paris hippiques** (sociétés de courses), fraction « loto du patrimoine » (Fondation du patrimoine) | Ce sont des **impositions de toutes natures** votées par le Parlement et recouvrées par l'administration, mais versées à des organismes **hors liste ODAC**. Leur enregistrement en PO suppose un **réacheminement** (*rerouting*) du flux à travers l'État en comptabilité nationale. | **Tranché : REJET sur C2**, par cohérence avec l'AGEFIPH et les CVO (§5.3) — c'est le classement appliqué dans `data/`. Mais c'est le bloc le plus fragile du document, une vingtaine de prélèvements : un arbitrage explicite de l'INSEE en faveur du réacheminement les ferait tous basculer d'un coup. Décrits au §4.10. |
| **Obligations d'achat d'électricité renouvelable** | Aucun flux vers une APU, mais la NTL d'Eurostat les enregistre en **D.29H** pour la France (« achats d'énergies renouvelables à prix contractuels »). | **Divergence assumée** entre l'analyse juridique (pas de versement à une APU → §5.4) et le traitement statistique (impôt sur la production imputé). Le second fait foi pour le ratio de 42,7 %. |
| **MACF / CBAM** | Achat obligatoire de certificats, premiers versements en 2027. | À surveiller (§4.11) : ressource propre de l'UE ou recette nationale. |
| **Redevances sanitaires et de contrôle** | Certaines sont des impositions (abattage, découpage), d'autres facturent un contrôle individualisé à l'opérateur. | Traitées **au cas par cas** ; les impositions figurent au §4.10, les facturations au §5.2. |

> **La leçon transversale** : un prélèvement peut entrer dans le champ des PO ou
> en sortir **sans qu'aucune règle fiscale ne change**, par simple reclassement
> sectoriel d'un organisme par l'INSEE. Le précédent d'Action Logement Services
> (2022) le prouve. Tout recensement est donc daté par construction.

---

## 7. Prélèvements récemment supprimés (mémoire)

**Nouvelle section.** Elle sert deux fins : éviter de réintroduire par erreur des
prélèvements abrogés (les listes en circulation en contiennent beaucoup), et
documenter deux corrections apportées à la version précédente de ce document.

### 7.1 Corrections apportées à ce document

| Entrée corrigée | Statut réel | Fondement |
|---|---|---|
| **Taxe pour la gestion des eaux pluviales urbaines (TGEPU)** — auparavant listée en §4.5 comme un PO en vigueur | **Supprimée** : instituée en 2011, **abrogée en 2015**, son coût de recouvrement excédant son rendement. Aucun financement de substitution n'a été institué. | Réponses ministérielles au Sénat (2023) sur le financement de la gestion des eaux pluviales après abrogation de la taxe. |
| **Taxe annuelle sur les résidences mobiles terrestres** — auparavant listée en §4.5 | **Abrogée au 1ᵉʳ octobre 2019** par le 20° du III de l'article 26 de la loi n° 2018-1317 du 28 décembre 2018 de finances pour 2019 (art. 1013 du CGI). | BOFiP, *ENR – Suppression de la taxe annuelle due sur les résidences mobiles terrestres*. |

### 7.2 Autres suppressions notables

- **Contribution sur les activités privées de sécurité** (« taxe CNAPS ») —
  supprimée au 1ᵉʳ janvier 2020 (LF 2019) ; le CNAPS est désormais financé par le
  budget du ministère de l'Intérieur.
- **Contribution à l'audiovisuel public** (particuliers) — supprimée en 2022,
  remplacée par une fraction de TVA.
- **Taxe d'habitation sur les résidences principales** — supprimée par paliers,
  éteinte en 2023.
- **Contribution sur la rente inframarginale de la production d'électricité
  (CRIM)** — dispositif temporaire (2022-2025), **éteint** : aucune recette
  attendue en 2026.
- **Contribution des gestionnaires de réseaux publics de distribution
  d'électricité au FACÉ** (financement de l'électrification rurale) — **supprimée
  au 1ᵉʳ août 2025** par la LF 2025 et remplacée par une fraction de l'accise sur
  l'électricité. Le prélèvement n'a pas disparu : il a changé de véhicule.
- **Taxe sur les hydrofluorocarbures (HFC)** — cas singulier : instituée par la
  LF 2019, son entrée en vigueur a été reportée trois fois (2021, 2023, 2025)
  avant son **abrogation par la loi n° 2025-127 du 14 février 2025**. Elle n'a
  donc **jamais été perçue**. À ne pas compter parmi les prélèvements, malgré sa
  présence dans plusieurs listes en circulation.
- **Contribution pour l'aide juridique** (« timbre de 35 € ») — supprimée en
  2014 ; à ne pas confondre avec le **nouveau droit de timbre sur les procédures
  civiles et prud'homales** créé en 2026 (§4.3).
- **Impôt de solidarité sur la fortune (ISF)** — remplacé par l'IFI en 2018.
- **Taxe de risque systémique des banques**, **imposition forfaitaire annuelle
  des sociétés (IFA)**, **taxe d'abattage**, **versement pour sous-densité**,
  **taxe sur les farines**, **taxe sur les boissons énergisantes**, **taxe sur
  les produits cosmétiques**, **taxe administrative sur les opérateurs de
  communications électroniques**, **taxe sur les produits de vapotage**,
  **contribution de solidarité des employeurs publics** (1 %, supprimée en 2018),
  **taxe sur l'édition des ouvrages de librairie** et **taxe sur les appareils de
  reproduction** — supprimées au fil des lois de finances.
- **Redevance d'archéologie préventive** — non pas supprimée mais **transformée**
  en *taxe d'archéologie préventive* (2022), adossée à la taxe d'aménagement.
- **Taxe locale d'équipement**, **taxe départementale des espaces naturels
  sensibles**, **taxe départementale CAUE**, **participation pour voirie et
  réseaux**, **versement pour dépassement du plafond légal de densité** —
  absorbées par la **taxe d'aménagement**.
- **Taxes communale et départementale sur la consommation finale d'électricité**
  — absorbées par l'**accise sur l'électricité**, dont les collectivités reçoivent
  une part.

> Ces absorptions ne réduisent pas la pression fiscale : elles **renomment et
> regroupent**. C'est l'une des principales sources d'erreur des recensements
> fondés sur des listes anciennes.

---

## 8. Du raisonnement au pipeline reproductible

Les §2–§3 décrivent la *méthode de décision* ; les §4–§7 l'appliquent à la main.
Pour produire la liste **ligne à ligne** de façon **reproductible et tracée**, le
dépôt fournit un pipeline (dossier [`pipeline/`](pipeline/)) qui automatise
exactement ce raisonnement :

```
fetch ──▶ normalize ──▶ classify ──▶ reconcile ──▶ report
sources    parsing       règle         dédup +       data/*.csv|json
officielles canonique    C1–C3         couverture    docs/RAPPORT.md
```

- **Sources** (cf. `pipeline/config/sources.yaml`) : la **National Tax List
  d'Eurostat** (liste détaillée impôt par impôt, classée D.2/D.5/D.91/D.61 avec
  montants) comme épine dorsale, le **Voies & Moyens Tome I** (PDF, énumération
  des *impositions de toutes natures*), la liste **OpenDataSoft des taxes
  affectées**, et un **socle curé** reprenant les §4–§5 ci-dessus (garantit un
  résultat même hors-ligne).
- **Règle de décision** : les critères C1–C3 et les cas limites (TEOM ≠ REOM,
  cotisations imputées, amendes, redevances…) sont encodés dans
  `pipeline/config/decision_rules.yaml`.
- **Preuve d'exhaustivité** : la couverture (Σ des PO retenus rapportée à
  l'enveloppe INSEE de 1 254 Md€) est calculée et publiée dans
  [`docs/RAPPORT.md`](docs/RAPPORT.md) ; les lignes non classables apparaissent
  explicitement en « à arbitrer ».

Lancement : `cd pipeline && make install && make all` (ou `make offline`).
Détails dans [`pipeline/README.md`](pipeline/README.md). Sorties versionnées
dans [`data/`](data/).

### Articulation entre le document et le jeu de données

Les deux formats ne font pas double emploi et ne se remplacent pas :

| | `README.md` (ce document) | `data/prelevements_obligatoires.{csv,json}` |
|---|---|---|
| Unité | La **famille** de prélèvements, avec son raisonnement | La **ligne**, avec sa provenance et son montant |
| Ce qu'il apporte | Pourquoi un candidat est pris ou rejeté ; les cas limites ; l'histoire des suppressions | Le décompte, les montants, la couverture vérifiable |
| Ce qu'il ne peut pas faire | Servir de base de calcul | Expliquer une décision de qualification |

Les entrées curées à la main — celles issues du dépouillement documentaire décrit
au §4 — sont versées au pipeline via `pipeline/seed/supplement.csv`, puis
fusionnées avec les sources officielles. **C'est le fichier à éditer** pour
ajouter un prélèvement au jeu de données ; `data/` est généré et ne doit jamais
être modifié à la main.

---

## 9. Sources

### 9.1 Définition et cadre statistique

- **INSEE — Définition des prélèvements obligatoires** :
  <https://www.insee.fr/fr/metadonnees/definition/c1571>
- **INSEE — Taux de prélèvements obligatoires rapporté au PIB** :
  <https://www.insee.fr/fr/statistiques/2381412>
- **INSEE — Liste des organismes divers d'administration centrale (ODAC)**,
  édition mai 2025 (situation 2023) — instrument de tranchage du critère C2 (y
  figurent Action Logement Services, le FIPHFP, l'AGS, le FGTI, le FGDR, la
  CGLLS, l'AMF, la H2A, l'OFII, l'ART, l'EPSF, l'INAO, le CPSSP, les OPCO, le
  CNM, l'ANSES ; n'y figure pas l'AGEFIPH) :
  <https://www.insee.fr/fr/statistiques/fichier/8574832/Liste_ODAC_SD2023.pdf>
- **OCDE — Statistiques des recettes publiques (brochure 2025, 3 critères)** :
  <https://www.oecd.org/content/dam/oecd/fr/topics/policy-sub-issues/recettes-fiscales-mondiales/brochure-statistiques-des-recettes-publiques.pdf>
- **Eurostat — National Tax List (NTL), onglet France** : la liste de référence
  ligne à ligne des impôts et cotisations français tels qu'ils sont *réellement
  enregistrés* en comptabilité nationale, avec leur code SEC (D.211, D.214,
  D.29, D.51, D.59, D.91) et leur montant annuel. **141 lignes-feuilles** pour
  la France. C'est la seule source qui tranche empiriquement les cas litigieux :
  elle a résolu dans cette version la PEEC (D.29C), la contribution au Fonds de
  résolution unique (D.29H) et les obligations d'achat d'électricité
  renouvelable (D.29H) :
  <https://ec.europa.eu/eurostat/statistics-explained/images/e/ef/National_tax_lists_2025_2026-04-22.xlsx>
- **Eurostat — Système européen des comptes (SEC 2010)**, référence pour le
  traitement des quotas d'émission en impôts sur la production (D.29) :
  <https://ec.europa.eu/eurostat/fr/web/esa-2010>
- **INSEE — Le compte des administrations publiques en 2024** (Insee Première
  n° 2054) : <https://www.insee.fr/fr/statistiques/8574492>
- **FIPECO — La définition, le niveau et la répartition des prélèvements obligatoires** :
  <https://www.fipeco.fr/fiche/La-d%C3%A9finition,-le-niveau-et-la-r%C3%A9partition-des-pr%C3%A9l%C3%A8vements-obligatoires>
- **FIPECO — Les prélèvements obligatoires en France et dans la zone euro en 2024** :
  <https://fipeco.fr/commentaire/Les%20pr%C3%A9l%C3%A8vements%20obligatoires%20en%20France%20et%20dans%20la%20zone%20euro%20en%202024>
- **FIPECO — Les administrations publiques de la comptabilité nationale** (ODAC
  vs ODAL, cas des agences de l'eau) :
  <https://www.fipeco.fr/fiche/Les-administrations-publiques-de-la-comptabilit%C3%A9-nationale>

### 9.2 Sources budgétaires primaires

- **Évaluation des voies et moyens, tome I (annexe au PLF 2026)** — dépouillée
  intégralement pour cette version : lignes de recettes fiscales, encadrés
  méthodologiques par impôt, plafonnement des taxes affectées, produit des impôts
  affectés à des personnes morales autres que l'État :
  <https://www.assemblee-nationale.fr/dyn/dyn/contenu/visualisation/1087930/file/PLF%202026%20-%20V&M%20TI%20-%20Evaluations%20des%20recettes.pdf>
- **Projet de loi de finances pour 2026, texte intégral** — deux sources
  primaires dépouillées intégralement pour cette version :
  l'**article 36 « Dispositions relatives à l'affectation de ressources à des
  tiers »**, tableau de **135 lignes** (référence juridique, intitulé,
  bénéficiaire, rendement prévisionnel 2026, plafond d'affectation), qui fonde
  le §4.10 ; et l'**état A « Voies et moyens »** (article 48), seule énumération
  officielle exhaustive des recettes du budget général, qui fonde les §4.1 à
  §4.4 :
  <https://www.assemblee-nationale.fr/dyn/17/textes/l17b1906_projet-loi.pdf>
- **budget.gouv.fr — PLF 2026 et documents annexés** (dont l'annexe *Liste des
  taxes affectées*, publiée séparément en format tableur depuis le PLF 2026) :
  <https://www.budget.gouv.fr/documentation/documents-budgetaires-lois/exercice-2026/plf-2026>
- **Conseil des prélèvements obligatoires (Cour des comptes)** — périmètre et
  taxes affectées : <https://www.ccomptes.fr/fr/conseil-des-prelevements-obligatoires-cpo>
- **economie.gouv.fr (DAJ) — Impôts et taxes affectés : les constats du CPO** :
  <https://www.economie.gouv.fr/daj/lettre-de-la-daj-impots-et-taxes-affectes-les-constats-du-conseil-des-prelevements-obligatoires>
- **Inspection générale des finances — Les taxes à faible rendement** (2014,
  192 taxes recensées) :
  <https://www.igf.finances.gouv.fr/files/live/sites/igf/files/contributed/IGF%20internet/2.RapportsPublics/2014/2013-M-095%20Tome%201.pdf>
- **Cour des comptes — Les taxes à faible rendement** (2019, recommandation d'un
  inventaire annuel exhaustif) :
  <https://www.ccomptes.fr/fr/publications/les-taxes-faible-rendement>

### 9.3 Sources sectorielles

- **Cour des comptes — « L'autonomie fiscale en outre-mer : Nouvelle-Calédonie,
  Polynésie française, Saint-Barthélemy, Saint-Martin, Saint-Pierre-et-Miquelon,
  Wallis-et-Futuna »** (rapport public thématique) :
  <https://www.ccomptes.fr/fr/documents/26287>
- **Cour des comptes — « L'octroi de mer, une taxe à la croisée des chemins »**
  (2024) : <https://www.ccomptes.fr/fr/publications/loctroi-de-mer-une-taxe-la-croisee-des-chemins>
- **Direction des services fiscaux de Nouvelle-Calédonie — contribution
  calédonienne de solidarité et TGC** : <https://dsf.gouv.nc/>
- **Direction des impôts et des contributions publiques de Polynésie française —
  contribution de solidarité territoriale, patentes, impôt foncier, centimes
  additionnels communaux** : <https://www.service-public.pf/dicp/>
- **Direction des services fiscaux de Saint-Pierre-et-Miquelon — Code local des
  impôts** (table analytique dépouillée pour le §4.7) :
  <https://www.services-fiscaux975.fr/files/file/Documentation/2022/CLI%202022.pdf>
- **IEOM — Rapport annuel Wallis-et-Futuna** (structure des recettes fiscales du
  territoire) :
  <https://www.ieom.fr/IMG/rapport_annuel_ieom_wallis-et-futuna_2022/files/basic-html/page60.html>
- **FIPECO — L'économie et les finances publiques de Saint-Barthélemy** :
  <https://www.fipeco.fr/commentaire/L'%C3%A9conomie%20et%20les%20finances%20publiques%20de%20Saint-Barth%C3%A9lemy>
- **Légifrance — Code de la sécurité sociale, section « Prélèvements sur les
  jeux, concours et paris » (art. L. 137-20 à L. 137-25)** :
  <https://www.legifrance.gouv.fr/codes/id/LEGISCTA000021535946>
- **Légifrance — Code des impositions sur les biens et services, section « Taxe
  sur l'exploitation des infrastructures de transport de longue distance »
  (art. L. 425-1 à L. 425-20)** :
  <https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000044595989/LEGISCTA000048796741/>
- **BOFiP — Taxe sur l'exploitation des infrastructures de transport de longue
  distance** (LF 2024, art. 100) :
  <https://bofip.impots.gouv.fr/bofip/14294-PGP.html/identifiant=BOI-AIS-MOB-50-20240612>
- **BOFiP — Suppression de la taxe annuelle due sur les résidences mobiles
  terrestres** (LF 2019, art. 26) :
  <https://bofip.impots.gouv.fr/bofip/12015-PGP.html/identifiant=ACTU-2019-00190>
- **collectivites-locales.gouv.fr — Taxe de balayage** (transfert du CGI au
  CGCT au 1ᵉʳ janvier 2019) :
  <https://www.collectivites-locales.gouv.fr/taxe-de-balayage>
- **Sénat — Financement de la gestion des eaux pluviales après abrogation de la
  taxe pluviale** :
  <https://www.senat.fr/questions/base/2023/qSEQ230406451.html>
- **Sénat — Conséquences de la suppression de la contribution des gestionnaires
  de réseau de distribution d'électricité au FACÉ** (2025) :
  <https://www.senat.fr/questions/base/2025/qSEQ25040446S.html>
- **Citepa — Suppression de la taxe sur les HFC** (jamais entrée en vigueur,
  abrogée en 2025) :
  <https://www.citepa.org/suppression-de-la-taxe-sur-les-hfc-initialement-prevue-pour-2021-et-de-la-tgap-sur-les-lubrifiants/>
- **BOFiP — Taxe sur les conventions d'assurances, tarifs applicables aux
  véhicules terrestres à moteur** :
  <https://bofip.impots.gouv.fr/bofip/3383-PGP.html/identifiant=BOI-TCAS-ASSUR-30-10-30-20240619>
- **Régime local d'assurance maladie d'Alsace-Moselle** (taux 2026 maintenu à
  1,30 %) : <https://regime-local.fr/>
- **Projet de loi de financement de la sécurité sociale pour 2026** (mesures de
  recettes, dont la contribution exceptionnelle sur les organismes
  complémentaires) :
  <https://www.securite-sociale.fr/files/live/sites/SSFR/files/medias/PLFSS/2026/PLFSS%20pour%202026.pdf>
- **Sénat — PLFSS 2026, examen des articles** :
  <https://www.senat.fr/rap/l25-131-21/l25-131-21.html>
- **Conseil d'État, 28 avril 2026, n° 498073** — contentieux du classement
  d'Action Logement Services en administration publique :
  <https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2026-04-28/498073>
- **Sénat — PLF 2026, conditions générales de l'équilibre financier** :
  <https://www.senat.fr/rap/l25-139-21/l25-139-21_mono.html>

### 9.4 Synthèses encyclopédiques

- **Wikipédia — Prélèvements obligatoires** :
  <https://fr.wikipedia.org/wiki/Pr%C3%A9l%C3%A8vements_obligatoires>
- **Wikipédia — Liste des impôts et taxes français** (≈ 430 entrées, en vigueur
  et supprimées ; dépouillée intégralement pour cette version — utile comme
  **liste de candidats**, mais partiellement datée : plusieurs entrées y sont
  mal classées, ce qui a nécessité les vérifications du §7) :
  <https://fr.wikipedia.org/wiki/Liste_des_imp%C3%B4ts_et_taxes_fran%C3%A7ais>
- **Wikipédia — Contribution volontaire obligatoire** (statut juridique des
  CVO/CVE) :
  <https://fr.wikipedia.org/wiki/Contribution_volontaire_obligatoire>
- **Wikipédia — Contribution tarifaire d'acheminement** :
  <https://fr.wikipedia.org/wiki/Contribution_tarifaire_d%27acheminement>

> *Note méthodologique.* Les montants et taux cités (1 254 Md€ ; 42,7 % du PIB en
> 2024) proviennent des comptes nationaux INSEE. Les rendements par ligne
> proviennent du Voies et moyens tome I du PLF 2026 : ce sont donc des
> **prévisions du projet de loi**, que le texte finalement adopté a pu modifier
> — c'est notamment le cas de la taxe sur le patrimoine financier (§4.1). La
> liste des dispositifs reflète le droit en vigueur **mi-2026**, lois de finances
> et de financement de la sécurité sociale pour 2026 comprises. Deux entrées sont
> du **droit voté non encore productif** et signalées comme telles : la taxe sur
> le patrimoine financier / holdings patrimoniales (§4.1) et le MACF (§4.11).

---

## 10. Pistes encore ouvertes

**Contrôle de couverture effectué.** Avant de lister ce qui manque, il faut dire
ce qui a été vérifié. Des confrontations automatiques ont été menées entre le
présent document et ses listes sources :

| Liste source | Entrées | Couverture finale |
|---|---|---|
| Article 36 du PLF 2026 (ressources affectées) | 131 lignes exploitables | **131 / 131** |
| État A du PLF 2026 (recettes du budget général) | ≈ 90 lignes fiscales | **intégralement dépouillé** |
| Liste encyclopédique, section « en vigueur » | 337 entrées | **337 / 337** |
| National Tax List d'Eurostat, onglet France | 141 lignes-feuilles | **dépouillée ; 3 cas litigieux tranchés** |

Le premier passage laissait six entrées non couvertes ; leur examen a produit
six décisions distinctes, ce qui illustre bien la méthode : la **TICHLC** est
fondue dans l'accise sur les énergies (§4.2) ; la **taxe HFC** n'a jamais été
perçue et est abrogée (§7) ; la **contribution FACÉ** a été supprimée en 2025 et
remplacée par une fraction d'accise (§7) ; la **taxe d'atterrissage** relève de
la fiscalité ultramarine (§4.6) ; la **taxe sur les obtentions végétales** entre
au §4.10 sous réserve C2 ; les **redevances de lancement aéronautique** sont
rejetées comme contrepartie de service (§5.2).

La confrontation à la **National Tax List d'Eurostat** est d'une autre nature :
elle ne mesure pas une couverture mais **arbitre**. C'est la seule source qui
dise ce que la comptabilité nationale enregistre *réellement* comme impôt. Elle
a tranché trois cas que le raisonnement laissait ouverts — PEEC, contribution au
Fonds de résolution unique, obligations d'achat d'électricité renouvelable — et
confirmé le classement de la quasi-totalité des autres.

Ce contrôle mesure la **couverture par rapport à des listes existantes**, pas
l'exhaustivité absolue — laquelle n'est atteignable par personne, y compris par
l'administration (§1). Ce qui reste à dépouiller, par ordre de rendement
attendu :

- **L'annexe « Liste des taxes affectées » du PLF 2026**, publiée séparément en
  format tableur. L'**article 36 du PLF** en donne l'essentiel — 135 lignes,
  dépouillées intégralement pour cette version — mais il ne couvre que les
  ressources **soumises à autorisation annuelle de perception** ; l'annexe
  complète, plus large, reste à récupérer (le site budget.gouv.fr refuse l'accès
  automatisé). Écart estimé : quelques dizaines de lignes sur ≈ 238.
- **Les six codes fiscaux des collectivités à autonomie fiscale** (§4.7). La
  structure de chacun a été relevée pour cette version — table analytique du code
  local de Saint-Pierre-et-Miquelon, répertoire de la direction des services
  fiscaux calédonienne, code des impôts polynésien, ventilation budgétaire de
  Saint-Barthélemy et de Wallis-et-Futuna. Reste le **détail article par
  article** : chacun compte plusieurs dizaines d'impositions et de tarifs, dont
  beaucoup n'ont aucun équivalent métropolitain. C'est le gisement le plus riche
  encore ouvert, mais le moins utile au ratio national, puisque cinq de ces six
  collectivités sont hors champ des comptes nationaux (§2.1).
- **La longue traîne des taxes à faible rendement** : l'IGF en recensait 192 en
  2014 sous le seuil de 150 M€, et la Cour des comptes constatait en 2019 qu'aucun
  inventaire à jour n'existait. Beaucoup ont été supprimées depuis (§7), d'autres
  créées ; l'état exact du stock est **inconnu de l'administration elle-même**.
- **Les taxes locales facultatives** instituées par délibération : leur existence
  dépend de chaque collectivité, ce qui rend l'énumération exhaustive
  impraticable. L'inventaire par catégorie du §4.5 est le bon niveau de
  granularité ; un décompte ne le serait pas.
- **Les cas limites du §6**, dont trois ne sont pas tranchés (FGDR, FRU,
  contributions conventionnelles aux OPCO) et exigeraient l'avis de l'INSEE ou de
  la Commission des comptes.
- **Le suivi des reclassements sectoriels** : tout reclassement d'organisme par
  l'INSEE peut faire entrer ou sortir un prélèvement du champ **sans modification
  de la règle fiscale**. Le précédent d'Action Logement montre que ce risque n'est
  pas théorique ; la contribution ACPR (§5.3) et le FGDR (§6) sont les candidats
  les plus exposés.
