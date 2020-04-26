from plot import Plot
from plot.utils import vec2
import math
import random
import numpy as np

def get_point_on_circle(t, radius):
    return vec2(
        50 + radius*math.cos(t*2*math.pi),
        50 + radius*math.sin(t*2*math.pi)
    )

def main(p: Plot):
    p.plot_size = 2
    p.setup()
    p.draw_bounding_box(True)
    num_lines = 100
    for _ in range(num_lines):
        t = random.random()
        edge = get_point_on_circle(t, 10)
        tangent = (edge-vec2(50)).rotate(90).normalize()
        p.goto(*(edge-70*tangent))
        p.lineto(*(edge+70*tangent))
