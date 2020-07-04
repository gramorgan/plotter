from plot import Plot
from plot.polygon import Polygon
from plot.utils import vec2

def draw_poly(p: Plot, poly: Polygon):
    p.goto(*poly.points[0])
    for point in poly.points[1:]:
        p.lineto(*point)
    p.lineto(*poly.points[0])

def main(p: Plot):
    p.setup()

    poly = Polygon([
        vec2(30, 30),
        vec2(70, 30),
        vec2(70, 70),
        vec2(30, 70),
    ])
    clip_poly = Polygon([
        vec2(50, 50),
        vec2(80, 50),
        vec2(80, 80),
        vec2(50, 80),
    ])
    # draw_poly(p, poly)
    # draw_poly(p, clip_poly)
    poly.clip(clip_poly)
    draw_poly(p, poly)

    # sp1 = vec2(10, 10)
    # sp2 = vec2(30, 20)
    # cp1 = vec2(15, 15)
    # cp2 = vec2(30, 45)

    # p.goto(*cp1)
    # p.lineto(*cp2)
    # p.goto(*sp1)
    # p.lineto(*sp2)
    
    # p.dot(*Polygon._do_clip_intersection(cp1, cp2, sp1, sp2))
    # print(Polygon._inside_clip(cp1, cp2, vec2(50, 40)))

