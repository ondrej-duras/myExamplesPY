#!/usr/bin/env python2


"""
Tu ide o vyhadzanie vsetkych poloziek
z pola v pripade, ze splnaju podmienku pre vyhodenie.

V pythone nemame:
 referencie ani dereferencie,
 smerniky ani navestia a dokonca ani unarne aritmeticke operatory
 A pri to vsetkom tu niesu ani obycajne  zatvorky pre ohranicenie bloku
 ... nech to pes po.... .

"""

# vyrobenie pola s nejakymi 10-kami, ktore vsetky chceme vyhadzat
import random
POLE = [ random.randint(10,15) for X in range(10) ]
POLE.append(10)
POLE.append(10)
POLE.append(10)
POLE.append(10)
print POLE

# sposob ako vsetky desiatky vyhadzat - cista assemblerovina
# meni sa pocet poloziek pola
# Kazdy kto robil so zoznamami v assembleri sa musi chytat
# za hlavu, ale kultivovanejsie to asi nejde.

# nastavenie indexu a poctu prvok pola
i = 0 ; lx = len(POLE)
while i<lx:
  # v pripade ze prvok vyhadzujeme, tak znizime pocet prvkov pola 
  # a dekrementujeme index, aby sme sa vratili na poziciu, kde bol zmazany prvok
  # a kde je momentalne prvok nasledujuci
  if POLE[i] == 10 : del POLE[i]; lx -= 1; i -= 1
  i += 1
  
print POLE

