# GIT

*Git* est un logiciel libre de gestion de versions décentralisé.

Interfaces graphiques : *gitk*, *gitg*, *giggle*

L'essentiel des commandes utiles sont listées et expliquées sur [la documentation d'Archlinux](https://wiki.archlinux.org/index.php/git).

## Commandes générales

- **init** : Créer un nouveau dépôt vide
- **clone**  : Cloner un dépôt existant via `git clone <repository> [<directory>]` où `<repository>` peut être :
    - `ssh://[user@]example.com/srv/git/foo.git`
    - `http://example.com/foo.git`
    - `git://example.com/foo.git`
- **status** : Déterminer quels fichiers sont dans quel état
- **diff** : Lister les changements effectués depuis le dernier commit via `git diff [<file>]`
- **log** : Lister (et parcourir) les derniers commits via `git log [-p|--stat]`
- **pull** : Télécharger les nouveautés
- **push** : Envoyer vos commits (nécessite une autorisation, irréversible, penser à faire un `git log -p` avant)

## Gestion des branches

- `git branch` : lister toutes les branches
- `git branch <newbranch>` : créer une nouvelle branche
- `git checkout <newbranch>` : changer de branche
- `git checkout -b <newbranch>` : créer une nouvelle branche ET changer de branche

## Trucs et astuces

- Créer un dépôt central :
```bash
git init --bare --shared foo.git # or git clone
chgrp -R foodevgroup foo.git
```
- Modifier le dernier message de commit (si pas encore transmis !) : `git commit --amend`
- Annuler le dernier commit (soft: fichiers non modifiés) : `git reset HEAD^`
- Annuler tous les changements du dernier commit (hard: fichiers modifiés) : `git reset --hard HEAD^`
- Annuler les modifications d’un fichier avant un commit (i.e. le restaurer tel qu'il était au dernier commit) : `git checkout file`
- Annuler un commit publié : `git revert commitid`
- Rechercher dans les fichiers sources : `git grep [-n] "TODO"`
- Demander à Git d’ignorer des fichiers en utilisant le fichier `.gitignore`
- Éviter les commits inutiles (mettre de côté des modifications) :
```bash
git stash
git stash pop
```
- Configurer git :
```bash
git config --global color.diff auto
git config --global color.status auto
git config --global color.branch auto
git config --global user.name "votre_pseudo"
git config --global user.email moi@email.com
```
