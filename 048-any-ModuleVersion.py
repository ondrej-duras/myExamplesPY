#!/bin/env python


ver=None
path=None
#module="colorama"  # Win32::Console::ANSI alternative
#module="pygame"    # PyGame.org
module="visual"    # VPython.org

try:     # skus nieco co mozno nedopadne dobre
  # takto to funguje tiez
  #import colorama as xmodule
  #ale takto do 'module' dame premennu
  xmodule = __import__(module)
except:  # tot sprav ak to dobre nedopadlo 
  ver = "missing"
else:    # alebo toto, ak to dobre dopadlo
  try:
    ver = str(xmodule.__version__)
  except:
    ver = 'Unknown'
  try:
    path = str(xmodule.__file__)
  except:
    path = 'Unknown'
  
finally: # 
  print "%s ........ %s at %s" % (module,ver,path)

