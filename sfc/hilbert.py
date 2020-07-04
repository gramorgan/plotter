from plot import Plot
from plot.utils import vec2
from functools import partial
import random
import math

def hilbert_gen(order, size, pos=vec2(0), heading=vec2(0, 1)):

    def draw_hilbert(symbols, order, size):
        if order == 0:
            return
        for symbol in symbols:
            op = operations[symbol]
            yield from op(order-1, size)
    
    def forward(order, size):
        nonlocal pos
        pos += heading * size
        yield pos
    
    def right(order, size):
        nonlocal heading
        heading = heading.rotate(90)
        return
        yield

    def left(order, size):
        nonlocal heading
        heading = heading.rotate(-90)
        return
        yield

    operations = {
        'A': partial(draw_hilbert, '-BF+AFA+FB-'),
        'B': partial(draw_hilbert, '+AF-BFB-FA+'),
        'F': forward,
        '+': right,
        '-': left,
    }

    yield from draw_hilbert('A', order, size)

RADIUS = 40
def get_weight(x, y):
    cx, cy = x-50, y-50
    dist = math.hypot(cx, cy)
    if dist > RADIUS:
        return 0
    dist /= RADIUS
    return math.sqrt(1-dist*dist)

def main(p: Plot):
    order = 7
    size = 100 / ((2 ** (order-1)) - 1)
    points_gen = hilbert_gen(order, size)
    rx = random.uniform(-1, 1)
    ry = random.uniform(-1, 1)
    for (x, y) in points_gen:
        weight = get_weight(x, y) * size * 2
        p.goto(x, y)
