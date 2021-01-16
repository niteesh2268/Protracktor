#!/bin/bash
sudo pip3 install python3-xlib
sudo apt-get install scrot
sudo apt-get install python3-tk
sudo apt-get install python3-dev
sudo pip3 install -r requirements.txt
sudo apt-get install python3.6
sudo apt-get install xdotool
sudo apt-get install nethogs
sudo setcap "cap_net_admin,cap_net_raw=ep" /usr/sbin/nethogs

