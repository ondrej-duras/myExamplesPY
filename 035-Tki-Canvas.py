#!/usr/bin/env python
# http://www.python-course.eu/python_tkinter.php  # manual ku Tk balicku, ktory je sucastou installacky Py
# http://www.python-course.eu/tkinter_canvas.php  # special ku Canvas/Platnu na kreslenie

from Tkinter import *
master = Tk()

WIDTH  = 640
HEIGHT = 480
w = Canvas(master, 
           width  = WIDTH  +1,
           height = HEIGHT +1)
w.pack()

w.create_line(    0,      0, WIDTH,      0, fill="#ff2020")
w.create_line(WIDTH,      0, WIDTH, HEIGHT, fill="#20ff20")
w.create_line(WIDTH, HEIGHT,     0, HEIGHT, fill="#2020ff")
w.create_line(    0, HEIGHT,     0,      0, fill="#ffff20")

w.create_line(    0,      0, WIDTH, HEIGHT, fill="#20ffff")
w.create_line(WIDTH,      0,     0, HEIGHT, fill="#ff20ff")


mainloop()

