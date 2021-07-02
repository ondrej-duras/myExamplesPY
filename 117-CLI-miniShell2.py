#!/usr/bin/env python2

## MANUAL ############################################################# {{{ 1

VERSION = "2021.070201"
MANUAL  = """
NAME: Minimalistic Command-Line interpreter
FILE: mini.py

DESCRIPTION:
  It's a minimalistic commanline interpreter.

  Have a look in two variables inside this script
    -- BASE
    -- ELEMENTS
  Variable BASE represents a grammar of your on-demand language
  which you can improve simply on daily basis.
  Variable ELEMENTS lists the build elements of your language grammar.

VERSION: %s
""" % (VERSION)

####################################################################### }}} 1
## BASE ############################################################### {{{ 1

BASE = """
# Co je za mriezkou, to sa preskakuje
# co je za bodkou, to sa zobrazi ako banner k danej polozke
# match je regularny vyraz rozsireny o vyznamove znaky
#  - samostatne stojacej hviezdicky ako volitelneho parametra 
#  - percento ako povinny parameter

. Test sekvencie
match straka 2
  host straka jedna
  host straka dva

. STRAKA - RPi3BP LABova hopina
. funguju regularne vyrazy ?
match (straka|vrana)
  host 10.8.110.170 C-986-BA-RPI-01

. tu jeden povinny parameter
match straka %
  ssh 10.8.110.170 C-986-BA-RPI-01
    

. sekundarny host v LABe
. test volitelneho parametra
match malina *
  host 10.8.110.173 malina 
 
. trocha muziky
. Jean Michael Jarre
. elektronicka hudba
match jarre *
  link http://youtube.com

. test dvoch povinnych parametrov
match duo % %
  link jeden druhy
"""

####################################################################### }}} 1
## MINISHELL ########################################################## {{{ 1

import sys
import re

def doTest(command,params):
  print "#TEST COMMAND: " + command
  print params
  print "#done."


ELEMENTS = {
"ssh"  : doTest,
"host" : doTest,
"link" : doTest
}

def miniExec(command,base = BASE):
  global CAPABILITIES
  COMMENT = ""
  FLAG = "none"
  for iline in base.splitlines():
    line=iline
    if re.match("\s*$", line): continue
    if re.match("\s*#", line): continue
    line=re.sub("#[^#]+$","",line)
    line=re.sub("^\s+","",line)
    line=re.sub("\s+$","",line)
    keyword=re.split("\s+",line)[0]
    pattern=re.sub("^"+keyword+"\s+","",line)
    pattern=pattern.replace(" *",r"(\s+\S+)?")
    pattern=pattern.replace(" %",r"\s+\S+")
    if keyword == "." :
       COMMENT += pattern + "\n"
       continue
    if keyword == "match":
       if FLAG == "found": return
       elif re.match(pattern+"$",command):
         FLAG="found"
         print COMMENT
         COMMENT=""
         continue
       else:
         FLAG="none"
         COMMENT=""
         continue
    if FLAG == "none" : continue
    try:
      parline=line+" "+command
      params = re.split("\s+",parline) 
      ELEMENTS[keyword](parline,params)
    except:
      print "Syntax error at '%s' !" % (iline)
      return

####################################################################### }}} 1
## MAIN ############################################################### {{{ 1

if __name__ == "__main__":
  cmd = " ".join(sys.argv[1:])
  #print cmd
  if cmd == "" : 
    print MANUAL
  else :
    miniExec(cmd,BASE)

####################################################################### }}} 1
