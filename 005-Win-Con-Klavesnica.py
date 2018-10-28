#!/usr/bin/env python2
# --- Win32 only ! ---

import sys        # systemove veci - teraz vlastne len sys.exit
if not sys.platform == 'win32':
  print "Runs with the Windows only !"
  exit()

import colorama   # unixove farbicky v okne
import msvcrt     # praca s Windows oknom Console
import time       # sleep - cakanie aby sa program nezblaznil


colorama.init()
print "\n\n\n\n\033[1;31mProgram mozno ukoncit stlacenim klavesy \033[1;33m'Q'\033[m"


ch = "x"
while True:
  time.sleep(0.1)
  if msvcrt.kbhit():
     ch = msvcrt.getch()
     xx = ord(ch)
     if xx == 224:
       cq = msvcrt.getch()
       xq = ord(cq)
       print "\033[1;36mSlacil si specialnu klavesu %c %03d , %c %03d\033[m" % (ch,xx,cq,xq)
     else:
       print "\033[1;32mStlacil si .... %c %03d\033[m" % (ch,xx)
  else:
     print "\033[1;35mNic nieje stlacene.\033[m"
  if ch == ' ':
    print "\033[1;33mPauzicka ...\033[m"
    ch = 'x'
    time.sleep(3)
  if ch == 'q':
    print "\033[0;33mKoniec programu.\033[m"
    sys.exit(0)

