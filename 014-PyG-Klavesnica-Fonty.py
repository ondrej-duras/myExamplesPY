#!/usr/bin/env python
#http://www.pygame.org/docs/ref/event.html

import pygame, sys
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("PyG-4 Klavesnica a Pismenka")
window.fill((0,0,0))

BasicFont = pygame.font.SysFont(None,20)
text1 = BasicFont.render(" Stlac 'Q' pre ukoncenie ",
       True,(255,255,255),(255,0,0))
text1Rect = text1.get_rect()
text1Rect.move_ip(20,20)
window.blit(text1,text1Rect)

CourFont = pygame.font.SysFont("Courier",35)
text3 = CourFont.render("Nieco divoke",False,(80,80,40),(0,0,0))
text3Rect = text3.get_rect()
text3Rect.move_ip(20,70)
window.blit(text3,text3Rect)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
             klaves_kod = event.key
             if klaves_kod < 256:
                klaves_znak = chr(klaves_kod)
             else:
                klaves_znak = ' '
             text2 = BasicFont.render("  %c %d  " % (klaves_znak,klaves_kod),
                                      True,(255,255,128),(0,255,0))
             text2Rect = text2.get_rect()
             text2Rect.move_ip(20,40)
             window.blit(text2,text2Rect)
             pass

        if event.type == KEYUP:
             klaves_kod = event.key
             if klaves_kod < 255:
                  klaves_znak=chr(klaves_kod)
             else:
                  klaves_znak=' '
             if(klaves_znak == 'q'):
                pygame.quit()
                sys.exit()     
             pass

        if event.type == QUIT:
             pygame.quit()
             sys.exit()
