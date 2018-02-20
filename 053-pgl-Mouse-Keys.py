#!/usr/bin/env python

import pyglet
from pyglet.window import key
from pyglet.window import mouse

window = pyglet.window.Window()
image  = pyglet.resource.image('030-PyG-Chalupa5.jpg')

# toto potrebuje FFmpeg :-)
#music = pyglet.resource.media('hudba.mp3')
# music = pyglet.resource.media('Logon.wav',streaming=False)
#music.play()

@window.event
def on_draw():
  window.clear()
  image.blit(0,0)

@window.event
def on_key_press(symbol,modifiers):
  print 'A key pressed '+str(symbol)+' modif '+str(modifiers) 
  if symbol == key.A:
     print "Stlacene 'A'"
  elif symbol == key.LEFT:
     print "Stlacene VLAVO"
  elif symbol == key.ENTER:
     print "Stlaceny ENTER"

@window.event
def on_mouse_press(x, y, button, modifiers):
  #if button == mouse.LEFT:
  print "myska tlacidlo: "+str(x)+":"+str(y)+" button "+str(button)

@window.event
def on_mouse_motion(x,y,dx,dy):
  print "myska pohyb: "+str(x)+":"+str(y)+":"+str(dx)+":"+str(dy)

# zapne vypis udalosti okna do konzoly
window.push_handlers(pyglet.window.event.WindowEventLogger())
# volanie standartnej slucky aplikacie
pyglet.app.run()

