# --- Win32 only ! ---

import colorama   # unixove farbicky v okne
import msvcrt     # praca s Windows oknom Console
import time       # sleep - cakanie aby sa program nezblaznil
import sys        # systemove veci - teraz vlastne len sys.exit

colorama.init()

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

