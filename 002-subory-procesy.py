#!/bin/env python

# none import necesary
fh=open("DATA.txt","w")
fh.write("hello 1\n")
fh.write("hello 2\n")
fh.write("hello 3\n")
fh.close()

import os
import sys
import subprocess


#print "DATA.txt dump ..."
#print subprocess.Popen("cat DATA.txt",shell=True,stdout=subprocess.PIPE).stdout.read()
#subprocess.call(["/bin/cat","DATA.txt"])
#os.system("cat DATA.txt")

if os.path.isfile("DATA.txt"):
  print("Deleting file DATA.txt")
  #os.remove("DATA.txt")
  os.unlink("DATA.txt")
else:
  print("DATA.txt does not exist !")

# Osetrovanie platforiem
if sys.platform == "win32":
  # ComSpec=C:\windows\system32\cmd.exe
  SHELL=os.environ["ComSpec"]
else:
  # SHELL=/bin/bash
  SHELL=os.environ["SHELL"]

# Odstartovanie (pod)programu
# a nasmerovanie jeho STDIN a STDOUT do trubiek
p = subprocess.Popen(
  [SHELL],
  stdin=subprocess.PIPE,
  stdout=subprocess.PIPE
)

# komunikacia s (pod)programom
# zadanie uloh
p.stdin.write("echo 'hello world'\n")
p.stdin.write("exit\n")
p.stdin.close()

# Komunikacia s (pod)programom
# spracovanie vysledkov
for line in p.stdout:
  if line == "":
    break
  print("1> " + line.rstrip())
p.stdout.close()

