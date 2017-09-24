#!/usr/bin/env python

# http://www.pygame.org/docs/ref/event.html
'''
Ovladanie udalosti v praxi:
-----------------------------------
QUIT             none
ACTIVEEVENT      gain, state
KEYDOWN          unicode, key, mod
KEYUP            key, mod
MOUSEMOTION      pos, rel, buttons
MOUSEBUTTONUP    pos, button
MOUSEBUTTONDOWN  pos, button
JOYAXISMOTION    joy, axis, value
JOYBALLMOTION    joy, ball, rel
JOYHATMOTION     joy, hat, value
JOYBUTTONUP      joy, button
JOYBUTTONDOWN    joy, button
VIDEORESIZE      size, w, h
VIDEOEXPOSE      none
USEREVENT        code
'''


import sys, pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Myska a Pixely")
win = pygame.display.set_mode((640,480),0,32)
BasicFont = pygame.font.SysFont(None,30)
win.fill((0,0,0))

update = 0
point  = 0
while True:
  if point:
    posx,posy = event.pos
    canvas = pygame.PixelArray(win)
    canvas[posx][posy]=(255,255,128)
    del canvas
    update = 1

  if update:
    pygame.display.update()
    update = 0

  for event in pygame.event.get():
    if event.type == QUIT: # zatvorenie aplikacie
      pygame.quit()
      sys.exit()
    
    if (event.type == KEYUP) and (event.key == 113):
      pygame.quit()
      sys.exit()
  
    if event.type == MOUSEBUTTONDOWN:
      point = 1

    if event.type == MOUSEBUTTONUP:
      point = 0
  
    if (event.type == MOUSEMOTION):
      posx,posy = event.pos
      pozicia = BasicFont.render(" X=%d Y=%d " % (posx,posy),
                                 True,(255,255,255),(0,80,0))
      poziciaRect = pozicia.get_rect()
      poziciaRect.move_ip(20,20)
      win.blit(pozicia,poziciaRect)
      update = 1

      
