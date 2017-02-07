#!/bin/env python

from visual import *

scene.title='Pokus otexturovat plochy'

imdata = materials.loadTGA("023-VPy-Baba3-Textura.tga")

tgrid = materials.texture(data=imdata,
                          mapping="sign",
                          interpolate=False)

sphere(pos = vector(-1,1,1), axis=(0,0,1), material = tgrid)

for a in range(0,100,1):
  rate(20)
  box(pos= vector(1,1,1), axis=(0,0,0.5), material = tgrid)

exit()


