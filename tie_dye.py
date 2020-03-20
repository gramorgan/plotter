from utils import Plot
import noise
import math

SQRT_2 = 1.41421356237

p = Plot()

def rotate(x, y, angle):
    x -= 50
    y -= 50
    point = (
        x*math.cos(angle) - y*math.sin(angle),
        x*math.sin(angle) + y*math.cos(angle),
    )
    return (
        point[0]+50,
        point[1]+50,
    )

def in_canvas(point):
    return (
        point[0] >= 0 and
        point[0] <= 100 and
        point[1] >= 0 and
        point[1] <= 100
    )

def draw_color(angle, threshold, noise_scale, noise_offset):
    num_rows = 100
    num_cols = 100
    grid_size = 100*SQRT_2

    for r in range(num_rows+1):
        y = (100-grid_size)/2 + r*(grid_size/num_rows)
        last_point = rotate((100-grid_size)/2, y, angle)
        need_move = True
        for c in range(num_cols+1):
            x = (100-grid_size)/2 + c*(grid_size/num_cols)
            rx, ry = rotate(x, y, angle)
            if in_canvas(last_point) and in_canvas((rx, ry)) and noise.snoise2(rx/noise_scale + noise_offset[0], ry/noise_scale + noise_offset[1]) > threshold:
                if need_move:
                    p.goto(*last_point)
                    need_move = False
                p.lineto(rx, ry)
            else:
                need_move = True
                last_point = (rx, ry)

    for c in range(num_cols+1):
        x = (100-grid_size)/2 + c*(grid_size/num_cols)
        last_point = rotate((100-grid_size)/2, y, angle)
        need_move = True
        for r in range(num_rows+1):
            y = (100-grid_size)/2 + r*(grid_size/num_rows)
            rx, ry = rotate(x, y, angle)
            if in_canvas(last_point) and in_canvas((rx, ry)) and noise.snoise2(rx/noise_scale + noise_offset[0], ry/noise_scale + noise_offset[1]) > threshold:
                if need_move:
                    p.goto(*last_point)
                    need_move = False
                p.lineto(rx, ry)
            else:
                need_move = True
                last_point = (rx, ry)

def main():
    draw_color(0.9, 0.1, 20, (100, 0))
    input()
    draw_color(1.7, 0.1, 11, (1001, -1231))

if __name__ == "__main__":
    p.plotter_enabled = True
    p.plot_size = 6
    p.setup()
    p.draw_bounding_box()
    main()
    p.done()