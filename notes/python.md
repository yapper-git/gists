Liens:

* [Tutoriel OC : Apprenez à programmer en Python](http://fr.openclassrooms.com/informatique/cours/apprenez-a-programmer-en-python)
* [Documentation officielle](https://docs.python.org/3/)
* [Erreurs courantes en Python (forum OC)](fr.openclassrooms.com/forum/sujet/les-erreurs-courantes-en-python-45319)

TO READ:

* [PEP8 - Style Guide for Python Code](http://legacy.python.org/dev/peps/pep-0008/)
* docstring (sphinx?)
* [PEP 328](http://legacy.python.org/dev/peps/pep-0328/#guido-s-decision) : import, conflits
* Se documenter sur **pip** (vs composer en PHP?)
* Se documenter sur les frameworks web : Flash et Django


# Introduction à Python

## Qu'est-ce que Python ?

- Python est un langage de programmation interprété, à ne pas confondre avec un langage compilé.
- Il permet de créer toutes sortes de programmes, comme des jeux, des logiciels, des progiciels, etc.
- Il est possible d'associer des **bibliothèques** à Python afin d'étendre ses possibilités.
- Il est portable, c'est à dire qu'il peut fonctionner sous différents systèmes d'exploitation (Windows, Linux, Mac OS X,…).

## Premiers pas avec l'interpréteur de commandes Python

- L'interpréteur de commandes Python permet de tester du code au fur et à mesure qu'on l'écrit.
- L'interpréteur Python accepte des nombres et est capable d'effectuer des calculs.
- Un nombre décimal s'écrit avec un point et non une virgule.
- Les calculs impliquant des nombres décimaux donnent parfois des résultats approximatifs, c'est pourquoi on préfèrera, dans la mesure du possible, travailler avec des nombres entiers.

## Le monde merveilleux des variables

- Les variables permettent de conserver dans le temps des données de votre programme.
- Vous pouvez vous servir de ces variables pour différentes choses : les afficher, faire des calculs avec, etc.
- Pour affecter une valeur à une variable, on utilise la syntaxe `nom_de_variable = valeur`.
- Il existe différents types de variables, en fonction de l'information que vous désirez conserver : `int`, `float`, chaîne de caractères etc.
- Pour afficher une donnée, comme la valeur d'une variable par exemple, on utilise la fonction `print`.

## Les structures conditionnelles

- Les **conditions** permettent d'exécuter certaines instructions dans certains cas, d'autres instructions dans un autre cas.
- Les conditions sont marquées par les mot-clés `if` (« si »), `elif` (« sinon si ») et `else` (« sinon »).
- Les mot-clés `if` et `elif` doivent être suivis d'un test (appelé aussi **prédicat**).
- Les **booléens** sont des données soit vraies (`True`) soit fausses (`False`).

## Les boucles

- Une **boucle** sert à répéter une portion de code en fonction d'un prédicat.
- On peut créer une boucle grâce au mot-clé `while` suivi d'un prédicat.
- On peut parcourir une séquence grâce à la syntaxe `for element in sequence:`.

## Pas à pas vers la modularité

- Une **fonction** est une portion de code contenant des instructions, que l'on va pouvoir réutiliser facilement.
- Découper son programme en fonctions permet une meilleure organisation.
- Les fonctions peuvent recevoir des informations en entrée et renvoyer une information grâce au mot-clé `return`.
- Les fonctions se définissent de la façon suivante : `def my_function(argument1, ..., argumentN):`.
- On peut écrire les programmes Python dans des fichiers portant l'extension `.py`.
- On peut créer des *fichiers* contenant des **modules** pour séparer le code.
- On peut créer des *répertoires* contenant des **packages** pour hiérarchiser un programme.

## Les exceptions

- On peut intercepter les **erreurs** (ou **exceptions**) levées par notre code grâce aux blocs `try` et `except`.
- La syntaxe d'une assertion est `assert test`.
- Les assertions lèvent une exception `AssertionError` si le test échoue.
- On peut lever une exception grâce au mot-clé `raise` suivi du type de l'exception.


# La programmation orientée objet (POO)

## Notre premier objet : les chaînes de caractères

- Les *variables* utilisées jusqu'ici sont en réalité des *objets*
- Les *types* de données utilisés jusqu'ici sont en fait des *classes*. Chaque objet est modelé sur une classe
- Chaque classe définit certaines fonctions, appelées **méthodes**, qui seront accessibles depuis l'objet grâce à `my_objet.my_method(args)`
- On peut directement accéder à un caractère d'une chaîne grâce au code suivant : `chaine[position_dans_la_chaine]`
- Il est tout à fait possible de sélectionner une partie de la chaîne grâce au code suivant : chaine[indice_debut:indice_fin].
- Méthodes intéressantes : capitalize, casefold, center, count, encode, index, isalnum, isalpha, isdecimal etc. (cf [Built-in Types](https://docs.python.org/3/library/stdtypes.html))

## Les listes et les tuples

- Une liste (**list**) est une séquence mutable pouvant contenir plusieurs autres objets.
- On peut **construire** une liste ainsi : `my_list = [item1, item2, ..., itemN]`.
- On peut **insérer** des éléments dans une liste à l'aide des méthodes `append(item)`, `insert(index, item)` et `extend(iterable)`.
- On peut **supprimer** un élément d'une liste avec le mot clé *del* (`del my_list[index]`) ou avec la méthode *remove* (`remove(item)` ne supprime que la 1ère occurrence).
- On peut **parcourir** une liste avec une boucle *for*. On peut utiliser la syntaxe `for i, item in enumerate(my_list)`.
- Un **tuple** est une séquence pouvant contenir des objets. À la différence de la liste, le tuple ne peut être modifié une fois créé. Lorsqu'on effectue une affectation multiple ou lorsqu'on veut qu'une fonction retourne plusieurs valeurs on utilise (implicitement) des tuples
- On peut **découper** une chaîne en fonction d'un séparateur en utilisant la méthode `split` de la chaîne. On peut **joindre** une liste contenant des chaînes de caractères en utilisant la méthode de chaîne `join`. Cette méthode doit être appelée sur le séparateur.
- On peut créer des fonctions attendant un nombre inconnu de paramètres grâce à la syntaxe `def fonction_inconnue(*parametres)` (les paramètres passés se retrouvent dans le tuple *parametres*).
- Les **compréhensions de listes** permettent de parcourir et filtrer une séquence en en renvoyant une nouvelle. La syntaxe pour effectuer un filtrage est la suivante : `[element for element in seq if condition].

Rq : idem str on peut faire my_list[index], len(my_list)...

## Les dictionnaires

* Un dictionnaire (**dict**) est un objet conteneur associant des clés à des valeurs.
* **Créer** un dictionnaire : `my_dict = {key1:value1, ..., keyN:valueN}`.
* **Ajouter** ou **remplacer** un élément dans un dictionnaire : `my_dict[key] = value`
* **Supprimer** une clé (et sa valeur correspondante) : `del my_dict[key]` ou `my_dict.pop(key)`
* On peut **parcourir** un dictionnaire grâce aux méthodes `keys()`, `values()` ou `items()`.
* On peut capturer les **paramètres nommés** passés à une fonction en utilisant cette syntaxe : *def my_function(**named_arguments)* (les paramètres nommés se retrouvent dans le dictionnaire *named_arguments*).

```python
def my_function(*positional, **keywords):
    print("Positional:", positional) # positional is a tuple
    print("Keywords:", keywords)     # keywords is a dict

my_function()
my_function('one', 'two', 'three')
my_function(a='four', b='five')
my_function('one', 'two', 'three', a='four', b='five')

kwargs = ('one', 'two', 'three')
posargs = {'a':'four', 'b':'five'}
my_function(*kwargs) # or my_function('one', 'two', 'three')
my_function(**posargs) # or my_function(a='four', b='five')
my_function(*kwargs, **posargs) # or my_function('one', 'two', 'three', a='four', b='five')
```

## Les fichiers

- On peut **ouvrir** un fichier en utilisant la fonction `open` prenant en paramètre le chemin vers le fichier et le mode d'ouverture (**r**ead, **w**rite, **a**ppend).
- On peut **lire** dans un fichier en utilisant la méthode `read`.
- On peut **écrire** dans un fichier en utilisant la méthode `write`.
- Un fichier doit être **refermé** après usage en utilisant la méthode `close` ou en utilisant la déclaration `with`.
- Le [module **pickle**](https://docs.python.org/3/library/pickle.html) est utilisé pour enregistrer des objets Python (*sérialiser*) dans des fichiers et les recharger ensuite.

```python
# serialize
with open('file.bin', 'wb') as file:
    my_pickler = pickle.Pickler(file)
    my_pickler.dump(variable)

# unserialize
with open('file.bin', 'rb') as file:
    my_unpickler = pickle.Unpickler(file)
    variable = my_unpickler.load()
```

## Portée des variables et références

TODO

## Première approche des classes

- À l'instar de Java, Python est **totalement orienté objet** (tout est objet).
  Derrière une variable, un module, une fonction… se cachent en réalité des objets.
  Ce qui différencie en premier lieu une variable d'une fonction, c'est qu'une fonction est exécutable (*callable*)
- On définit une classe en suivant la syntaxe `class MaClasse:` (convention *Camel Case*).
- Une **méthode** est une fonction membre d'une classe.
  En Python, elles se définissent comme des fonctions, sauf qu'elles se trouvent dans le corps de la classe.
- Une **méthode d'instance** (ou **méthode d'objet**) n'agit que sur un seul objet (instance de la classe) à la fois.
  En Python, elles prennent en premier paramètre `self`, l'instance de l'objet manipulé.
  L'appel `objet.methode(...)` correspond à `MaClasse.methode(objet, ...)`.
- Une **méthode de classe** ou une **méthode statique** est indépendante de toute instance de la classe (objet).
  En Python, il faut faire appel à `classmethod` ou `staticmethod` après la définition d'une telle méthode.
  Une méthode de classe prend en premier paramètre `cls`, la classe.
- On construit une **instance de classe** en appelant son **constructeur**, une méthode d'instance appelée `__init__`.
- Un **attribut** est une sorte de membre de classe.
  En Python, les attributs sont créés dynamiquement et n'ont pas besoin d'être déclarés.
- Un **attribut d'instance** est spécifique à chaque instance.
  On définit les attributs d'instance dans une méthode d'instance (en général le constructeur).
  En Python, on y accède depuis une méthode d'instance via `self.nom_attribut` ou depuis l'extérieur via `objet.nom_attribut`.
- Un **attribut de classe** est accessible sans avoir à créer une instance de cette classe en écrivant `MaClasse.nom_attribut`.
  Toutes les instances auront le même attribut de classe.
- Technique d'**introspection** :
    + La fonction `dir` renvoie une liste des attributs et des méthodes de l'objet qu'on lui passe en paramètre.
    + L'attribut `__dict__` est un dictionnaire qui contient en guise de clés les noms des attributs et, en tant que valeurs, les valeurs des attributs.

```python
class MyClass:

    # Méthode d'instance ou méthode d'objet
    def myInstanceMethod(self, argument1, ..., argumentN):
        ...

    # Méthode de classe
    def myClassMethod(cls, argument1, ..., argumentN):
        ...
    myClassMethod = classmethod(myClassMethod)

    # Méthode statique
    def myStaticMethod(argument1, ..., argumentN):
        ...
    myStaticMethod = staticmethod(myStaticMethod)

MyClass.myStaticMethod(args)

MyClass.myClassMethod(args)

instance = MyClass(args)
instance.myInstanceMethod(args)
```

## Les propriétés (et le principe d'encapsulation en Python)

- On accède à un attribut d'un objet en écrivant `objet.nom_propriete`.
- En Python, il n'y a pas d'attribut privé, tout est **public**.
  La convention veut qu'on n'accède pas, depuis l'extérieur de la classe, à un attribut ou à une méthode commençant par un souligné `_`.
- Les propriétés (**property**) sont un moyen transparent de manipuler des attributs d'objet.
  Elles permettent par exemple de dire à Python : « Quand un utilisateur souhaite modifier cet attribut, fais cela ».
  Si une action particulière doit être menée quand on veut lire/modifier/supprimer un attribut, on fait en sorte que l'attribut soit une propriété avec certaines méthodes (accesseur, mutateur ou autres) qui définissent ce que Python doit faire.
- Les propriétés sont utilisées pour gérer les cas particuliers de certains attributs.
  Pour un traitement récurrent sur tous les attributs, on aura plutôt recours aux méthodes spéciales.
- Les propriétés permettent de contrôler l'accès à certains attributs d'une instance.
- Elles se définissent dans le corps de la classe en suivant cette syntaxe : `nom_propriete = property(methode_accesseur, methode_mutateur, methode_suppression, methode_aide)`. On y fait appel ensuite en écrivant `objet.nom_propriete` comme pour n'importe quel attribut. Si l'on souhaite juste lire l'attribut, c'est la méthode définie comme accesseur qui est appelée. Si l'on souhaite modifier l'attribut, c'est la méthode mutateur, si elle est définie, qui est appelée. Chacun des paramètres à passer à `property` est optionnel.

```python
property(fget=None, fset=None, fdel=None, doc=None)
```

## Les méthodes spéciales

TODO

## Parenthèse sur le tri en Python

TODO

* `my_list.sort()` 
* `sorted(my_list)`

## L'héritage

TODO

## Derrière la boucle for

TODO

## Les décorateurs

- Les décorateurs permettent de modifier le comportement d'une fonction.
- Ce sont eux-mêmes des fonctions, prenant en paramètre une fonction et renvoyant une fonction (qui peut être la même).
- On peut déclarer une fonction comme décorée en plaçant, au-dessus de la ligne de sa définition, la ligne `@nom_decorateur`.
- Au moment de la définition de la fonction, le décorateur est appelé et la fonction qu'il renvoie sera celle utilisée.
- Les décorateurs peuvent également prendre des paramètres pour influer sur le comportement de la fonction décorée.

## Les métaclasses

TODO


# Les merveilles de la bibliothèque standard

[Documentation officielle](https://docs.python.org/3/)

## Les expressions régulières (re)

- Le [module **re**](https://docs.python.org/3/library/re.html) permet de manipuler des expressions régulières.
- La fonction `re.search(pattern, subject)` permet de *chercher* une expression dans une chaîne.
- La fonction `re.sub(pattern, replacement, subject)` permet de *remplacer* une certaine expression dans une chaîne.
- On peut *compiler* les expressions régulières grâce à la fonction `re.compile(pattern)`.
- On peut utiliser le *flag* **r** (*raw string literal*) pour échapper les antislashs automatiquement.
- On peut utiliser les quantificateurs non gourmands (*non-greedy*) : `*?`, `+?`, `??`, ou `{m,n}?`.
- Pour la substitution, on peut utiliser les **groupes** numérotés (\1, \2 etc.) ou donner des noms aux groupes avec la syntaxe `(?P<nom>pattern)` et `\g<nom>` (avec les chevrons).

## Le temps

- [Module **time**](https://docs.python.org/3/library/time.html)
    + `time()` renvoie le timestamp actuel
    + `localtime([seconds])` renvoie un objet isolant les informations d'un timestamp
    + `mktime(tuple)` renvoie le timestamp correspondant à une date
    + `sleep(seconds)` met en pause l'exécution du programme
    + `strftime(format, [tuple])` (par exemple `format='%Y-%m-%d %H:%M:%S'`) renvoie une date formatée
- [Module **datetime**](https://docs.python.org/3/library/datetime.html)
    + Classe **date** :
        + `date(year, month, day)`
        + `date.today()`
        + `date.fromtimestamp(timestamp)`
    + Classe **time** :
        + `time([hour[, minute[, second[, microsecond[, tzinfo]]]]])`
    + Classe **datetime** :
        + `datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])`
        + `datetime.now()`
        + `datetime.fromtimestamp(timestamp)`

## Un peu de programmation système

- [Module **sys**](https://docs.python.org/3/library/sys.html) :
    + Flux standards : `stdin`, `stdout`, `stderr`, `__stdin__`, etc.
    + `stdout.write("message")` écrit sur la sortie standard
    + `exit([status])` quitter le programme
    + `argv` contient la liste des arguments
- [Module **os**](https://docs.python.org/3/library/os.html) :
    + `getcwd()` renvoie le *current working directory*
    + `chdir(path)` modifie le *current working directory*
    + `system(command)` exécute la commande
    + `popen(command)` renvoie un objet (un *pipe*) qui permet de lire le retour de la commande (avec sa méthode *read*)
- [Module **signal**](https://docs.python.org/3/library/signal.html) : `signal.signal(signal.SIGINT, my_function)` permet d'intercepter des signaux envoyés à un programme
- Module **argparse** : [documentation](https://docs.python.org/3/library/argparse.html), [tutoriel](https://docs.python.org/3/howto/argparse.html)

## Un peu de mathématiques

- [Module **math**](https://docs.python.org/3/library/math.html)
    + Fonction usuelles : *pow, *sqrt*, *exp*, *fabs*
    + Trigonométrie : *degrees*, *radians*, *cos*, *acos*, etc.
    + Arrondir un nombre : *ceil*, *floor*, *trunc*
    + Constantes usuelles : *pi*, *e*
- [Module **fractions**](https://docs.python.org/3/library/fractions.html) : classe *Fraction* (utile pour la précision des calculs)
- [Module **random**](https://docs.python.org/3/library/random.html) :
    + `random()` génère un nombre pseudo-aléatoire entre 0 et 1
    + `randrange(start, end, step=1)` génère un nombre aléatoire entre *start* (inclus) et *end* (non inclus)
    + `randint(start, end)` génère un nombre aléatoire entre *start* et *end* inclus
    + `choice(sequence)` renvoie au hasard un élément d'une séquence
    + `shuffle(sequence)` mélange la séquence

## Gestion des mots de passe

- [Module **getpass**](https://docs.python.org/3/library/getpass.html) : `getpass(prompt)` pour la saisie d'un mot de passe par l'utilisateur
- [Module **hashlib**](https://docs.python.org/3/library/hashlib.html)
    + Lister les algorithmes `algorithms_guaranteed` et `algorithms_available`
    + Chiffrer un mot de passe : `sha1(my_pass.encode()).hexdigest()`

## Le réseau

TODO

## Les tests unitaires avec unittest

TODO

## La programmation parallèle avec threading

TODO

## Des interfaces graphiques avec tkinter

- [**tkinter** (*Tk interface*)](https://docs.python.org/3/library/tkinter.html) est un module intégré à la bibliothèque standard et permettant de créer des interfaces graphiques.
- Les objets graphiques (boutons, zones de texte, cases à cocher…) sont appelés des **widgets**.
- Dans **tkinter**, les **widgets** prennent, lors de leur construction, leur objet parent en premier paramètre.
- Chaque **widget** possède des options qu'il peut préciser comme arguments nommés lors de sa construction.
- On peut également accéder aux options d'un widget ainsi : `widget["nom_option"]`.


# Annexes

## Écrire nos programmes Python dans des fichiers

Pour mettre en pause un programme sous Windows :

```python
# -*-coding:Latin-1 -*

import os
print("Hello world !")
os.system("pause")
```

ou bien (méthode universelle) :

```python
#!/usr/bin/env python
# -*-coding:Utf-8 -*

print("Hello world !")
input("Appuyez sur ENTRÉE pour fermer ce programme...")
```

## Distribuer facilement nos programmes Python avec cx_Freeze

TODO

## De bonnes pratiques

TODO

## Pour finir et bien continuer

TODO



# [ElementTree XML API](https://docs.python.org/3/library/xml.etree.elementtree.html)

```python
import xml.etree.ElementTree as ET

# from file
tree = ET.parse('data.xml')
root = tree.getroot()

# from string
root = ET.fromstring(country_data_as_string)

# Element
element.tag    # str
element.attrib # dict
element.text
element.tail
element.set('name', 'value')

element.iter('neighbor')

element.findall('xpath')
```
