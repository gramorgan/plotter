from utils import Plot
import math
import random

def draw_hump(p, start, radius, reverse):
    len_segments = 0.01 / p.inches_per_unit
    num_divisions = round((math.pi*radius)/len_segments)
    for i in range(num_divisions+1):
        t = i/num_divisions
        x = start[0] + radius - radius*math.cos(t*math.pi)
        y = start[1] + radius*math.sin(t*math.pi) * (1 if reverse else -1)
        p.lineto(x, y)

def draw_color(p, num_rows, color_assignments, color):
    radius = 10
    vert_spacing = (100-2*radius)/num_rows
    horiz_spacing = (100-4*radius)/(num_rows-1)
    for r in range(num_rows):
        if color_assignments[r] != color:
            continue
        x = 0
        y = radius + vert_spacing*r
        p.goto(x, y)
        x = horiz_spacing*r
        p.lineto(x, y)
        draw_hump(p, (x, y), radius, False)
        x += 2*radius
        draw_hump(p, (x, y), radius, True)
        x += 2*radius
        p.lineto(100, y)

def main(p):
    num_colors = 2
    num_rows = 20
    color_assignments = []
    last_color = 1
    for r in range(num_rows):
        cur_color = random.randint(1, num_colors)
        while cur_color == last_color:
            cur_color = random.randint(1, num_colors)
        last_color = cur_color
        color_assignments.append(cur_color)
    for color in range(1, num_colors+1):
        draw_color(p, num_rows, color_assignments, color)
        p.penup()
        input()

if __name__ == '__main__':
    p = Plot()
    p.plot_size = 4
    p.plotter_enabled = False
    p.setup()

    main(p)

    p.done()