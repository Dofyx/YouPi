#!/bin/sh

vlc --extraintf --telnet --telnet-password you314 --telnet-host 127.0.0.1 --telnet-port 5824
python3 /home/pi/YouPi/webflask/youpi.py
