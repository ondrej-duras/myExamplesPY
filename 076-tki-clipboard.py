#!/usr/bin/env python2

import Tkinter
wnd = Tkinter.Tk()

wnd.withdraw() # schova okno
vstup = wnd.clipboard_get()

vystup = "Nova hodnota v clipboarde"
wnd.clipboard_clear()
wnd.clipboard_append(vystup)

wnd.destroy() # vyhodi objekt okna z pamate
print "V clipboarde bolo:"
print vstup
print "A pozri, co je v clipboarde teraz:"




