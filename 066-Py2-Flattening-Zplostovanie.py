#!/usr/bin/env python2

# viac-rozmerne pole/list
xlist = [[1,2,3],[4,5,6],[7,8,9]]

# vypis povodneho pola
print xlist

# pomocou "list comprehension" metody urobime splostenie pola (flattening)
flatten = [ x for sublist in xlist for x in sublist ]

# vypis pola zplosteneho
print flatten

# --- end ---

