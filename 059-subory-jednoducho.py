#!/usr/bin/env python2

file=open("060-subory-data.txt","w")
file.write("Hello world !\n")
file.write("sometihng more\n")
file.write("even sometihng more again\n")
file.close()

i=1
file=open("060-subory-data.txt","r")
for line1 in file:
  line2=line1.rstrip()
  print "%05u %s" % (i,line2)
  i=i+1
file.close

