from plot import Plot
import numpy as np

def draw_square_norm(p: Plot, center_pos, size):
    num_lines = 50
    for _ in range(num_lines):
        r = abs(np.random.normal(0, size*0.7))
        if r > size:
            continue
        r = size-r
        p.goto(center_pos[0]-r, center_pos[1])
        p.lineto(center_pos[0], center_pos[1]-r)
        p.lineto(center_pos[0]+r, center_pos[1])
        p.lineto(center_pos[0], center_pos[1]+r)
        p.lineto(center_pos[0]-r, center_pos[1])

def draw_square_even(p: Plot, center_pos, size):
    num_lines = 6
    for i in range(num_lines+1):
        r = (i*size)/num_lines
        if r > size:
            continue
        p.goto(center_pos[0]-r, center_pos[1])
        p.lineto(center_pos[0], center_pos[1]-r)
        p.lineto(center_pos[0]+r, center_pos[1])
        p.lineto(center_pos[0], center_pos[1]+r)
        p.lineto(center_pos[0]-r, center_pos[1])

def main(p: Plot):
    p.options.speed_pendown = 40
    p.plot_size = 2
    p.setup()
    p.draw_bounding_box(True)

    grid_size = 3
    offset = 100/grid_size
    for r in range(grid_size+1):
        for c in range(grid_size+1):
            x = r*offset
            y = c*offset
            # draw_square_even(p, (x, y), offset/2)
            draw_square_norm(p, (x, y), offset/2)
    for r in range(grid_size):
        for c in range(grid_size):
            x = offset/2 + r*offset
            y = offset/2 + c*offset
            # draw_square_even(p, (x, y), offset/2)
            draw_square_norm(p, (x, y), offset/2)
