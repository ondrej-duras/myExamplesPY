#!/usr/bin/env python
# http://www.programcreek.com/python/index/module/list # zoznam najuspesnejsich balickov Py
# http://www.python-course.eu/python_tkinter.php       # kurz ku Tk (sucast instalacky  Py)
# http://www.python-course.eu/tkinter_dialogs.php      # specialne ku dialogom


from Tkinter import *
from tkMessageBox import *

wnd=Tk()
wnd.withdraw()  # do not show the main window

text = "Hello Tk Clipboard."
wnd.clipboard_clear()
wnd.clipboard_append(text)
clipped = wnd.clipboard_get()
showinfo('Clip', 'Text "%s" has been clipped.' % (clipped))

# --- koniec ---

