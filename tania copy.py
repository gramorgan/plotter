from plot import *
import math

p = Plot()

def rotate(pos, origin, angle):
    x = pos[0] - origin[0]
    y = pos[1] - origin[1]
    return (
        x*math.cos(angle) - y*math.sin(angle) + origin[0],
        x*math.sin(angle) + y*math.cos(angle) + origin[1],
    )

def draw_heart(scale, origin, angle):
    line_size = p.inches_to_units(0.02)
    num_divisions = round(64*scale / line_size)
    for i in range(num_divisions+1):
        t = i/num_divisions * 2*math.pi
        x = origin[0] + scale*16*(math.sin(t)**3)
        y = origin[1] - scale*(13*math.cos(t) - 5*math.cos(2*t) - 2*math.cos(3*t) - math.cos(4*t))
        x, y = rotate((x, y), origin, angle)
        if i == 0:
            p.goto(x, y)
        else:
            p.lineto(x, y)

def draw_hearts():
    draw_heart(0.6, (20, 40), 0.6)
    draw_heart(0.9, (5, 52), 1.2)
    draw_heart(0.85, (16, 11), 0.2)
    draw_heart(0.2, (15, 28), 3.1)
    draw_heart(0.62, (4, 29), -0.65)
    draw_heart(0.33, (1, 16), 2.8)
    draw_heart(0.2, (22.5, 29), -0.5)
    draw_heart(0.19, (20.5, 23.5), 0.8)
    draw_heart(0.59, (-3.5, 2.5), -0.63)
    draw_heart(0.42, (22.5, 53.5), 4.4)
    draw_heart(0.58, (34, 58), 1.22)
    draw_heart(0.18, (28, 48), 3.6)
    draw_heart(0.78, (37, 34.5), 4.2)
    draw_heart(0.42, (31, 19), 5.5)
    draw_heart(0.49, (34, 2), 4.1)
    draw_heart(0.52, (42, 17), 2.3)
    draw_heart(0.52, (17, -6), 3.8)

def main():
    draw_hearts()

if __name__ == "__main__":
    p.plot_size = 6
    p.plotter_enabled = True
    p.set_canvas_size(40, 60)
    p.setup()
    p.draw_bounding_box(True)
    main()
    p.done()