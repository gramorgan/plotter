from plot import *
import math

p = Plot()

def main():
    for t in range(1, 150):
        spacing = 0.4
        x = 50 + spacing*math.cos(t*0.5)
        y = 50 + spacing*math.sin(t*0.5)
        circle(p, (x, y), t*0.5)
    
if __name__ == '__main__':
    p.plot_size = 8
    p.plotter_enabled = False
    p.setup()
    p.draw_bounding_box(True)
    main()
    p.done()
