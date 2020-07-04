from plot import Plot
from plot.camera import Camera
from plot.utils import vec3

def make_icosahedron():
    t = (1 + 5 ** 0.5) / 2
    points = [
        vec3(-1, t, 0),
        vec3(1, t, 0),
        vec3(-1, -t, 0),
        vec3(1, -t, 0),

        vec3(0, -1, t),
        vec3(0, 1, t),
        vec3(0, -1, -t),
        vec3(0, 1, -t),

        vec3(t, 0, -1),
        vec3(t, 0, 1),
        vec3(-t, 0, -1),
        vec3(-t, 0, 1),
    ]
    points = [vec3.normalize(e) for e in points]
    indices = [
        (0, 11, 5),
        (0, 5, 1),
        (0, 1, 7),
        (0, 7, 10),
        (0, 10, 11),

        (1, 5, 9),
        (5, 11, 4),
        (11, 10, 2),
        (10, 7, 6),
        (7, 1, 8),

        (3, 9, 4),
        (3, 4, 2),
        (3, 2, 6),
        (3, 6, 8),
        (3, 8, 9),

        (4, 9, 5),
        (2, 4, 11),
        (6, 2, 10),
        (8, 6, 7),
        (9, 8, 1),
    ]
    return [
        (
            points[e[0]],
            points[e[1]],
            points[e[2]],
        )
        for e in indices
    ]

def make_icosphere(iters):
    icos = make_icosahedron()
    faces = icos
    for _ in range(iters):
        new_faces = []
        for face in faces:
            a = ((face[0]+face[1])/2).normalize()
            b = ((face[1]+face[2])/2).normalize()
            c = ((face[2]+face[0])/2).normalize()

            new_faces.append((face[0], a, c))
            new_faces.append((face[1], b, a))
            new_faces.append((face[2], c, b))
            new_faces.append((a, b, c))
        faces = new_faces
    return faces

def main(p: Plot):
    p.plot_size = 4
    p.setup()
    cam = Camera()
    eye = vec3(0, 3, 3)
    cam.set_view(eye, vec3(0))
    cam.set_proj_persp(30, 0, 1)
    # cam.set_proj_orth(2, 0, 1)

    faces = make_icosphere(3)
    for path in faces:
        # backface culling
        # only really works for perspective projection
        normal = (path[1]-path[0]).cross(path[2]-path[0]).normalize()
        if ((path[0]-eye).normalize().dot(normal)) < 0:
            continue

        p.goto(*cam.eval(path[0]).xy)
        for point in path[1:]:
            p.lineto(*cam.eval(point).xy)
        p.lineto(*cam.eval(path[0]).xy)