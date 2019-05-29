#!/usr/bin/env python2
#coding: utf-8 

FN_INPUT = "INPUT.txt"
FN_OUTPUT= "OUTPUT.pdf"

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# That registers a font ...but also it attaches whole font into the PDF file
# .... so PDF file size increases significanly with each font used.
pdfmetrics.registerFont(TTFont('Courier', 'cour.ttf'))
pdfmetrics.registerFont(TTFont('Times', 'Times.ttf'))
pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
pdfmetrics.registerFont(TTFont('Bookman', 'BOOKOS.TTF'))

# BOOKOS.TTF   cour.ttf   arial.ttf   times.ttf   - basic
# BOOKOSB.TTF  courbd.ttf arialbd.ttf timesbd.ttf - bold
# BOOKOSBI.TTF courbi.ttf arialbi.ttf timesbi.ttf - bold italic
# BOOKOSI.TTF  couri.ttf  ariali.ttf  timesi.ttf  - italic
# lucon.ttf    - lucida console
# arimon__.ttf - arial monospaced
# arimonbd.ttf - arial monospaced bold
# BOKOS - Bookman Old Style
# times - Times New Roman

# HelvNeue35_W1G.ttf ... cislo udava hrubku ciary fontu
# HelvNeue45_W1G.ttf Helvetica font
# HelvNeue55_W1G.ttf
# HelvNeue65_W1G.ttf
# HelvNeue75_W1G.ttf


# A4: sirka=595 vyska=841
width,height=A4
print "vyska=%i sirka=%i" % (height,width)




c = canvas.Canvas(FN_OUTPUT, pagesize=A4)
c.setStrokeColorRGB(1.0,0,0)
c.line(0,0,0,841)
c.line(0,841,595,841)


c.setStrokeColorRGB(0,0,0)
c.setFillColorRGB(0,0,0)

c.setFont("Bookman",14)
c.drawString(0,820,u"Začiatok stránôčky žčňľ ĎČŠŇĽŤ")
c.setFont("Times", 20)
c.drawString(100,100,"Hello World")
c.drawString(100,130,u'Mačiatko má rado mäsko.')
c.setFont("Courier", 17)
c.drawString(20,160,u"Žriebätko vyskočilo na stôl.")
c.drawString(20,190,unicode(u"Čučoriedka zmäkla málo.").strip())
c.drawString(20,220,unicode(u"Ňoňoňo. či ľúbia tie ťaŤapôčučky").strip())
c.drawString(20,250,unicode(u"\x61\x62šmudlíčok ? Žužlia ďuĎubky.").strip())
c.showPage()


# rozmer A4 je 841 vyskovych x 595 sirkovych bodov.
# Bod [0,0] ja vlavo dole, 
# referencny bod pismena je taktiez   v lavo dole,
# cize 1. pismeno v prvom riaku o vyske 10pt je na 0,841-10 ... ak nechceme aspon nejaky okraj 
# 20pt z lava aj z hora je celkom komfortny okraj pri vyske 8pt.

#c.setFont("Verdana", 8)
c.setFont("Courier", 8)
i=820
try:
  file=open(FN_INPUT,"r")
  for line1 in file:
    line2=line1.rstrip()
    c.drawString(20,i,line2)
    i=i-9
    if i<=0: break
  file.close
except:
  print "make a file %s with some UTF-8 CE characters !" % (FN_INPUT)

c.showPage()
c.save()

