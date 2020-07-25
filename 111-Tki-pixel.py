#!/usr/bin/env python2

import Tkinter as tk

wnd = tk.Tk()
wnd.title("okienko")
wnd.resizable(width=False,height=False)
wnd.geometry("640x480")
can = tk.Canvas(width=640,height=480)
img = tk.PhotoImage(width=640,height=480)
can.create_image((320,240),image=img,state="normal")
can.place(x=0,y=0)

obr = """
{#fff #fff #fff #fff #fff #fff #fff #fff}
{#f00 #f00 #f00 #f00 #f00 #f00 #fff #f00}
{#f00 #f00 #f00 #f00 #f00 #f00 #ff0 #f00}
{#f00 #f00 #f00 #f00 #f00 #f00 #fff #f00}
{#fff #fff #fff #fff #fff #fff #fff #fff}
{#f00 #fff #f00 #f00 #f00 #f00 #f00 #f00}
{#f00 #fff #f00 #f00 #f00 #f00 #f00 #f00}
{#f00 #fff #f00 #f00 #f00 #f00 #f00 #f00}
"""

tik = 0
def Xupdate():
  global tik 
  img.put(obr,(tik,0,tik+320,200))
  if tik <= 0: x=8
  else: x=x-1
  #wnd.update_idletasks()
  #wnd.update()
  wnd.after(1,Xupdate)

Xupdate()
wnd.mainloop()

