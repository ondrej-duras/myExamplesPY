#!/usr/bin/env python
# Polygons - Old ScreenSaver
# 20170209, Ing. Ondrej DURAS (dury)

import sys, pygame, random
from pygame.locals import *

WIDTH=640; HEIGHT=480;


class point:
  def __init__(self):  # konstruktor objektu
    self.ax = self.bx = random.randint(0,WIDTH)
    self.ay = self.by = random.randint(0,HEIGHT)
    self.dx = self.qx = (random.randint(0,1)*2*1)-1
    self.dy = self.qy = (random.randint(0,1)*2*1)-1

  def move(self):
    if self.ax <= 0:      self.ax=0;        self.dx= -self.dx
    if self.ax >= WIDTH:  self.ax=WIDTH-1;  self.dx= -self.dx
    self.ax += self.dx
    if self.ay <= 0:      self.ay=0;        self.dy= -self.dy
    if self.ay >= HEIGHT: self.ay=HEIGHT-1; self.dy= -self.dy
    self.ay += self.dy
  
  def step(self):
    (self.ax, self.ay, self.dx, self.dy) = (self.bx, self.by, self.qx, self.qy)
    self.move()
    (self.bx, self.by, self.qx, self.qy) = (self.ax, self.ay, self.dx, self.dy)

  def position(self):
    return (self.ax, self.ay)

  def __del__(self): # sedtruktor objektu - tu iba demonstrative
    return None

class polygon:
  def __init__(self, size=5):
    if size < 3: size=3
    self.size  = size
    self.last  = size - 1
    self.color =(random.randint(0,255), \
                 random.randint(0,255), \
                 random.randint(0,255), \
                 (random.randint(0,1)*2)-1,
                 (random.randint(0,1)*2)-1,
                 (random.randint(0,1)*2)-1,
                )
    self.qolor =list(self.color)
    self.points = []
    for i in range(size):
      self.points.append(point())

  def get_color(self):
    return (self.color[0],self.color[1],self.color[2])

  def draw(self):
    last = self.last
    for i in range(last):
      (x1,y1) = self.points[i].position()
      (x2,y2) = self.points[i+1].position()
      pygame.draw.line(win, self.get_color(), (x1,y1),(x2,y2),1)
    pygame.draw.line(win,self.get_color(),(x2,y2), self.points[0].position(),1)

  def move(self):
    for i in range(self.size):
      self.points[i].move()
    (ar,ag,ab, dr,dg,db) = self.color
    ar = ar + dr 
    if ar <= 0:   ar=0;   dr = -dr
    if ar >= 255: ar=255; dr = -dr
    ag = ag + dg 
    if ag <= 0:   ag=0;   dg = -dg
    if ag >= 255: ag=255; dg = -dg
    ab = ab + db 
    if ab <= 0:   ab=0;   db = -db
    if ab >= 255: ab=255; db = -db
    self.color=(ar,ag,ab, dr,dg,db)  

  def step(self):
    for i in range(self.size):
      self.points[i].step()
    (ar,ag,ab, dr,dg,db) = self.qolor
    ar = ar + dr 
    if ar <= 0:   ar=0;   dr = -dr
    if ar >= 255: ar=255; dr = -dr
    ag = ag + dg 
    if ag <= 0:   ag=0;   dg = -dg
    if ag >= 255: ag=255; dg = -dg
    ab = ab + db 
    if ab <= 0:   ab=0;   db = -db
    if ab >= 255: ab=255; db = -db
    self.qolor=(ar,ag,ab, dr,dg,db)  
    self.color=list(self.qolor)


def done():
  pygame.quit()
  sys.exit()



win = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
pygame.display.set_caption("Polygon Q")
clock = pygame.time.Clock()
poly = polygon(7)       # pocet ciar jedneho polygonu

while True:
  win.fill((0,0,0))

  poly.step()
  for i in range(8):    # pocet polygonov
    for y in range(10): # odstup medzi polygonmi
      poly.move()
    poly.draw()

  pygame.display.flip()
  clock.tick(100)       # pocet obrazkov za sekundu
  for event in pygame.event.get():
    if event.type == QUIT:
      done()
    if (event.type == KEYDOWN) and (event.key == 113):
      done()


#### --- koniec zdrojaku ----




