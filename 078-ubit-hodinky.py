#!/usr/bin/env python2

from microbit import *

ALL_CLOCKS=[Image.CLOCK1,Image.CLOCK2,Image.CLOCK3,Image.CLOCK4,
            Image.CLOCK5,Image.CLOCK6,Image.CLOCK7,Image.CLOCK8,
            Image.CLOCK9,Image.CLOCK10,Image.CLOCK11,Image.CLOCK12]

while True:
  for x in range(1,12,1):
    display.show(Image.ALL_CLOCKS[x])
    sleep(200)

# --- end ---

