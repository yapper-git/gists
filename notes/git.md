# GIT

Git est un logiciel libre de gestion de versions décentralisé.
gitk, gitg, giggle

* Cloner un dépôt git existant :
  `git clone <repository> [<directory>]`
  (`<repository>` peut être `ssh://user@example.com/srv/git/foo.git`, `http://example.com/foo.git`, `git://example.com/foo.git`)
* Créer un dépôt central :
  `git init|clone... --bare --shared foo.git && chgrp -R foodevgroup foo.git`
* Déterminer quels fichiers sont dans quel état : `git status`
* Lister les changements effectués depuis le dernier commit : `git diff [file]`
* Lister (et parcourir) les derniers commits : `git log [-p|--stat]`
* Modifier le dernier message de commit (si pas encore transmis!) : `git commit --amend`
* Annuler le dernier commit (soft: fichiers non modifiés) : `git reset HEAD^`
* Annuler tous les changements du dernier commit (hard: fichiers modifiés) : `git reset --hard HEAD^`
* Annuler les modifications d’un fichier avant un commit (ie le restaurer tel qu'il était au dernier commit) : `git checkout file`
* Télécharger les nouveautés : `git pull`
* Envoyer vos commits (nécessite une autorisation, irréversible, penser à faire un `git log -p` avant!) : `git push`
* Annuler un commit publié : `git revert commitid`

## Branches
* `git branch` : lister toutes les branches
* `git branch newbranch` : créer une nouvelle branche
* `git checkout newbranch` : changer de branche
* `git checkout -b newbranch` : créer une nouvelle branche ET changer de branche

Éviter les commits inutiles (mettre de côté des modifications)
`git stash`
`git stash pop`

* Rechercher dans les fichiers sources : `git grep [-n] "TODO"`
* Demander à Git d’ignorer des fichiers (`.gitignore`)

```
git push origin master
git push origin my-new-feature
# Source: github minituto
```

```
git ls-files
git clone location folder
git pull location master
git push location branch
git remote add label location
git fetch label
git tag 2.14 checksum
# Source: https://wiki.archlinux.org/index.php/git
```

```
git config --global color.diff auto
git config --global color.status auto
git config --global color.branch auto
git config --global user.name "votre_pseudo"
git config --global user.email moi@email.com
```
