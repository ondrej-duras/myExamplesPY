#!/usr/bin/env python

import pyglet

window = pyglet.window.Window(width=700, height=500, fullscreen=False, caption="Hello")
#label = pyglet.text.Label('Hello world !', font_name='Time New Roman', font_size = 36)
label = pyglet.text.Label('Hello world !', font_name='Courier New', font_size = 36, x=10, y=50, color=(128,128,0,50))

@window.event
def on_draw():
  window.clear()
  pyglet.graphics.draw(4,pyglet.gl.GL_LINES,
    ('v2i',(10,10,700,500, 30,500,550,0)),
    ('c3B',(0,0,255, 0,255,0, 255,0,0, 255,255,0))
  )
 
  pyglet.graphics.draw(6,pyglet.gl.GL_TRIANGLES,
    ('v2i',(
       40,140, 80,220, 200,150,
       350,170, 400,400, 550,300
    )),
    ('c3B',(0,0,255, 0,255,0, 255,0,0,
            255,255,0, 255,0,255, 0,255,255
    ))
  )
  label.draw()

@window.event
def on_move(x,y):
  on_draw()

@window.event
def on_mouse_motion(x,y,dx,dy):
  on_draw()

#window.push_handlers(on_draw)
pyglet.app.run()

