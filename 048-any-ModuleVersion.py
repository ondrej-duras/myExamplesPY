#!/bin/env python


ver=None
path=None
module="colorama"

try:     # skus nieco co mozno nedopadne dobre
  # takto to funguje tiez
  #import colorama as xmodule
  #ale takto do 'module' dame premennu
  xmodule = __import__(module)
except:  # tot sprav ak to dobre nedopadlo 
  ver = "missing"
else:    # alebo toto, ak to dobre dopadlo
  ver = str(xmodule.__version__)
  path= str(xmodule.__file__)
finally: # 
  print "%s ........ %s at %s" % (module,ver,path)

