#!/usr/bin/env python2

import colorama
colorama.init()

TEST_COLOR = """
#: debug 1
#: debug 2
#+ good 1
#+ good 2
#- wrong 1
#- wrong 2
#_ description 1
#_ description 2
"""

import re
def color(msg):
  #if not MODE_COLOR: return msg
  msg = re.sub(r"^(#:.*)$", "\033[1;34m\\1\033[m",msg,0,re.M)
  msg = re.sub(r"^(#-.*)$", "\033[1;31m\\1\033[m",msg,0,re.M)
  msg = re.sub(r"^(#\+.*)$","\033[1;32m\\1\033[m",msg,0,re.M)
  msg = re.sub(r"^(#_.*)$", "\033[1;36m\\1\033[m",msg,0,re.M)
  return msg

print color(TEST_COLOR)
