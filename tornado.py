import turtle as t
from pyaxidraw import axidraw
import math

PLOTTER_ENABLED = True

# plot size in inches
SIZE = 8

ad = None

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
    num_iters = 3000
    goto(50, 90)
    for i in range(num_iters):
        x = 50 + 10*i/num_iters * math.cos(i/10) + 5*math.sin(i/500) + 2*math.sin(i/350)
        y = 90-80*i/num_iters
        lineto(x, y)

if __name__ == '__main__':
    t.setworldcoordinates(0, 100, 100, 0)
    t.hideturtle()
    t.tracer(500, 0)

    if PLOTTER_ENABLED:
        ad = axidraw.AxiDraw()
        ad.interactive()
        ad.options.const_speed = True
        ad.connect()

    main()

    if PLOTTER_ENABLED:
        ad.plot_setup()
        ad.options.mode = 'align'
        ad.plot_run()
        ad.disconnect()

    t.update()
    t.done()
