#!/usr/bin/env python2
# -*- coding: ascii -*-
#=vim high Comment ctermfg=brown

VERSION = "2021.031101"
MANUAL  = """
NAME: Simplified SSH Session with WLC
FILE: SSH-Session-crossPlatform.py

DESCRIPTION:
  Demonstrates how to work with network devices
  via SSH protocol.

SEE ALSO: https://github.com/ondrej-duras/

VERSION: %s
""" % (VERSION)

import sys
import os
import time
import getpass


try:
  from pwa import *
except:
  def pwaLogin(cred):
    return raw_input("Login("+cred+")> ")
  
  def pwaPassword(cred):
    return getpass.getpass("Passw("+cred+")> ")

# this is for standard SSH implementation
def sshExec(host,cred,action):
  # collecting session details
  user=pwaLogin(cred)
  pasw=pwaPassword(cred)

  # Opening and authenticating the SSH session with the WLC
  if sys.platform == "win32":
    command="plink.exe -no-antispoof -batch -ssh -l %s -pw \"%s\" %s" % (user,pasw,host)
  else:
    command="sshpass -p \"%s\" ssh -tt -o StrictHostKeyChecking=no -l %s %s" % (pasw,user,host)

  stdin,stdout = os.popen4(command)
  stdin.write("terminal length 0\r")
  stdin.write(action + "\r")
  stdin.write("exit\r")

  stdin.close()             # that point realy starts the session
  data=stdout.read()        # read everything in single string
  stdout.close()            # closing SSH session
  return data


# this is for old Cisco AIR-CT55xx wireless lan cotrollers or some other devices
# where is authentication method = "none" 
def wlcExec(host,cred,action):
  # collecting session details
  user=pwaLogin(cred)
  pasw=pwaPassword(cred)

  # Opening and authenticating the SSH session with the WLC
  if sys.platform == "win32":
    command="plink.exe -no-antispoof -batch -ssh -l %s %s" % (user,host)
  else:
    command="ssh -tt -o StrictHostKeyChecking=no -o KexAlgorithms=+diffie-hellman-group1-sha1 -l %s %s" % (user,host)
  stdin,stdout = os.popen4(command)
  stdin.write(user + "\r") # login is provided twice ... :-)
  stdin.write(pasw + "\r") # password (authentication method=none, then chat
  stdin.write("config paging disable\r") # disabling --more--

  # Pushing activity
  # stdin.write("show sysinfo\r")   # AirOS version
  # stdin.write("show inventory\r") # Harware inventory
  stdin.write(action + "\r")     # or anything else

  # Logout and session termination
  stdin.write("logout\r")   # command to exit
  stdin.write("N\n")        # do not write configuration
  stdin.close()             # that point realy starts the session
  data=stdout.read()        # read everything in single string
  stdout.close()            # closing SSH session
  return data



if __name__ == "__main__":
  print("1 - IOS/IOS-XE/IOS-XR/NX-OS")
  print("2 - Air-OS")
  opt  = raw_input("1/2?>> ").strip()
  host = raw_input("host>> ").strip()
  comd = raw_input("comd>> ").strip()
  
  if opt == "2":
    print(wlcExec(host,"user",comd))
  else:
    print(sshExec(host,"user",comd))

# --- end ---
