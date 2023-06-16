# SPPNaut Carting

SPPNaut est une startup d'Etat dont la mission est la modernisaton et l'ouverture des publications nautiques.

## Développement

L'application est basée sur :

-   [Django et GeoDjango](https://www.djangoproject.com) pour le backend
-   [DSFR](https://www.systeme-de-design.gouv.fr) pour les composants frontend
-   [Stimulus](https://stimulus.hotwired.dev) pour la dynamisation du frontend
-   [OpenLayers](https://openlayers.org) pour les cartes

### Pré-requis

-   Python >= 3.10
-   Node.js >= 18

La base de données est utilisée pour la modélisaton des normes s1xy et le fonctionnement de l'administration de Django.

### Installation

1. Installation des librairies nécessaire à GeoDjango

    Sur Debian/ubuntu :

    ```sh
    sudo apt-get install binutils libproj-dev gdal-bin
    ```

    Sur MacOS :

    ```sh
    brew install gdal
    ```

1. Création et activation de votre environnement virtuel. Par exemple via ces commandes :

    ```sh
    python -m venv .venv --prompt $(basename $(pwd))
    source .venv/bin/activate
    ```

1. Installation des dépendances

    ```sh
    pip install pip-tools
    pip-sync requirements.txt dev-requirements.txt
    ```

1. Création des variables d'environnement

    En développement :

    ```sh
    cp .env.template .env
    ```

    Dans les autres environnements, prenez exemple sur le fichier `.env.template` pour configurer vos variables d'environnement sur l'environnement d'execution

1. Implémenter le schéma de la base de données

    `./manage.py migrate`

    La base de données est composée des tables d'administration de django pour assurer l'authentification et des tables de modélisations de la norme s1xy

1. Installation des dépendances JavaScript

    `npm install`

1. Lancement des serveurs de développement

    `honcho start`

    L'interface est disponible sur votre navigateur à l'adresse [http://localhost:8000](http://localhost:8000)

### Ingestion du fichier document.xml d'un ouvrage en base de données

Exécuter,

```sh
./manage.py ingest_ouvrage_xml z99.xml
./manage.py import_some_geometry
```

### Lister les licenses

Processus à suivre en utilisant le package pip-licenses

```sh
rm -rf .venv
python -m venv .venv --prompt $(basename $(pwd))
source .venv/bin/activate
pip install -r requirements.txt -r dev-requirements.txt
pip install -U pip-licenses
pip-licenses > licenses.csv
```
