#!/usr/bin/env python2

import sys, pygame
from pygame.locals import *

pygame.init()

size = width, height = 640, 480
speed = [1, 1]
black = 0, 0, 0
key = 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("012-PyG-Animacia-Gula.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if (event.type == pygame.KEYDOWN ) and ( event.key == 113): sys.exit()
        # key 113 - is a 'q' key

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
