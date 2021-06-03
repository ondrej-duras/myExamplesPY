#!/usr/bin/env python2
#=vim high Comment ctermfg=brown

import re

def txtMatch(pat,txt,empty=0):
  out=""
  for line in txt.splitlines():
    if empty and re.match("^\s*$",line): # includes empty lines (explicit option)
      out += line+"\n"
    if re.match(pat,line):   # includes lines matching pattern
      out += line+"\n"
  return out

def txtFilter(pat,txt,empty=1):
  out=""
  for line in txt.splitlines():
    if empty and re.match("^\s*$",line): continue # cuts out an empty lines (default option)
    if re.match(pat,line): continue  # filters out lines matching pattern
    out += line+"\n"
  return out


text="""
ahoj Janci
Janci cau
hello Jozi
ciao Adam
nazdar Janci
"""

if __name__ == "__main__":
  print "txtMatch"
  print txtMatch(".*Janci",text)
  print "\ntxtFilter"
  print txtFilter(".*Janci",text)

# --- end ---


