from plot import Plot
from plot.utils import SQRT_3
import random

def draw_sod(p: Plot, pos, size, angle):
    p.goto(*pos)
    p.set_angle(angle)
    p.penup()
    p.forward(size/SQRT_3)
    p.right(150)
    p.pendown()

    p.forward(size)
    p.right(120)
    p.forward(size)
    p.right(120)
    p.forward(size)

    p.right(90)
    p.penup()
    p.forward(size/SQRT_3)
    p.right(90)
    p.pendown()

    p.forward(size)
    p.right(120)
    p.forward(size)
    p.right(120)
    p.forward(size)

def main(p: Plot):
    p.plot_size = 2
    p.setup()
    # p.draw_bounding_box(True)

    gridsize = 6

    # draw_sod(p, (50, 50), 10, 0)

    for r in range(gridsize+1):
        for c in range(gridsize+1):
            x = 100*r/gridsize + random.uniform(-2, 2)
            y = 100*c/gridsize + random.uniform(-2, 2)
            size = random.uniform(10, 15)
            angle = random.uniform(0, 360)
            draw_sod(p, (x, y), size, angle)
