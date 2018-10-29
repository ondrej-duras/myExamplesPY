#!/usr/bin/env python2

import psutil

# Zoznam Process ID
tasklist = psutil.process_iter()

# prebehneme procesy
for proc in tasklist:

  # vyberiee si nejaky proces s PID vyssim ako 1000 (nejaky bezny proces)
  if proc.pid < 1000: continue

  # skusime ho rozanalyzovat
  # niektore atributy su dostupne iba administratorovi
  try:
    # vytvarame pole dvojic (meno,typ vlastnosti) pre vsetky vlastnosti objektu proc
    data=[(name,type(getattr(proc,name))) for name in dir(proc)]
  except:
    # ak sme narazili na "access denied", tak si pre rozbor vyberieme
    # nejaky dalsi proces
    continue

  # Atu ucinime rozbor
  for (name,vtype) in data:
    value = getattr(proc,name)
    # ak je hodnota elementu smernikom na metodu, tak prepiseme slovickom _REF
    if callable(value): value="_REF"
    # vypis vlastnosti, ziskatelnych o kazdom procese
    print "name: %s type: %s value: %s" % (name,vtype,value)
  # jeden proces takto staci.
  break

# pockame
raw_input("--enter--")

# a este raz sa pozrieme na vsetky procesy
for proc in tasklist:
  # zistime si ProcessID, Meno(.EXE suboru), 
  # vytazenie CPU a mnozstvo pamate, ktore process vyuziva
  pid = int(proc.pid)
  name = str(proc.name())
  cpu = float(proc.cpu_percent())
  mem = str(proc.memory_info().pagefile)
  print "pid: %i name: %s cpu: %5.3f mem: %s" % (pid,name,cpu,mem)

# --- end ---

