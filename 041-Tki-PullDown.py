#!/usr/bin/env python

from Tkinter import *
from tkMessageBox import *

master = Tk()

txt = Label(master,text="Jeden"); txt.pack()
var = StringVar(master)
var.set("Jeden") # initial value

hodnoty = ["Jeden","Dva","Tri","Styri"]
#
# test stuff

def ok(x=1):
    print "value is", var.get()
    txt.config(text=var.get())
    #master.quit()

def ok2(x):
    txt.config(text=var.get())

def koniec():
    if askyesno('Koniec','Naozaj skoncit ?'):
      showwarning('Koniec','OK. Koncime :-)')
      master.quit()
    else:
      showinfo('Koniec','Pokracujeme...')

option1 = OptionMenu(master, var, "Jeden", "Dva", "Tri", "Styri")
option2 = OptionMenu(master, var, *hodnoty, command=ok2)
option1.pack()
option2.pack()

button1 = Button(master, text="OK", command=ok)
button1.pack()
button2 = Button(master, text="Koniec", command=koniec)
button2.pack()

mainloop()
