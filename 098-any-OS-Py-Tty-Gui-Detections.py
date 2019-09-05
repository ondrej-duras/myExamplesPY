#!/usr/bin/env python2

import os
import sys
import re

# Win32(x64) - tested
# Linux(RPi) - tested
# sunos5     - tested


# OS detection
class osDetect():
  VERSION= "2019.090401"
  detail = "UNKNOWN"
  short  = "unknown"
  unix   = True
  gui    = False
  python = 0  # 2 or 3
  tty    = True
  colors = False  # TTY colors

  def __init__(self):
    if sys.version_info[0] < 3:
      self.python = 2
    else:
      self.python = 3

    if sys.stdout.isatty():
      self.tty = True
    else:
      self.tty = False
      self.colors = False

    if re.match("^win",sys.platform):
      self.detail = "Windows(" + str(sys.platform) +")"
      self.short  = "windows"
      self.unix   = False
    
    if re.match("^sun",sys.platform):
      self.detail = "Solaris(" + str(sys.platform) + ")"
      self.short  = "solaris"
    
    if re.match("^hp-ux",sys.platform):
      self.detail = "HP-UX(" + str(sys.platform) + ")"
      self.short  = "hp-ux"
    
    if re.match("^freebsd",sys.platform):
      self.detail = "FreeBSD(" + str(sys.platform) + ")"
      self.short  = "freebsd"
    
    if re.match("^darwin",sys.platform):
      self.detail = "MacOSX(" + str(sys.platform) + ")"
      self.short  = "mac"
    
    if re.match("lin",sys.platform):
      ANDROCT = 0
      for var in os.environ:
        if re.match("^ANDROID",var): ANDROCT += 1
      if ANDROCT < 5 :
        self.detail = "Linux(" + str(sys.platform) + ")"
        self.short  = "linux"
      else :
        self.detail = "Android(" + str(sys.platform) + ")" + str(ANDROCT)
        self.short  = "android"


    # TTY Colors Detection
    if self.tty:
      if self.unix: 
        self.colors = True
      else:
        try:
          import colorama
          colorama.init()
          self.colors = True
        except:
          self.colors = False

    # GUI Detection
    # ... windows may also run scripts via 
    # WinRM, RMI or SSH where is no GUI
    try:
      if sys.version_info[0] < 3:
        import Tkinter
        wh = Tkinter.Tk()
      else:
        import tkinter
        wh = tkinter.Tk()
      self.gui = True
    except:
      self.gui = False
   

if __name__ == "__main__":
  for arg in sys.argv:
    print "cli parameter ..... %s" % (arg)
  x=osDetect()
  print   "python ............ %s" % str(x.python)
  print   "short ............. %s" % (x.short)
  print   "detail ............ %s" % (x.detail)
  print   "unix .............. %s" % str(x.unix)
  print   "tty ............... %s" % str(x.tty)
  print   "tty colors ........ %s" % str(x.colors)
  print   "gui ............... %s" % str(x.gui)
  
# --- end ---


