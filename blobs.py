from plot import Plot
from plot.utils import vec2
import random

def draw_blob(p: Plot, origin, radius):
    if random.choice([True, False]):
        p.circle(origin, 0.3)
    start = radius*vec2(0, 1)
    p.goto(*(origin + start))
    angle = 0
    while True:
        angle += random.uniform(20, 50)
        blob_angle = random.uniform(200, 300)
        if 360-angle < 20:
            break
        p.arcto(*(origin + start.rotate(angle)), blob_angle)
    p.arcto(*(origin + start), blob_angle)

def main(p: Plot):
    p.setup()
    grid_size = 8
    for r in range(grid_size+1):
        for c in range(grid_size+1):
            x = c * 100/grid_size
            y = r * 100/grid_size
            draw_blob(p, vec2(x, y), 25/grid_size)