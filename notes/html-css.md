# HTML/CSS

## Sites internet

* W3C : [Validator](http://validator.w3.org/), [Unicorn](http://validator.w3.org/unicorn/)
* Browser compatibility : [caniuse.com](http://caniuse.com/), [normansblog.de (CSS only)](http://www.normansblog.de/demos/browser-support-checklist-css3/)
* CSS pre-processor : [{LESS}](http://lesscss.org/), [Sass](http://sass-lang.com/)...
* [HTML5 Shiv (or Shim)](https://code.google.com/p/html5shiv/) :  HTML5 IE enabling script
* [HTML5 Boilerplate](http://html5boilerplate.com/)
* [Selectivizr](http://selectivizr.com/) : CSS3 selectors for IE
* [CSS3Pie](http://css3pie.com/) : CSS3 decorations for IE
* [Modernizr](http://modernizr.com/) : a JavaScript library that detects HTML5 and CSS3 features in the user's browser
* [normalize.css](http://necolas.github.io/normalize.css/) : a modern, HTML5-ready alternative to CSS resets
* [KNACCS](http://www.knacss.com/) : a simple and lightweight CSS framework
* [Ink](http://ink.sapo.pt/)
* [FontSquirrel](http://www.fontsquirrel.com/)
* [FontAwesome](http://fortawesome.github.io/Font-Awesome/)
* [Bootstrap](http://getbootstrap.com/)
* [freehtml5templates.com](http://freehtml5templates.com/)
* Google H4x0r http://fr.wikipedia.org/wiki/Leet

## Documentation, mémo

* [WebPlatform.org](http://www.webplatform.org/)
* [Mozilla Developer Network](https://developer.mozilla.org/)
* [W3 Schools](http://www.w3schools.com/)
* [HTML elements](http://www.w3.org/TR/html-markup/elements-by-function.html http://www.w3.org/TR/html-markup/elements.html)
* [CSS Selectors](http://www.w3.org/TR/css3-selectors/#selectors)
* OpenClassRooms : [Mémento des balises HTML](http://fr.openclassrooms.com/informatique/cours/apprenez-a-creer-votre-site-web-avec-html5-et-css3/memento-des-balises-html), [Mémento des propriétés CSS](http://fr.openclassrooms.com/informatique/cours/apprenez-a-creer-votre-site-web-avec-html5-et-css3/memento-des-proprietes-css)

## Mémento

* HTML pour le fond, CSS pour la forme
* **HTML** : permet d'écrire et organiser le contenu de la page (paragraphes, titres…)
* **CSS** : permet de mettre en forme la page (couleur, taille…)
* Ne pas confondre **Internet** et le **Web** (inclus les e-mails, partie d'Internet)
* Le Web a été inventé par **Tim Berners-Lee** au début des années 1990.
* Héritage en CSS : Le CSS décide que c'est la déclaration la plus précise qui l'emporte, peu importe l'ordre
* Nouvelles balises : `<header>` (en-tête), `<footer>` (pied de page), `<nav>` (liens principaux de navigation), `<section>` (section de page), `<aside>` (informations complémentaires), `<article>` (article indépendant)
* Ne pas oublier d'utiliser `word-wrap: break-word;` dans le cas où un bloc est susceptible de contenir du texte saisi par des utilisateurs (et `overflow` si le bloc est de taille fixe)
* Proposer une alternative à la base audio avec **Dewplayer**
* Format des **polices** de caractères
    * `.ttf` : TrueType Font (IE9 et tous les autres navigateurs)
    * `.eot` : Embedded OpenType (IE uniquement, format propriétaire)
    * `.otf` : OpenType Font (pas compatible avec IE)
    * `.svg` : SVG Font (seul format reconnu sur les iPhones et iPads pour le moment)
    * `.woff` : Web Open Font Format (nouveau format conçu pour le Web, fonctionne sur IE9 et tous les autres navigateurs)
* Types de balises
    + **block** (`<p>`, `<h1>`…) : créent un retour à la ligne et occupent par défaut toute la largeur disponible. Elles se suivent de haut en bas.
    + **inline** (`<a>`, `<strong>`…) : ces balises délimitent du texte au milieu d'une ligne. Elles se suivent de gauche à droite.
* **Positionnement** flottant, inline-block, absolu, fixe, relatif.
* **Tableau** : `table`, `tr`, `td`, `th`, `caption`, `thead`, `tfoot`, `tbody`
* **Listes** : `ol > li` ; `ul > li` ; `dl > dt + dd`
* inline-block pour IE http://www.alsacreations.com/article/lire/76-haslayout-internet-explorer.html
* IE6-8 ne connaissent pas les **media queries**. Pour éviter qu'ils lisent les propriétés CSS alors qu'ils ne sont pas concernés par la règle, on peut utiliser le mot-clé *only* que ces vieilles versions ne connaissent pas (`@media only screen` ne provoquera pas de bug sur les vieux navigateurs)
* Au lieu d'utiliser **IETester** (instable) on peut simplement changer le comportement d'IE afin de simuler une ancienne version avec F12 (à partir de IE7)

```html
<!--[if IE 6]><script>if(confirm('Votre version actuelle d\'internet explorer est trop ancienne. Il est conseille d\'effectuer une mise a jour si vous voulez acceder a une version optimise de ce site web. Veuillez nous excuser du desagrement.')) {
document.location.href="http://www.microsoft.com/france/windows/internet-explorer"; 
}</script><![endif]-->
<!--[if IE 7]><script>if(confirm('Votre version actuelle d\'internet explorer est trop ancienne. Il est conseille d\'effectuer une mise a jour si vous voulez acceder a une version optimise de ce site web. Veuillez nous excuser du desagrement.')) {
document.location.href="http://www.microsoft.com/france/windows/internet-explorer"; 
}</script><![endif]-->
```
