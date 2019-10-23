# Django

> The Web framework for perfectionists with deadlines
>
> Le framework web pour perfectionnistes déchaînés

- Tutoriels OC :
  + [Développez votre site web avec le framework Django](http://openclassrooms.com/courses/developpez-votre-site-web-avec-le-framework-django)
  + [Découvrez le framework Django](https://openclassrooms.com/fr/courses/4425076-decouvrez-le-framework-django)
  + [Déployez une application Django](https://openclassrooms.com/fr/courses/4425101-deployez-une-application-django)
- [Official documentation (en)](https://docs.djangoproject.com/en/stable/)
- [Documentation officielle (fr)](https://docs.djangoproject.com/fr/stable/)

---

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

### Les bases de données et Django
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

### La gestion des fichiers
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
- La classe Q permet d'effectuer des requêtes complexes avec les opérateurs « OU », « ET » et « NOT ». Avg, Max et Min permettent d'obtenir respectivement la moyenne, le maximum et le minimum d'une certaine colonne dans une table. Elles peuvent être combinées avec Count pour déterminer le nombre de lignes retournées.
- L'héritage de modèles permet de factoriser des modèles ayant des liens entre eux. Il existe plusieurs types d'héritage : abstrait, classique et les modèles proxy.
- L'application ContentType permet de décrire un modèle et de faire des relations génériques avec vos autres modèles (pensez à l'exemple des commentaires !).

### Simplifions nos templates : filtres, tags et contextes
- Django permet aux développeurs d'étendre les possibilités des templates en créant des filtres et des tags.
- Les filtres et tags créés sont organisés par modules. Pour utiliser un filtre ou un tag il faut charger son module via `{% load nom_module %}`.
- Les filtres sont de simples fonctions, prenant en entrée 1 ou 2 arguments et renvoyant toujours une chaîne de caractères.
- Le contexte des templates est l'ensemble des variables disponibles et utilisables dans un template. Ce contexte est rempli par toutes les fonctions citées dans `TEMPLATE_CONTEXT_PROCESSORS`, puis par la vue appelée et enfin par les éventuels tags du template.
- Les tags permettent des traitements plus complexes sur les données à afficher. Les tags peuvent avoir une « mémoire », plusieurs arguments, former des blocs…

### Les signaux et middlewares
- Un signal est une notification envoyée par une application à Django lorsqu'une action se déroule, et renvoyée par le framework à toutes les autres parties d'applications qui se sont enregistrées pour savoir quand ce type d'action se déroule, et comment.
- Les signaux permettent d'effectuer des actions à chaque fois qu'un événement précis survient.
- Les middlewares sont des classes instanciées à chaque requête, exception, ou encore génération de template, dans l'ordre donné par `MIDDLEWARE`.
- Ils permettent d'effectuer une tâche précise à chaque appel.


## Des outils supplémentaires

### Les utilisateurs
- Django propose une base de modèles qui permettent de décrire les utilisateurs et groupes d'utilisateurs au sein du projet. Ces modèles possèdent l'ensemble des fonctions nécessaires pour une gestion détaillée des objets : `set_password`, `check_password`, `authenticate`, `login`…
- Il est possible d'étendre le modèle d'utilisateur de base, pour ajouter ses propres champs.
- Le framework dispose également de vues génériques pour la création d'utilisateurs, la connexion, l'inscription, la déconnexion, le changement de mot de passe… En cas de besoin plus spécifique, il peut être nécessaire de les réécrire soi-même.
- Il est possible de restreindre l'accès à une vue aux personnes connectées via `@login_required` ou à un groupe encore plus précis via les permissions et `@permission_required`.

### Les messages
- Les messages permettent d'afficher des notifications à l'utilisateur, en cas de succès ou d'échec lors d'une action, ou si un événement particulier se produit.
- Il existe différents types de messages : ceux d'information, de succès, d'erreur, d'avertissement, et enfin de débogage.
- Il est possible de créer son propre type de message et de configurer son comportement.
- L'affichage de messages peut être limité : chaque type de message est caractérisé par une constante entière, et nous pouvons afficher les messages ayant un niveau supérieur ou égal à un certain seuil, via `messages.set_level`.

### La mise en cache
- Le cache permet de sauvegarder le résultat de calculs ou traitements relativement longs, afin de présenter le résultat sauvegardé pour les prochaines visites, plutôt que de recalculer la même donnée à chaque fois.
- Il existe plusieurs systèmes de mise en cache : par fichier, en base de données, dans la mémoire RAM (ou avec le logiciel Memcached).
- La mise en cache peut être définie au niveau de la vue, via `@cache_page`, dans le fichier `urls.py`, ou encore dans les templates avec le tag `{% cache %}`.
- Django fournit également un ensemble de fonctions permettant d'appliquer une mise en cache à tout ce que nous souhaitons, et d'en gérer précisément l'expiration de la validité.

### La pagination
- La classe `django.core.paginator.Paginator` permet de générer la pagination de plusieurs types de listes d'objets et s'instancie avec au minimum une liste et le nombre d'éléments à afficher par page.
- Les attributs et méthodes clés de `Paginator` à retenir sont `p.num_pages` et `p.page()`. La classe `Page` a notamment les méthodes `has_next()`, `has_previous()` et est itérable afin de récupérer les objets de la page courante.
- Il est possible de rendre la pagination plus pratique en prenant en compte l'argument `orphans` de `Paginator`.
- Pensez à uniformiser vos paginations en terme d'affichage au sein de votre site web, pour ne pas perturber vos visiteurs.

### L'internationalisation
- Le processus de traduction se divise en deux parties :
  + L'internationalisation, où nous indiquons ce qui est à traduire ;
  + La localisation, où nous effectuons la traduction et l'adaptation à la culture.
- Ce processus se base essentiellement sur l'utilisation de l'outil gettext, permettant la génération de fichiers de traduction utilisables par des novices en développement.
- Django permet également d'adapter l'affichage des dates et des nombres à la langue, en même temps que leur traduction.
- Grâce aux sessions et aux middlewares, le framework peut deviner la langue de l'utilisateur automatiquement, en fonction de son navigateur ou de ses précédentes visites.

### Les tests unitaires
- Les tests unitaires permettent de s'assurer que vous n'avez introduit aucune erreur lors de votre développement, et assurent la robustesse de votre application au fil du temps.
- Les tests sont présentés comme une suite de fonctions à exécuter, testant plusieurs assertions. En cas d'échec d'une seule assertion, il est nécessaire de vérifier son code (ou le code du test), qui renvoie un comportement anormal.
- Les tests sont réalisés sur une base de données différente de celles de développement ; il n'y a donc aucun souci de corruption de données lors de leur lancement.
- Il est possible de tester le bon fonctionnement des modèles, mais aussi des vues. Ainsi, nous pouvons vérifier si une vue déclenche bien une redirection, une erreur, ou si l'enregistrement d'un objet a bien lieu.

### Ouverture vers de nouveaux horizons : django.contrib
- Django est un framework très puissant, il propose de nombreux modules complémentaires et optionnels pour simplifier le développement.
- Ce cours a traité de quelques-uns de ces modules, mais il est impossible de les présenter tous : la documentation présente de façon complète chacun d'entre eux.
- Il existe des centaines de modules non officiels permettant de compléter votre installation et d'intégrer de nouvelles fonctionnalités.
- Nous avons présenté ici `humanize`, qui rend vos données plus naturelles dans vos templates, et `flatpages` qui permet de gérer vos pages statiques via l'administration.
- Liste de modules : admin, auth, contenttypes, flatpages, formtools, gis, humanize, messages, redirects, sessions, sitemaps, sites, staticfiles, syndication, webdesign


## Annexes

### Déployer votre application en production
- Il ne faut pas utiliser le serveur `python manage.py runserver`  en production ;
- Une des méthodes d'installation possible passe par Apache2 avec le `mod_wsgi`, en exécutant le script `wsgi.py` contenu dans le répertoire du projet ;
- Il existe également le combo nginx + gunicorn, que l'on a également décrit (ou mieux nginx + uwsgi) ;
- Si l'on désactive le mode `DEBUG`, Django enverra un e-mail à toutes les personnes listées dans le tuple `ADMINS` en cas d'erreur 500 sur le site. Il est possible d'être averti en cas d'erreurs 404, et de filtrer les données sensibles envoyées (telles que les mots de passe) ;
- Sentry est un projet Django permettant de surveiller votre propre projet de manière plus fine ;
- Le site [djangofriendly.com](http://djangofriendly.com) donne une liste d'hébergeurs supportant Django.

### L'utilitaire manage.py
- Les commandes de base : `runserver`, `shell`, `version`, `help`, `startproject` (depuis `django-admin.py`), `startapp`, `diffsettings`, `check`, `test`, `testserver`
- La gestion de la base de données : `migrate` (zero), `makemigrations`, `dbshell`, `dumpdata`, `loaddata`, `inspectdb` (fonction inverse de `makemigrations` et `migrate`), `showmigrations`
- Les commandes d'application :  `clearsessions`, `changepassword`, `createsuperuser`, `makemessages`, `compilemessages`,`createcachetable`

---

## Medley (Trouvailles en vrac)

- **uwsgi** a de meilleures performances que **gunicorn** d'après des benchmark d'internet
- Dans nginx, `alias` et `root` fonctionnent différemment (cf [stackoverflow.com](https://stackoverflow.com/questions/10631933/nginx-static-file-serving-confusion-with-root-alias)) : partie restante ou requête totale

```
location = /favicon.ico  {
    root /path/to/app;
    # or : alias  /path/to/app/favicon.ico;
}
```

- Sentry
- `python manage.py runserver 0.0.0.0:8000`
- [Syndication = flux RSS/Atom](https://docs.djangoproject.com/fr/2.2/ref/contrib/syndication/)
- [Writing custom django-admin commands](https://docs.djangoproject.com/en/stable/howto/custom-management-commands/)
- http://djangosnippets.org/
- https://www.djangopackages.com/
- Pypi est l'index des paquets Python de référence (gère les dépendances)
- `(?P<slug>[-_\w]+)`


## Extraits de code

### Installer django

```shell
apt-get install python-pip
pip install Django==2.2.6
pip install Django --upgrade
```

### Obtenir le numéro de version

```shell
python -m django --version
```

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
- truncatewords
- pluralize
- default
- add
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
{% load static %}<img src="{% static "my_app/myexample.jpg" %}" alt="My image"/>
```

## Modèles

```python
from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField("Date de parution", auto_now_add=True, auto_now=False)

    def __str__(self):  # pour l'administration
        return self.titre
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

https://docs.djangoproject.com/en/1.8/topics/db/examples/

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

#### OneToOne

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

---

## Notes du cours "Découvrez le framework Django"

- Installer `psycopg2` pour utiliser une base PostgreSQL
- L'ordre des `MIDDLEWARE` est important, cf [middleware-ordering](https://docs.djangoproject.com/en/2.2/ref/middleware/#middleware-ordering)
- Architecture MVT (inspiré de MVC) : Modèle / Vue / Template
- [Tutoriel sur les requêtes HTTP](https://openclassrooms.com/fr/courses/4087036-construisez-une-api-rest-avec-symfony/4280556-une-architecture-pas-un-protocole#r-4280629)
- L'outil [SQL Designer](https://ondras.zarovi.cz/sql/demo/) permet de réaliser un diagramme SQL
- [Tutoriel sur les clés étrangères et primaires](https://openclassrooms.com/courses/faites-une-base-de-donnees-avec-uml/apprehendez-les-objets-et-le-modele-relationnel)
- Relations :
  + un à un : `models.OneToOneField`
  + plusieurs à un : `models.ForeignKey`
  + plusieurs à plusieurs : `models.ManyToManyField` (`related_name`)
- `MyModel.objects.create()` vs `MyModel.save()`
- `object_list.exisdansts()` renvoie `True` si résultats trouvés dans la queryset donnée

> albums étant un objet QuerySet, vous vous dites certainement "gardons la méthode len" pour vérifier qu'il n'y a pas de résultat. Holà, manant ! Cela générerait une seconde requête SQL tout à fait inutile puisque vous avez déjà les résultats. Utilisez plutôt la méthode exists() :

- "Queries are lazy" (ou "les requêtes sont paresseuses")
Les QuerySets sont différés (« lazy ») ; la création d’un QuerySet ne génère aucune activité au niveau de la base de données. Vous pouvez empiler les filtres toute la journée, Django ne lance aucune requête tant que le QuerySet n’est pas évalué.
https://docs.djangoproject.com/fr/1.11/topics/db/queries/#querysets-are-lazy
- Administration :
  + `TabularInline` permet de définir comment afficher les champs liés (à préciser dans `inlines`) pour les 3 types de relation.
  + `readonly_fields` + `has_add_permission`
- On peut créer des liens dans l'admin dans `readonly_fields`, `fieldsets` ou `list_display`.
- Déployer sur le cloud avec Heroku (Paas, simplifie la configuration du serveur de production) :
  + Configurer les settings, par exemple : `SECRET_KEY = os.environ.get('SECRET_KEY', 'clededev')`, `DEBUG`, `ALLOWED_HOSTS`
  + Utiliser `whitenoise` pour servir les fichiers statiques
  + Utiliser `dj-database-url` pour récupérer sur le serveur Heroku les informations sur la base de données qu'il a automatiquement créé.
  + Créer `Procfile` pour préciser la commande à lancer sur le serveur
  + Préciser les dépendances à installer dans `requirements.txt`
  + Utiliser un dépôt git pour envoyer le code
  + Installer Heroku CLI et lancer `heroku login`, `create`, `config:set`, `run`...
  + Exporter via `dumpdata` et importer avec `loaddata`
- Recommande le livre *Two Scoops of Django* et le tutoriel officiel de Django
- `forms.TextInput(attrs={'class': 'form-control'}`
- LOGOUT REDIRECT, ALLOWED_HOSTS, ADMINSFILE_UPLOAD_PERMISSIONSINTERNAL_IPS

LOGIN_REDIRECT_URL =  # si pas next précisé
LOGIN_URL =
LOGOUT_REDIRECT_URL

- Transactions (important pour ne pas corrompre la bdd) :
  + activer pour toutes les vues : DATABASES = {
    'default': {
      # ...
      'ATOMIC_REQUESTS': True,
    }
}
puis @transaction.non_atomic_requests
Mais peut affecter les performances
  + activer au cas par cas : avec le décorateur `@transaction.atomic` ou avec `with transaction.atomic():`

- TDD = Test-Driven Development = développement piloté par les tests (en 3 phases : red, green, refactor)

Notes du cours ...

- Types de cloud :
  + SAAS (Software As A Service) : Google Drive, DropBox
  + PAAS (Platform As a Service) : Heroku, Clever cloud
  + IAAS (Infrastructure As A Service) : Amazon webservices, openstack

  En vérité, il existe plusieurs types de Cloud différents, selon la latitude de configuration que vous souhaitez :

  SAAS (Software as a Service) : une plateforme web avec laquelle vous interagissez via un site web. Vous n'avez aucun moyen de connaître l'état des serveurs. Exemples : Google Drive, One Drive, Dropbox...

  PAAS (Plateform as a Service) : une plateforme web à qui vous confiez votre code et qui configure les serveurs pour vous de manière automatique. Vous avez plus ou moins de maîtrise sur les serveurs. Exemple : Heroku, Clever Cloud.

  IAAS (Infrastructure as a Service) : une entreprise qui s'occupe de l'infrastructure pour vous. Vous avez loué un espace sur un serveur et vous y installez ce que vous souhaitez. Rien n'est fait pour vous, sauf si vous le souhaitez. Exemples : Amazon Web Services, Openstack...

Pour utiliser le serveur de dev avec nginx :
```
location / {
    proxy_set_header Host $http_host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_redirect off;
    proxy_pass http://127.0.0.1:8000;
}
```
