# XMI exploration

XMI récupéré sur : https://iho.int/en/nipwg-product-specifications

-   https://iho.int/uploads/user/Services%20and%20Standards/NIPWG/MISC/ProdSpecs/S-127/Model-S127_1_0_1_20191115.zip

---

Fichier exploré :

-   Model-S127_1_0_1_20191115/S127_1_0_1_20191115.xmi
-   À partir de la définition du fichier, logiciel utilisé : https://www.sparxsystems.fr/products/ea/
-   Sparx Systems Enterprise Architect propose un export d'un XMI en [DDL](https://en.wikipedia.org/wiki/Data_definition_language)

## Exportation en sql depuis Enterprise Architect

1.  import du fichier .xmi
1.  transformation en DDL https://stackoverflow.com/a/23685559
1.  configuration d'un DBMS (Postgres)
1.  génération d'un DDL https://sparxsystems.com/enterprise_architect_user_guide/15.2/model_domains/generateddl.html

---

## Traduction du fichier SQL en modèle django

1.  Nettoyage des doublons dans le fichier .sql (certaines tables sont créées plusieurs fois ce qui fait échouter l'import)
1.  Import du fichier SQL dans postgres
1.  Config django pour atteindre la db importée
1.  `./manage.py inspectdb`
1.  Remplacement `managed = False` par `managed = True`
1.  Remplacement `max_length=-1` par `max_length=255`

## Observations

### Relations

Certaines FK sont bien générées (ex `Pilotservice`).
Des liens sont manquants :

-   FK de `Pilotservice` > `Pilotagedistrict`

ManyToMany semblent absentes :

-   Ex : `Pilotboardingplace` > `Pilotservice`

### Types de champs

Les champs sont tous des `CharField`

-   Ex : `Pilotservice` > `remotepilot` devrait être un booléen
