from plot import Plot
from plot.utils import vec2
import random

def draw_star(p, star_center: vec2, radius):
    p.circle(star_center, radius)
    p.goto(star_center.x, star_center.y)

    star_length = radius * 1.9

    p.forward(radius)
    p.right(162)
    p.pendown()
    for _ in range(5):
        p.forward(star_length)
        p.right(720/5)

def main(p: Plot):
    p.setup()
    p.draw_bounding_box()

    gridsize = 6

    for r in range(gridsize+1):
        for c in range(gridsize+1):
            x = 100*r/gridsize + random.uniform(-5, 5)
            y = 100*c/gridsize + random.uniform(-5, 5)
            size = random.uniform(3, 8)
            angle = random.uniform(0, 360)
            p.right(angle)
            draw_star(p, vec2(x, y), size)
