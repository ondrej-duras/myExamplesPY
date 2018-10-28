#!/usr/bin/env python
# http://www.programcreek.com/python/index/module/list # zoznam najuspesnejsich balickov Py
# http://www.python-course.eu/python_tkinter.php       # kurz ku Tk (sucast instalacky  Py)
# http://www.python-course.eu/tkinter_dialogs.php      # specialne ku dialogom


from Tkinter import *
from tkMessageBox import *

def answer():
    showerror("Answer", "Sorry, no answer available")

def callback():
    if askyesno('Verify', 'Really quit?'):
        showwarning('Yes', 'Not yet implemented')
    else:
        showinfo('No', 'Quit has been cancelled')

Button(text='Quit', command=callback).pack(fill=X)
Button(text='Answer', command=answer).pack(fill=X)
mainloop()

# --- koniec ---

