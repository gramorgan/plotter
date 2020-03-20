import turtle as t
from pyaxidraw import axidraw
import math
from random import uniform

PLOTTER_ENABLED = True

# size in inches
SIZE = 4

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

def main():
    num_lines = 100
    line_res = 200
    rand = uniform(-1, 1)
    radius = 0.03
    for c in range(num_lines):
        x = 1+(100/(num_lines+1)) * c
        goto(x, 0)
        for r in range(line_res):
            rand = lerp(rand, uniform(-1, 1), 0.2)
            y = 1+(100/line_res)*r
            d = smoothstep(1/math.hypot(x-50, y-50), 0.8*radius, radius)
            d *= 0.7
            lineto(x+rand*d, y)
    
if __name__ == '__main__':
    t.setworldcoordinates(0, 100, 100, 0)
    t.hideturtle()
    t.tracer(500, 0)

    main()

    if PLOTTER_ENABLED:
        ad.moveto(0, 0)
        ad.plot_setup()
        ad.options.mode = 'align'
        ad.plot_run()
        ad.disconnect()

    t.update()
    t.done()
