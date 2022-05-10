#!/usr/bin/env python
##!/usr/bin/env python2
##!/usr/bin/env python3
## works fot both

# 1. IPv4 addhost & maskhost
# 2. ansible filters

CONFIG={ "net_a":"1.1.1.0/24", "net_b":"2.2.2.16/24", "pozdrav":"ahoj", "uprava":"KONIEC." }
TEMPLATE = """
  {{pozdrav|upper()}}
  {{net_a|addhost(2)}} {{net_b|addhost(3)}}
  {{net_a|addhost(0)}} {{net_b|addhost(3)}}
  {{net_a|maskhost(5)}} {{net_b|maskhost(0)}}
  {{uprava|lower()}}
"""
import re
import itertools

## Filters - IP math ################################################## {{{ 1

def filter_upper(text,param):
  return str(text).upper()

def filter_lower(text,param):
  return str(text).lower()


def filter_dbghost(addr_p,sft):
  # IP IP/M IP/MASK => binary_ip
  print(addr_p)
  addr_1 = re.sub("\/.*","",addr_p)
  if "/" in addr_p:
    mask = re.sub("^.*/","/",addr_p)
  else:
    mask = ""
  print(addr_1)
  print(mask)
  (a,b,c,d)=addr_1.split(".")
  print("%s %s %s %s" % (a,b,c,d))
  addr_i=((int(a)*256+int(b))*256+int(c))*256+int(d)
  print(addr_i)

  # binary_ip => string_ip
  sd=str(addr_i >>  0 & 255)
  sc=str(addr_i >>  8 & 255)
  sb=str(addr_i >> 16 & 255)
  sa=str(addr_i >> 24 & 255)
  addr_s="%s.%s.%s.%s%s" % (sa,sb,sc,sd,mask)
  print("%s >> %i >> %s" % (addr_p,addr_i,addr_s))

# nezachovana masku
def filter_addhost(addr_p,sft):
  # IP IP/M IP/MASK => binary_ip
  addr_1 = re.sub("\/.*","",addr_p)
  (a,b,c,d)=addr_1.split(".")
  addr_i=((int(a)*256+int(b))*256+int(c))*256+int(d)

  addr_i += int(sft)

  # binary_ip => string_ip
  sd=str(addr_i >>  0 & 255)
  sc=str(addr_i >>  8 & 255)
  sb=str(addr_i >> 16 & 255)
  sa=str(addr_i >> 24 & 255)
  addr_s="%s.%s.%s.%s" % (sa,sb,sc,sd)
  return addr_s

# zachovava masku
def filter_maskhost(addr_p,sft):
  # IP IP/M IP/MASK => binary_ip
  addr_1 = re.sub("\/.*","",addr_p)
  if "/" in addr_p:
    mask = re.sub("^.*/","/",addr_p)
  else:
    mask = ""
  (a,b,c,d)=addr_1.split(".")
  addr_i=((int(a)*256+int(b))*256+int(c))*256+int(d)

  addr_i += int(sft)

  # binary_ip => string_ip
  sd=str(addr_i >>  0 & 255)
  sc=str(addr_i >>  8 & 255)
  sb=str(addr_i >> 16 & 255)
  sa=str(addr_i >> 24 & 255)
  addr_s="%s.%s.%s.%s%s" % (sa,sb,sc,sd,mask)
  return addr_s

# returns ip_mask only
# example
# {{net_a}} => 10.0.0.0/8
# {{net_a|ipmask()}} => /8
# {{net_a|addhost(1)}}{{net_a|ipmask()}} => 10.0.0.1/8
def filter_ipmask(addr_p,parm):
  if "/" in addr_p:
    mask = re.sub("^.*/","/",addr_p)
  else:
    mask = ""
  return mask 

def filter_hostmask(addr_p,parm):
  if "/" in addr_p:
    mask = re.sub("^.*/","",addr_p)
  else:
    mask = ""
  return mask 



####################################################################### }}} 1
## prepareFilters ##################################################### {{{ 1

FILTERS={
  "addhost":filter_addhost,"maskhost":filter_maskhost,"ipmask":filter_ipmask,"ipaddr":filter_addhost,
  "ansible.netcommon.nthhost":filter_addhost,"ansible.netcommon.hostmask":filter_hostmask,
  "upper":filter_upper,"lower":filter_lower}
def prepareFilters(template,config,filters=FILTERS):
  OUTPUT=config.copy()
  for item in itertools.product(config.keys(),filters.keys()):
    config_key=item[0] ; config_val=config[config_key]
    filter_key=item[1] ; filter_val=filters[filter_key]
    pattern = "\\{\\{%s\\|%s\\([^)]*\\)\\}\\}" % (config_key,filter_key)
    #print("---")
    #print(pattern)
    for found in re.finditer(pattern,template):
       found_str=found.group(0)
       filter_par = re.sub(r"^.*\(","",found_str)
       filter_par = re.sub(r"\)\}\}$","",filter_par)
       filter_out = filter_val(config_val,filter_par)
       found_str = re.sub(r"^\{\{","",found_str)
       found_str = re.sub(r"\}\}$","",found_str)
       #print("%s ==> %s" % (found_str,filter_out))
       OUTPUT[found_str] = filter_out
  return OUTPUT


####################################################################### }}} 1
## prepareConfig - simple version ##################################### {{{ 1

def prepareConfigSimple(template,config):
  output = template
  for item in config.keys():
    output = output.replace("{{"+str(item)+"}}",str(config[item]))
  return output

####################################################################### }}} 1
## MAIN ############################################################### {{{ 1

if __name__ == "__main__":
  print(filter_addhost("255.255.255.255/32",0))
  print(filter_addhost("1.0.0.0/255.0.0.0",1))
  print(filter_addhost("0.1.0.0/8",513))
  print(filter_addhost("0.0.255.0/8",513))
  print(filter_addhost("0.0.0.1/16",4))
  print(filter_addhost("0.0.1.1/24",5))
  
  print(filter_maskhost("255.255.255.255/32",0))
  print(filter_maskhost("1.0.0.0/255.0.0.0",1))
  print(filter_maskhost("0.1.0.0/8",513))
  print(filter_maskhost("0.0.255.0/8",513))
  print(filter_maskhost("0.0.0.1/16",4))
  print(filter_maskhost("0.0.1.1/24",5))

  print("")
  for key in CONFIG.keys():
    val = CONFIG[key]
    print("%s => %s" % (str(key),str(val)))

  print("")
  print(CONFIG)
  print("")
  print(prepareFilters(TEMPLATE,CONFIG,FILTERS))
  print(prepareConfigSimple(TEMPLATE,CONFIG))
  print(prepareConfigSimple(TEMPLATE,prepareFilters(TEMPLATE,CONFIG,FILTERS)))

####################################################################### }}} 1


