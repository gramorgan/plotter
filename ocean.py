from plot import Plot
import math

def draw_wave(p, yoffset, xoffset, height):
    divisions = 1000
    first = True
    for i in range(divisions+1):
        t = i / divisions
        t = -50 + 100*t
        x = 50 + xoffset + height * 0.4 * (t + 4 * math.sin(t))
        y = yoffset + height * (math.sin(t) + 0.1 * math.sin(t*3))
        if first:
            p.goto(x, y)
            first = False
        else:
            p.lineto(x, y)

def main(p: Plot):
    p.setup()
    p.draw_bounding_box(True)
    num_waves = 7
    for i in range(num_waves+1):
        yoffset = 100*i/num_waves
        size = 50/num_waves
        draw_wave(p, yoffset, 0, size)