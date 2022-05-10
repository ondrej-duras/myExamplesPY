##!/usr/bin/env python2 ... :-) no
## py2hex 128* 
## copy 128* e:\
## then
## putty com9 (or chek with device manager) 115200 bps no parity 1stop bit
## :-)  print sends data to your PuTTY


from microbit import *
while(True):
  tt=temperature()
  print("micro:bit nameral teplotu %s'C" % (tt))
  display.scroll("%s'C " % (tt))
  sleep(500) # pol sekundy


