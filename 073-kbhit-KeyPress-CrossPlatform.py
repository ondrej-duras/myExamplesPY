#!/usr/bin/env python2
# CrossPlatformovy test, ci je stlacena klavesa
# ak stlacena je, tak vrati jej asci hodnotu ako cislo
# ak nieje, potom vrati cislo nula


try:
    import msvcrt
    def keypressed():
        x = msvcrt.kbhit()
        if x:
           return ord(msvcrt.getch())
        else:
           return 0
   
except ImportError:
    import termios, fcntl, sys, os
    def keypressed():
        fd = sys.stdin.fileno()
        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
        try:
            while True:
                try:
                    code = ord(sys.stdin.read(1))
                    #return True
                    return code
                except IOError:
                    return 0
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)


if __name__ == "__main__":
  import time
  print "Press Esc to quit."
  NEXT = True
  while NEXT:
    code = keypressed()
    if not code : continue
    print "pressed '%s' (%u)" % (chr(code),code)
    if code == 27 : NEXT=False

