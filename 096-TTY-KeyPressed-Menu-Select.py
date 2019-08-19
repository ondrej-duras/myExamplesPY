#!/usr/bin/env python2
# 096-TTY-KeyPressed-Menu-Select.py - /// once... simple UDP Echo server - multisocket/onethread
# 20190819, Ing. Ondrej DURAS (dury)

## MANUAL ############################################################# {{{ 1

VERSION = 2019.081901
MANUAL  = """
NAME: CrossPlatform script controll library
FILE: 096-TTY-KeyPressed-Menu-Select.py

DESCRIPTION:
  Small collection of functions for script controll.
  These functions provide Input/Output interface simulating:
   - 16x2 characters of I2C LED display
   - 5 buttons connected via I2C (arrows, enter and escape key on keyboard)
   - RGB LED connected via I2C (here as a text notice only)
   - or strip of 8 simple LEDs connected to GPIO PINs

  as same as known shields for raspberry pi.
  https://www.gme.sk/raspberry-shiled-s-lcd-16x2-tlacitky-a-rgb-led
  https://www.gme.sk/data/attachments/dsh.769-403.1.pdf

  For now tested on RPi/ssh and on Win7 terminal.
  

NOTE:
 a script for my RPi scripts, nothing else.
 Needed for my network LAB.
 Development still in progress :-)

"""
####################################################################### }}} 1
## DEFAULTS & INIT #################################################### {{{ 1
import sys
import os
import re


MODE_COLOR = 2  # Terminal Colors 0=disabled 1=enabled 2=ToBeDiscussed
# CrossPlatform Win32::Console::ANSI
# We use terminal for output (LCD is intended for further use)
if sys.platform == "win32":
  try:
    import colorama
    colorama.init()
    MODE_COLOR = 1
  except:
    MODE_COLOR = 0

####################################################################### }}} 1
## keyPressed() ####################################################### {{{ 1

"""
PROTOTYPE:
  code = keyPressed()

PARAMETERS:
  none

RETURNS:
  code - ascii of returned keystroke.

  When OS returns a sequece of codes,
  then a function must be called multiple times, where
  each time it returns a single one of codes in sequence.

DESCRIPTION:
  function returns an ASCII of stroked key.
  If nothing is actually pressed, then it returns 0 (zero).
  Function is platform independent (tested on Windows,Linux,MacOSX).
  Function keyPressed() flushes pressed code from input queue.

ISSUES:
  Function acts platform independent for standard ASCII codes only.
  For Escape key "Esc", or Functional keys (F1 .. F12) or arrow keys
  its behaviour is platform dependent for now.

"""


# CrossPlatformovy test, ci je stlacena klavesa
# ak stlacena je, tak vrati jej asci hodnotu ako cislo
# ak nieje, potom vrati cislo nula


try:
    import msvcrt
    def keyPressed():
        x = msvcrt.kbhit()
        if x:
           return ord(msvcrt.getch())
        else:
           return 0
   
except ImportError:
    import termios, fcntl  #, sys, os  - defined at begin
    def keyPressed():
        fd = sys.stdin.fileno()
        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
        try:
            while True:
                try:
                    code = ord(sys.stdin.read(1))
                    #return True
                    return code
                except IOError:
                    return 0
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)


def keyPressed_test():
  NEXT = True
  print "Test of 'keyPressed()'"
  print "Press Esc or 'q' to quit"
  while NEXT:
    code = keyPressed()
    if not code: continue
    print "pressed '%s' (%u)" % (chr(code),code)
    if code == 27  : NEXT=False  # Esc
    if code == 113 : NEXT=False  # 'q'
    if code == 81  : NEXT=False  # 'Q'
  
if __name__ == "__main__":
  keyPressed_test()
    

####################################################################### }}} 1
## arrowPressed() ##################################################### {{{ 1

"""
PROTOTYPE:
  code = arrowPressed()

PARAMETERS:
  none

RETURNS:
  a string.
  if string is empty, then nothing has been pressed
  otherwise one of following values is returned:
  "stop"  - when Esc or 'Q' has been pressed -> intended for termination
  "enter" - when enter has been pressed -> intended for selection
  "up"    - when UP arrow has been pressed -> intended for move in menu options 
  "down"  - when DOWN arrow has been pressed -> intended for move in menu options 
  "right" - when RIGHT arrow has been pressed -> intended for move in submenu options 
  "left"  - when LEFT arrow has been pressed -> intended for move in submenu options 

"""

def arrowPressed():
  code = keyPressed()
  if code == 0:     return ""      # none key pressed
  if code == 113:   return "stop"  # odr('q') == 113
  if code == 81:    return "stop"  # odr('Q') == 81
  if code == 107:   return "up"    # ord('k') == 107 vi-UP
  if code == 106:   return "down"  # ord('j') == 106 vi-down
  if code == 108:   return "right" # ord('l') == 108 vi-right
  if code == 104:   return "left"  # ord('h') == 104 vi-left  
  if code == 13:    return "enter" # enter pressed on windows
  if code == 10:    return "enter" # enter pressed on all unix platforms

  # windows platform
  if sys.platform == "win32":
    if code == 27:  return "stop"
    if code == 224:
      code = keyPressed()
      if code == 72: return "up"
      if code == 80: return "down"
      if code == 77: return "right"
      if code == 75: return "left"
    return ""
 
  # all unix platforms
  else:
    if code == 27:
      code = keyPressed()
      if code == 0:  return "stop"
      if code <> 91: return ""
      code = keyPressed()
      if code == 65: return "up"
      if code == 66: return "down"
      if code == 67: return "right"
      if code == 68: return "left"
    return "" 
 

def arrowPressed_test():
  print "Test of 'arrowPressed()'"
  print "Press Esc or 'q' to quit"
  FFLAG = True
  while FFLAG:
    code = arrowPressed()
    if not code: continue
    print code
    if code == "stop": FFLAG = False; break
    
if __name__ == "__main__":
  arrowPressed_test()


####################################################################### }}} 1
## arrowMenu() ######################################################## {{{ 1

def arrowMenu(name,items):
  position = 0
  number   = len(items)
  if number == 0: return ""
  #      1234567890123456  (LCD display width)
  EMPTY="                "
  FFLAG = True
  while FFLAG:
    print """%s[%s]\015""" % (str(name),(str(items[position]) + str(EMPTY))[0:16]),
    code = arrowPressed()
    if (code == "up")   and (position > 0):          position=position-1; continue
    if (code == "down") and (position < (number-1)): position=position+1; continue
    if (code == "enter"):  FFLAG=False;
    if (code == "stop"):   return "";
  return items[position]


def arrowMenu_test():
  code = arrowMenu("My Menu:",["First","Second","Third","12345678901234567"])
  print "Your option is \"%s\"" % (code)

if __name__ == "__main__":
  arrowMenu_test()

####################################################################### }}} 1
## arrowSubMenu() ##################################################### {{{ 1

def arrowSubMenu(name,items):
  position = 0
  number   = len(items)
  if number == 0: return ""
  #      1234567890123456  (LCD display width)
  EMPTY="                "
  FFLAG = True
  while FFLAG:
    print """%s[%s]\015""" % (str(name),(str(items[position]) + str(EMPTY))[0:16]),
    code = arrowPressed()
    if (code == "left")   and (position > 0):          position=position-1; continue
    if (code == "right")  and (position < (number-1)): position=position+1; continue
    if (code == "enter"):  FFLAG=False;
    if (code == "stop"):   return "";
  return items[position]


def arrowSubMenu_test():
  code = arrowSubMenu("My SubMenu:",["First","Second","Third","12345678901234567"])
  print "Your option is \"%s\"" % (code)

if __name__ == "__main__":
  arrowSubMenu_test()

####################################################################### }}} 1
# --- end ---
