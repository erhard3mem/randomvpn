#!/usr/bin/python3

from pathlib import Path
import random
import subprocess

p = Path('.');
l = list(p.glob('./vpn/*.ovpn'))
rnd = random.randint(0,len(l))
vpn = l[rnd]
subprocess.run(['sudo',"openvpn", str(vpn) ])
