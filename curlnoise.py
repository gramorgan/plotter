from plot import Plot
from plot.utils import vec2, lerp
import noise
import random
import math

def fract(v: vec2):
    return vec2(math.modf(v.x)[0], math.modf(v.y)[0])

def interp(grid, pos):
    size = len(grid)
    pos = (size-1) * pos/100
    topleft = vec2(math.floor(pos.x), math.floor(pos.y))
    topright = topleft + vec2(1, 0)
    bottomright = topleft + vec2(1)
    bottomleft = topleft + vec2(0, 1)

    d = fract(pos)
    top = lerp(grid[topleft.y][topleft.x], grid[topright.y][topright.x], d.x)
    bottom = lerp(grid[bottomleft.y][bottomleft.x], grid[bottomright.y][bottomright.x], d.x)
    return lerp(top, bottom, d.y)

SEED = vec2(random.uniform(-1000, 1000), random.uniform(-1000, 1000))

def get_noise(p: vec2):
    noise_scale = 0.02
    return noise.snoise2(*(SEED + p*noise_scale))

def get_curl(p: vec2):
    delta = 0.1
    dx = (get_noise(p + vec2(delta, 0)) - get_noise(p - vec2(delta, 0))) / (delta * 2)
    dy = (get_noise(p + vec2(0, delta)) - get_noise(p - vec2(0, delta))) / (delta * 2)
    return vec2(dy, -dx)

def main(p: Plot):
    p.options.speed_pendown = 90
    p.plot_size = 6
    p.setup()
    p.draw_bounding_box(True)

    min_dist = p.inches_to_units(0.04)

    # grid_size = 11
    # for r in range(grid_size):
    #     for c in range(grid_size):
    #         x = c * 100/(grid_size-1)
    #         y = r * 100/(grid_size-1)
    #         pos = vec2(x, y)
    #         pos2 = pos
    #         p.goto(*pos)

    #         for _ in range(50):
    #             if pos.x < 0 or pos.y < 0 or pos.x > 100 or pos.y > 100:
    #                 break
    #             step_size = 20
    #             d = get_curl(pos2) * step_size
    #             pos2 += d
    #             if (pos2 - pos).mag() < min_dist:
    #                 continue
    #             pos = pos2
    #             p.lineto(*pos)

    num_lines = 120
    for i in range(num_lines):
        print('line', f'{i+1}/{num_lines}')
        pos = vec2(random.uniform(1, 99), random.uniform(1, 99))
        pos2 = pos
        p.goto(*pos)

        for _ in range(100):
            step_size = 20
            d = get_curl(pos2) * step_size
            pos2 += d
            if (pos2 - pos).mag() < min_dist:
                continue
            pos = pos2
            p.lineto(*pos)
