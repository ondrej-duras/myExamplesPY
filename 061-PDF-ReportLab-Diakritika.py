#!/usr/bin/env python2
#coding: utf-8 

filename = "062-PDF-ReportLab-VstupText.txt"

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Times-Roman', 'Times.ttf'))
pdfmetrics.registerFont(TTFont('Courier', 'cour.ttf'))

c = canvas.Canvas("063-PDF-ReportLab-Output.pdf", pagesize=A4)
c.setFont("Times-Roman", 20)
c.drawString(100,100,"Hello World")
c.drawString(100,130,u'Mačiatko má rado mäsko.')
c.setFont("Courier", 17)
c.drawString(20,160,u"Žriebätko vyskočilo na stôl.")
c.drawString(20,190,unicode(u"Čučoriedka zmäkla málo.").strip())
c.drawString(20,220,unicode(u"Ňoňoňo. či ľúbia tie ťaŤapôčučky").strip())
c.drawString(20,250,unicode(u"\x61\x62šmudlíčok ? Žužlia ďuĎubky.").strip())
c.showPage()



pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
c.setFont("Verdana", 8)
i=400
try:
  file=open(filename,"r")
  for line1 in file:
    line2=line1.rstrip()
    c.drawString(20,i,line2)
    i=i-30
    if i<=0: break
  file.close
except:
  print "make a file %s with some UTF-8 CE characters !" % (filename)

c.showPage()
c.save()

