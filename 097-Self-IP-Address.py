#!/usr/bin/python3
#!/usr/bin/env python2
# module for getting the lan ip address of the computer
#
# works on with python2 and python3
# source of example:
# https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
#

import sys   # for python version detection in two lines only
import os
import socket

if os.name != "nt":
    import fcntl
    import struct
    def get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # for Python2
        if sys.version_info[0] < 3:
          return socket.inet_ntoa(fcntl.ioctl(
                  s.fileno(),
                  0x8915,  # SIOCGIFADDR
                  struct.pack('256s', bytes(ifname[:15]))
              )[20:24])


        # for Python3
        else:
          return socket.inet_ntoa(fcntl.ioctl(
                  s.fileno(),
                  0x8915,  # SIOCGIFADDR
                  struct.pack('256s', bytes(ifname[:15], 'utf-8'))
                  # Python 2.7: remove the second argument for the bytes call
              )[20:24])


def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = ["eth0","eth1","eth2","wlan0","wlan1","wifi0","ath0","ath1","ppp0"]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break;
            except IOError:
                pass
    return ip



print (get_lan_ip())

# --- end ---
