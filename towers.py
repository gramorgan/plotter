from plot import Plot
from plot.camera import Camera
from plot.utils import vec3
import noise

def make_tower(origin, height, width):
    verts = [
        origin,
        origin + vec3(width, 0, 0),
        origin + vec3(width, 0, width),
        origin + vec3(0, 0, width),

        origin + vec3(0, height, 0),
        origin + vec3(width, height, 0),
        origin + vec3(width, height, width),
        origin + vec3(0, height, width),
    ]
    indices = [
        (0, 1, 2, 3),
        (0, 4, 5, 1),
        (1, 5, 6, 2),
        (2, 6, 7, 3),
        (3, 7, 4, 0),
        (7, 6, 5, 4),
    ]
    return [tuple(verts[j] for j in i) for i in indices]

def main(p: Plot):
    p.plot_size = 6
    p.setup()
    p.draw_bounding_box(True)

    cam = Camera()
    eye = vec3(10, 150, 70)
    cam.set_view(eye, vec3(0, 0, 10))
    cam.set_proj_persp(40, 0, 1)
    # cam.set_proj_orth(150, 0, 1)

    for r in range(10):
        for c in range(10):
            noise_scale = 1/15
            height = 15 + noise.snoise2(r * noise_scale, c * noise_scale) * 15
            origin = vec3(r*15-75, 0, c*15-75)

            tower = make_tower(origin, height, 10)
            for face in tower:
                # normal = (face[2]-face[0]).cross(face[1]-face[0]).normalize()
                # if ((face[0]-eye).normalize().dot(normal)) < 0:
                #     continue

                p.goto(*cam.eval(face[0]).xy)
                for point in face[1:]:
                    p.lineto(*cam.eval(point).xy)
                p.lineto(*cam.eval(face[0]).xy)