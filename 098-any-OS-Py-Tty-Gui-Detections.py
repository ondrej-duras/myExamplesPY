#!/usr/bin/env python2

import os
import sys
import re
import platform

# Win32(x64) - tested
# Linux(RPi) - tested
# sunos5     - tested


# HW,OS,TTY and GUI detection
class myPlatform():
  VERSION= "2019.090502"
  detail = "UNKNOWN"
  short  = "unknown"
  unix   = True
  gui    = False
  python = 0  # 2 or 3
  tty    = True
  colors = False  # TTY colors
  bit    = 32
  text   = "" # getText() call first

  def __init__(self):
    if sys.version_info[0] < 3:
      self.python = 2
    else:
      self.python = 3

    (x,y) = platform.architecture()
    if (x == "64bit"):
      self.bit = 64

    if sys.stdout.isatty():
      self.tty = True
    else:
      self.tty = False
      self.colors = False

    if re.match("^win",sys.platform,re.IGNORECASE):
      self.detail = "Windows(" + str(sys.platform) +")"
      self.short  = "windows"
      self.unix   = False
    
    if re.match("^sun",sys.platform,re.IGNORECASE):
      self.detail = "SunSolaris(" + str(sys.platform) + ")"
      self.short  = "sun"
    
    if re.match("^hp-ux",sys.platform,re.IGNORECASE):
      self.detail = "HP-UX(" + str(sys.platform) + ")"
      self.short  = "hp-ux"
    
    if re.match("^freebsd",sys.platform,re.IGNORECASE):
      self.detail = "FreeBSD(" + str(sys.platform) + ")"
      self.short  = "freebsd"
    
    if re.match("^darwin",sys.platform,re.IGNORECASE):
      self.detail = "MacOSX(" + str(sys.platform) + ")"
      self.short  = "mac"
    
    # Linux like systems Linux86 / Linux64 / android / 
    if re.match("^lin",sys.platform,re.IGNORECASE):
      ANDROCT = 0
      self.detail = "Linux(" + str(sys.platform) + ")"
      self.short  = "linux"
      for var in os.environ:
        if re.match("^ANDROID",var): ANDROCT += 1
      if ANDROCT > 4 :
        self.detail = "Android(" + str(sys.platform) + ")" + str(ANDROCT)
        self.short  = "android"
      try:
        fh = open("/sys/firmware/devicetree/base/model","r")
        rpi_text = fh.read()
        fh.close()
        #print rpi_text
        rpi_split= rpi_text.split()
        if re.match("^Raspberry Pi [0-9]+ Model.*",rpi_text):
          self.short = "rpi"
          self.detail ="RPi"+str(rpi_split[2])+str(rpi_split[4])
          if rpi_split[5] == 'Plus':
             self.detail += "P"
          self.detail += "(" + sys.platform + ")"
      except:
        pass

    if self.short == "unknown":
      try:
        x = sys.uname()
        self.detail = str(x[0])
        self.short  = self.detail
      except:
        pass

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
 

  def getText(self): 
    text =  ""
    text += "python ............ %s\n" % str(self.python)
    text += "short ............. %s\n" % (self.short)
    text += "detail ............ %s\n" % (self.detail)
    text += "unix .............. %s\n" % str(self.unix)
    text += "tty ............... %s\n" % str(self.tty)
    text += "tty colors ........ %s\n" % str(self.colors)
    text += "gui ............... %s\n" % str(self.gui)
    self.text = text
    return text

if __name__ == "__main__":
  for arg in sys.argv:
    print "cli parameter ..... %s" % (arg)
  print myPlatform().getText()

# --- end ---


