#!/bin/env python
# http://www.python-course.eu/tkinter_labels.php

from Tkinter import *


def zobrazit():
  global hodnA, hodnB, premA, premB
  hodnA.config(text=premA.get())
  hodnB.config(text=premB.get())


okno=Tk()
okno.title("Zadavanie premennych")

Label(okno, text="Premenna A").grid(row=0,column=0)
Label(okno, text="Premenna B").grid(row=1,column=0)
Label(okno, text="Hodnota A:").grid(row=2,column=0)
Label(okno, text="Hodnota B:").grid(row=3,column=0)

premA = Entry(okno);         premA.grid(row=0,column=1)
premB = Entry(okno);         premB.grid(row=1,column=1)
hodnA = Label(okno,text=""); hodnA.grid(row=2,column=1)
hodnB = Label(okno,text=""); hodnB.grid(row=3,column=1)

Button(okno,text="Koniec",  command=okno.quit).grid(row=4, column=0)
Button(okno,text="Zobrazit",command=zobrazit ).grid(row=4, column=1)

mainloop()

