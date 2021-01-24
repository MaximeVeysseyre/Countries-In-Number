# Countries-In-Number

Reprenez votre brief "Les pays en chiffre" pour recréer une base de données Mongo et déporter la logique (procédure et fonction) dans une API construite en Flask.


## **Description**

Projet individuel "Les pays en chiffres".

Création d'une base de données Mongo DB

Utilisation de Mongo Compass pour la visualisation des données.

Utilisation de Flask afin de requêter sur notre base de données.

Récolte d'informations basiques sur les pays ainsi que manipulation des données.


## **Installation**

Exécution du fichier main.py
Se rendre à l'adresse "http://localhost:8080/" dans votre navigateur internet.


### Requête 1

Création d'une fonction qui retourne le pays qui correspond au critère passé en paramètre. Ce paramètre est le nom du pays.

Adresse : "http://localhost:8080//api/request_country/"

Exemple : "http://localhost:8080//api/request_country/France"


### Requête 2

Création d'une fonction qui insert un nouveau pays avec des données aléatoires (On précise uniquement le pays).

Adresse : "http://localhost:8080///api/add_fake/"

Exemple : "http://localhost:8080///api/add_fake/MarioWorld"


### Requête 3

Réalisation d'une fonction pour retourner les pays qui sont regroupés par 4 tranches de densité de population.

Adresse : "http://localhost:8080///api/request_density/slice"


## **Auteur**

VEYSSEYRE Maxime