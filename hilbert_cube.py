import turtle as t
from pyaxidraw import axidraw
import math
from functools import partial

PLOTTER_ENABLED = False

# size in inches
SIZE = 8

ad = None
if PLOTTER_ENABLED:
    ad = axidraw.AxiDraw()
    ad.interactive()
    ad.options.const_speed = True
    ad.connect()

def lerp(a, b, t):
    return a*(1-t) + b*t

def smoothstep(x, lo, hi):
    x = max(0, min(1, (x - lo) / (hi - lo)))
    return x*x * (3 - 2 * x)

def goto(x, y):
    t.penup()
    t.goto(x, y)
    if PLOTTER_ENABLED:
        t.update()
        ad.moveto((x/100)*SIZE, (y/100)*SIZE)

def lineto(x, y):
    t.pendown()
    t.goto(x, y)
    if PLOTTER_ENABLED:
        t.update()
        ad.lineto((x/100)*SIZE, (y/100)*SIZE)

def hilbert_gen(order, size, pos=t.Vec2D(0, 0), heading=t.Vec2D(0, 1)):
    inc = size / ((2 ** (order-1)) - 1)

    def draw_hilbert(symbols, order):
        if order == 0:
            return
        for symbol in symbols:
            op = operations[symbol]
            yield from op(order-1)
    
    def forward(order):
        nonlocal pos
        pos += heading * inc 
        yield pos
    
    def right(order):
        nonlocal heading
        heading = heading.rotate(90)
        return
        yield

    def left(order):
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

    yield from draw_hilbert('A', order)

def remap(point, topleft, topright, bottomleft, bottomright):
    top = (
        lerp(topleft[0], topright[0], point[0]),
        lerp(topleft[1], topright[1], point[0]),
    )
    bottom = (
        lerp(bottomleft[0], bottomright[0], point[0]),
        lerp(bottomleft[1], bottomright[1], point[0]),
    )
    return (
        lerp(top[0], bottom[0], point[1]),
        lerp(top[1], bottom[1], point[1]),
    )

def draw_warped_hilbert(topleft, topright, bottomleft, bottomright):
    goto(*topleft)
    for point in hilbert_gen(6, 1):
        x, y = remap(point, topleft, topright, bottomleft, bottomright)
        lineto(x, y)

def onclick(x, y):
    print(x, y)
t.onscreenclick(onclick)

def main():
    center = (50, 50)
    bottom = (50, 90)
    top = (71, 26)
    right = (90, 30)
    left = (11, 41)

    goto(35, 19)
    lineto(*top)
    lineto(*center)
    lineto(*left)
    lineto(35, 19)

    goto(*top)
    lineto(71, 63)
    lineto(*bottom)
    lineto(*center)

    goto(*left)
    lineto(12, 79)
    lineto(*bottom)

    draw_warped_hilbert(
        (35, 19),
        top,
        left,
        center
    )
    draw_warped_hilbert(
        left,
        center,
        (12, 79),
        bottom
    )
    draw_warped_hilbert(
        center,
        top,
        bottom,
        (71, 63)
    )


if __name__ == '__main__':
    t.setworldcoordinates(0, 100, 100, 0)
    t.hideturtle()
    t.tracer(500, 0)

    main()

    if PLOTTER_ENABLED:
        ad.plot_setup()
        ad.options.mode = 'align'
        ad.plot_run()
        ad.disconnect()

    t.update()
    t.done()
