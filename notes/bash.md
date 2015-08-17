# Bash

## Mémo

- `!cmd` : dernière commande commençant par cmd
- `!N` : la commande n°N dans l'historique
- `!!` : dernière commande càd la précédente (ex: `sudo !!`)
- `!*` : arguments de la commande précédente
- `!!$` : dernier argument de la commande précédente
- `text.{old,new}`
- `cd -` et `~-`
- préférer `$()` à `backquotes` (imbrications possibles)
- Tests sur :
    - [les objets du système de fichiers](http://fr.wikibooks.org/wiki/Programmation_Bash/Tests#Tests_sur_les_objets_du_syst.C3.A8me_de_fichiers)
    - [les chaînes de caractères](http://fr.wikibooks.org/wiki/Programmation_Bash/Tests#Tests_sur_les_cha.C3.AEnes_de_caract.C3.A8res)
    - [les nombres](http://fr.wikibooks.org/wiki/Programmation_Bash/Tests#Tests_sur_les_nombres)

## Raccourcis claviers habituels dans un terminal

- Ctrl+L : efface l'écran
- Ctrl+D : efface le caractère courant ou déconnecte si la ligne est déjà vide
- Ctrl+R : pour une recherche dans l'historique
- Ctrl+T : échange deux lettres
- Ctrl+A : début de ligne
- Ctrl+E : fin de ligne
- Ctrl+U : efface tout à gauche du curseur
- Ctrl+K : efface tout à droite du curseur
- Ctrl+W : efface le mot à gauche du curseur
- Ctrl+Y : qui colle ce qui avait été saisi précédemment
- Alt+B  : pour se déplacer au mot par mot dans la ligne de commande en arrière
- Alt+F  : pour se déplacer au mot par mot dans la ligne de commande en avant
- Alt+D  : efface le mot suivant
- Alt+T  : échange le mot courant et le mot précédent
- Alt+C  : met en majuscule la lettre courante, en minuscule les autres lettres du mot courant, puis se place au mot suivant

## Trucs et astuces

### Éteindre l'écran (économise la batterie)

```bash
xset dpms force off
```

### [Aspirer un site](http://forum.ubuntu-fr.org/viewtopic.php?id=78954)

```bash
wget -r -l5 -k -E "http://example.com"
```

### mirror local folder to FTP remote

```bash
lftp "ftp://user@hostname" -e "mirror --no-perms --delete --exclude secrets.ini --reverse /var/www/mysite /; quit"
```

### Rechercher les fichiers/dossiers n'appartenant à un utilisateur ou à un groupe

```bash
find [<folder>] ! -user <user>
find [<folder>] ! -group <user>
```

### Renommage en lots

Voir [parameter expansion](http://wiki.bash-hackers.org/syntax/pe#case_modification) pour plus de détails.

```bash
# Rename all *.txt to *.md
for FILE in *.txt; do
    mv "$FILE" "${FILE%.txt}.md"  # or "${FILE/%.txt/.md}"
done

# Rename all *.txt to lowercase
for FILE in *.txt; do
  mv "$FILE" "${FILE,,}"
done

#function myrename() {
#    [ ! -z $2 ] && find -type f -name "*$1*" -exec rename 's/'$1'/'$2'/g' {} \;
#}
```

### Export ODF (.odt, .ods, etc.) to PDF using LibreOffice

```bash
libreoffice --headless --invisible --convert-to pdf <file>
```

### Convert EPUB to MOBI

```bash
ebook-convert myfile.epub myfile.mobi  # requires calibre
```

### IP fixe

```bash
ifconfig eth0 inet 192.168.0.1 netmask 255.255.255.0 up
```

### rot13: simple letter substitution cypher (rotate by 13 places)

```bash
function rot13()
{
    echo $@ | tr a-zA-Z n-za-mN-ZA-M
}
```

### Archives tar (alias)

```bash
alias lstar='tar -tf'
alias mktar='tar -cvf archive.tar'
alias untar='tar -xvf'
```

### Caractères spéciaux

```bash
# Find non-ascii chars + color + number line !
# http://stackoverflow.com/questions/3001177/how-do-i-grep-for-non-ascii-characters-in-unix
#grep --color='auto' -P -n "[\x80-\xFF]" file.xml
function nonasciichars()
{
    grep -P "[^\x00-\x7F]" "$1"
}
```

### [dos2unix](http://www.commentcamarche.net/faq/5978-sed-conversion-retours-chariots-dos-crlf-unix-lf)

```bash
# dos2unix
sed 's/\x0D$//' "$1" # for GNU Sed or 's/^M$//'

# unix2dox
sed 's/$/\r/' "$1" # for GNU Sed or 's/$/^M/'
```

### Retours chariots

```bash
# List all files containing CR
# http://stackoverflow.com/questions/73833/how-do-you-search-for-files-containing-dos-line-endings-crlf-with-grep-on-linu
find . -not -type d -exec file "{}" ";" | grep CR
```

```bash
# https://en.wikipedia.org/wiki/Newline
#   * LF:    Line Feed, U+000A
#   * VT:    Vertical Tab, U+000B
#   * FF:    Form Feed, U+000C
#   * CR:    Carriage Return, U+000D
#   * CR+LF: CR (U+000D) followed by LF (U+000A)
#   * NEL:   Next Line, U+0085
#   * LS:    Line Separator, U+2028
#   * PS:    Paragraph Separator, U+2029
function newlinetype()
{
    [ $# -eq 0 ] && echo "Usage: newlinetype FILE1 [FILE2 ...]" 1>&2 && return 1
    
    while [ -n "$1" ]
    do
        echo -n "$1:"
        grep -l $'\u000D' "$1" > /dev/null && echo -n ' CR'
        grep -l $'\u000A' "$1" > /dev/null && echo -n ' LF'
        grep -l $'\u000B' "$1" > /dev/null && echo -n ' VT'
        grep -l $'\u000C' "$1" > /dev/null && echo -n ' FF'
        grep -l $'\u0085' "$1" > /dev/null && echo -n ' NEL'
        grep -l $'\u2028' "$1" > /dev/null && echo -n ' LS'
        grep -l $'\u2029' "$1" > /dev/null && echo -n ' PS'
        echo
        shift
    done
}
```

### BOM (Byte Order Marker)

```bash
# http://muzso.hu/2011/11/08/using-awk-sed-to-detect-remove-the-byte-order-mark-bom
function bom_show()
{
    [ $# -ne 0 ] && echo "Usage: bom_show" 1>&2 && return 1
    grep -rl $'\xEF\xBB\xBF' .
}

function bom_clear()
{
    [ $# -eq 0 ] && echo "Usage: bom_clear FILE1 [FILE2 ...]" 1>&2 && return 1
    sed -i '1 s/^\xEF\xBB\xBF//' $@ # GNU sed
    #sed -i .bak '1 s/^\xef\xbb\xbf//' $@ # FreeBSD or Mac OS X
}

function bom_clear_all()
{
    [ $# -ne 0 ] && echo "Usage: bom_clear_all" 1>&2 && return 1
    find . -type f -exec sed -i.bak -e '1s/^\xEF\xBB\xBF//' {} \; -exec rm '{}.bak' \;
}
```

### Convertion wav → flac

```bash
function dir2flac()
{
    if [ $# -eq 0 ]
    then
        echo "Aucun fichier à traiter"
        return 1
    fi
    
    for ((i = 1; i <= $#; i++)); do
        echo "${!i} => ${!i}.flac"
        ffmpeg -i "${!i}" -acodec flac "${!i}.flac"
    done
}
```

### cdb: Managing bookmarks with cd

```bash
function cdb()
{
    [ ! -e ~/.cdb ] && mkdir ~/.cdb
    
    if [ -z "$1" ]
    then
        echo "Usage: cdb [-c|-g|-d|-l] [bookmark]" 1>&2
    else
        case $1 in
            # Create a bookmark
            -c) shift
                if [ ! -f ~/.cdb/$1 ]
                then
                    echo "cd \"$(pwd)\"" > ~/.cdb/"$1"
                else
                    echo "Error : cdb: '$1': ce signet existe déjà" 1>&2
                fi
                ;;
            # Goto a bookmark
            -g) shift
                if [ -f ~/.cdb/$1 ]
                then
                    source ~/.cdb/"$1"
                    pwd
                else
                    echo "Error : cdb: '$1': ce signet n'existe pas" 1>&2
                fi
                ;;
            # Delete a bookmark
            -d) shift
                if [ -f ~/.cdb/$1 ]
                then
                    rm ~/.cdb/"$1"
                else
                    echo "Error : cdb: '$1': ce signet n'existe pas" 1>&2
                fi
                ;;
            # List all bookmarks
            -l) shift
                ls ~/.cdb/
                ;;
            # Other option : unknown
            -*) echo "Error : cdb: '$1': argument inconnu" 1>&2
                ;;
            # Other : call to 'Goto'
             *) cdb -g $1
                ;;
        esac
    fi
}
```

### PS1 variables

```bash
# List of available codes for PS1 variable :
#
#  \a an ASCII bell character (07)
#  \d the date in "Weekday Month Date" format (e.g., "Tue May 26")
#  \D{format} - the format is passed to strftime(3) and the result is inserted
#    into the prompt string; an empty format results in a locale-specific time
#    representation. The braces are required
#  \e an ASCII escape character (033)
#  \h the hostname up to the first part
#  \H the hostname
#  \j the number of jobs currently managed by the shell
#  \l the basename of the shell's terminal device name
#  \n newline
#  \r carriage return
#  \s the name of the shell, the basename of $0 (the portion following the final
#    slash)
#  \t the current time in 24-hour HH:MM:SS format
#  \T the current time in 12-hour HH:MM:SS format
#  \@ the current time in 12-hour am/pm format
#  \A the current time in 24-hour HH:MM format
#  \u the username of the current user
#  \v the version of bash (e.g., 2.00)
#  \V the release of bash, version + patch level (e.g., 2.00.0)
#  \w the current working directory, with $HOME abbreviated with a tilde
#  \W the basename of the current working directory, with $HOME abbreviated with a tilde
#  \! the history number of this command
#  \# the command number of this command
#  \$ if the effective UID is 0, a #, otherwise a $
#  \nnn the character corresponding to the octal number nnn
#  \\ a backslash
#  \[ begin a sequence of non-printing characters, which could be used to embed
#    a terminal control sequence into the prompt
#  \] end a sequence of non-printing character
#  [not sure] \$? : Status of the last command
```
