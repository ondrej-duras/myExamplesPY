#!/usr/bin/env python2

from microbit import *

HODINY=[Image.CLOCK12,
        Image.CLOCK1,Image.CLOCK2,Image.CLOCK3,Image.CLOCK4,
        Image.CLOCK5,Image.CLOCK6,Image.CLOCK7,Image.CLOCK8,
        Image.CLOCK9,Image.CLOCK10,Image.CLOCK11,Image.CLOCK12]

display.scroll("Kalibrujem")
compass.calibrate()
display.show(Image.HAPPY)


while True:
  xx = compass.heading()
  ss = "<" + str(xx) + ">"
  hh = (( 360 - xx ) // 30 ) % 12
  display.scroll(xx)
  display.show(HODINY[hh])
  sleep(3000)

# --- end ---

