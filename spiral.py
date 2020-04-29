from plot import Plot
import math

def main(p: Plot):
    p.plot_size = 8
    p.setup()
    p.draw_bounding_box(True)

    for t in range(1, 150):
        spacing = 0.4
        x = 50 + spacing*math.cos(t*0.5)
        y = 50 + spacing*math.sin(t*0.5)
        p.circle((x, y), t*0.5)

if __name__ == '__main__':
    p = Plot()
    main(p)
