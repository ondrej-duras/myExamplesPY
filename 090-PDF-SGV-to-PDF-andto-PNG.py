#!/usr/bin/env python2

# svg_demo.py
 
from reportlab.graphics import renderPDF, renderPM
from svglib.svglib import svg2rlg
 
 
def svg_demo(image_path, output_path):
    drawing = svg2rlg(image_path)
    print output_path + '.pdf'
    renderPDF.drawToFile(drawing, output_path + '.pdf')
    print output_path + '.png'
    renderPM.drawToFile(drawing, output_path + '.png', 'PNG')
 
 
if __name__ == '__main__':
    svg_demo('091-IETF-Sample.svg', '092-Obrazok-SinglePage')
