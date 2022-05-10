##!/usr/bin/env python2 

from microbit import *
import speech
import music

speaker.on()
FLAG=0

while True:
  if button_a.is_pressed():
    audio.play(Sound.HELLO)
    FLAG|=1
  if button_b.is_pressed():
    audio.play(Sound.HELLO)
    FLAG|=2
  
  if FLAG == 3:
    sleep(2000)
    speech.say("Ahoj Saska",pitch=200,speed=150,mouth=255)
    display.scroll("Ahoj Saska")
    sleep(2000)
    music.play(music.PRELUDE)
    FLAG = 0

  


