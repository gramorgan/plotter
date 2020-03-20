from plot import *
import math

p = Plot()

def circle(origin, radius):
    len_segments = p.inches_to_units(0.02)
    num_divisions = round((2*math.pi*radius)/len_segments)
    p.goto(origin[0]+radius, origin[1])
    for t in range(1, num_divisions+1):
        x = origin[0] + radius*math.cos((t/num_divisions)*(2*math.pi))
        y = origin[1] + radius*math.sin((t/num_divisions)*(2*math.pi))
        p.lineto(x, y)


def main():
    for t in range(1, 150):
        spacing = 0.4
        x = 50 + spacing*math.cos(t*0.5)
        y = 50 + spacing*math.sin(t*0.5)
        circle((x, y), t*0.5)
    
if __name__ == '__main__':
    p.plotter_enabled = False
    p.setup()
    p.draw_bounding_box(True)
    main()
    p.done()
