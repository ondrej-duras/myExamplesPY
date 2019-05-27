#!/usr/bin/env python2
#=vim high Comment ctermfg=brown

## Manual ############################################################# {{{ 1

VERSION = 2019.052601
MANUAL  = """
NAME: Config to PDF exporter
FILE: cfg2pdf
FILE: 085-PDF-ReportLab-Code2PDF.py

DESCRIPTION:
  Convers Configuration Implementation Procedure File into PDF.
  For now it's very simple exporter.
  In future it may accept s few POD tags, line =CODE =TEXT =LABEL etc.

USAGE:
  cfg2pdf -i CRQ123.txt -o CRQ123-4DNO.pdf

PARAMETERS:
  -i   --input file
  -o   --output file

SEE ALSO:
  https://github.com/ondrej-duras

VERSION: %s 
""" % (VERSION)

####################################################################### }}} 1
## Defaults and Packages `############################################# {{{ 1

import sys
import re


from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


MODE_COLOR = 2
MODE_DEBUG = ""

FILE_INPUT  = ""
FILE_OUTPUT = ""
fhin  = None
fhout = None


####################################################################### }}} 1
## Initiation ######################################################### {{{ 1

# That registers a font ...but also it attaches whole font into the PDF file
# .... so PDF file size increases significanly with each font used.
pdfmetrics.registerFont(TTFont('Courier', 'cour.ttf'))
#pdfmetrics.registerFont(TTFont('Times', 'Times.ttf'))
pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
#pdfmetrics.registerFont(TTFont('Bookman', 'BOOKOS.TTF'))

# A4: sirka=595 vyska=841
pageWidth,pageHeight=A4
#print "vyska=%i sirka=%i" % (height,width)


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


####################################################################### }}} 1
## CLI Interface ###################################################### {{{ 1

def interface():
  global MODE_COLOR, MODE_DEBUG
  global MANUAL, FILE_INPUT, FILE_OUTPUT

  # when no command-line parameters given, show the manual
  if len(sys.argv) < 2:
    print MANUAL
    exit(0)

  # handling command-line parameters
  idx = 1;
  while idx < len(sys.argv):
    argx=sys.argv[idx]; idx=idx+1
    #debug(str(idx)+" : "+argx)
    if re.match("-+i",argx):     FILE_INPUT  = sys.argv[idx]; idx=idx+1; continue # --input
    if re.match("-+o",argx):     FILE_OUTPUT = sys.argv[idx]; idx=idx+1; continue # --output
    if re.match("-+c",argx):     MODE_COLOR = 1;    continue  # --color
    if re.match("-+d",argx):     MODE_DEBUG = ".*"; print "debug"; continue # --debug
    if re.match("-+D",argx):     MODE_DEBUG=sys.argv[idx+1]; idx=idx+1; continue # --Debug <filter>
    if re.match("-+no-?c",argx): MODE_COLOR = 0;    continue # --no-color
    if re.match("-+no-?d",argx): MODE_DEBUG = "";   continue # --no-debug
    if re.match("-+e",argx):     TEST_ECHO.append(sys.argv[idx+1]); idx=idx+1; continue  # --echo <text>
    print("Wrong parameter '%s' !" % (argx))  # command-line syntax error handling

  # Handling TTY colors  
  if MODE_COLOR == 2:
    if sys.stdout.isatty(): MODE_COLOR = 1
    else:                   MODE_COLOR = 0
  if MODE_COLOR == 1:
    try:
       import colorama
       colorama.init()        
    except:
       MODE_COLOR = 0

####################################################################### }}} 1
## PDF Export ######################################################### {{{ 1

def pdfExport(FILE_INPUT,FILE_OUTPUT):
  global fhin,fhout

  fhin  = open(FILE_INPUT,"r")
  fhout = canvas.Canvas(FILE_OUTPUT,pagesize=A4) 

  PGNUM=1
  fhout.setStrokeColorRGB(0,0,0)
  fhout.setFillColorRGB(0,0,0)
  fhout.setFont("Courier", 10)
  bgline = 820
  DIRTY = 0
  MODE  = 'cut'

  for line in fhin:

    line = line.rstrip() # equivalent to chomp()
    if re.match("#",line): continue
    if re.match("=",line):
      # POD - Plain Old Documentation Tags 
      if re.match('=code',line):
        fhout.setStrokeColorRGB(0,0,0)
        fhout.setFillColorRGB(0,0,0)
        fhout.setFont("Courier", 10)
        MODE='code'
        continue
      if re.match('=text',line):
        fhout.setStrokeColorRGB(0,0,0.5)
        fhout.setFillColorRGB(0,0,0.5)
        fhout.setFont("Verdana", 10)
        MODE='text'
        continue
      if re.match('=page',line):
        bgline = 820
        PGNUM = PGNUM + 1
        fhout.showPage()
        DIRTY = 0
        continue
      if re.match('=cut',line):
        MODE = 'cut'
        continue
   
    if MODE == 'cut': continue 
    fhout.drawString(20,bgline,line); DIRTY=1
    bgline = bgline - 10
    if bgline < 20:
      bgline = 820
      PGNUM = PGNUM + 1
      fhout.showPage()
      DIRTY = 0

  if DIRTY: fhout.showPage()
  fhout.save()
  fhin.close()


####################################################################### }}} 1
## Main procedure ##################################################### {{{ 1

if __name__ == "__main__":
  interface()
  if (not FILE_INPUT) or (not FILE_OUTPUT):
    print "#! Error: input or output file name was not given !\n";
    exit(1)
  pdfExport(FILE_INPUT,FILE_OUTPUT)


####################################################################### }}} 1
# --- end ---
