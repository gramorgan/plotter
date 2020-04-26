from plot import Plot
import random

def make_road_straight(p: Plot, size):
    p.pendown()
    p.forward(size/3)
    p.right(90)
    p.forward(size)
    p.right(90)
    p.forward(size/3)
    p.right(90)
    p.forward(size/3)
    p.right(90)
    p.forward(size/3)
    p.penup()
    p.forward(size/3)
    p.pendown()
    p.forward(size/3)
    p.right(90)
    p.forward(size/3)
    p.right(90)
    p.forward(size/3)
    p.right(90)
    p.forward(size)
    p.right(90)
    p.forward(size/3)
    p.right(90)
    p.forward(size/3)
    p.right(90)
    p.forward(size/3)
    p.penup()
    p.forward(size/3)
    p.pendown()
    p.forward(size/3)
    p.right(90)
    p.forward(size/3)

def main(p: Plot):
    p.plot_size = 4
    p.setup()
    p.draw_bounding_box()

    grid_size = 20
    padding = 0.5
    spacing = (100-padding)/grid_size
    size = spacing - padding

    for r in range(grid_size):
        for c in range(grid_size):
            p.goto(padding+c*spacing, size+padding+r*spacing)
            p.set_angle(0)
            p.penup()
            for _ in range(random.randint(0, 3)):
                p.forward(size)
                p.right(90)
            make_road_straight(p, size)
