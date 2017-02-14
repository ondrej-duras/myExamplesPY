#!/bin/env python

from Tkinter import *


# Inicializacia okna s konkretnymi rozmermi
okno=Tk()
okno.title("Radio & Check")
okno.resizable(width=False, height=False)
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



# Vytvorenie premennych prostredia
hodnota=StringVar(value="modra")   # IntVar() StringVar() DoubleVar() BooleanVar()
hodR=IntVar(value=0)
hodG=IntVar(value=0)
hodB=IntVar(value=1)


# Ovladacie prvky
Label(okno,text="Zaklikaj si", justify=LEFT, padx=20, pady=20).pack()
Radiobutton(okno, text="Cervena", variable=hodnota, value="cervena", command=show, justify=LEFT, padx=20, pady=20).pack(anchor=W)
Radiobutton(okno, text="Zelena",  variable=hodnota, value="zelena",  command=show, justify=LEFT, padx=20, pady=20).pack(anchor=W)
Radiobutton(okno, text="Modra",   variable=hodnota, value="modra",   command=show, justify=LEFT, padx=20, pady=20).pack(anchor=W)


Checkbutton(okno, text="Cervena", variable=hodR, command=show, justify=LEFT, padx=20, pady=20).pack(anchor=W)
Checkbutton(okno, text="Zelena",  variable=hodG, command=show, justify=LEFT, padx=20, pady=20).pack(anchor=W)
Checkbutton(okno, text="Modra",   variable=hodB, command=show, justify=LEFT, padx=20, pady=20).pack(anchor=W)

vystup = Label(okno,text=hodnota.get()); vystup.pack()
Button(okno,text="Koniec", command=okno.quit).pack()
mainloop()


# --- koniec ---

