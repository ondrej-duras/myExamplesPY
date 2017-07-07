#!/usr/bin/env python

from Tkinter import *
okno = Tk()
okno.wm_title("Geometria")
okno.resizable(width=False,height=False)
#okno.geometry('{}x{}'.format(640,480))  # funguje
okno.geometry('640x480')  # tiez funguje


napis = Label(okno,text="Hey.")
napis.place(x=10,y=10)

koniec = Button(okno,text="Koniec",command=okno.quit,height=1,width=20)
koniec.place(x=300,y=450)

okno.mainloop()

