#!/usr/bin/env python

from base64  import *
# http://effbot.org/tkinterbook/photoimage.htm
# https://www.base64encode.org/
obrazok = """
R0lGODlhHwAyAPcAAAAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwArZgArmQArzAAr/wBVAABV
MwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCqmQCqzACq/wDVAADV
MwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMAzDMA/zMrADMr
MzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA/zOqADOq
MzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YAAGYA
M2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaA
M2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/
M2b/Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlV
M5lVZplVmZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnV
M5nVZpnVmZnVzJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwr
M8wrZswrmcwrzMwr/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyq
M8yqZsyqmcyqzMyq/8zVAMzVM8zVZszVmczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8A
M/8AZv8Amf8AzP8A//8rAP8rM/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+A
M/+AZv+Amf+AzP+A//+qAP+qM/+qZv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//
M///Zv//mf//zP///wAAAAAAAAAAAAAAACH5BAEAAPwALAAAAAAfADIAAAj/AJUJHEiwoMGD
BOkJVKiMocOFEBtGZKgMgQCLGC9qzMhxo0dlFxGIHClSBo4w8OCpAyaDpEsELemVFNCSxYMc
aZAdUxmmJ7CZNWGGrOjyBxBQzlRiSvPAoi6ML4XKpCkgwY84yvDBCwYq1B0gORAsgjlTJIuR
REXmuAPtnrpdQIAYiWMHyAMxGBVE27dPHxeRF+iFnGFEmdtdOVrm+HEHDpCRCaL5jbyPC4R9
FRWDigdvl4OMV+EYyUHzyL5hF02zM01UwI+kwkYDMWr0Thw4TRHE2WdL5OV2FjCHTAZvXahQ
fbze8QrqzmiRu3mJDN4OwQCZCMQcU9ccrIXFD35A/7jZVIDpYQhYmK6OoKKAS/Aw2f4RtSXZ
yPqs4LciEnswdUDAEcpzF81w03cPhDTAXn39tRtICKhzRg5A3NHYbLPF0VhT9pEUkkhEqSPS
AwFaaKJoPyQwEk1QldTeRZGEAdMPJBphRFw0ljVSSzKEJIBMLQVDji5h4HBTDjep2KOLZ7XY
kntQfRgVAipSed+S7UUkkUQKdcnllhQ9ZBAxAhEzTCZoDkMmmWUilNBAZ0qCxiRoNILGnZNk
Mswwbw7kTpvKDEMnnWmIMcYPY4yBhiRpSJKnJHrqyaZAySiUySSYTJKGGpqEosmnn6qRBpqO
TmJqngPRQ+almaSRhibEgP8qKzGbpDEJKGeiiaYy87AZ6RhwFKMJHJRowimncHxaDBxpsMnn
pIGi+eqnxMKhxrXYJgtHrM0mQyafcBIzSbLGWovtptgiuwkcmYDi7ULEJKPJMEBQe20a9fLF
bLrk6gAtnOSaey0cfO0TihpGoUtuGspMqqYyOax7b4AF70MMEGpgnIa1cGzyw0Gg6DCsGhxX
HA3Cs2U8sCY6gNvmJD9YCxbBFSOcLYUDA5FJqsrok0YOOuSwWD0VF10wUzmokcMYFClTzxgJ
5JDADMsYbbUmUz8wQBqYNawMNJMkIPZNylhdMcRSiz1J2RLtk8kAUR+5jD716LMMjQ884EDe
ec/1IHYm+9QzkOACIJnDeDkoE43TyjClgw4QAP2ADgkSA03XPUcjAwQQ6FABEJETpAkEHABh
Aeji5YADX4IrRIzbUZ8u+w+aNKyJ7KZboIMFA2RSN+b0RFOPDLIfYcERs2mSyQ9HNH+86UDI
wODik1qMgPFHGNG8jXJln30HQByBgCZ9EQ3m5WHH0XwT6rPv/hHqiw/42QVVnQkCcJiov4ns
IzAJ6wUrk0P2ogkZPMBCfdifHXJwA/IV7HKYoUcyvCaQ32UCBwigkGPog4P/GY1tPCPI7wI1
qExUjS+MCyG0hkGRZTSEQWVrGkIYMkE3aUlMfxJIQAAAOw==
"""

from Tkinter import *
#from PIL import Image, ImageTk

okno = Tk()

#photo = PhotoImage(file="Untitled.gif")
#photo = PhotoImage(file="lenna.pgm")
#bin_obrazok = b64decode(obrazok)
#photo = PhotoImage(data=bin_obrazok)

photo = PhotoImage(data=b64decode(obrazok))

# PIL - ine ako gif/pgm
#image = Image.open("lenna.jpg")
#photo = ImageTk.PhotoImage(image)



label = Label(okno,image=photo)
#label.image = photo # pouzitelne ak chceme napr zmenit obrazok.
label.pack()

mainloop()

