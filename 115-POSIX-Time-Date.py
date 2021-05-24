#!/usr/bin/env python2

DEAD = 28224  # POH Power On Hours to 1st reload of Nexus
DAYS = 1176   # Power On Days

import time
import datetime

# POSIX struct tm tm;  :-) 
# (tm_year,tm_mon,tm_mday,tm_hour,tm_min,tm_sec,tm_wday,,tm_yday,tm_isdst{0,1,-1})
# tm_isdst je informacia, ci je, alebo nieje letny cas 1=je letny cas, 0=je zimny cas, -1=nevieme

a = time.strptime("2017-01-21","%Y-%m-%d")
b = time.strptime("2021-05-27","%Y-%m-%d")
c = time.strptime("2021-05-28","%Y-%m-%d")
print a  
print b

# vypocet casoveho rozdielu v sekundach medzi dvoma datumami
s = time.mktime(c)-time.mktime(b)
print "%f rozdiel v sekundach" % (s)
s = time.mktime(time.localtime())-time.mktime(a)
print s

d = ( time.mktime(time.localtime())-time.mktime(time.gmtime())) / 3600 
print "Casovy posun oproti GMT %+f hodin" % (d)


q = time.strftime("%Y-%m-%d",time.strptime("2021-05-21","%Y-%m-%d"))
print q

