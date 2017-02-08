#!/bin/env python

import sys, pygame, random
from pygame.locals import *

win = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Sniezik sa nam chumeli (medzera, Q)")
win.fill((0,0,0))
clock = pygame.time.Clock()

NUM1 = NUM2 = 3
chalupai = chalupar = None
def NovaChalupa():
  global chalupai, chalupar
  global NUM1, NUM2
  while NUM1 == NUM2:
    NUM1 = str(random.randint(1,5))
  NUM2 = NUM1
  chalupai = pygame.image.load("030-PyG-Chalupa" + NUM1 + ".jpg")
  chalupar = chalupai.get_rect()
  chalupar.move_ip(0,0)
NovaChalupa()

DATA=[
 [22345, 14678, (255,255,255), 123, 251],
 [27344, 14213, (201,201,201), 173, 231],
 [21426, 17677, (177,177,177), 222, 201],
 [21426, 17677, (137,137,137), 222, 177],
 [20773, 15531, (101,101,101), 155, 154],
 [20343, 13331, (101,101,101), 155, 135],
 [25426, 11677, ( 70, 70, 70), 222, 100]
]

def Snow(A,B,C):
  for I in range(200):
    A = (A + 1) % 65536
    B = (B + A) % 65536
    X = (B  % 256) * 640 // 257
    Y = (B // 256) * 480 // 257
    pixels[X][Y] = C

while True:

  #win.fill((0,0,0))
  win.blit(chalupai,chalupar)
  pixels = pygame.PixelArray(win)

  for ITEM in DATA:
    ITEM[3] += ITEM[4];
    if ITEM[3] // 256:
      ITEM[3] = ITEM[3]  % 256
      ITEM[1] = (ITEM[1] + 256) % 65536
    Snow(ITEM[0],ITEM[1],ITEM[2])

  del pixels
  pygame.display.update()
  clock.tick(100)

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

    if (event.type == KEYDOWN) and (event.key == 113):
      pygame.quit()
      sys.exit()

    if (event.type == KEYDOWN) and (event.key == 32):
      NovaChalupa()
 

