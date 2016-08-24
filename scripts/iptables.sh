#!/bin/bash

[[ $EUID -ne 0 ]] && echo "root rights required" 2>&1 && exit 1



# Reset iptables
# ---------------------------------------------------------------------------- #

# set the default policy on the iptables to ACCEPT:
iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT

# then flush the rules:
iptables -F INPUT
iptables -F OUTPUT
iptables -F FORWARD


# INPUT CHAIN
# ---------------------------------------------------------------------------- #

iptables -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
iptables -A INPUT -i lo -j ACCEPT

iptables -A INPUT -p icmp -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
iptables -A INPUT -p tcp --dport 9418 -j ACCEPT

iptables -P INPUT DROP


# FORWARD CHAIN
# ---------------------------------------------------------------------------- #

iptables -P FORWARD DROP



# Save the configuration
# /!\ WARNING: Caution it saves the config! Reboot won't change something!
# ---------------------------------------------------------------------------- #

iptables-save > /etc/iptables/iptables.rules
