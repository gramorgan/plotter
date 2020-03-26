from plot import *
import math
from random import uniform

p = Plot()

def main():
    num_lines = 100
    line_res = 200
    rand = uniform(-1, 1)
    radius = 0.03
    for c in range(num_lines):
        x = 1+(100/(num_lines+1)) * c
        p.goto(x, 0)
        for r in range(line_res):
            rand = lerp(rand, uniform(-1, 1), 0.2)
            y = 1+(100/line_res)*r
            d = smoothstep(1/math.hypot(x-50, y-50), 0.8*radius, radius)
            d *= 0.7
            p.lineto(x+rand*d, y)
    
if __name__ == '__main__':
    p.setup()
    main()
    p.done()