#!/usr/bin/env python2
# hello.py - The first attempt to write something in Python
# 20170126, Ing. Ondrej DURAS (dury)
# ~/prog/Socket-UDP-TCP/074-UDP-Hello.py


## MANUAL ############################################################# {{{ 1

VERSION = 2019.030301
MANUAL  = """
NAME: UDP Hello Template
FILE: 074-UDP-Hello.py
FILE: udp-hello

DESCRIPTION:
  A simple example how to write small UDP scripts.
  It contains both parts, the server and client as well.


USAGE:
  074-UDP-Hello.py --recv
  074-UDP-Hello.py --send 10
  074-UDP-Hello.py --send 10 --stop
  074-UDP-Hello.py --send 10 --stop --addr 1.1.1.1 -port 1188
  074-UDP-Hello.py --reply
  074-UDP-Hello.py --reply -bind 1.1.1.4 -port 1188
  074-UDP-Hello.py --echo 10 --stop
  074-UDP-Hello.py --proxy 1188 -addr 1.1.1.7 -port 1177


PARAMETERS:
  --port 1177         - UDP port for both sending/listening (default 1177)
  --addr 1.1.1.1      - destination IP for -send/-echo is 1.1.1.1
  --bind 1.1.1.1      - IP address for listening -recv / -reply
  --recv              - acting as a server, receiving and displaying 
                        packets till "stop" message is received
  --reply             - acting as a server, receiving and replying 
                        packets till "stop" message is received
  --echo 10           - acting as a client, sending 10 packets
                        After each packet the script waits for reply (2sec).
  --proxy 1177        - acting as a bidirectional forwarder
                        Mandatory argument is a port on which it listens
  --fwd 1177          - acting as an uniderectional forwarder.
                        Mandatory argument is a port on which it listens
  --send 10           - acting as a client, sending 10 echo packets
  --mesg "My message" - acting as a client, sending message
  --stop              - sends an "stop" message to server
  

SEE ALSO:
  https://wiki.python.org/moin/UdpCommunication
  https://github.com/ondrej-duras/

VERSION: %s  
""" % (VERSION)

####################################################################### }}} 1
## DEFAULTS ########################################################### {{{ 1

import sys
import os
import re
import socket
import time

MODE_DEBUG = "" # Filter of troubleshooting messages
MODE_COLOR = 2  # TTY colors 0=OFF 1=ON 2=TBD
TEST_ECHO  = [] # message to be displayed on STDOUT
UDP_ADDR   = "127.0.0.1"   # Address where we send data
UDP_BIND   = "0.0.0.0"     # Address where we listen for data
UDP_PORT   = 1177          # UDP port -//-
UDP_PROXY  = 1177          # UDP port for listeny, when script works as proxy
UDP_COUNT  = 10            # client counter, how much packets to send -1=never_ending
UDP_SENT   = 0             # counter of how many packets have been sent already
UDP_RECV   = 0             # counter of how many packets have been received already
UDP_MODE   = "none"        # mode of operation "send/recv/echo/reply"
UDP_STOP   = False         # whether client should send "stop' message or not
UDP_MISS   = []            # missing sequences (sent but not received yet)
UDP_LAST   = 0             # sequence number of the last received packet
UDP_DONE   = 0             # sequence number of the last received packet, where is none previous packet missing
UDP_FORGIVE= 10            # how many packet must be received in seuence to forget/forgive missing sequences 
UDP_MESG   = "echo"        # message to be send via -mesg

# Unix ANSI TTY Escape prefixes with Windows as well
if sys.platform == "win32":   
  try:
    import colorama
    colorama.init()
  except:
    MODE_COLOR = 0

####################################################################### }}} 1
## PROCEDURES ######################################################### {{{ 1


TEST_COLOR = """
#: debug
#+ pass
#- fail
#_ info
#! intrusive
#. confidential
## highlight
#& status
#? prompt
#> interaction
<< received
>> send
<> issue
"""


def color(msg):
  global MODE_COLOR
  if not MODE_COLOR: return msg
  msg = re.sub(r"^(#:.*)$", "\033[0;33m\\1\033[m",msg,re.M)     # debug
  msg = re.sub(r"^(#-.*)$", "\033[1;31m\\1\033[m",msg,re.M)     # warning/error
  msg = re.sub(r"^(#\+.*)$","\033[0;36m\\1\033[m",msg,re.M)     # success
  msg = re.sub(r"^(#\&.*)$","\033[1;33m\\1\033[m",msg,re.M)     # status
  msg = re.sub(r"^(#_.*)$", "\033[0;36m\\1\033[m",msg,re.M)     # notice
  msg = re.sub("^(#\>.*)$", "\033[1;36m\\1\033[m",msg,re.M)     # interaction
  msg = re.sub("^(\>\>.*)$", "\033[0;32m\\1\033[m",msg,re.M)    # sent
  msg = re.sub("^(\<\<.*)$", "\033[0;32m\\1\033[m",msg,re.M)    # received
  msg = re.sub("^(\<\>.*)$", "\033[0;31m\\1\033[m",msg,re.M)    # issue
  msg = re.sub(r"^(#\?.*)$", "\033[1;35m\\1\033[m",msg,re.M)    # prompt
  msg = re.sub(r"^(##.*)$", "\033[1;37m\\1\033[m",msg,re.M)     # highlight
  msg = re.sub(r"^(#\..*)$", "\033[0;34m\\1\033[m",msg,re.M)    # confidential
  msg = re.sub(r"^(#\!.*)$", "\033[1;37;41m\\1\033[m",msg,re.M) # intrusive
  return msg

def strip(msg,mode=2):
  global MODE_COLOR
  if mode == 2: mode=MODE_COLOR
  if mode: return msg
  return re.sub(r"\033[[;0-9]+[mHJ]","",msg)

def debug(msg="DEBUG"):
  global MODE_DEBUG
  if not MODE_DEBUG : return
  if not re.match(MODE_DEBUG,msg): return
  print color("#: "+msg)

def warn(msg="Warning!"):
  print color("#- "+msg)

def good(msg="Good."):
  print color("#+ "+msg)

def die(msg="Error!",code=1):
  if msg: warn(msg)
  sys.exit(code)

def done(msg="Done.",code=0):
  if msg: good(msg)
  sys.exit(code)


####################################################################### }}} 1
## DUMP ############################################################### {{{ 1

def dump():
  print color("#: VERSION ........ %s" % (VERSION  ))
  print color("#: UDP_ADDR ....... %s" % (UDP_ADDR )) 
  print color("#: UDP_BIND ....... %s" % (UDP_BIND )) 
  print color("#: UDP_PORT ....... %u" % (UDP_PORT ))
  print color("#: UDP_PROXY ...... %u" % (UDP_PROXY))
  print color("#: UDP_COUNT ...... %u" % (UDP_COUNT))
  print color("#: UDP_SENT ....... %u" % (UDP_SENT ))
  print color("#: UDP_RECV ....... %u" % (UDP_RECV ))
  print color("#: UDP_MODE ....... %s" % (UDP_MODE ))
  print color("#: UDP_STOP ....... %r" % (UDP_STOP ))
  print color("#: UDP_MESG ....... %s" % (UDP_MESG ))

####################################################################### }}} 1
## INTERFACE ########################################################## {{{ 1
  
def interface():
  global MODE_COLOR, MODE_DEBUG, UDP_MODE, UDP_ADDR, UDP_BIND, UDP_PORT 
  global UDP_COUNT, UDP_STOP, UDP_MESG, UDP_PROXY

  # handling command-line parameters
  idx = 0; rang = len(sys.argv)-1
  while idx < rang:
    idx += 1
    argx=sys.argv[idx]
    debug(str(idx)+" : "+argx)
    if re.match("-+col",argx):     MODE_COLOR = 1;    continue  # --color
    if re.match("-+deb",argx):     MODE_DEBUG = ".*"; print "debug"; continue # --debug
    if re.match("-+Deb",argx):     MODE_DEBUG=sys.argv[idx+1]; idx=idx+1; continue # --Debug <filter>
    if re.match("-+no-?col",argx): MODE_COLOR = 0;    continue # --no-color
    if re.match("-+no-?deb",argx): MODE_DEBUG = "";   continue # --no-debug

    if re.match("-+reply", argx):  UDP_MODE="reply"; continue  # --reply
    if re.match("-+proxy", argx):  UDP_MODE="proxy"; UDP_PROXY=int(sys.argv[idx+1]); idx=idx+1;  continue  # --reply
    if re.match("-+fwd",   argx):  UDP_MODE="fwd";   UDP_PROXY=int(sys.argv[idx+1]); idx=idx+1;  continue  # --reply
    if re.match("-+stop",  argx):  UDP_STOP=True;    continue  # --stop
    if re.match("-+echo",  argx):  UDP_MODE="echo";  UDP_COUNT=int(sys.argv[idx+1]); idx=idx+1; continue  # --echo <number>
    if re.match("-+send",  argx):  UDP_MODE="send";  UDP_COUNT=int(sys.argv[idx+1]); idx=idx+1; continue  # --send <number>
    if re.match("-+mesg",  argx):  UDP_MODE="mesg";  UDP_MESG =str(sys.argv[idx+1]); idx=idx+1; continue  # --send <number>
    if re.match("-+recv",  argx):  UDP_MODE="recv";  continue  # --recv <number>
    if re.match("-+addr",  argx):  UDP_ADDR=sys.argv[idx+1]; idx=idx+1; continue  # --addr <ip>
    if re.match("-+bind",  argx):  UDP_BIND=sys.argv[idx+1]; idx=idx+1; continue  # --addr <ip>
    if re.match("-+port",  argx):  UDP_PORT=int(sys.argv[idx+1]); idx=idx+1; continue  # --recv <port>
    warn("Wrong parameter '%s' !" % (argx))  # command-line syntax error handling

  # Handling TTY colors  
  if MODE_COLOR == 2:
    if sys.stdout.isatty(): MODE_COLOR = 1
    else:                   MODE_COLOR = 0


####################################################################### }}} 1
## SEND & MESG ###################################################### {{{ 1


def myMesg():
  global UDP_MESG,UDP_ADDR,UDP_PORT
  sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  sock.sendto(UDP_MESG,(UDP_ADDR,UDP_PORT))
  print color(">> UDP sent \"%s\" to %s:%u" % (UDP_MESG,UDP_ADDR,UDP_PORT))
  sock.close()


def mySend():
  global UDP_SENT,UDP_ADDR,UDP_PORT
  sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  for UDP_SENT in range(1,UDP_COUNT+1):
    UTIME   = int(round(time.time() * 1000))
    message = "echo %u [%u]" % (UDP_SENT,UTIME)
    sock.sendto(message,(UDP_ADDR,UDP_PORT))
    print color(">> UDP sent \"%s\" to %s:%u" % (message,UDP_ADDR,UDP_PORT))
  sock.close()

####################################################################### }}} 1
## STOP ############################################################### {{{ 1

def myStop():
  global UDP_SENT,UDP_ADDR,UDP_PORT
  sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  UDP_SENT += 1
  sock.sendto("stop "+str(UDP_SENT),(UDP_ADDR,UDP_PORT))
  print color(">> UDP message 'stop' sent to "+UDP_ADDR+":"+str(UDP_PORT))
  sock.close()

####################################################################### }}} 1
## RECV ############################################################### {{{ 1

def myRecv():
  global UDP_RECV,UDP_BIND,UDP_PORT
  sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  sock.bind((UDP_BIND,UDP_PORT))
  print color("#+ UDP Listening on %s:%u" % (UDP_BIND,UDP_PORT))
  NEXT = True
  while NEXT:
    data, sender = sock.recvfrom(1024)
    UDP_RECV += 1
    print color("<< UDP received \"%s\" from %s:%u as seq %u" % (data,sender[0],sender[1],UDP_RECV))
    if re.match("^stop .*",data) : NEXT=False
  print color("#+ UDP message 'stop' received")
  sock.close()

####################################################################### }}} 1
## REPLY ############################################################## {{{ 1

def myReply():
  global UDP_RECV,UDP_BIND,UDP_PORT
  sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  sock.bind((UDP_BIND,UDP_PORT))
  print color("#+ UDP Listening on %s:%u" % (UDP_BIND,UDP_PORT))
  print color("#+ UDP Starting to reply ...")
  NEXT = True
  while NEXT:
    data, sender = sock.recvfrom(1024)
    UDP_RECV += 1
    sock.sendto(data,sender)
    if re.match("^stop .*",data) : NEXT=False
  print color("#+ UDP message 'stop' received and forwarded")
  print color("#+ UDP replied %u packets" % (UDP_RECV))
  sock.close()


####################################################################### }}} 1
## PROXY - bidir forward ############################################## {{{ 1

def myProxy():
  global UDP_RECV,UDP_SENT,UDP_ADDR,UDP_PORT,UDP_BIND,UDP_PROXY
  send = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  recv = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  send.settimeout(2)
  recv.bind((UDP_BIND,UDP_PROXY))
  print color("#+ UDP Listening on  %s:%u" % (UDP_BIND,UDP_PROXY))
  print color("#+ UDP Forwarding to %s:%u" % (UDP_ADDR,UDP_PORT))
  print color("#+ UDP Starting to fotward ...")
  NEXT = True
  while NEXT:
    data1, sender1 = recv.recvfrom(1024)
    send.sendto(data1,(UDP_ADDR,UDP_PORT))
    UDP_SENT += 1
    data2, sender2 = send.recvfrom(1024)
    UDP_RECV += 1
    recv.sendto(data2,sender1)
    if re.match("^stop .*",data2) : NEXT=False
    print color(">> UDP forwarded \"%s\" from %s:%u to %s:%u as seq %u" 
          % (data2,sender1[0],sender1[1],sender2[0],sender2[1],UDP_RECV))
  print color("#+ UDP message 'stop' received and forwarded")
  print color("#+ UDP bidirectionaly forwarded %u packets" % (UDP_RECV))
  send.close()
  recv.close()


####################################################################### }}} 1
## FWD - unidir forward ############################################### {{{ 1

def myForward():
  global UDP_RECV,UDP_SENT,UDP_ADDR,UDP_PORT,UDP_BIND,UDP_PROXY
  send = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  recv = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  send.settimeout(2)
  recv.bind((UDP_BIND,UDP_PROXY))
  print color("#+ UDP Listening on  %s:%u" % (UDP_BIND,UDP_PROXY))
  print color("#+ UDP Forwarding to %s:%u" % (UDP_ADDR,UDP_PORT))
  print color("#+ UDP Starting to fotward ...")
  NEXT = True
  while NEXT:
    data1, sender1 = recv.recvfrom(1024)
    send.sendto(data1,(UDP_ADDR,UDP_PORT))
    UDP_SENT += 1
    #data2, sender2 = send.recvfrom(1024)
    UDP_RECV += 1
    #recv.sendto(data2,sender1)
    if re.match("^stop .*",data1) : NEXT=False
    print color("<< UDP forwarded \"%s\" from %s:%u as seq %u" 
          % (data1,sender1[0],sender1[1],UDP_RECV))
  print color("#+ UDP message 'stop' received and forwarded")
  print color("#+ UDP unidirectionaly forwarded %u packets" % (UDP_RECV))
  send.close()
  recv.close()


####################################################################### }}} 1
## ECHO ############################################################### {{{ 1

def myEcho():
  global UDP_ADDR,UDP_BIND,UDP_PORT
  global UDP_SENT, UDP_RECV
  sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  sock.settimeout(2)

  for UDP_SENT in range(1,UDP_COUNT+1):
    UTIME   = int(round(time.time() * 1000))
    message = "echo %u [%u]" % (UDP_SENT,UTIME)

    # sending a message
    try:
      sock.sendto(message,(UDP_ADDR,UDP_PORT))
    except:
      print color("<> UDP failed to send ...... \"%s\" to %s:%u" % (message,UDP_ADDR,UDP_PORT))
      # print "Unexpected error:", sys.exc_info()[0]
    else:
      print color(">> UDP sent ....... \"%s\" to   %s:%u" % (message,UDP_ADDR,UDP_PORT))

    # receiving a message
    try:
      recvdata, sender = sock.recvfrom(1024)
      UDP_RECV += 1
    except:
      print color("<> UDP failed to receive a packet.") 
    else:
      print color("<< UDP received ... \"%s\" from %s:%u at [%u] as seq %u" 
            % (recvdata,sender[0],sender[1],UTIME,UDP_RECV))

  sock.close()

####################################################################### }}} 1
## MAIN ############################################################### {{{ 1

def main():
  interface()
 
  dump()
  if UDP_MODE == "mesg"  : myMesg()
  if UDP_MODE == "send"  : mySend()
  if UDP_MODE == "recv"  : myRecv()
  if UDP_MODE == "reply" : myReply()
  if UDP_MODE == "proxy" : myProxy()
  if UDP_MODE == "fwd"   : myForward()
  if UDP_MODE == "echo"  : myEcho()
  if UDP_STOP            : myStop()  # musi byt na konci :-)
  done()

if __name__ == "__main__":
  main()

####################################################################### }}} 1
# --- end ---

