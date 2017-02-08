#!/bin/env python

import sys, pygame
from pygame.locals import *

win = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Sniezik sa nam chumeli")
win.fill((0,0,0))
clock = pygame.time.Clock()

A1=22345; B1=14678

while True:

  win.fill((0,0,0))
  pixels = pygame.PixelArray(win)
  A=A1; B=B1
  for I in range(200):
    A = (A + 1) % 65536
    B = (B + A) % 65536
    X = (B  % 256) * 640 // 257
    Y = (B // 256) * 480 // 257
    pixels[X][Y] = (255,255,255)
  del pixels

  pygame.display.update()
  clock.tick(100)
  B1 = (B1 + 256) % 65536

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

    if (event.type == KEYDOWN) and (event.key == 113):
      pygame.quit()
      sys.exit()



