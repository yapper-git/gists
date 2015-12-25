# Archlinux

* [Beginners' guide](https://wiki.archlinux.org/index.php/beginners%27_guide)
* [Installation guide](https://wiki.archlinux.org/index.php/Installation_guide)

## Configuration (general)

* [bash: tab completion](https://wiki.archlinux.org/index.php/Bash_completion#Tab_completion)
* [bash: pkgfile or command-not-found](https://wiki.archlinux.org/index.php/bash#Command-not-found_.28AUR.29)
* [bash: auto cd when entering just a path](https://wiki.archlinux.org/index.php/bash#Auto_.22cd.22_when_entering_just_a_path)
* [bash: line wrap on window resize](https://wiki.archlinux.org/index.php/bash#Line_wrap_on_window_resize)
* [sudo: use wheel group](https://wiki.archlinux.org/index.php/sudo)
* [avahi: hostname resolution](https://wiki.archlinux.org/index.php/Avahi#Hostname_resolution)

## Configuration (server)

* SSH (`PermitRootLogin`)
* MySQL (`/usr/bin/mysql_secure_installation`)
* PostgreSQL
* PHP (php-fpm, php-gd, php-intl, php-sqlite, php-tidy, php-xsl)
* Nginx
* [PhpMyAdmin](https://wiki.archlinux.org/index.php/PhpMyAdmin#Nginx_Configuration) (il faut que `/etc/webapps/` soit dans `open_basedir` de `php.ini` pour que `AllowNoPassword = true` soit pris en compte)

## Tips

```bash
# update
sudo paman -Syu
yaourt -Syu --devel --aur
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

## useful package

* gnome-system-monitor
* gnome-system-log
* gnome-search-tool
* nautilus-open-terminal
* gcalctool
* mlocate (for locate and updatedb)
* dnsutils (for host)
* whois

## En vrac

### Utiliser le protocole Zerogroup/Bonjour/Personnes de proximité

(Attention, c'est le *souk* ici)

sur le RPI :
```bash
pacman -S avahi nss-mdns
systemctl restart dbus
systemctl start dbus
systemctl enable dbus
```

NB : La dernière action suffit !! (sudo systemctl enable avahi-daemon)
* (Installer nss-mdns puis ajouter mdns4 à la liste des hosts dans le fichier /etc/nsswitch.conf)
* démarrer le deamon avahi-daemon

### Bumblebee et les mises à jours

```bash
sudo pacman -Rdd libgl
yaourt -S nvidia-utils-bumblebee
yaourt -S nvidia-bumblebee
sudo pacman -S libgl
```

⚠ La version compilée dont l'être sous le noyau lancé pour fonctionner.

Il faut lancer un jeu avec optirun (sinon c'est le même chipset graphique que pour le bureau).
Il est conseillé d'utiliser bbswitch, qui économise la batterie (éteint la carte graphique qui sinon tourne en continue!)
bbswitch doit être réinstaller à chaque mise à jour du noyau !

### Partage d'imprimantes (réseau local)

Passer par `system-config-printer`
(et non gnome-control-center qui ne fonctionne pas, même s'il propose de l'ajouter mais n'y arrive pas...)
avahi-daemon?

### Sans ifconfig, ni Networkmanager

```bash
ip link show
dhcpcd INTERFACE
```
