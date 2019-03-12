#!/usr/bin/env python2

# Skusame tlacitka 

from microbit import *

while True:
  a = button_a.is_pressed()
  b = button_b.is_pressed()
  if a and b:
    display.show("X")
  elif a:
    display.show("A")
  elif b:
    display.show("B")
  else:
    display.show("-")
  sleep(200)

# --- end ---
 
