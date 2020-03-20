from utils import Plot
import math

p = Plot()

def main():
    num_lines = 200
    for i in range(num_lines):
        t = i/num_lines
        p.goto(50, 50)
        p.lineto(50+40*math.cos(2*math.pi*t), 50+40*math.sin(2*math.pi*t))

if __name__ == "__main__":
    p.plotter_enabled = True
    p.setup()
    main()
    p.done()