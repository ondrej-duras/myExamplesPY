#!/usr/bin/env python2

import Tkinter as tk
import time

QUIT = False
POSX = 100
POSY = 100
DIFX = 5
DIFY = 5
KURX = 100
KURY = 100

cihla = """
{#f00 #f00 #f00 #f00 #f00 #f00 #ff0 #f00}
{#ff0 #ff0 #ff0 #ff0 #ff0 #ff0 #ff0 #ff0}
{#f00 #ff0 #f00 #f00 #f00 #f00 #f00 #f00}
{#f00 #ff0 #f00 #f00 #f00 #f00 #f00 #f00}
{#f00 #ff0 #f00 #f00 #f00 #f00 #f00 #f00}
{#ff0 #ff0 #ff0 #ff0 #ff0 #ff0 #ff0 #ff0}
{#f00 #f00 #f00 #f00 #f00 #f00 #ff0 #f00}
{#f00 #f00 #f00 #f00 #f00 #f00 #ff0 #f00}
"""


def koniec():
  global QUIT
  QUIT=True


def klavesa(event):
  global QUIT
  key = event.char
  if key == "q" : QUIT = True

def pohyb(event):
  global KURX,KURY
  KURX = event.x - 320 + 400
  KURY = event.y - 200 + 250 


wnd=tk.Tk()
wnd.geometry('640x480')
wnd.title('buffer experiment')
wnd.protocol('WM_DELETE_WINDOW',koniec)
bt1=tk.Button(wnd,text="Koniec",width=10,command=koniec)
bt1.place(x=10,y=450)
img=tk.PhotoImage(width=800,height=500)
can=tk.Canvas(wnd,width=640,height=400,bg="#000")
can.create_image((320,200),image=img,state="normal",anchor=tk.CENTER)
can.place(x=0,y=0)
wnd.bind("<KeyPress>",klavesa)
can.bind("<Motion>",pohyb)

while not QUIT:
  img.put("#000",(0,0,799,499))
  img.put(cihla,(POSX,POSY,POSX+20,POSY+20))
  POSX += DIFX
  POSY += DIFY
  if POSX > 779 : POSX = 779; DIFX = -abs(DIFX)
  if POSX < 0   : POSX = 0;   DIFX =  abs(DIFX)
  if POSY > 479 : POSY = 479; DIFY = -abs(DIFY)
  if POSY < 0   : POSY = 0;   DIFY =  abs(DIFY)

  img.put("#00f",(KURX,KURY,KURX+10,KURY+10))  
  wnd.update()
  time.sleep(0.1)

wnd.destroy()
wnd.quit()
exit()

