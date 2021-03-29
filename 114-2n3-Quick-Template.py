#!/usr/bin/env python
# 20210329, Ondrej DURAS (dury)
# Both Python v2 and v3 compatible

## CONFIG ############################################################# {{{ 1

CONFIG="""
<AA> aaaaaaaaaaa
<BB> bbbbbbbbb   # bbbbbbbbb  # fojwiofiwoerj
<CC> ccccccccccc
#<!DATE> datetime.date.today().strftime("%Y-%m-%d") 
<!DATE> datetime.datetime.now().strftime("%Y-%m-%d")  # nejaky pokec
"""

####################################################################### }}} 1
## TEMPLATE ########################################################### {{{ 1

TEMPLATE="""
iqwejrfiojr <AA> ijriofjer <AA>
hwefowe <BB> iuefiou <BB>
237tr8237 <CC> uy4uiofg34ui <CC>
<!DATE>
"""

####################################################################### }}} 1
## PYCODE ############################################################# {{{ 1

import datetime
import re

def learnItems(src):
  out={}
  for aline in src.splitlines():
    line = re.sub("#[^#]+$","",aline)
    if not re.match("\S+\s+\S+",line): continue
    (item,value) = re.split("\s+",line,1)
    # print "'%s' == '%s'" % (item,value) #DEBUG
    out[item] = value
  return out


def replaceItems(text,source):
  if isinstance(source,str): src=learnItems(source)
  elif isinstance(source,dict): src=source
  else: print("Error !")
  out=text
  for item in src.keys():
    if item[0:2] == "<!": value=eval(src[item])
    else: value = src[item]
    out = out.replace(item,value)
  return out


if __name__ == "__main__":
  # print replaceItems(TEST,learnItems(DEF)) # works too
  print(replaceItems(TEMPLATE,CONFIG))  # this is more simple
  

####################################################################### }}} 1
# --- end ---
