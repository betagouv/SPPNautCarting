# SPPNaut

SPPNaut est une startup d'Etat dont la mission est la modernisaton et l'ouverture des publications nautiques.


## Dévéloppement

### Prerequis

Pour faire tourner l'interface en local, il est conseiller d'utiliser :
* un environnement virtuel pour faire tourner python >= 3.10
* pipenv (voir pour passer à piplock ?)
* docker et docker-compose pour faire tourner la base de données Postgresql

### Installation

Installation des dépendances :

`pipenv install`

Lancement de la base de données

`docker-compose -f docker-compose.db.yml up -d`

Migration

`pipenv run python manage.py migrate`

lancement de django

`pipenv run python manage.py runserver 0.0.0.0:8000`

L'interface est disponible sur votre navigateur à l'adresse [http://localhost:8000](http://localhost:8000)
