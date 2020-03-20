from utils import Plot
import math
import random

def draw_hump(p, start, radius, reverse):
    len_segments = 0.005 / p.inches_per_unit
    num_divisions = round((math.pi*radius)/len_segments)
    for i in range(num_divisions+1):
        t = i/num_divisions
        x = start[0] + radius - radius*math.cos(t*math.pi)
        y = start[1] + radius*math.sin(t*math.pi) * (1 if reverse else -1)
        p.lineto(x, y)

def draw_color(p, num_rows, color_assignments, color):
    vert_spacing = 100/num_rows
    radius = 3
    for r in range(num_rows):
        if color_assignments[r] != color:
            continue
        x = 0
        y = radius+ vert_spacing*r
        if y+radius > 100:
            break
        p.goto(x, y)
        num_humps = 2
        for i in range(num_humps):
            max_x = 100-2*radius*(num_humps-i)
            r = random.uniform(x, max_x)
            r += random.uniform(x, max_x)
            x = abs(r-x-max_x)+x
            p.lineto(x, y)
            draw_hump(p, (x, y), radius, random.choice((True, False)))
            x += 2*radius
        p.lineto(100, y)

def main(p):
    num_colors = 4
    num_rows = 70
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
        # input()

if __name__ == '__main__':
    p = Plot()
    p.plot_size = 4
    p.plotter_enabled = False
    p.setup()

    main(p)

    p.done()