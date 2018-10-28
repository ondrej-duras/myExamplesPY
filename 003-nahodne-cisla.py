#!/usr/bin/env python2

# from random import *
# from random import randint ... :-)
# random()                  # float 0.0 <= x <= 1.0
# uniform(1,10)             # float 1.0 <= x <= 10.0
# randint(1,10)             # integer 1 <= x <= 10
# randrange(0,101,2)        # "even"=parny .. teda delitelny "2"-oma z rozsahu 0..101 
# choise('abcdefghi')       # lubovolny prvok z pola
# shuffle([1,2,3,4,5,6,7])  # vsetky prvky pola ovsem v lubovolnom poradi
# sample([1,2,3,4,5,6,7],3) # vzorka troch lubovolnych prvok z pola

import random

print random.random()
print random.uniform(1,10)
print random.randint(1,10)
print random.randrange(0,101,2)
print random.choice('abcefghijklmn')
print random.sample([1,2,3,4,5,6,7],7)


pole=[];
for y in range(0,7,1):
  pole.append([])
  for x in range(0,10,1):
    pole[y].append(random.choice("XxyYAaBb. "))
 

print pole;

print pole[2][2];

