#!/usr/bin/env python

import pyglet

window = pyglet.window.Window()
image  = pyglet.resource.image('030-PyG-Chalupa5.jpg')

@window.event
def on_draw():
  window.clear()
  image.blit(0,0)

@window.event
def on_key_press(symbol,modifiers):
  print 'A key pressed '+str(symbol)+' modif '+str(modifiers) 

pyglet.app.run()

