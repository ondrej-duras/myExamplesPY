#!/usr/bin/env python
# http://effbot.org/tkinterbook/listbox.htm

from Tkinter import *


def show_tty():
  global listbox
  values  = listbox.get(0,END)
  indexes = listbox.curselection()
  for i in indexes:
    print "Vyznaceny je %s (%s)" % (i,values[i])
  print "Aktivny/pociarknuty je %s" % listbox.get(ACTIVE)

master = Tk()
master.title("Vyber v DropDown menu")

listbox = Listbox(master,selectmode=MULTIPLE)
items = map(int,listbox.curselection())

#listbox.pack()
listbox.grid(row=0)

listbox.insert(END, "Prvy riadok")

for item in ["Druhy", "Treti riadok", "stvrty", "a piaty riadok"]:
    listbox.insert(END, item)

Button(master,text='Koniec',command=master.quit).grid(row=1, column=0, sticky=W, pady=4)
Button(master,text='Ukaz',command=show_tty).grid(row=1, column=1, sticky=W, pady=4)

mainloop()
