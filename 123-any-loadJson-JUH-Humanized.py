#!/usr/bin/env python2

import re
import json

# loads humanized .json
# "humanized" means it may contain some comments
def loadJson(fname):
  fh = open(fname,"r")
  text1 = fh.read()
  text2 = ""
  fh.close()
  for line in text1.splitlines():
    if re.match(r"\s*#",line): continue
    line = re.sub(r'#[^"]+$','',line)
    text2 += line + "\n"
  return json.loads(text2)


juh = loadJson("08-config.juh")
print(json.dumps(juh, sort_keys=True,indent=2,separators=(',',':')))
   
