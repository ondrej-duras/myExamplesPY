#!/bin/env python


ver=None
path=None
module="colorama"

try:     # skus nieco co mozno nedopadne dobre
  import colorama as xmodule
except:  # tot sprav ak to dobre nedopadlo 
  ver = "missing"
else:    # alebo toto, ak to dobre dopadlo
  ver = str(xmodule.__version__)
  path= str(xmodule.__file__)
finally: # 
  print "%s ........ %s at %s" % (module,ver,path)

