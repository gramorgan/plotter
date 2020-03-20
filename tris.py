import turtle as t
from pyaxidraw import axidraw
import math
import random

PLOTTER_ENABLED = True

# plot size in inches
SIZE = 4

SQRT_3 = 1.73205080757

ad = None

overlap_inches = 0.015
pen_width = (100/SIZE) * overlap_inches

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

def draw_tri(origin, size, angle):
    cur_point = t.Vec2D(*origin)
    orientation = t.Vec2D(1, 0).rotate(angle)
    goto(*cur_point)
    cur_point += orientation*size
    lineto(*cur_point)
    cur_point += orientation.rotate(-120)*size
    lineto(*cur_point)
    lineto(*origin)

def draw_tri_filled(origin, size, angle):
    origin = t.Vec2D(*origin)
    spacing = pen_width
    corner = t.Vec2D(1, 0).rotate(angle-30)
    goto(*origin)
    while size > spacing:
        cur_point = t.Vec2D(*origin)
        orientation = t.Vec2D(1, 0).rotate(angle)
        lineto(*cur_point)
        cur_point += orientation*size
        lineto(*cur_point)
        cur_point += orientation.rotate(-120)*size
        lineto(*cur_point)
        lineto(*origin)

        size -= 2*spacing*SQRT_3
        origin += corner*spacing*2

def main():
    num_rows = 10
    num_cols = 10
    size = 100/num_cols - pen_width*SQRT_3
    distance = size+pen_width*SQRT_3
    vert_size = (size/2)*SQRT_3
    vert_distance = (size/2)*SQRT_3 + pen_width
    r = 0
    tris = []
    num_colors = 4
    while vert_size + vert_distance*r < 100:
        for c in range(num_cols*2-1):
            if c % 2 == 0:
                origin = (
                    (c/2) * distance,
                    vert_size + vert_distance*r
                )
                angle = 0
            else:
                origin = (
                    size + (c//2)*distance+ distance/2,
                    vert_distance*r
                )
                angle = 180
            tris.append( (
                origin, angle, random.randint(1, num_colors)
            ) )
        r += 1
    for color in range(1, num_colors+1):
        for tri in tris:
            if tri[2] == color:
                draw_tri_filled(tri[0], size, tri[1])
        t.update()
        if PLOTTER_ENABLED:
            ad.penup()
        input()

if __name__ == '__main__':
    t.setworldcoordinates(0, 100, 100, 0)
    t.hideturtle()
    t.tracer(500, 0)

    if PLOTTER_ENABLED:
        ad = axidraw.AxiDraw()
        ad.interactive()
        ad.options.const_speed = True
        ad.options.pen_rate_raise = 100
        ad.options.pen_delay_down = -10
        ad.connect()

    main()

    if PLOTTER_ENABLED:
        ad.moveto(0, 0)
        ad.plot_setup()
        ad.options.mode = 'align'
        ad.plot_run()
        ad.disconnect()

    t.update()
    t.done()
