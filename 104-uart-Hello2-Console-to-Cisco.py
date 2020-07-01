#!/usr/bin/env python2
# nahrada minicom appky
# 20200629-1, dury
# pip2 install pySerial


import serial # pip2 install pySerial
import time

tty = serial.Serial(
   port="COM4",         # windows   (FTDI UC232R)
   #port="/dev/ttyUSB0" # raspberry
   baudrate=9600,       # line setup for cisco,juniper,f5 and other hungry pigs
   bytesize = serial.EIGHTBITS,
   parity = serial.PARITY_NONE,
   stopbits = serial.STOPBITS_ONE,
   timeout = 2
)
tty.close() # that closes previously opened sessions ... :-)
tty.open()  # opens new session
tty.set_buffer_size(64000)
if not tty.isOpen(): exit() # checks whether the session has been opened

print dir(tty) # ...lebo medved :-)

tty.flushInput()  # vyhadzeme z buffrov
tty.flushOutput()

while 1:   # slucka, cakajuca na exit
  line = raw_input(">> ")
  if "exit" in line:
    tty.close()
    exit()
  tty.writelines(line + "\n")
  output = tty.read_until(">|-",64000)
  print output

# --- end ---

