from plot import Plot
import numpy as np

def main(p: Plot):
    p.plot_size = 2
    p.plotter_enabled = False
    p.setup()
    p.draw_bounding_box(True)

    num_lines = 100
    mean = 0
    sd = 25
    for _ in range(num_lines):
        r = np.random.normal(mean, sd)
        p.goto(-r, r)
        p.lineto(100-r, 100+r)