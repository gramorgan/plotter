from plot import Plot
import noise
import random
from bisect import bisect

def make_simplex_cdf():
    num_steps = 1000
    scale = 10
    result = [0]
    for i in range(num_steps):
        result.append(result[-1] + noise.snoise2(scale*i/num_steps, 3245)/2+0.5)
    return [e/result[-1] for e in result]

def grid(p: Plot):
    scale = 3.5
    min_gap = 0.2

    x = 0
    while x < 100:
        n = noise.snoise2(x, 15167)/2+0.5
        x += min_gap + random.uniform(0, n*scale)
        p.goto(x, -1)
        p.lineto(x, 101)
    
    y = 0
    while y < 100:
        n = noise.snoise2(x, 52434)/2+0.5
        y += min_gap + random.uniform(0, n*scale)
        p.goto(-1, y)
        p.lineto(101, y)

def circle(p: Plot):
    scale = 7
    min_gap = 0.2

    r = 0
    while r < 71:
        n = noise.snoise2(r, 15167)/2+0.5
        r += min_gap + random.uniform(0, n*scale)
        p.circle((50, 50), r)


def main(p: Plot):
    p.plot_size = 2
    p.setup()
    p.draw_bounding_box(True)

    # p.goto(0, 100)
    # cdf = make_simplex_cdf()
    # num_points = len(cdf)
    # for i, point in enumerate(cdf):
    #     p.lineto(100*i/num_points, 100-point*100)

    cdf = make_simplex_cdf()
    num_points = len(cdf)

    for _ in range(200):
        r = random.random()
        x = bisect(cdf, r)
        x = 100*x/num_points
        p.goto(x, -1)
        p.lineto(x, 101)
