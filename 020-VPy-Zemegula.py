#!/usr/bin/env python

from visual import *

G1 = sphere( pos = vector(1,1,1), material = materials.earth )

for i in range(1,130,1):
  rate(40)
  G1.pos = vector(1,1,i)

for i in range(130,1,-1):
  rate(40)
  G1.pos = vector(1,1,i)

exit()

