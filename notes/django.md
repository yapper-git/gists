# Django

- [Tutoriel OC: Développez votre site web avec le framework Django](http://openclassrooms.com/courses/developpez-votre-site-web-avec-le-framework-django)
- [Official documentation](https://docs.djangoproject.com/en/1.7/)

- [Writing custom django-admin commands](https://docs.djangoproject.com/en/1.7/howto/custom-management-commands/)

## Présentation de Django

### Créez vos applications web avec Django
- Un framework (cadre de travail en français) est un ensemble d'outils qui simplifie le travail d'un développeur.
- Un framework est destiné à des développeurs, et non à des novices. Un framework nécessite un temps d'apprentissage avant de pouvoir être pleinement utilisé.
- Django est un framework web pour le langage Python très populaire, très utilisé par les entreprises dans le monde : Mozilla, Instagram ou encore la NASA l'ont adopté !
- Ce cours traite de la version 1.7, sortie en septembre 2014. Nous ne garantissons pas que les exemples donnés soient compatibles avec des versions antérieures et postérieures.

###  Le fonctionnement de Django
- Django gère de façon autonome la réception des requêtes et l'envoi des réponses au client (partie contrôleur) ;
- Un projet est divisé en plusieurs applications, ayant chacune un ensemble de vues, de modèles et de schémas d'URL ;
- Si elles sont bien conçues, ces applications sont réutilisables dans d'autres projets, puisque chaque application est indépendante.

```shell
apt-get install python-pip
pip install Django==1.7
pip install Django --upgrade
```

```python
import django
django.get_version()
```

### Gestion d'un projet
- L'administration de projet s'effectue via le script `manage.py`. Tout particulièrement, la création d'un projet se fait via la commande `django-admin.py startproject mon_projet` ;
- À la création du projet, Django déploie un ensemble de fichiers, facilitant à la fois la structuration du projet et sa configuration ;
- Pour tester notre projet, il est possible de lancer un serveur de test, via la commande `python manage.py runserver`, dans le dossier de notre projet. Ce serveur de test ne doit pas être utilisé en production ;
- Il est nécessaire de modifier le `settings.py`, afin de configurer le projet selon nos besoins. Ce fichier ne doit pas être partagé avec les autres membres ou la production, puisqu'il contient des données dépendant de votre installation, comme la connexion à la base de données.

###  Les bases de données et Django
- Une base de données permet de stocker vos données de façon organisée et de les récupérer en envoyant des requêtes à votre système de gestion de base de données ;
- De manière générale, nous communiquons la plupart du temps avec les bases de données via le langage SQL ;
- Il existe plusieurs systèmes de gestion de bases de données, ayant chacun ses particularités ;
- Pour faire face à ces différences, Django intègre une couche d'abstraction, afin de communiquer de façon uniforme et plus intuitive avec tous les systèmes : il s'agit de l'ORM que nous avons présenté brièvement ;
- Une ligne dans une table peut être liée à une autre ligne d'une autre table via le principe de clés étrangères : nous gardons l'identifiant de la ligne de la seconde table dans une colonne de la ligne de la première table.

## Premiers pas

### Les vues
- Le minimum requis pour obtenir une page web avec Django est une vue, associée à une URL.
- Une vue est une fonction placée dans le fichier `views.py` d'une application. Cette fonction doit toujours renvoyer un objet `HttpResponse`.
- Pour être accessible, une vue doit être liée à une ou plusieurs URL dans les fichiers `urls.py` du projet.
- Les URL sont désignées par des expressions régulières, permettant la gestion d'arguments qui peuvent être passés à la vue pour rendre l'affichage différent selon l'URL visitée.
- Il est conseillé de diviser le `urls.py` du projet en plusieurs fichiers, en créant un fichier `urls.py` par application.
- Il existe des réponses plus spéciales permettant d'envoyer au navigateur du client les codes d'erreur 404 (page non trouvée) et 403 (accès refusé), ou encore d'effectuer des redirections.

### Les templates
- En pratique, et pour respecter l'architecture dictée par le framework Django, toute vue doit retourner un objet `HttpResponse` construit via un template.
- Pour respecter cette règle, il existe des fonctions nous facilitant le travail, comme `render`, présentée tout au long de ce chapitre. Elle permet de construire la réponse HTML en fonction d'un fichier template et de variables.
- Les templates permettent également de faire plusieurs traitements, comme afficher une variable, la transformer, faire des conditions... Attention cependant, ces traitements ont pour unique but d'afficher les données, pas de les modifier.
- Il est possible de factoriser des blocs HTML (comme le début et la fin d'une page) via l'utilisation des tags `{% block %}` et `{% extends %}`.
- Afin de faciliter le développement, Django possède un tag `{% url %}` permettant la construction d'URL en lui fournissant la vue à appeler et ses éventuels paramètres.
- L'ajout de fichiers statiques dans notre template (images, CSS, JavaScript) peut se faire via l'utilisation du tag `{% static %}`.

### Les modèles
- Un modèle représente une table dans la base de données et ses attributs correspondent aux champs de la table.
- Tout modèle Django hérite de la classe mère `Model` incluse dans `django.db.models`.
- Chaque attribut du modèle est typé et décrit le contenu du champ, en fonction de la classe utilisée : `CharField,` `DateTimeField`, `IntegerField`…
- Les requêtes à la base de données sur le modèle Article peuvent être effectuées via des appels de méthodes sur `Article.objects`, tels que `all()`, `filter(nom="Un nom")` ou encore `order_by('date')`.
- L'enregistrement et la mise à jour d'articles dans la base de données se fait par la manipulation d'objets de la classe `Article`, et via l'appel à la méthode `save()`.
- Deux modèles peuvent être liés ensemble par le principe des clés étrangères. La relation dépend cependant des contraintes de multiplicité qu'il faut respecter : `OneToOneField`, `ManyToManyField`.
- Il est possible d'afficher les attributs d'un objet dans un template de la même façon qu'en Python via des appels du type `article.nom`. Il est également possible d'itérer une liste d'objets, pour afficher une liste d'articles par exemple.

### L'administration
- L'administration est un outil optionnel : il est possible de ne pas l'utiliser. Une fois activée, de très nombreuses options sont automatisées, sans qu'il y ait besoin d'ajouter une seule ligne de code !
- Ce module requiert l'usage de l'authentification, et la création d'un super-utilisateur afin d'en restreindre l'accès aux personnes de confiance.
- De base, l'administration permet la gestion complète des utilisateurs, de groupes et des droits de chacun, de façon très fine.
- L'administration d'un modèle créé dans une de nos applications est possible en l'enregistrant dans le module d'administration, via `admin.site.register(MonModele)` dans le fichier `admin.py` de l'application.
- Il est également possible de personnaliser cette interface pour chaque module, en précisant ce qu'il faut afficher dans les tableaux de listes, ce qui peut être édité, etc.

### Les formulaires
- Un formulaire est décrit par une classe, héritant de `django.forms.Form`, où chaque attribut est un champ du formulaire défini par le type des données attendues.
- Chaque classe de `django.forms` permet d'affiner les données attendues : taille maximale du contenu du champ, champ obligatoire ou optionnel, valeur par défaut…
- Il est possible de récupérer un objet `Form` après la validation du formulaire et de vérifier si les données envoyées sont valides, via `form.is_valid()`.
- La validation est personnalisable, grâce à la réécriture des méthodes `clean_NOM_DU_CHAMP()` et `clean()`.
- Pour moins de redondances, la création de formulaires à partir de modèles existant se fait en héritant de la classe `ModelForm`, à partir de laquelle nous pouvons modifier les champs éditables et leurs comportements.

### La gestion de fichiers
TODO

## En vrac

stackoverflow.com/questions/2260727/accessing-local-django-webserver-from-outside-world
```bash
python manage.py runserver 0.0.0.0:8000
```
