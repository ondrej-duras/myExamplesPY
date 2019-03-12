#!/usr/bin/env python2

from microbit import *

POS = [ [2,2],[2,2],[2,2] ]

XX = 2
YY = 2
DX = 0
DY = 0

def zubrienka(x,y):
  x = int(x) % 5; y = int(y) % 5
  if (x==POS[0][0]) and (y==POS[0][1]):
    return
  display.clear()
  display.set_pixel(POS[2][0],POS[2][1],3)
  POS[2] = POS[1]
  display.set_pixel(POS[1][0],POS[1][1],5)
  POS[1] = POS[0]
  display.set_pixel(POS[0][0],POS[0][1],7)
  POS[0][0] = x; POS[0][1] = y


while True:
  sleep(5)
  if accelerometer.is_gesture("up"):
    DY = 1
  if accelerometer.is_gesture("down"):
    DY = -1
  if accelerometer.is_gesture("right"):
    DX = 1
  if accelerometer.is_gesture("left"):
    DX = -1

  XX += DX ; YY += DY
  if XX < 0:
    XX = 0; DX =  abs(DX * 0.7)
  if XX > 4:
    XX = 4; DX = -abs(DX * 0.7)
  if YY < 0:
    YY = 0; DY =  abs(DY * 0.7)
  if YY > 4:
    YY = 4; DY = -abs(DY * 0.7)

  zubrienka(XX,YY)

# --- end ---

