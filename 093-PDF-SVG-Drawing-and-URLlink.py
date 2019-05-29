#!/usr/bin/env python2
# svg_on_canvas.py

# https://www.blog.pythonlibrary.org/2018/04/12/adding-svg-files-in-reportlab/
# plus treba instalovat svglib3 (na PC), alebo svglib na inych platformach
# vyzera to byt kompatibilne
 
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from svglib.svglib import svg2rlg
 
def add_image(img_path,doc_path):
    my_canvas = canvas.Canvas(doc_path)
    drawing = svg2rlg(img_path)
    my_canvas.drawString(50, 820, 'Moj SVG Obrazok')
    renderPDF.draw(drawing, my_canvas, 50, 770)
    my_canvas.drawString(50, 750, 'A nejakyy pokec')
    my_canvas.drawString(50, 700, "SVG obrazky najdes aj na ")

    my_canvas.saveState()
    my_canvas.setStrokeColorRGB(0,0,1)
    my_canvas.setFillColorRGB(0,0,1)
    my_canvas.drawString(50, 670, "https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/")
    sirka=my_canvas.stringWidth("https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/")
    my_canvas.linkURL("https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/",(50,670,350,700))
    my_canvas.restoreState()
   
    my_canvas.drawString(50,300,"Alebo si dobre SVG nakreslis v programe Dia")  # ma predoslu (ciernu) farbu :-)
    drawing2 = svg2rlg('095-Diagram1.svg')
    renderPDF.draw(drawing2, my_canvas, 50, 170)
    my_canvas.save()
 
if __name__ == '__main__':
    img_path = '091-IETF-Sample.svg'
    doc_path  = '094-PDF-SVGdrawing-URLlink.pdf'
    add_image(img_path,doc_path)

# --- end ---

