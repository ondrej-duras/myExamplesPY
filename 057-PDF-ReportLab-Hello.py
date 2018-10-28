#!/usr/bin/env python2
#coding: utf-8 
from reportlab.lib.pagesizes import A5
from reportlab.pdfgen import canvas
c = canvas.Canvas("058-PDF-ReportLab-Hello.pdf", pagesize=A5)
c.setFont("Times-Roman", 20)
c.drawString(100,100,"Hello World")
c.drawString(100,130,u'Mačiatko má rado mäsko.')
c.setFont("Courier", 17)
c.drawString(20,160,u"Žriebätko vyskočilo na stôl.")
c.drawString(20,190,unicode(u"Čučoriedka zmäkla málo.").strip())
c.drawString(20,220,unicode(u"Ňoňoňo. či ľúbia tie ťaŤapôčučky").strip())
c.drawString(20,250,unicode(u"\x61\x62šmudlíčok ? Žužlia ďuĎubky.").strip())
c.showPage()
c.save()

