#!/bin/env python

x = 7
y = 7

if x < y :
  print "Hello world 1.";

  print "Ok. now.";

elif x > y :
  print "x > y"

else:
  print "x == y :-)"

  print "Asi sa teda rovnaju"

print "done.";


l = [ 'a','b','c','a']
print "Dlzka pola je " + str(len(l))
if 'a' in l:
  print "'a' je v zozname :-)"

l.append('d')
l.remove('a')

for x in l:
  print x

