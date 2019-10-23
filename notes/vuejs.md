# VueJS

[Tutoriel grafikart.fr](https://www.grafikart.fr/tutoriels/vuejs)

## 1. Introduction
- VueJS (+ implicite) vs React (+ explicite)
- VueJS vs AngularJS/Angular2 (framework plus complet, bcp + d'outils, TypeScript)

## 2. Découverte
- `{{ message }}` pour afficher une propriété (déclarée dans `data`)
- `:attr="[..]"` correspond à `v-bind:attr="[..]"` pour afficher une propriété dans un attribut
- `v-if="[condition]"` et `v-else`
- `new Vue()` : `el`, `data`, `methods`
- `v-show="[condition]"` ressemble à `v-if` mais utilise une autre technique (`display:none`)
- `v-for="element in list"`
- `@click` correspond à `v-on:click` (idem pour les autres événements)
- `v-model` est utile sur un champ input pour synchroniser une donnée
- `v-model="cls" :true-value="'success'" :false-value="'error'"` pour choisir ce que vaut cls si case cochée ou non

## 3. L'instance
- `let vm = new Vue(..)`
- `vm.$data`, système de getters et de setters
- Limitations : on ne peut pas ajouter un élt de tableau directement (tab.push() fonctionne car greffé dessus, mais pas tab[0]), ni ajouter de nouvelles propriétés non déclarées.
- `vm.$el` pour greffer un plugin Javascript dans un composant VueJS
- Lifecycle (cf https://vuejs.org/v2/guide/instance.html#Lifecycle-Diagram) : `mounted`, `destroyed` fréquemment utilisés

## 4. Propriétés combinées & Watchers
- `computed` permet de définir des propriétés qui dépendent d'autres propriétés, mais contrairement à `methods` il est capable de détecter s'il faut recharger ou pas. On peut définir un getter et un setter, en déclarant un objet plutôt qu'une fonction.
- `watch` permet de détecter lorsqu'une propriété a été modifié.

## 5. Les Directives
- Les directives permettent de greffer un comportement spécial. Nous en avons déjà vu certaines dans la première partie avec par exemple v-if, v-show ou v-for. Il est d'ailleurs possible de créer ses propres directives pour ajouter ses propres comportements.
- Modifieurs :
  + `@click.prevent`, `.stop`, `.self`, etc.
  + `v-model.lazy`, `v-model.trim`
  + `@keyup.space`
  + `Vue.directive` permet de créer des directives personnalisées.

## 6. Les Filtres

## 7. x

## 8. x

## 9. x

## 10. x

## 11. x

## 12. x

## 13. x

## 14. x

## 15. x
