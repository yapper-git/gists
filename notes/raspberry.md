# Raspberry Pi

## Installation

1. Download image of [Archlinux ARM for RPi](http://archlinuxarm.org/platforms/armv6/raspberry-pi)
2. Copy to the SD Card: `sudo dd bs=1M if=archlinux-hf-2013-07-22.img of=/dev/sdX`
3. Extend partition with gparted
4. Connect via ssh (username=root, password=root)
5. Update and configure

## Services

* NTP : ntp
* SSH : openssh
* Web : nginx (HTTP, HTTPS)
* SFTP : vsftpd
* GIT : git-daemon.socket

## Backup/Restore

```bash
sudo dd bs=1M if=/dev/sdX of=sdcard.img # Backup
sudo dd bs=1M if=sdcard.img of=/dev/sdX # Restore
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

## Problème DNS orange

* Installer le paquet `bind`
* Ajouter dans `/etc/named` une ligne contenant `"listen-on { 127.0.0.1; };"` dans la section `Options`
* Lancer (*start*) et activer (*enable*) le démon `named`
* Editer `/etc/resolv.conf` et mettre dedans `"nameserver 127.0.0.1"` (Perso, j'ai rajouté à la fin du fichier /etc/dhcpd.conf la ligne suivante "nohook resolv.conf") (essayer avec /etc/resolv.conf.tail|head)
* Faire un `sudo chmod g+w /var/named` si `systemctl status named` affiche du rouge :)
* Pour networkmanager (pas sur mon RPi qui utilise dhcp), créer un fichier exécutable(!) dans `/etc/Networkmanager/dispatcher.d/` contenant : `cp -f /etc/resolv.conf.myDNSoverride /etc/resolv.conf`
