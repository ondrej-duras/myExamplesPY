##...compiled to hex
##apply onto microbit from win10/python2:
##   py2hex 129-ubit-pc-with-ubit.py
##   copy 129-ubit-pc-with-ubit.hex e:\
##   :: where e:\ is drive mounted by mbed driver
##!/usr/bin/env python2 not applicable here
##!/usr/bin/env python3 not applicable here

from microbit import *
import machine
import os
import speech

#while True:
#  if uart.any():
#    line=uart.read()  # precita 1 byte :-)
#    print(line)

VERSION=2022.041701
DIG = 0
SIG = +1
uart.init(115200)  # initiates a console via USB-TTY
speaker.on()
#compass.calibrate()
print("ubicon ready...")
print("press backspace to entercommand")
print("type helpfor help")
while True:
  if uart.any():
    cmd=input("microbit>>")
    cmd=cmd.strip()
    #print("Text: '%s'" % (cmd))
    if cmd in ("py","python","exec"):
      cmd=input(">>> ")
      exec(cmd)
      continue

    if (cmd == "uname") or (cmd[0:3] == "ver"):
      ver = os.uname()
      print("sysname ........... %s" % (ver.sysname))
      print("nodename .......... %s" % (ver.nodename))
      print("release ........... %s" % (ver.release))
      print("version ........... %s" % (ver.version))
      print("machine ........... %s" % (ver.machine))
      uid = str(machine.unique_id())[2:-1].replace(r"\x","")
      freq= machine.freq()/1000000
      ups = str(int(running_time() / 1000))
      print("CPU frequency ..... %5.3f MHz" % (freq))
      print("Board Unique ID ... %s" % (uid))
      print("uptime ............ %s" % (ups))
      continue

    if cmd[0:3] == "say":
      print("saying .... %s" % (cmd))
      cmd=cmd[3:]
      #speech.say(cmd)
      speech.say(cmd,pitch=200,speed=150,mouth=255)
      continue 

    if cmd[0:4] == "data":
      # display.set_pixel(0,0,0) # not necessary to turn OFF leds on display(based on manuals)
      print("temperature ........ %s`C" % (temperature()))
      print("light <0-255> ...... %s" % (str(display.read_light_level()))) # viacia nuly ...asi chybka
      #print("azimut ............. %s" % (str(compass.heading()))
      print("X-axis.............. %s nT" % (str(compass.get_x())))
      print("Y-axis.............. %s nT" % (str(compass.get_y())))
      print("Z-axis.............. %s nT" % (str(compass.get_z())))
      continue
      
    if cmd[0:3] == "cal":
      print("compass calibration....")
      compass.clear_calibration()
      compass.calibrate()
      print("compass calibrated.")
      continue

    if cmd in ("compass","magnetic"):
      while(not uart.any()):
        x=compass.get_x()
        y=compass.get_y()
        z=compass.get_z()
        print("x=%d y=%d z=%d" % (x,y,z))
        sleep(500)

    if (cmd[0:4] == "help") or ("?" in cmd):
      print("uname   - system version")
      print("version - system version") 
      print("data    - some technical details")
      print("calib   - calibrate compass")
      print("compass - continuous compass data till keypressed")
      print("exec    - execute a python command")
      continue

    print("Syntax error.")

  # display.show(str(DIG))
  DIG += SIG
  if DIG > 9: DIG=9; SIG=-1
  if DIG < 0: DIG=0; SIG=+1
  display.set_pixel(0,0,DIG)
  sleep(100)

  



