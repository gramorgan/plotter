from plot import Plot
from plot.utils import vec3
from plot.camera import Camera

def main(p: Plot):
    p.clipping = False
    p.setup()

    paths = [
        [
            vec3(-1, -1, -1),
            vec3(-1, -1, 1),
            vec3(1, -1, 1),
            vec3(1, -1, -1),
            vec3(-1, -1, -1),
        ],
        [
            vec3(-1, 1, -1),
            vec3(-1, 1, 1),
            vec3(1, 1, 1),
            vec3(1, 1, -1),
            vec3(-1, 1, -1),
        ],
        [
            vec3(-1, 1, -1),
            vec3(-1, -1, -1),
        ],
        [
            vec3(-1, 1, 1),
            vec3(-1, -1, 1),
        ],
        [
            vec3(1, 1, 1),
            vec3(1, -1, 1),
        ],
        [
            vec3(1, 1, -1),
            vec3(1, -1, -1),
        ],
    ]

    cam = Camera()
    cam.set_view(vec3(4, 8, 10), vec3(0))
    cam.set_proj_persp(20, -1, 1)
    # cam.set_proj_orth(4, -1, 1)

    for path in paths:
        p.goto(*cam.eval(path[0]).xy)
        for point in path[1:]:
            point = cam.eval(point)
            print(point)
            p.lineto(*point.xy)