#!/usr/bin/env python
# 047-CLI-ipka.py / ipka.py / ipka - IP address calculator & library
# 20170707, Ing. Ondrej DURAS (dury)

## MANUAL ############################################################# {{{ 1

VERSION = 2017.070701
MANUAL  = """
NAME: IPka
FILE: ipka.py

DESCRIPTION:
  IPka is an simplified IP address calculator.
  ipka.py also provides a set of function usefull 
  for IP address translations

SYNTAX:
  ipka <IPaddress>/<Mask>

USAGE:
  ipka 1.2.3.4/24 2.3.4.5/27 3.4.5.6/255.255.255.192

PARAMETERS:
  IPaddress - Any IPv4 address (Unicast/Network/Broadcast...)
  Mask      - network mask, /xx or /x.x.x.x format

SEE ALSO:
  https://github.com/ondrej-duras/

VERSION: %s
""" % (VERSION)

####################################################################### }}} 1
####################################################################### {{{ 1

import sys
import os
import re

IPS = []  # List of IP/MASK parameters taken from the command-line
MODE_DEBUG = "" # filter for debugging messages

def debug(msg="DEBUG"):
  global MODE_DEBUG
  if not MODE_DEBUG : return
  if not re.match(MODE_DEBUG,msg) : return
  print "#: %s" % (msg)

def warn(msg="Warning !"):
  print "#- %s" % (msg)

def die(msg="Error !",code=1):
  warn(msg)
  sys.exit(code)

def isIP(ip):
  if re.match("^[0-9]{1,3}(\.[0-9]{1,3}){3}$",ip)        : return 1;
  if re.match("^[0-9]{1,3}(\.[0-9]{1,3}){3}/[0-9]+$",ip) : return 2;
  if re.match("^[0-9]{1,3}(\.[0-9]{1,3}){3}/" + 
               "[0-9]{1,3}(\.[0-9]{1,3}){3}$",ip)        : return 3;
  return 0;

def interface():
  global IPS, MODE_DEBUG
  if not len(sys.argv)-1:
    print MANUAL
    sys.exit(0)
  for idx in range(1,len(sys.argv),1):
    argx = sys.argv[idx]
    debug("argv %u : %s" % (idx,argx))
    if isIP(argx) : IPS.append(argx); continue
    if re.match("^-+v",argx) : MODE_DEBUG = ".*"; continue
    warn("Bad argument (%s) !" % argx)

def main():
  interface()
  sys.exit(0)

####################################################################### }}} 1
if __name__ == "__main__" : main()

