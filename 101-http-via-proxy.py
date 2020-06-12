#!/usr/bin/env python2

"""
Description:
 Example how to access outside world from
 corporation via proxy.
 An issue is a 'requests' package as it is
 not python2 native.
"""


import requests
import getpass

from requests.auth import HTTPProxyAuth

user = getpass.getuser()
pasw = getpass.getpass("Password(%s):" % (user))
proxies = {"http":"10.0.0.1:80"}
auth = HTTPProxyAuth(user,pasw)

http = requests.get("http://www.google.com/", proxies=proxies, auth=auth)
print http.text


# --- end ---

