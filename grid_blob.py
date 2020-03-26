from plot import Plot, smin
import math

p = Plot()

def rotate(x, y):
    x -= 50
    y -= 50
    dist = smin(math.hypot(x, y)/40, 1, 0.2)
    angle = -(1-dist)*0.9
    point = (
        x*math.cos(angle) - y*math.sin(angle),
        x*math.sin(angle) + y*math.cos(angle),
    )
    return (
        point[0]+50,
        point[1]+50,
    )

def main():
    num_rows = 100
    num_cols = 100
    for r in range(num_rows+1):
        y = 1 + r * (98/num_rows)
        p.goto(*rotate(1, y))
        for c in range(num_cols+1):
            x = 1 + c * (98/num_cols)
            p.lineto(*rotate(x, y))

    for c in range(num_cols+1):
        x = 1 + c * (98/num_cols)
        p.goto(*rotate(x, 1))
        for r in range(num_rows+1):
            y = 1 + r * (98/num_rows)
            p.lineto(*rotate(x, y))

if __name__ == "__main__":
    p.plotter_enabled = False
    p.plot_size = 4
    p.setup()
    main()
    p.done()
