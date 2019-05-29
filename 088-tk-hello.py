#!/usr/bin/env python2


import Tkinter as tk


okno=tk.Tk()
okno.title("CS1 Document - New AGG Vlan")
okno.resizable(width=False,height=False)
okno.geometry('640x480')



koniec = tk.Button(okno,text="Quit",command=okno.quit,height=1,width=20)
koniec.place(x=500,y=450)

tk.mainloop()
