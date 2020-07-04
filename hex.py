from plot import Plot
from plot.utils import vec2, SQRT_3

def draw_hex(p: Plot, origin, size, angle):
    p.goto(*origin)
    p.set_angle(angle)
    p.penup()
    p.forward(size)
    p.right(120)
    p.pendown()
    for _ in range(6):
        p.forward(size)
        p.right(60)

def draw_hex_filled(p: Plot, origin, size, angle):
    p.goto(*origin)
    p.set_angle(angle)
    p.penup()
    p.forward(size)
    p.right(120)
    p.pendown()

    stepover = p.inches_to_units(0.02)
    while True:
        for _ in range(6):
            p.forward(size)
            p.right(60)
        size -= stepover
        if size < stepover:
            break
        p.right(60)
        p.forward(stepover)
        p.left(60)
    
    p.dot(*origin)

def draw_grid(p: Plot, origin, grid_size, size, angle, color):
    spacing = p.inches_to_units(0.02)
    hex_size = size/grid_size/2
    for r in range(grid_size):
        for c in range(grid_size):
            if (c+r) % 3 != color:
                continue
            offset = vec2((c + 0.5*(r%2))*(hex_size*SQRT_3 + spacing), r*(hex_size*1.5 + spacing)).rotate(angle)
            draw_hex_filled(p, origin+offset, hex_size, angle)

def main(p: Plot):
    p.plot_size = 4
    p.setup()
    p.draw_bounding_box()

    draw_grid(p, vec2(-50), 15, 300, 10, 0)
    p.pen_change()
    draw_grid(p, vec2(-50), 15, 300, 10, 1)
    p.pen_change()
    draw_grid(p, vec2(-50), 15, 300, 10, 2)