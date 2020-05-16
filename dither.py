from plot import Plot
from PIL import Image
import random

def luminance(r, g, b):
    return 0.2126*r + 0.7152*g + 0.0722*b

def main(p: Plot, img_filename):
    p.plot_size = 6
    p.setup()

    img = Image.open(img_filename)
    max_res = 250
    max_size = max(img.width, img.height)
    img = img.resize( (round(max_res*img.width/max_size), round(max_res*img.height/max_size)) )

    pixels = [luminance(*c) for c in img.getdata()]

    def getpix( r, c ):
        return pixels[ r * img.width + c ]

    def setpix( r, c, col ):
        pixels[ r * img.width + c ] = col

    def find_closest_palette_color(col):
        return 255 if col > 127 else 0

    for r in range(1,img.height-1):
        print('row {}/{}'.format(r, img.height-2))
        for c in range(1,img.width-1):
            oldpixel = getpix(r, c)
            newpixel = find_closest_palette_color(oldpixel)
            if newpixel == 0:
                x = (c/max_res) * 100 + random.uniform(-0.1, 0.1)
                y = (r/max_res) * 100 + random.uniform(-0.1, 0.1)
                p.dot(x, y)
            quant_error = oldpixel - newpixel
            setpix(r  , c+1, getpix(r  , c+1) + quant_error * 7/16)
            setpix(r+1, c-1, getpix(r+1, c-1) + quant_error * 3/16)
            setpix(r+1, c  , getpix(r+1, c  ) + quant_error * 5/16)
            setpix(r+1, c+1, getpix(r+1, c+1) + quant_error * 1/16)
