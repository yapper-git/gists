# Raspberry Pi

## Installation

- Follow installation instructions from [Archlinux ARM](http://archlinuxarm.org/platforms/armv7/broadcom/raspberry-pi-2).
- Handle users and root access
    - Create new users (in `wheel` group if needed) with `useradd -m -G wheel -s /bin/bash [username]`
    - Set passwords using `passwd` command
    - Remove `alarm` user with `userdel -r alarm`
- Update, then install some packages
    - base-devel git rsync unzip screen pkgfile bash-completion mlocate dnsutils whois imagemagick
    - vim emacs-nox
    - lilypond texlive-most
    - nginx
    - mariadb
    - php php-fpm
    - python3 python-pip python-virtualenv python-jinja uwsgi-plugin-python
- Configure `php-fpm` to store errors (set `catch_workers_output = yes` in `php-fpm.conf`)
- Add SSL certificate

## Services

- SSH : openssh
- HTTP(S) : nginx
- SQL : mariadb (ou postgresql)
- GIT : git-daemon.socket (gitolite?)
- SFTP : vsftpd
- NTP : ntp

## Backup/Restore (obsolete)

```bash
sudo dd bs=1M if=/dev/sdX of=sdcard.img # Backup
sudo dd bs=1M if=sdcard.img of=/dev/sdX # Restore
```

## OpenSSL

```bash
# Create 1 year self-signed certificate (and key)
# http://conshell.net/wiki/index.php/OpenSSL_usage_tips_and_examples
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout yvand.dtdns.net.key -out yvand.dtdns.net.crt
# Create 1 year self-signed certificate with existing key
openssl req -nodes -x509 -days 365 -new -key yvand.dtdns.net.key -out yvand.dtdns.net.crt

# Create self-signed certificate (you can change key size and days of validity)
openssl genrsa -des3 -out server.key 1024
openssl req -new -key server.key -out server.csr
cp server.key server.key.org
openssl rsa -in server.key.org -out server.key
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
```

## Repair

### Dirty bit (due to power cut)

```bash
sudo fdisk -l
sudo umount /dev/sdbX
sudo fsck -a /dev/sdbX
```

### SD Card read only

```bash
sudo mount -o remount,rw /
sudo systemctl --failed
sudo systemctl restart ...
```

### Problème DNS orange

- Installer le paquet `bind`
- Ajouter dans `/etc/named` une ligne contenant `"listen-on { 127.0.0.1; };"` dans la section `Options`
- Lancer (*start*) et activer (*enable*) le démon `named`
- Editer `/etc/resolv.conf` et mettre dedans `"nameserver 127.0.0.1"` (Perso, j'ai rajouté à la fin du fichier /etc/dhcpd.conf la ligne suivante "nohook resolv.conf") (essayer avec /etc/resolv.conf.tail|head)
- Faire un `sudo chmod g+w /var/named` si `systemctl status named` affiche du rouge :)
- Pour networkmanager (pas sur mon RPi qui utilise dhcp), créer un fichier exécutable(!) dans `/etc/Networkmanager/dispatcher.d/` contenant : `cp -f /etc/resolv.conf.myDNSoverride /etc/resolv.conf`
