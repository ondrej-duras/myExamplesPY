#!/usr/bin/env python

import colorama
import random

colorama.init()

for i in range(30):
  cislo = random.randint(10,90)
  farba = random.randint(30,37)
  hlaska = "\033[1;%smVymyslel som cislo ....  %s" % (farba,cislo)
  print hlaska










