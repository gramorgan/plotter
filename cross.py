from plot import *
import numpy as np

p = Plot()

def main():
    num_lines = 20
    mean = 0
    sd = 10
    for _ in range(num_lines):
        r = np.random.normal(mean, sd)
        p.goto(-r, r)
        p.lineto(100-r, 100+r)
        r = np.random.normal(mean, sd)
        p.goto(100-r, 100+r)
        p.lineto(-r, r)

    for _ in range(num_lines):
        r = np.random.normal(mean, sd)
        p.goto(100-r, -r)
        p.lineto(-r, 100-r)
        r = np.random.normal(mean, sd)
        p.goto(-r, 100-r)
        p.lineto(100-r, -r)

if __name__ == "__main__":
    p.plot_size = 2
    p.plotter_enabled = True
    p.setup()
    p.draw_bounding_box(True)
    main()
    p.done()