#!/usr/bin/env python

from visual import *
checkerboard = ( (0,1,0,1),
                 (1,0,1,0),
                 (0,1,0,1),
                 (1,0,1,0) )

tex = materials.texture(data=checkerboard,
                     mapping="rectangular",
                     interpolate=False)

box(pos= vector(1,1,1), axis=(0,0,1), color=color.cyan, material=tex)


