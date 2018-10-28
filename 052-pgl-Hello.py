#!/usr/bin/env python

# bud takto
# pip install .\pyglet-pyglet-4e4fcdf65724.zip
# alebo takto
# pip install pyglet
# ma to iba 5.5MB a ziadne zavislosti mimo OS.
# rozhranie v mnohom identicke s OpenGL
# dobra praca s mediami : jpg, mp3 ...


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

