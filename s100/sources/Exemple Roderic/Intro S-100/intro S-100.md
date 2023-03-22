# Introduction à la S-100

## norme

## Contexte

* 1992 - **S-57**: l’Organisation Hydrographique Internationale (OHI - International Hydrographic Organization, IHO) adopte une **norme** ("standard", en anglais) **pour définir les spécifications**
  * **des cartes électroniques** (ENC - Electronic Nautical Chart) appelées à être utilisées à bord des navires, ainsi que
  * **des systèmes qui les affichent** (Electronic Chart Display and Information System - [ECDIS](https://www.francis-fustier.fr/Glossaire/glossaire.html#ecdis)).
* 1995 - **S-57 entre en vigueur** (c'est la norme officielle pour les ECDIS).
* 2000 - S-57 version 3.1: actualisation et refonte de la norme. 10 ans sont laissés aux industriels et éditeurs pour mettre en conformité leurs systèmes de navigation embarqués sur les navires.
* 2008 - **ECDIS obligatoire** sur les navires à grande vitesse.
* 2010 - **S-100**: Publication de la norme **S-100 (Universal Hydrographic Data Model)**. Le but est s’adapter à la croissance rapide des données disponibles pour la navigation en proposant un modèle de données extensible (universel).
* 2011 - L'Organisation Maritime Internationale (OMI - International Maritime Organization, IMO) adopte la S-100.
* 2011- **S-101**: respectant les critères de la norme S-100, une nouvelle norme destinée à remplacer la S-57 est publiée: la **S-101 (Electronic navigational chart)**.
* 2012-2018 - **ECDIS** rendus progressivement **obligatoires** sur les navires SOLAS (passagers 500T+, cargo 10000T+, tankers 3000T+).
* 2024 - Mise en production d'**ENC à la norme S-101**, conjointement aux recommandations de l'OMI pour la production des nouveaux ECDIS.
* 2024 - Les **ECDIS** mis sur le marché à partir de 2024 doivent être capables de **consommer des ENC en S-57 et en S-100**.
* 2024-2030 - Période de transition pendant laquelle **les ENC sont conjointement proposée aux normes** **S-57 et S-101**.
* 2026 - sortie prévue des premiers **ECDIS S-100**
* 2030 - Fin de la période de transition. Tous les **ECDIS en fonction doivent être compatibles S-101**.

## Qu'est-ce que la norme S-100?

La S-100 fournit le cadre nécessaire pour le développement de la prochaine génération d'ENC, ainsi que d’autres produits numériques demandés par les communautés hydrographiques, maritimes et des SIG.

A terme, la S-100 remplacera la S-57, qui est la norme encore en usage pour les données hydrographiques numériques.

### Limites de la norme S-57

**La S-57** (en particulier version 4) a été aligné sur les normes ISO 19100 à mesure de leur publication, Cependant elle **s'avère insuffisante pour consommer tous** **les nouveaux types de données** utiles à la sécurité et à l'opération normale du trafic maritime rendus disponibles depuis sa conception.

Les principales limitations de la S-57 sont les suivantes:

* La S-57 a servi exclusivement (même si elle pouvait faire plus) pour l'encodage des ENC consommées par les ECDIS
* La S-57 n'est pas une norme qui s'est imposée en géomatique
* Sa maintenance étant peu flexible, la S-57 est donc difficilement évolutive
* De plus, on ne peut la faire évoluer vers la prise en compte d'un certain nombre de besoins: modèles numériques de terrain, données temporelles.
* le modèle de données est couplé au format, ce qui limite la facilité de certains usages (transfert).

### La norme S-100

La norme S-100 est le document de référence qui précise comment l’OHI utilise et étend la suite de normes géospatiales **ISO 19100 (information géographique et géomatique)** dans les applications hydrographiques, maritimes et connexes (environnement marin, météo, communications...).

## Atouts de la S-100

#### S-100 est interopérable

ISO 19100 n'est pas une norme mais une **série de normes** (environ 35), incluant les normes **ISO 19101** (modèle de référence), **ISO 19110** (définition des classe d'entité géographiques), **ISO 19113** (concepts), **ISO** **19114** (qualité, principes), **ISO** **19138** (qualité, évaluation), **ISO** **19131** (spécifications), **ISO 19115** (métadonnées des données et services), **ISO 19139** (métadonnées, encodage)...

D'autre part, l'OHI et l'Open Geospatial Consortium (OGC) travaillent en partenariat favorisant l'adoption des normes OGC par l'OHI et son implication dans la définition de nouvelles normes techniques ou l'évolution de normes existantes.

Pour un produit ou service géospatial, respecter les normes ISO 19100 et les normes de l'OGC le rend interopérable.

**La S-100 étend la portée de la norme S-57** pour l'échange des données hydrographiques et ouvre à l'utilisation d'autres types de données et services. Elle est aussi **totalement alignée sur l'ISO 19100**: Une donnée, un service ou un système S-100 est donc aussi ISO 19100. Elle peut donc aussi être utilisée pour d'autres données et services en rapport avec le domaine maritime hors hydrographie proprement dite.

#### S-100 et e-navigation

La S-100 permet la mise en oeuvre du concept de **e-navigation** développé par l'OMI.

L'e-navigation est définie par l'OMI comme étant la manipulation (collection, intégration, échange, (re)présentation et l'analyse harmonisés) de l'information maritime à bord et à terre par des moyens électroniques afin d'améliorer la navigation de quai à quai ainsi que les services associés dans un but de sûreté et de sécurité en mer, et de protection de l'environnement marin.

#### S-100 est extensible et évolutive

La S-100 se veut plus flexible que la S-57: **c'est modèle de données hydrographiques universel**. Elle favorise l'usage d'une plus grande variété de sources de données numériques, de produits, et d'utilisateurs en rapport avec l'hydrographie. Elle doit permettre le développement de nouveaux types d'applications qui sortent du champ traditionnel de l'hydrographie. Par exemple:

* bathymétrie haute densité
* classification des fonds marins
* Géomatique maritime
* ...

La S-100 a été conçue **extensible** et peut donc facilement intégrer de nouveaux domaines. Par exemple:

* 3D, séries temporelles et données 4D (x, y, z, t) alors que la S-57 se limite à la 2D
* services web pour la manipulation (collecter -accéder/acquérir/échanger, intégrer/transformer, analyser, (re)présenter)
* la S-100 est conçue pour être machine-readable (XML)v, contrairement à la S-57
* la représentation des données (portayal) et la cybersécurité sont inclus chaque spécification de produit (PS), ce qui n'est pas le cas de de la S-57 (il faut lui adjoindre la S-63 pour la protection des données et la S-52 pour leur représentation)

Elle est **évolutive**: elle permet un régime de maintenance plus flexible et dynamique *via* une base de registres dédiée en ligne.

Le mode de développement et de maintenance de la S-100 est conçu pour permettre les contributions hors OHI ouvrant l'usage des données hydrographiques à de nouveaux utilisateurs.

#### Où trouver la S-100 ?

Une **base de registres** en ligne de la S-100 conforme à la norme **ISO 19135** (Procédures pour l'enregistrement d'éléments d'Information géographique) a été établie pour l'enregistrer, gérer et maintenir des différents dictionnaires d'élément de la S-100. Elle se trouve ici: **<http://registry.iho.int>**. Elle contient les sous-registres suivants:

* Registre de dictionnaires des données
* Registre de présentation
* Registre des métadonnées
* Registre des codes de producteurs de données

#### S-100 ou S-1XX ?

Suivant les usages, voire les besoin d'organisations représentant ces usages, la S-100 se décline en plusieurs branches développées par l'OHI, que l'on désigne génériquement par le sigle S-1XX. Par exemple, La S-101 traite de l'hydrographie et suffit à elle seule à remplacer la S-57.

D'autres organisation ou groupes que l'OHI peuvent être amenés à proposer des normes spécialisant la S-100. Par exemple:

* les normes S-2XX développées par l'association internationale de la signalisation maritime (AISM - IALA, International Association of Marine Aids to Navigation and Lighthouse Authorities, Organisation Internationale pour les Aides à la Navigation Maritime),
* les S-3XX de la Commisson Océanographique intergouvernementale (IOC)
* les S-40X du groupe d'harmonisation pour la navigation intérieure
* les S-41X de l'Organisation Météorologique Mondiale (WMO),
* la S-421 de la Commission Electrotechnique Internationale (IEC).
* ou encore l'OTAN (S-5XX) pour ce qui est des couches et applications militaires.

#### Où trouver les S-100 ?

La liste est consultable ici: <https://iho.int/en/s-100-based-product-specifications>

D'autre part l'ensemble des documents en rapport avec ces normes sont disponibles via le registre de OHI:

* <https://registry.iho.int/productspec/list.do> pour les normes publiées
* <https://registry.iho.int/testbed/list.do> pour les normes en préparation

Indépendemment, j'ai effectué un recensement de la disponibilité des normes (publiées ou non, OHI et hors OHI) disponible ici: [https://cloud.shom.fr/apps/files/?dir=/SPPNaut/spécifications S-100&openfile=848064](https://cloud.shom.fr/apps/files/?dir=/SPPNaut/sp%C3%A9cifications%20S-100&openfile=848064)

les normes S-100 sont proposées de manière uniforme sous la forme d'un document principal (Product Specifications) et de plusieurs annexes, de la manière indiquée ici: [https://cloud.shom.fr/apps/files/?dir=/SPPNaut/spécifications S-100&openfile=872174](https://cloud.shom.fr/apps/files/?dir=/SPPNaut/sp%C3%A9cifications%20S-100&openfile=872174)

## Références

(-- à compléter)

##### OHI

registre OHI:

##### OMI

ECDIS – GUIDE DE BONNES PRATIQUES. [https://iho.int/uploads/user/About IHO/International_Organisations/ECDIS-ENC/French/MSC.1-Circ.1503-Rev.1 - Ecdis - Guide De Bonnes Pratiques.pdf](https://iho.int/uploads/user/About%20IHO/International_Organisations/ECDIS-ENC/French/MSC.1-Circ.1503-Rev.1%20-%20Ecdis%20-%20Guide%20De%20Bonnes%20Pratiques.pdf)

e-navigation. <https://www.imo.org/en/OurWork/Safety/Pages/eNavigation.aspx>

##### CIRM

[https://cirm.org/documents/position-papers/CIRM Position Paper - Transition to S-101 ENCs in ECDIS - October 2020.pdf](https://cirm.org/documents/position-papers/CIRM%20Position%20Paper%20-%20Transition%20to%20S-101%20ENCs%20in%20ECDIS%20-%20October%202020.pdf)

26 Jan, 2011

SOLAS: Mandatory Requirements for ECDIS and BNWAS. 26 Jan, 2011 <https://www.westpandi.com/publications/news/solas-mandatory-requirements-for-ecdis-and-bnwas/>