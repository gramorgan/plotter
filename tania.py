from plot import *
import math
import random

p = Plot()

def rotate(pos, origin, angle):
    x = pos[0] - origin[0]
    y = pos[1] - origin[1]
    return (
        x*math.cos(angle) - y*math.sin(angle) + origin[0],
        x*math.sin(angle) + y*math.cos(angle) + origin[1],
    )

def draw_heart(scale, origin, angle, yoffset, move=True):
    line_size = p.inches_to_units(0.02)
    num_divisions = round(64*scale / line_size)
    for i in range(num_divisions+1):
        t = i/num_divisions * 2*math.pi
        x = origin[0] + scale*16*(math.sin(t)**3)
        y = origin[1] - scale*(13*math.cos(t) - 5*math.cos(2*t) - 2*math.cos(3*t) - math.cos(4*t)) + yoffset
        x, y = rotate((x, y), origin, angle)
        if i == 0 and move:
            p.goto(x, y)
        else:
            p.lineto(x, y)

# def draw_heart_filled(scale, origin, angle):
#     s = scale
#     move = True
#     y = origin[1]
#     while s > 0.02:
#         draw_heart(s, (origin[0], y), angle, move)
#         move = False
#         y += s * 0.55
#         if s > 0.2/0.9:
#             s *= 0.9
#         else:
#             s -= 0.02

def draw_hearts(num_colors, color_assignments, scale, yoffset):
    # draw_heart_filled(0.9, (15, 12), 0)
    # return
    hearts = [
        (0.6, (20, 40), 0.6),
        (0.9, (5, 52), 1.2),
        (0.85, (16, 11), 0.2),
        (0.2, (15, 28), 3.1),
        (0.62, (4, 29), -0.65),
        (0.33, (1, 16), 2.8),
        (0.2, (22.5, 29), -0.5),
        (0.19, (20.5, 23.5), 0.8),
        (0.59, (-3.5, 2.5), -0.63),
        (0.42, (22.5, 53.5), 4.4),
        (0.58, (34, 58), 1.22),
        (0.18, (28, 48), 3.6),
        (0.78, (37, 34.5), 4.2),
        (0.42, (31, 19), 5.5),
        (0.49, (34, 2), 4.1),
        (0.52, (42, 17), 2.3),
        (0.52, (17, -6), 3.8),
    ]
    for c in range(num_colors):
        for i, heart in enumerate(hearts):
            if color_assignments[i] == c:
                draw_heart(heart[0]*scale, heart[1], heart[2], yoffset)
        p.pen_change()

def main():
    color_assignments = [0] * 20
    draw_hearts(1, color_assignments, 1, 0)
    num_colors = 3
    color_assignments = [random.randint(0, num_colors-1) for _ in range(20)]
    draw_hearts(num_colors, color_assignments, 0.7, 0.3)

if __name__ == "__main__":
    p.plot_size = 6
    p.plotter_enabled = False
    p.set_canvas_size(40, 60)
    p.setup()
    p.draw_bounding_box(True)
    main()
    p.done()