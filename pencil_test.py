from plot import Plot
import math

def main(p):
    num_lines = 200
    for i in range(num_lines):
        t = i/num_lines
        p.goto(50, 50)
        p.lineto(50+40*math.cos(2*math.pi*t), 50+40*math.sin(2*math.pi*t))
