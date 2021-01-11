#!/usr/bin/env python2

# pip install qrcode
# pip install Pillow (import PIL ....)

import qrcode
from PIL import Image

#img = qrcode.make("Hello World!")
img = qrcode.make("skuska testu")
img.save("x.png")
print "Simple image 'x.png' has been created."

#import qrcode
qr = qrcode.QRCode(
    version=1,
    #error_correction=qrcode.constants.ERROR_CORRECT_L,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    # ERROR_CORRECT_L (7%), ERROR_CORRECT_M (15% default), 
    # ERROR_CORRECT_Q (25%), ERROR_CORRECT_H (30%)
    box_size=20,
    border=1,
)
qr.add_data('Hello World !')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
#img = qr.make_image(fill_color="teal", back_color="#d0d0d0")
imx, imy = img.size

logo = Image.open('113g-QRcode-Hello-gmail.png')
lox, loy = logo.size

#logo = logo.resize(xmin, ymin, [xmax, ymax]))
#logo = logo.resize((imx // 3, imy // 3))
#logo = logo.resize((lox * 3, loy * 3))
#img.paste(logo, ( imx // 3, imy // 3))

img.save("y.png")
print "Image 'y.png' with the gmail icon has been created."


# --- end ---



