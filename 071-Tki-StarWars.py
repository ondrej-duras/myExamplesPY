#!/usr/bin/env python2

import Tkinter as tk
import time
import random
random.seed(time.time())

QUIT = False
myxx = 350
myyy = 450
VECI = []
VECT = 0

JASTRAB = """
{#000 #000 #000 #000 #f00 #000 #000 #000 #000}
{#000 #000 #000 #000 #f00 #000 #000 #000 #000}
{#000 #000 #000 #ff0 #f00 #ff0 #000 #000 #000}
{#000 #000 #000 #ff0 #f00 #ff0 #000 #000 #000}
{#000 #000 #ff0 #ff0 #f00 #ff0 #ff0 #000 #000}
{#000 #000 #ff0 #ff0 #f00 #ff0 #ff0 #000 #000}
{#000 #ff0 #ff0 #0f0 #f00 #0f0 #ff0 #ff0 #000}
{#000 #ff0 #ff0 #0f0 #f00 #0f0 #ff0 #ff0 #000}
{#ff0 #ff0 #ff0 #0f0 #f00 #0f0 #ff0 #ff0 #ff0}
{#ff0 #ff0 #ff0 #0f0 #f00 #0f0 #ff0 #ff0 #ff0}
{#ff0 #ff0 #ff0 #0f0 #f00 #0f0 #ff0 #ff0 #ff0}
{#ff0 #ff0 #ff0 #ff0 #ff0 #ff0 #ff0 #ff0 #ff0}
{#000 #ff0 #ff0 #fff #ff0 #fff #ff0 #ff0 #000}
{#000 #000 #ff0 #fff #ff0 #fff #ff0 #000 #000}
"""
SAT1 = """
{#000 #088 #088 #088 #088 #088 #088 #088 #000}
{#088 #000 #000 #000 #088 #000 #000 #000 #088}
{#088 #000 #000 #000 #088 #000 #000 #000 #088}
{#000 #000 #000 #000 #088 #000 #000 #000 #000}
{#000 #000 #000 #088 #088 #088 #000 #000 #000}
{#000 #000 #088 #000 #000 #000 #088 #000 #000}
{#000 #000 #088 #000 #000 #000 #088 #000 #000}
{#000 #000 #088 #000 #000 #000 #088 #000 #000}
{#000 #000 #088 #000 #000 #000 #088 #000 #000}
{#000 #000 #000 #088 #088 #088 #000 #000 #000}
{#000 #000 #000 #000 #088 #000 #000 #000 #000}
{#088 #000 #000 #000 #088 #000 #000 #000 #088}
{#088 #000 #000 #000 #088 #000 #000 #000 #088}
{#000 #088 #088 #088 #088 #088 #088 #088 #000}
"""
SAT2 = """
{#088 #088 #088 #088 #088 #000 #000 #000 #000}
{#088 #000 #088 #000 #000 #088 #000 #000 #000}
{#088 #000 #088 #000 #000 #000 #000 #088 #000}
{#088 #000 #088 #000 #000 #000 #000 #000 #088}
{#088 #000 #088 #088 #088 #088 #000 #000 #088}
{#088 #000 #088 #000 #000 #000 #088 #000 #088}
{#088 #000 #088 #000 #000 #000 #088 #000 #088}
{#088 #000 #088 #000 #000 #000 #088 #000 #088}
{#088 #000 #088 #000 #000 #000 #088 #000 #088}
{#088 #000 #000 #088 #088 #088 #088 #000 #088}
{#000 #088 #000 #000 #000 #000 #088 #000 #088}
{#000 #000 #000 #000 #000 #000 #088 #000 #088}
{#008 #000 #000 #088 #000 #000 #088 #000 #088}
{#000 #000 #000 #000 #088 #088 #088 #088 #088}
"""
SAT3 = """
{#000 #000 #088 #000 #000 #000 #088 #000 #000}
{#000 #088 #000 #000 #000 #000 #000 #088 #000}
{#000 #088 #000 #000 #000 #000 #000 #088 #000}
{#088 #000 #000 #000 #000 #000 #000 #000 #088}
{#088 #000 #000 #088 #088 #088 #000 #000 #088}
{#088 #000 #088 #000 #000 #000 #088 #000 #088}
{#088 #088 #088 #000 #000 #000 #088 #088 #088}
{#088 #088 #088 #000 #000 #000 #088 #088 #088}
{#088 #000 #088 #000 #000 #000 #088 #000 #088}
{#088 #000 #000 #088 #088 #088 #000 #000 #088}
{#088 #000 #000 #000 #000 #000 #000 #000 #088}
{#000 #088 #000 #000 #000 #000 #000 #088 #000}
{#000 #088 #000 #000 #000 #000 #000 #088 #000}
{#000 #000 #088 #000 #000 #000 #088 #000 #000}
"""
SAT4 = """
{#000 #000 #000 #000 #088 #088 #088 #088 #088}
{#008 #000 #000 #088 #000 #000 #088 #000 #088}
{#000 #000 #000 #000 #000 #000 #088 #000 #088}
{#000 #088 #000 #000 #000 #000 #088 #000 #088}
{#088 #000 #000 #088 #088 #088 #088 #000 #088}
{#088 #000 #088 #000 #000 #000 #088 #000 #088}
{#088 #000 #088 #000 #000 #000 #088 #000 #088}
{#088 #000 #088 #000 #000 #000 #088 #000 #088}
{#088 #000 #088 #000 #000 #000 #088 #000 #088}
{#088 #000 #088 #088 #088 #088 #000 #000 #088}
{#088 #000 #088 #000 #000 #000 #000 #000 #088}
{#088 #000 #088 #000 #000 #000 #000 #088 #000}
{#088 #000 #088 #000 #000 #088 #000 #000 #000}
{#088 #088 #088 #088 #088 #000 #000 #000 #000}
"""

SATANIM  = [SAT1,SAT2,SAT3,SAT4]
SATELITS = []
SATLIMIT = 10

def satUpdate():
  global SATELITS,SATLIMIT,img
  if len(SATELITS) < SATLIMIT:
    sat = { 'x':random.uniform(50.0,650.0), 'y':0, 
           'dx':random.uniform(-5.0,5.0), 
           'dy':random.uniform(0.0,10.0),
           'delete':False,
           'anim' : random.randint(0,3)
          }
    SATELITS.append(sat)
  for i in range(len(SATELITS)):
     sat = SATELITS[i]
     if sat['x'] > 670.0 : sat['x'] =670.0 ; sat['dx'] = -abs(sat['dx'])
     if sat['x'] <  30.0 : sat['x'] =30.0  ; sat['dx'] =  abs(sat['dx'])
     sat['x'] += sat['dx']; sat['y'] += sat['dy']
     SATELITS[i] = sat
  i = 0 ; ct = len(SATELITS)
  while i < ct:
    if SATELITS[i]['y'] > 450:
       del SATELITS[i]
       i  -= 1
       ct -= 1
    i += 1
  for i in range(len(SATELITS)):
    sat = SATELITS[i]
    img.put(SATANIM[sat['anim']],(int(sat['x']),int(sat['y'])))


FIRES = []

def fireCheck(x,y):
  return 0

def fireAdd():
  global FIRES,myxx,myyy,img
  fire = { 'x':int(myxx), 'y': int(myyy) }
  FIRES.append(fire)
  #print "fire add(%u)" % (len(FIRES))

def fireUpdateOne(ix):
  global FIRES,img
  # return 0 = strela pokracuje
  # return 1 = strelu treba zmazat
  fire=FIRES[ix]
  x = fire['x']
  y = fire['y']
  if y < 30 : return 1
  FIRES[ix]['y'] -= 30
  s = y - 30
  while y > s:
    if '0 0 0' <> img.get(x,y):
       if fireCheck(x,y): return 1
    y -= 1
  img.put("#720",(x,y,x+1,y+25))
  return 0


def fireUpdate():
  global FIRES,img
  ix=0 ; ct=len(FIRES)
  while ix < ct:
    if fireUpdateOne(ix):
       del FIRES[ix]
       ix -= 1
       ct -= 1
    ix += 1

 



def koniec():
  global QUIT
  QUIT=True

def klavesy(event):
  global myxx,myyy
  key = event.char
  kod = event.keycode
  if kod == 27 : koniec()
  if kod == 37 : myxx -= 3
  if kod == 39 : myxx += 3 
  if kod == 38 : myyy -= 3
  if kod == 40 : myyy += 3
  if kod == 32 : fireAdd()
  #print kod

wnd = tk.Tk()
wnd.title("Star Wars IV - Imperium utoci")
wnd.geometry('640x480')
wnd.resizable(width=False,height=False)

can = tk.Canvas(wnd,width=640,height=450,bg="#000")
img = tk.PhotoImage(width=700,height=510)
can.create_image((320,225),image=img,state="normal",anchor=tk.CENTER)
can.place(x=0,y=0)
wnd.protocol('WM_DELETE_WINDOW',koniec)
wnd.bind('<KeyPress>',klavesy)

while not QUIT:
  img.put("#000",(30,30,670,482))
  satUpdate()
  fireUpdate()

  if myxx > 670 : myxx = 670
  if myxx < 30  : myxx = 30
  if myyy > 480 : myyy = 480
  if myyy < 30  : myyy = 30
  img.put(JASTRAB,(myxx-4,myyy))

  time.sleep(0.1)
  wnd.update()

wnd.quit()
wnd.destroy()

