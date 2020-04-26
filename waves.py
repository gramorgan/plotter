from plot import Plot
import math

def draw_wave(p, offset, ystart, base_scale):
    num_cuts = round(100/p.inches_to_units(0.02))
    p.goto(ystart, 0)
    for i in range(num_cuts+1):
        x = (i / num_cuts) * 100 
        scale = (0-abs(offset-x))/50
        y = ystart + math.sin(x/1.5)*scale*base_scale
        p.lineto(y, x)

def draw_color(p, color_num, num_colors):
    num_waves = 10
    for i in range(num_waves+1):
        if i % num_colors == color_num:
            ystart = (i/num_waves) * 100
            draw_wave(p, (i/num_waves)*100, ystart, 10)

def main(p: Plot):
    p.plot_size = 3
    p.setup()
    p.draw_bounding_box(True)

    num_colors = 2
    for c in range(num_colors):
        # p.pen_change()
        draw_color(p, c, num_colors)