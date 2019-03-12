#!/usr/bin/env python2

from microbit import *

# zobrazi jedno pismeno staticky bez scrollovania
display.show("Z")

# Podla manualu 2 sekundy cakania
sleep(2000)

# a zaverom maly obrazok v tvare domceka
A = Image("00500:05050:50005:50005:50005")
display.show(A)

# --- end ---

