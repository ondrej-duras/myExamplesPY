#!/usr/bin/env python2

import random
import pyglet

window = pyglet.window.Window(width=700,height=500,caption="Lines")

@window.event
def on_draw():
    pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

    howmany=i=100
    coords=[];colors=[]
    while i>0:
        x  =random.randint(0,700); y  = random.randint(0,500)
        x2 =random.randint(0,700); y2 = random.randint(0,500)
        coords.append(x); coords.append(y); coords.append(x2); coords.append(y2)
        c=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        c2=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        for cx in c:  colors.append(cx)
        for cx in c2: colors.append(cx)
        i=i-1

    coords=tuple(coords)
    colors=tuple(colors)
    vertex_list=pyglet.graphics.vertex_list(howmany*2,('v2i', coords),('c3B', colors))
    vertex_list.draw(pyglet.gl.GL_LINES)

@window.event
def on_move(x,y):
  on_draw()

#pyglet.clock.set_fps_limit(10)
#pyglet.clock.schedule_interval(on_draw, 0.5)
pyglet.app.run()
