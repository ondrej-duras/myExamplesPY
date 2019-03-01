#!/usr/bin/env python2
# 20190228, dury
# ~/prog/Socket-UDP-TCP/003-any-Caller-inspect.py
# ~/prog/py-priklady/072-any-Caller-inspect.py

import inspect

def f1():
  print "hello from f1()"
  print "going to call f2()"
  f2()
  print "bye from f1()"

def f2():
  print "hello from f2() ...a caller detector"
  current_frame = inspect.currentframe()
  caller_frame  = inspect.getouterframes(current_frame,2)
  print "caller name ...... "+str(caller_frame[1][3])
  print "caller line ...... "+str(caller_frame[1][2])
  print "caller file ...... "+str(caller_frame[1][1])
  # print ""
  # print "All details from stack\n===================="
  # print caller_frame  # velmi neprehladne
  print "bye from f2()"

f1()

# --- end ---

