import turtle as t
import math
import numpy as np
from itertools import combinations
from pyaxidraw import axidraw

from mats import MATS

SQRT_3 = 1.73205080757

PLOTTER_ENABLED = True

ad = None
if PLOTTER_ENABLED:
    ad = axidraw.AxiDraw()
    ad.interactive()
    ad.connect()

def goto(x, y):
    t.penup()
    t.goto(x, y)
    if PLOTTER_ENABLED:
        t.update()
        ad.moveto(x, y)

def lineto(x, y):
    t.pendown()
    t.goto(x, y)
    if PLOTTER_ENABLED:
        t.update()
        ad.lineto(x, y)

def calc_mag(a):
    return math.sqrt(sum(e*e for e in a))

def normalize(a):
    mag = calc_mag(a)
    if mag == 0:
        return a
    return tuple(e/mag for e in a)

def gen_simplex_coords(num_divisions):
    for x in range(num_divisions+1):
        for y in range(num_divisions+1-x):
            yield (x/num_divisions, y/num_divisions, (num_divisions-x-y)/num_divisions)

def draw_tri(origin=(0, 0), size=100):
    goto(origin[0]+size/2, origin[1]-(size/2)*SQRT_3)
    lineto(origin[0], origin[1])
    lineto(origin[0]+size, origin[1])
    lineto(origin[0]+size/2, origin[1]-(size/2)*SQRT_3)

def simplex_to_cart(pos, origin=(0, 0), size=100):
    points = (
        origin,
        (origin[0]+size, origin[1]),
        (origin[0]+size/2, origin[1]-(size/2)*SQRT_3),
    )
    zipped = list(zip(points, pos))
    return (
        sum(p*point[0] for point, p in zipped),
        sum(p*point[1] for point, p in zipped),
    )

def get_mat_grad(pos, mat):
    s_x, s_y, s_z = pos
    W_x = s_x*mat[0,0] + s_y*mat[0,1] + s_z*mat[0,2]
    W_y = s_x*mat[1,0] + s_y*mat[1,1] + s_z*mat[1,2]
    W_z = s_x*mat[2,0] + s_y*mat[2,1] + s_z*mat[2,2]
    W_bar = s_x*W_x + s_y*W_y + s_z*W_z

    return (
        s_x*(W_x-W_bar),
        s_y*(W_y-W_bar),
        s_z*(W_z-W_bar),
    )

# line segments
# def draw_arrow(start, end):
#     t.penup()
#     t.goto(start[0], start[1])
#     t.pendown()
#     t.goto(end[0], end[1])

# actual arrows
def draw_arrow(start, end):
    orth = normalize( (
        -(end[1]-start[1]),
        end[0]-start[0]
    ) )
    # fixed units
    width = 0.01

    goto(start[0]+orth[0]*width, start[1]+orth[1]*width)
    lineto(end[0], end[1])
    lineto(start[0]-orth[0]*width, start[1]-orth[1]*width)

def draw_flow(mat, origin, size):
    grads = {}
    num_divisions = 10
    for pos in gen_simplex_coords(num_divisions):
        grads[pos] = get_mat_grad(pos, mat)
    
    max_grad = 0
    for pos, grad in grads.items():
        max_grad = max(max_grad, calc_mag(grad))
    
    linelength=(1/num_divisions)
    # spacing between flow and border
    spacing = 0.1
    draw_tri(origin=origin, size=size)

    flow_origin = (origin[0]+spacing*SQRT_3, origin[1]-spacing)
    flow_size = size-2*spacing*SQRT_3
    
    for pos, grad in grads.items():
        if max_grad == 0:
            grad_scaled = (0, 0, 0)
        else:
            grad_scaled = tuple(p/max_grad for p in grad)

        start = simplex_to_cart(pos, origin=flow_origin, size=flow_size)
        end = simplex_to_cart(tuple(p+g*linelength for p, g in zip(pos, grad_scaled)), origin=flow_origin, size=flow_size)
        draw_arrow(start, end)

if __name__ == '__main__':
    t.setworldcoordinates(0, 4, 4, 0)
    t.hideturtle()
    t.tracer(100, 0)

    num_cols = 3

    mat = MATS[7]

    draw_flow(mat, (0.5, 3.5), 3)

    if PLOTTER_ENABLED:
        ad.penup()
        ad.disconnect()

    t.update()
    t.done()
