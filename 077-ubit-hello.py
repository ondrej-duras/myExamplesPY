#!/usr/bin/env python2
# toto je urcene pre micro:bit

"""
Na to aby vsetko zafungovalo ako ma, treba dve veci:
 - mbed driver zo stranky mbed.org (od firmy ARM)
 - pip intsall uflash
 - pripadne pip install PyBluez pre bluetooth

mbed driver vytvori asociaciu so portom com12 .
Uflash balicek okrem vsetkych python sucasti nesie
so sebou aj utilitku "uflash" . Ta je potrebna
pre preprogramovanie micro:bit-u.

1. Nasledne staci napisat script, ako je hoci tento,
2. pripojit micro:bit pomocou USB kabla k pocitacu
a nakopirovat ho do Micro;bit-u . To sa da napriklad
takto:
C:> uflash 077-ubit-hello
"""
from microbit import *

while True:
    display.scroll("*** Ahoj Danka ***")

# --- end ---

