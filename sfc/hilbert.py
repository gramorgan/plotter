import turtle as t
from functools import partial
import random
import math
# from PIL import Image
from sample_image import sample_image
from pyaxidraw import axidraw

def lerp(a, b, t):
    return (1-t)*a + t*b

def remap(a, orig_lo, orig_hi, new_lo, new_hi):
    return new_lo + (new_hi - new_lo) * ((a - orig_lo) / (orig_hi - orig_lo))

def hilbert_gen(order, size, pos=t.Vec2D(0, 0), heading=t.Vec2D(0, 1)):

    def draw_hilbert(symbols, order, size):
        if order == 0:
            return
        for symbol in symbols:
            op = operations[symbol]
            yield from op(order-1, size)
    
    def forward(order, size):
        nonlocal pos
        pos += heading * size
        yield pos
    
    def right(order, size):
        nonlocal heading
        heading = heading.rotate(90)
        return
        yield

    def left(order, size):
        nonlocal heading
        heading = heading.rotate(-90)
        return
        yield

    operations = {
        'A': partial(draw_hilbert, '-BF+AFA+FB-'),
        'B': partial(draw_hilbert, '+AF-BFB-FA+'),
        'F': forward,
        '+': right,
        '-': left,
    }

    yield from draw_hilbert('A', order, size)

RADIUS = 40
def get_weight(x, y):
    cx, cy = x-50, y-50
    dist = math.hypot(cx, cy)
    if dist > RADIUS:
        return 0
    dist /= RADIUS
    return math.sqrt(1-dist*dist)

# img = Image.open('depth_maps/cross.png')
# def get_weight(x, y):
#     return max(0, remap(sample_image(img, x/100, (100-y)/100), 0.2, 1, 0, 1))

def onclick(x, y):
    t.getscreen().getcanvas().postscript(file='plain_hilbert.eps')
t.onscreenclick(onclick)

if __name__ == '__main__':
    t.tracer(500)
    t.setworldcoordinates(0, 0, 4, 4)
    t.hideturtle()
    ad = axidraw.AxiDraw()
    ad.interactive()
    ad.connect()
    ad.pendown()

    order = 7
    size = 4 / ((2 ** (order-1)) - 1)
    points_gen = hilbert_gen(order, size)
    rx = random.uniform(-1, 1)
    ry = random.uniform(-1, 1)
    for (x, y) in points_gen:
        weight = get_weight(x, y) * size * 2
        rx = lerp(rx, random.uniform(-1, 1), 0.6)
        ry = lerp(ry, random.uniform(-1, 1), 0.6)
        # x += weight*rx
        # y += weight*ry
        ad.lineto(x, y)
        t.goto(x, y)
    t.update()
    t.done()

    # ad.disconnect()
