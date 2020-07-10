#!/usr/bin/env python2
#=vim color desert

import re

def Option(input,*options):
  ct=int(len(options)/2)
  #print "ct=%u" % (ct)  #DEBUG
  for ix in range(0,ct,1):
    pt=ix*2
    #print "ix=%u regx=%s return=%s" % (pt,options[pt],options[pt+1]) #DEBUG
    if re.search(options[pt],input):
      return options[pt+1]
  return ""

#SITE_ID="X-937-ZA"
SITE_ID="X-938-MT"
#SITE_ID="X-521-LM"
print Option(SITE_ID,"-ZA",65051,"-MT",65072,"-LM",65024)                         # Private I-BGP AS number
print Option(SITE_ID,"-ZA","P-936-ZA-RR-401","-MT","P-938-MT-RR-431","-LM","P-521-LM-RR-311") # Primary   PE Router HostName
print Option(SITE_ID,"-ZA","P-937-ZA-RR-402","-MT","P-939-MT-RR-432","-LM","P-522-LM-RR-312") # Secondary PE Router HostName
print Option(SITE_ID,"-ZA","P-936-ZA-RS-401","-MT","P-938-MT-RS-431","-LM","P-521-LM-RS-311") # Primary   Core Switch HostName
print Option(SITE_ID,"-ZA","P-937-ZA-RS-402","-MT","P-939-MT-RS-432","-LM","P-522-LM-RS-312") # Secondary Core Switch HostName
print Option(SITE_ID,"-ZA","Q-936-ZA-FW-401","-MT","Q-938-MT-FW-431","-LM","Q-521-LM-FW-311") # Primary   Core FireWall HostName
print Option(SITE_ID,"-ZA","Q-937-ZA-FW-402","-MT","Q-939-MT-FW-432","-LM","Q-522-LM-FW-312") # Secondary Core FireWall HostName

# --- end ---

