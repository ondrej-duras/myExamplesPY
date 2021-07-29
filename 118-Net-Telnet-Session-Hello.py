#!/usr/bin/env python
# 20210729, Ondrej DURAS (dury)
# Very basic Telnet session
# 1st - uses raw strings
# 2nd - uses sets of regular expressions
# to identify the prompt (end of command output)
#


import getpass
import sys
import os
import telnetlib


HOST="VALM-SW-01"
try:
  USER=os.environ["SSHUSER"]
except:
  pass

if not USER:
  if sys.version_info[0] == 2:
    USER = raw_input("Login: ")
  else:
    USER = input("Login: ")

PASS=getpass.getpass("Password[%s]: " % USER)


tel = telnetlib.Telnet(HOST,23,10) # 23/tcp,10sec.
tel.read_until("Username: ")
tel.write(USER + "\r\n")
tel.read_until("Password: ")
tel.write(PASS + "\r\n")
print(tel.read_until(HOST+"#",10)) # sent command in echo

tel.write("terminal length 0\r\n")
print(tel.read_until(HOST+"#",10))

tel.write("show int status\r\n")
#print tel.read_all()
#print tel.expect(["^"+HOST+"#"],10)[2].replace(r"\r\n","\n")
print(tel.read_until(HOST+"#",10))

tel.write("show mac address-table\r\n") # command
#print tel.expect(["^"+HOST+"#"],10)[2].replace(r"\r\n","\n")
print(tel.read_until(HOST+"#",10))
#print tel.read_until(HOST+"#",10)

#print tel.read_until(HOST+"#",10)
tel.write("exit\r\n")
tel.close()

# ------
print "#"*70

# Opening and Authenticating a session
tel = telnetlib.Telnet(HOST,23,10)
tel.expect(["[Ll]ogin: ?","[Uu]ser(name)?: ?"],15)
tel.write(USER + "\r\n")
tel.expect(["[Pp]assword: ?"],15)
tel.write(PASS + "\r\n")
tel.expect([""+HOST+"#"],10)

tel.write("terminal length 0\r\n")
print(tel.expect([""+HOST+"#"],10)[2].replace(r"\r\n","\n"))

tel.write("show int status\r\n")
print(tel.expect([""+HOST+"#"],10)[2].replace(r"\r\n","\n"))

tel.write("show mac address-table\r\n")
print(tel.expect([""+HOST+"#"],10)[2].replace(r"\r\n","\n"))
#print tel.expect([""+HOST+"#"],10)[2].replace(r"\r\n","\n")


tel.write("exit\r\n")
tel.close()

# --- end ---

