#!/usr/bin/env python

import random
from visual import *



imdata = materials.loadTGA("023-VPy-Baba3-Textura.tga")

tgrid = materials.texture(data=imdata,
                          mapping="sign",
                          interpolate=False)

body = [];
for z in range(0,9,1):
  body.append([])
  for x in range(0,9,1):
    body[z].append( vector(x/10.0,random.uniform(0.0,0.3),z/10.0) )

pole = [];
for z in range(0,8,1):
  for x in range(0,8,1):
    pole.extend( [ body[z][x], body[z][x+1], body[z+1][x], 
                   body[z+1][x], body[z][x+1], body[z+1][x+1] 
                 ])

#plachta = faces(pos = pole, material = materials.plastic, color = color.green, normal = vector(0,0.5,-0.3))
plachta = faces(pos = pole, material = tgrid, normal = vector(0,0.5,-0.3))
#plachta.make_twosided()






