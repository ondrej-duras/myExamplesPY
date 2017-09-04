#!/usr/bin/env python

import pygame, sys
from pygame.locals import *
pygame.init()

win = pygame.display.set_mode((500,300),0, 32)
pygame.display.set_caption("Hello World !")

win.fill((80,80,10))



while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

