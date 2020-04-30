from plot import Plot
from plot.utils import vec2
import random

def draw_box(p: Plot, lo, hi, scale, origin):
    p.goto(origin.x + scale*lo.x, origin.y+scale*lo.y)
    p.lineto(origin.x + scale*lo.x, origin.y+scale*hi.y)
    p.lineto(origin.x + scale*hi.x, origin.y+scale*hi.y)
    p.lineto(origin.x + scale*hi.x, origin.y+scale*lo.y)
    p.lineto(origin.x + scale*lo.x, origin.y+scale*lo.y)

def main(p: Plot):
    p.plot_size = 4
    p.setup()
    p.draw_bounding_box()
    lo = vec2(0, 0)
    hi = vec2(1, 1)
    bounds = []

    grid_size = 4
    spacing = 7
    scale = (100-spacing*(grid_size+1))/grid_size

    inc = 0.2
    min_space = p.inches_to_units(0.02)/scale
    while lo.x < hi.x and lo.y < hi.y:
        bounds.append( (lo, hi) )
        inc = max(inc - random.uniform(0.015, 0.02), min_space)
        r = random.random()
        if r > 0.75:
            lo += vec2(inc)
        elif r > 0.5:
            lo += vec2(inc, 0)
            hi -= vec2(0, inc)
        elif r > 0.25:
            lo += vec2(0, inc)
            hi -= vec2(inc, 0)
        else:
            hi -= vec2(inc)

    for r in range(grid_size):
        for c in range(grid_size):
            for lo, hi in bounds:
                origin = vec2(spacing+c*(scale+spacing), spacing+r*(scale+spacing))
                draw_box(p, lo, hi, scale, origin)