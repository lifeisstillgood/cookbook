#!/bin/sh

### pbrian - fixes to make using my local network better

echo "domain	home.paul-brian.com" > /etc/resolv.conf
echo "nameserver      192.168.1.20" >> /etc/resolv.conf
echo "nameserver	195.74.113.58" >> /etc/resolv.conf


