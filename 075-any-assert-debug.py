#!/usr/bin/env python2

# assert condition,message
# sprava sa zobrazi, ak pomienka pocas behu programu nieje splnena


# Podmienka moze byt funkcia, ktora v pripade chyby vracia nulu, inak nenulu
# Sprava moze tiez byt funkcia, ktora vrati text chybovej spravy 

#import sys
#sys.stderr = object
a=4
def testing():
  if a>5 : return 1
  return 0
def message():
  return "Toto je chybova sprava z funkcie"

assert testing(),message()

# Ale ako spravu mozme pouzit aj premennu, ktorej hodnota
# sa nam zobrazi ako chybova sprava
a=4
txt = "Da sa to vlozit aj do premennej"
assert a>5 , txt

# Mno a tu je priklad ten najzakladnejsi,
# ktory ukazuje, ako to vlastne funguje
# Prva podmienka chybovu spravu nezobrazi
# Druha podmienka, kedze nieje splnena, tak
# chybovu spravu zobrazi

a=4
assert a<5, "Premeena nieje mensia ako pat" 
assert a>5, "Premenna nieje vacsia ako pat"


# A este pecuocka ku potlacaniu chybovych sprav
# v pythone je vsetko objekt
# cize priradme handleru sys.stderr prazdny objekt
# a tym sposobim vypis chybovej spravy nikam
# Cize asi takto

import sys
sys.stderr = object

# aj ked tento priklad nezabrani ukonceniu programu,
# aspon nevypise lavinu grcov do terminalu.
# V takom pripade by bolo ale fajn
# zabezpecit informovanie pouzivatela
# o chybach prostrednictvom funkcie zobrazujucej
# spravu v prikazoch assert

# --- end ---


