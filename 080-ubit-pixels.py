#!/usr/bin/env python2

from microbit import *

PIX = [ [2,0], [3,0], [4,0], [4,1], [4,2], [4,3], [4,4],
        [3,4], [2,4], [1,4], [0,4], [0,3], [0,2], [0,1],
        [0,0], [1,0] ]

AZI = 0

def vzorka():
  display.set_pixel(1,1,0); display.set_pixel(2,1,1); display.set_pixel(3,1,2)
  display.set_pixel(1,2,3); display.set_pixel(2,2,4); display.set_pixel(3,2,5)
  display.set_pixel(1,3,6); display.set_pixel(2,3,7); display.set_pixel(3,3,8)

def stvorcek(x):
  x = int(x) % 10
  display.set_pixel(1,1,x); display.set_pixel(2,1,x); display.set_pixel(3,1,x)
  display.set_pixel(1,2,x); display.set_pixel(2,2,x); display.set_pixel(3,2,x)
  display.set_pixel(1,3,x); display.set_pixel(2,3,x); display.set_pixel(3,3,x)

def azimut(uhol,svetlo):
  idx = (((uhol % 360) * 16 ) // 360 ) & 15
  # display.clear()
  display.set_pixel(PIX[idx][0],PIX[idx][1],svetlo)


DX = 1
DY = 5

display.clear()
vzorka()
while True:
  AZI = (AZI + DX) % 360
  azimut(AZI +  0,0)
  azimut(AZI + 30,3)
  azimut(AZI + 60,5)
  azimut(AZI + 90,7)
  azimut(AZI +120,9)
  #vzorka()

  if accelerometer.is_gesture("right"):
    DX += 1
  if accelerometer.is_gesture("left"):
    DX -= 1
  if DX < 0:
    DX = 0
  else:
    DX = DX % 15

  if accelerometer.is_gesture("up"):
    DY += 0.03
  if accelerometer.is_gesture("down"):
    DY -= 0.03
  if DY < 0:
    DY = 0
  elif DY > 9 :
    DY = 9
  stvorcek(DY)
  sleep(5)

# --- end ---

