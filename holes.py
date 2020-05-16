from plot import Plot
from plot.utils import vec2, SQRT_2
import random

def main(p: Plot):
    p.plot_size = 4
    # p.options.speed_pendown = 50
    p.setup()
    p.draw_bounding_box(True)
    lo = vec2(0, 0)
    hi = vec2(1, 1)
    layers = []

    grid_size = 4
    spacing = 7
    scale = (100-spacing*(grid_size+1))/grid_size

    inc = 0.2
    min_space = p.inches_to_units(0.01)/scale
    while lo.x < hi.x and lo.y < hi.y:
        inc = max(inc - random.uniform(0.015, 0.025), min_space)
        r = random.random()
        if r > 0.75:
            lo += vec2(inc)
            layers.append( (
                vec2(lo.x, hi.y),
                lo,
                vec2(hi.x, lo.y),
            ) )
        elif r > 0.5:
            lo += vec2(inc, 0)
            hi -= vec2(0, inc)
            layers.append( (
                lo,
                vec2(lo.x, hi.y),
                hi,
            ) )
        elif r > 0.25:
            lo += vec2(0, inc)
            hi -= vec2(inc, 0)
            layers.append( (
                lo,
                vec2(hi.x, lo.y),
                hi,
            ) )
        else:
            hi -= vec2(inc)
            layers.append( (
                vec2(lo.x, hi.y),
                hi,
                vec2(hi.x, lo.y),
            ) )
    layers.pop()

    for r in range(grid_size):
        for c in range(grid_size):
            origin = vec2(spacing+c*(scale+spacing), spacing+r*(scale+spacing))
            p.goto(*origin)
            p.lineto(*(origin+scale*vec2(1, 0)))
            p.lineto(*(origin+scale*vec2(1)))
            p.lineto(*(origin+scale*vec2(0, 1)))
            p.lineto(*origin)
            for s, m, e in layers:
                p.goto(*(origin+scale*s))
                p.lineto(*(origin+scale*m))
                p.lineto(*(origin+scale*e))