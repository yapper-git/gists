
Beamer est basé sur un environnement de page (frame) qui représente un «transparent», lequel peut être affiché en plusieurs étapes par une succession de couches (slides).

# Les frames
- Titres via `\frametitle` et `\framesubtitle`
- Option `label` pour utiliser les références : `\begin{frame}[label=nom-de-la-diapo]`
- Option `fragile` pour utiliser l’environnement `verbatim` à l'intérieur sans l'interpréter. Pour que le code soit interprété, utiliser plutôt l'environnement `semiveratim`
- Option `plain` pour supprimer le pied de page
- Option `allowframebreaks` pour utiliser plusieurs diapos si besoin

## Les éléments de base du diaporama
- Options `\documentclass[options]{beamer}`, `t`, `b`, `c` pour l'alignement vertical des slides et `Npt` pour la taille de la police
- `\titlepage` permet de créer une page de titres (`\title`, `\author`, `\institute`, `\date` à configurer)
- `\tableofcontents` permet de créer une table des matières (options possibles pour pause, profondeur)
- `\setbeamersize` permet de changer les marges
- `\logo` permet de personnaliser un logo à afficher sur toutes les pages


## Les overlays
- La commande `\pause` permet de faire apparaître le contenu progressivement. On peut aussi modifier l'ordre en utilisant `\pause[X]`.
- Les **spécifications** permettent d'appliquer une commande seulement pour certaines slides, par exemple appliquée à la commande `\textbf<3>{texte}` ou `\textbf<3,5-7>{texte}`.
