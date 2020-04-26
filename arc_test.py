from plot import Plot
from plot.utils import SQRT_2

def main(p: Plot):
    p.setup()
    p.draw_bounding_box(True)

    spacing = 0.5

    p.goto(50, 50)
    p.forward(spacing)
    p.pendown()
    for i in range(1, round(50*SQRT_2/spacing)):
        p.left(90)
        p.arc(spacing*i, 1.61803398875*120, True)
        p.right(90)
        p.forward(spacing)