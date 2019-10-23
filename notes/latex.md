# LaTeX

* [Tutoriel LaTeX d'OpenClassrooms](http://openclassrooms.com/courses/redigez-des-documents-de-qualite-avec-latex)
* [Wikibooks](http://fr.wikibooks.org/wiki/LaTeX/Cr%C3%A9er_une_extension_ou_une_classe)
* [MathJax](http://www.mathjax.org/) pour afficher des formules sur des pages web
* [Stackexchange: Change TEXMFHOME](http://tex.stackexchange.com/questions/66614/change-texmfhome-per-user)

---

## 1. Découverte de LaTeX

### 1.1 Qu'est-ce que LaTeX ?
- LaTeX est un langage de description libre et gratuit. Il permet de concevoir des documents de qualité professionnelle sans connaissances en typographie et mise en page.
- Contrairement à un traitement de texte comme Word, LaTeX vous permet de vous concentrer sur le contenu de votre document. Tout le reste est généré automatiquement par LaTeX. Pas besoin de se préoccuper de la numérotation des pages, de la création d'un sommaire, de la numérotation des figures ou encore des marges et alinéas !
- LaTeX permet de produire des documents PDF qui s'affichent de la même façon sur tous les ordinateurs, qu'ils soient sous Windows, Mac OS ou Linux.
- C'est un langage très populaire dans les études supérieures, chez les scientifiques et dans le monde de l'édition. Il excelle en particulier dans l'écriture de formules mathématiques, domaine dans lequel il fait figure d'outil de référence.
- Ce livre a été écrit en LaTeX. ;)

### 1.2. Installer LaTeX
- Il existe trois grandes familles de logiciels utilisés pour concevoir des documents en LaTeX : **les distributions, les éditeurs LaTeX et les lecteurs**.
- Un éditeur LaTeX n'est pas indispensable à l'apprentissage de LaTeX (mais en utiliser un simplifie énormément l'apprentissage grâce à la coloration du code et aux différents outils disponibles).
- Le format de prédilection que nous choisirons par la suite sera le **PDF**. Nous nous souviendrons néanmoins de l'attrait que suscite le format de fichier **PostScript** pour certains laboratoires de recherche.
- **Kile**, **TeXShop** et **TeXnicCenter** sont actuellement très utilisés dans le monde de la recherche. Nous utiliserons ces éditeurs LaTeX sur des ordinateurs équipés respectivement de Linux, Mac OS et Windows.

### 1.3. Structurer son premier document
- Pour transformer un fichier LaTeX (`.tex`) en PDF (`.pdf`), on passe par une étape dite de **compilation**.
- La compilation d'un document se déclenche grâce à des raccourcis présents dans l'éditeur LaTeX. Il est aussi possible d'utiliser la ligne de commande. Il suffit de taper : `pdflatex fichier.tex`.
- Certains caractères spéciaux (comme `$ # & %`...) doivent être précédés d'un backslash (\textbackslash) pour être insérés dans un texte (L'oubli d'un backslash devant ces caractères spéciaux peut entraîner de multiples erreurs et bugs lors d'une compilation.).
- Un document LaTeX peut être de type `article`, `book`, `letter` ou `report` selon le type de document que vous souhaitez écrire.
- Nous écrirons le contenu de notre document à l'intérieur de l'environnement `document`, c'est-à-dire entre les commandes `\begin{document}` et `\end{document}`.

### 1.4. Les packages
- Les packages sont des outils permettant à LaTeX d'exécuter de nouvelles tâches : coloration du texte, règles typographiques, lettrines, encadrements... Grâce à eux, il est possible d'étendre les possibilités de LaTeX.
- Il existe des milliers de packages. Sous Windows, MiKTeX les télécharge et les installe automatiquement à la volée. Sous Mac OS et Linux il faut parfois télécharger manuellement ces fichiers.
- Pour utiliser un package, il suffit de l'appeler au début de votre document avec la commande `\usepackage{nompackage}`.
- La communauté des utilisateurs (dont vous faites désormais partie) peut ajouter autant de fonctions qu'elle le souhaite à LaTeX via la création de packages. Créez-en un qui prépare le café et vous ferez fortune. :)

## 2. Utilisation basique de LaTeX

### 2.1. Maîtriser sa mise en page
- Les documents LaTeX respectent une hiérarchie très précise : une partie contient des chapitres, scindés en sections, elles-mêmes divisées en sous-sections...
- Un document de classe `book` (livre) propose en plus un découpage global avec un préambule, un corps, des annexes et des chapitres épilogues
- Les différentes parties d'un livre n'ont pas la même numérotation, ni au niveau des titres, ni au niveau des numéros de pages.
- Une page de garde simple (Il est bien sûr possible de faire une page de garde bien plus compliquée) comporte un titre, le nom du ou des auteurs et une date.
- Les environnements `flushright`, `center` et `flushleft` permettent respectivement d'aligner à droite, de centrer ou d'aligner à gauche du texte. Par défaut, LaTeX justifie le texte.
- Pour créer un nouveau paragraphe, il suffit de sauter deux lignes. Si vous le souhaitez, il est aussi possible d'utiliser `\newline` ou `\\` qui permettent d'effectuer un simple retour à la ligne. Enfin, `\newpage` engendre un saut de page.

### 2.3. Les polices

### 2.4. Les notes

## 3. Utilisation avancée de LaTeX

### 3.1. Les figures

### 3.2. Les tableaux

### 3.3. Les mathématiques

### 3.4. Sommaire et index

### 3.5. La bibliographie

## 4. Annexes

### 4.1. Les caractères spéciaux

### 4.2. Liste des packages

### 4.3. Les gabarits

### 4.4. Mémento

### 4.5. Aller plus loin
