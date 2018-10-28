#!/usr/bin/env python
#20180104, Mato

# prvy programcok s Martinom :-)

import sys
import Tkinter as tk


def zmena():
    global vstup, napis
    X=vstup.get()
    napis.config(text=X)

def xexit():
    global okno
    okno.destroy()
    sys.exit()


okno=tk.Tk()
okno.wm_title("Norska Vlajka")
okno.resizable(width=False, height=False)
okno.geometry('640x480')


platno=tk.Canvas(okno,width=350,height=250,bg="red");
platno.place(x=10, y=10)
#platno.pack()
platno.create_rectangle(0,100,350,150, fill="white",outline="white")
platno.create_rectangle(100,0,150,250, fill="white",outline="white")
platno.create_rectangle(0,112,350,138, fill="navy",outline="navy")
platno.create_rectangle(112,0,138,250, fill="navy",outline="navy")

napis=tk.Label(okno,text="Daco");napis.place(x=10,y=300)
napis.config(text="Nieco ine")
vstup=tk.Entry(okno); vstup.place(x=10,y=330)

tlacidlo=tk.Button(okno,text="Zmenit",command=zmena); tlacidlo.place(x=10, y=350)
koniec=tk.Button(okno,text="Koniec",command=xexit); koniec.place(x=100,y=350)
tk.mainloop()
