from plot import Plot
import math
import noise

def get_noise(x, y):
    return noise.snoise2(x, y, octaves=4, lacunarity=3, persistence=0.4)

def main(p: Plot):
    p.plotter_enabled = False
    p.plot_size = 6
    p.setup()
    p.draw_bounding_box(True)

    num_rows = 150
    horiz_increment = 0.02
    num_cols = round(p.plot_size / horiz_increment)
    scale = 2.5
    for r in range(num_rows+1):
        y = scale + r*(100-scale*2)/num_rows
        n =  get_noise(4*r/num_rows, 0) * scale
        p.goto(0, y+n)
        for c in range(num_cols+1):
            n = get_noise(4*r/num_rows, 4*c/num_cols) * scale
            x = c*(100/num_cols)
            p.lineto(x, y+n)