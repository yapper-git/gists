# Archlinux

- [Beginners' guide](https://wiki.archlinux.org/index.php/beginners%27_guide)
- [Installation guide](https://wiki.archlinux.org/index.php/Installation_guide)

## Configuration (general)

- Set the *hostname* (in `/etc/hostname`)
- Set the *timezone* (create `/etc/localtime` using symbolic link)
- Set the *locales* (in `/etc/locale.gen` and `/etc/locale.conf`, then run `locale-gen`)
- [bash: tab completion](https://wiki.archlinux.org/index.php/Bash_completion#Tab_completion)
- [bash: pkgfile or command-not-found](https://wiki.archlinux.org/index.php/bash#Command-not-found_.28AUR.29)
- [bash: auto cd when entering just a path](https://wiki.archlinux.org/index.php/bash#Auto_.22cd.22_when_entering_just_a_path)
- [bash: line wrap on window resize](https://wiki.archlinux.org/index.php/bash#Line_wrap_on_window_resize)
- [pacman](https://wiki.archlinux.org/index.php/pacman#Configuration): uncomment `Color` and `TotalDownload` in `/etc/pacman.conf`
- [sudo: use wheel group](https://wiki.archlinux.org/index.php/sudo): install `sudo`, edit `/etc/sudoers` using `visudo` command, uncomment wheel related line.
- [avahi: hostname resolution](https://wiki.archlinux.org/index.php/Avahi#Hostname_resolution)
- [Disable PC speaker beep](https://wiki.archlinux.org/index.php/Disable_PC_speaker_beep#Globally)
- [Utiliser le dépôt archlinuxfr via yaourt](https://wiki.archlinux.fr/Depot_archlinuxfr)

## Configuration (server)

- SSH (`PermitRootLogin`)
- MariaDB ( `/usr/bin/mysql_secure_installation`) ou PostgreSQL
- Nginx
    + [PhpMyAdmin](https://wiki.archlinux.org/index.php/PhpMyAdmin#Nginx_Configuration)
    + PHP (`php php-fpm php-gd php-intl php-sqlite php-tidy php-xsl`)
    + Django (`python3 python-pip python-virtualenv uwsgi-plugin-python`)

## Tips

```bash
# update
sudo paman -Syu
pikaur -Sua --devel
sudo updatedb
sudo pkgfile --update

# search (in packages'names and descriptions) for packages
pacman -Ss string1 string2 ...

# display extensive information
pacman -Si package_name

# list changed configuration files
pacman -Qii | grep ^MODIFIED | cut -f2

# list all packages no longer required as dependencies (orphans)
pacman -Qdt  # add q to hide package version

# list all packages explicitly installed
pacman -Qe  # add q to hide package version

# list all packages explicitly installed and not required as dependencies
pacman -Qet  # add q to hide package version

# list all foreign packages
pacman -Qm  # add q to hide package version

# retrieve a list of the files installed by a package
pacman -Ql package_name
```

## En vrac

### Partage d'imprimantes (sur réseau local)

Passer par `system-config-printer`
(et non gnome-control-center qui ne fonctionne pas, même s'il propose de l'ajouter mais n'y arrive pas...)
avahi-daemon?

### Sans ifconfig, ni Networkmanager

```bash
ip link show
dhcpcd INTERFACE
```

### Erreur PGP lors mise à jour pikaur

```bash
gpg --recv-keys FC918B335044912A
```
