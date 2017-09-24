#!/usr/bin/env python

from Tkinter import *

# Inicializacia okna konkretnych rozmerov
okno=Tk()
okno.title("Tk - Vsetko v jednom")
okno.resizable(width=False,height=False)
okno.minsize(width=640,height=480)
okno.maxsize(width=640,height=480)


# akcia, zobrazujuca zmeny obsahu premennych
def show():
  global vystup, hodnota, hodR, hodG, hodB
  FARBY=hodnota.get() + " ["
  if hodR.get(): FARBY += "R"
  if hodG.get(): FARBY += "G"
  if hodB.get(): FARBY += "B"
  vystup.config(text=FARBY + "]")


def zobrazit():
  global hodnA, hodnB, premA, premB
  hodnA.config(text=premA.get())
  hodnB.config(text=premB.get())


# Vytvorenie premennych prostredia
hodnota=StringVar(value="modra")   # IntVar() StringVar() DoubleVar() BooleanVar()
hodR=IntVar(value=0)
hodG=IntVar(value=0)
hodB=IntVar(value=1)
textV=StringVar(value="Hello\nWorld\n!")


# Ovladacie prvky
Label(okno,text="Zaklikaj si", justify=LEFT, padx=2, pady=2).grid(row=1,column=5)
Radiobutton(okno, text="Cervena", variable=hodnota, value="cervena", command=show, justify=LEFT, padx=2, pady=2).grid(row=2,column=5)
Radiobutton(okno, text="Zelena",  variable=hodnota, value="zelena",  command=show, justify=LEFT, padx=2, pady=2).grid(row=3,column=5)
Radiobutton(okno, text="Modra",   variable=hodnota, value="modra",   command=show, justify=LEFT, padx=2, pady=2).grid(row=4,column=5)


Checkbutton(okno, text="Cervena", variable=hodR, command=show, justify=LEFT, padx=2, pady=2).grid(row=5,column=5)
Checkbutton(okno, text="Zelena",  variable=hodG, command=show, justify=LEFT, padx=2, pady=2).grid(row=6,column=5)
Checkbutton(okno, text="Modra",   variable=hodB, command=show, justify=LEFT, padx=2, pady=2).grid(row=7,column=5)


Label(okno, text="Premenna A").grid(row=0,column=0)
Label(okno, text="Premenna B").grid(row=1,column=0)
Label(okno, text="Hodnota A:").grid(row=2,column=0)
Label(okno, text="Hodnota B:").grid(row=3,column=0)

premA = Entry(okno);         premA.grid(row=0,column=1)
premB = Entry(okno);         premB.grid(row=1,column=1)
hodnA = Label(okno,text=""); hodnA.grid(row=2,column=1)
hodnB = Label(okno,text=""); hodnB.grid(row=3,column=1)

textL = Label(okno,justify=LEFT, text="Viacriadkova premenna").grid(row=6,column=1)
textX = Text(okno,height=3, width=30).grid(row=7,column=1)

Button(okno,text="Koniec",  command=okno.quit).grid(row=4, column=0)
Button(okno,text="Zobrazit",command=zobrazit ).grid(row=4, column=1)

vystup = Label(okno,text=hodnota.get()); vystup.grid(row=8,column=5)
Button(okno,text="Koniec", command=okno.quit).grid(row=9,column=5)
mainloop()

