# Django

- [Tutoriel OC: Développez votre site web avec le framework Django](http://openclassrooms.com/courses/developpez-votre-site-web-avec-le-framework-django)
- [Official documentation](https://docs.djangoproject.com/en/stable/)

## Présentation de Django

### Créez vos applications web avec Django
- Un framework (cadre de travail en français) est un ensemble d'outils qui simplifie le travail d'un développeur.
- Un framework est destiné à des développeurs, et non à des novices. Un framework nécessite un temps d'apprentissage avant de pouvoir être pleinement utilisé.
- Django est un framework web pour le langage Python très populaire, très utilisé par les entreprises dans le monde : Mozilla, Instagram ou encore la NASA l'ont adopté !
- Ce cours traite de la version 1.7, sortie en septembre 2014. Nous ne garantissons pas que les exemples donnés soient compatibles avec des versions antérieures et postérieures.

###  Le fonctionnement de Django
- Django respecte l'architecture MVT, directement inspirée du très populaire modèle MVC ;
- Django gère de façon autonome la réception des requêtes et l'envoi des réponses au client (partie contrôleur) ;
- Un projet est divisé en plusieurs applications, ayant chacune un ensemble de vues, de modèles et de schémas d'URL ;
- Si elles sont bien conçues, ces applications sont réutilisables dans d'autres projets, puisque chaque application est indépendante.

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
- L'installation de la bibliothèque Pillow est nécessaire pour gérer les images dans Django. Cette bibliothèque permet de faire des traitements sur les images (vérification et redimensionnement notamment).
- Le stockage d'une image dans un objet en base se fait via un champ `models.ImageField`. Le stockage d'un fichier quelconque est similaire, avec `models.FileField`.
- Les fichiers uploadés seront stockés dans le répertoire fourni par `MEDIA_ROOT` dans votre `settings.py`.

## Techniques avancées

### Les vues génériques
- Django fournit un ensemble de classes permettant d'éviter de réécrire plusieurs fois le même type de vue (affichage d'un template statique, liste d'objets, création d'objets…) ;
- Les vues génériques peuvent être déclarées directement au sein de `urls.py` (cas le plus pratique pour les `TemplateView`) ou dans `views.py` ;
- Chaque vue générique dispose d'un ensemble d'attributs permettant de définir ce que doit faire la vue : modèle concerné, template à afficher, gestion de la pagination, filtres… ;
- Il est possible d'automatiser les formulaires d'ajout, de mise à jour et de suppression d'objets via des vues génériques ;
- Le module `django.views.generic` regorge de classes (plusieurs dizaines en tout), n'hésitez pas à regarder si l'une d'entre elles fait ce que vous souhaitez avant de vous lancer.

Ressources :
- [Documentation officielle](https://docs.djangoproject.com/en/stable/ref/class-based-views/)
- [ccbv.co.uk](http://ccbv.co.uk/)

### Techniques avancées dans les modèles
TODO

### Simplifions nos templates : filtres, tags et contextes
TODO

### Les signaux et middlewares
TODO

## Des outils supplémentaires

### Les utilisateurs
TODO

### Les messages
TODO

### La mise en cache
TODO

### La pagination
TODO

### L'internationalisation
TODO

### Les tests unitaires
TODO

### Ouverture vers de nouveaux horizons : django.contrib
TODO


## Extraits de code

### Installer django

```shell
apt-get install python-pip
pip install Django==1.8
pip install Django --upgrade
```

## Obtenir le numéro de version

```shell
python -c "import django; print(django.get_version())"
```

```python
import django
django.get_version()
```

## Vues

```python
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render

def hello_world(request):
    message = request.GET['msg'] if 'msg' in request.GET else 'Hello world!'
    return HttpResponse(message)

def error404(request):
    raise Http404("Road not found") # or raise Http404

def redirect(request):
    return redirect("https://www.djangoproject.com")
    # or return redirect(hello_world, permanent=True)
    # or return redirect('myapp:url_name', id_article=42)
    # or return redirect('myapp.views.myview', id_article=42)

def date_actuelle(request):
    return render(request, 'myapp/date.html', {'date': datetime.now()})
    # locals()
```

## Templates

Filtres :
- truncatewords: `{{ texte|truncatewords:80 }}`
- pluralize: `Vous avez message{{ nb_messages|pluralize }}`,
  `Il y a {{ nb_chevaux }} chev{{ nb_chevaux|pluralize:"al,aux" }}`
- default: `Bienvenue {{ pseudo|default:"visiteur" }}`
- add: `{{ nombre1 }} + {{ nombre2 }} = {{ nombre1|add:nombre2 }}`
- linebreaks
- safe
- length
- …

```
{% extends "base.html" %}
{% block title %} … {% endblock %}
{% if condition %} … {% elif condition %} … {% else %} … {% endif %}
{% for object in object_list %} … {% empty %} … {% endfor%}
{% url "myapp.views.myview" 42 %}
{% comment %} … {% endcomment %}
{% load staticfiles %}<img src="{% static "my_app/myexample.jpg" %}" alt="My image"/>
```

## Modèles

```
from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField("Date de parution", auto_now_add=True, auto_now=False)

    def __str__(self):  # pour l'administration
        return self.titre
```

```shell
python manage.py shell
```

```python
article = Article(author='Me', title='My Article')
article.full_clean() # raise django.core.exceptions.ValidationError
article.save() # raise django.db.utils.IntegrityError…
# or article.create()
article.delete()

# QuerySet : all, filter, exclude, order_by, reverse, count, distinct…
Articles.objects.all()
Articles.objects.filter(
    author='dupond',
    title__contains/startswith='keyword'
    date__lte=datetime.now()) # or .exclude()
Articles.objects.order_by('field1', '-field2')
Articles.objects.update(author='Anonymous')

Article.objects.get(author='dupont') # idem filter/exclude # raise MultipleObjectsReturned
Article.objects.get_or_create(author='dupont', )
```

## Vues génériques

```python
# blog/views.py
from django.views.generic import TemplateView

class FAQView(TemplateView):
   template_name = "blog/faq.html"

# blog/urls.py
from django.conf.urls import url
from blog.views import FAQView

urlpatterns = [
   url(r'^faq$', FAQView.as_view()),
]
```

```python
# blog/urls.py
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
   url(r'^faq', TemplateView.as_view(template_name='blog/faq.html')),
]
```

### Relations

[https://docs.djangoproject.com/en/1.8/topics/db/examples/]

- [Many-to-One relationships](https://docs.djangoproject.com/en/1.8/topics/db/examples/many_to_one/)
- [Many-to-many relationships](https://docs.djangoproject.com/en/1.8/topics/db/examples/many_to_many/)
#### OneToMany

```
class Category(models.Model):
    pass

class Article(models.Model):
     category = models.ForeignKey('Category')

article.category
category.article_set.all()
Articles.objects.filter(category__name__contains='and')
```

### OneToOne

```
class Engine(models.Model):
    pass

class Vehicle(models.Model):
     engine = models.OneToOneField(Engine)

# create engine first, then create vehicule
vehicle.engine
engine.vehicle # if available
vehicle.objects.get(engine__name="V8")
```



## Secret key

```python
import os

"""
Two things are wrong with Django's default `SECRET_KEY` system:

1. It is not random but pseudo-random
2. It saves and displays the SECRET_KEY in `settings.py`

This snippet gets an environment variable `DJANGO_SECRET_KEY`

The result is a random and safely hidden `SECRET_KEY`.
"""

try:
    SECRET_KEY
except NameError:
    SECRET_FILE = os.path.join(PROJECT_DIR, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
```

```
SECRET_KEY = ''.join([random.SystemRandom().choice("{}{}{}".format(string.ascii_letters, string.digits, string.punctuation)) for i in range(50)])
```

## En vrac

```bash
python manage.py runserver 0.0.0.0:8000
```

- [Writing custom django-admin commands](https://docs.djangoproject.com/en/stable/howto/custom-management-commands/)
- http://djangosnippets.org/
- https://www.djangopackages.com/

Pypi est l'index des paquets Python de référence (gère les dépendances)

```bash
django-admin.py startproject crepes_bretonnes

python manage.py migrate
python manage.py runserver [port]
python manage.py runserver 0.0.0.0:8000
python manage.py help
python manage.py startapp blog
```

Syndication: https://docs.djangoproject.com/fr/1.8/ref/contrib/syndication/

(?P<slug>[-_\w]+)
