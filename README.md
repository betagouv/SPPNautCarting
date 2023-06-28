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

 Ces instructions sont utiles pour travailler sur le développement du projet.  
Si vous chercher les instructions de déploiement, elles se trouvent [plus bas ⏬](#déploiement)

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

### Mise à jour de Django

Plusieurs fichiers sont dupliqués depuis le code source de Django pour en modifier le fonctionnement.  
Une montée de version de ce dernier peut entraîner des régressions.  
Il est important de vérifier à chaque mise à jour que les fichiers supplantés par ce projet ne sont pas modifiés également dans Django. Dans ce cas, il faut mettre à jour les templates ci-dessous :

-   `templates/admin/change_form_with_ordered_formset_test.html` with [fieldset.html](https://github.com/django/django/blob/stable/4.2.x/django/contrib/admin/templates/admin/includes/fieldset.html)
-   `static/to_compile/entrypoints/admin-map-widget.ts` with [django/contrib/gis/static/gis/js/OLMapWidget.js](https://github.com/django/django/blob/main/django/contrib/gis/static/gis/js/OLMapWidget.js)

## Déploiement

En production, il faut également disposer de Python et Node.js.

### Compilation des assets statiques

Le projet repose sur une phase de compilation des assets statiques (CSS, JavaScript).

```sh
# Depuis la racine du dépôt
# Installation des dépendances
npm ci

# Compilation
npm run build
```

Ces fichiers statiques devront être compilés sur le serveur de production.  
Ils seront ensuite collectés via la [commande `collectstatic`](https://docs.djangoproject.com/fr/4.2/howto/static-files/deployment/) qu'il est nécessaire de lancer avant le démarrage du serveur web (voir ci-dessous).

### Django

Le projet repose sur Django, framework web dont le déploiement sur un serveur de production est richement documentée dans la [documentation officielle du projet](https://docs.djangoproject.com/fr/4.2/howto/deployment/wsgi/).

Il est possible de s'inspirer du [Dockerfile](./Dockerfile) pour connaître les instructions de déploiement spécifiques à Carting.
