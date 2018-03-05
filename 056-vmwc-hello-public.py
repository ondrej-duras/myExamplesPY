#!/usr/bin/env python
# instalacia balicka:
# pip install --trusted-host pypi.python.org vmwc
# Popis API
# https://pypi.python.org/pypi/vmwc/1.0.2

import os
import getpass
from vmwc import VMWareClient

host = 'vcenter.domain.com'
myvm = 'my_server'
username = os.getenv('USERNAME','')
password = getpass.getpass("Password:")


if not (username and password):
  print "Login or password !"
  exit() 

with VMWareClient(host, username, password) as client:
    for vm in client.get_virtual_machines():
        if vm.name == myvm: 
          print "%s ... starting." % (myvm)
          vm.power_on()
        else:
          print "%s .... found" % (vm.name)

