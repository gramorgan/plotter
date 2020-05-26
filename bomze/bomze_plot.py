from plot import Plot
from plot.utils import vec2, vec3, SQRT_3
from plot.text import draw_string
import math

from .mats import MATS

def gen_simplex_coords(num_divisions):
    for x in range(num_divisions+1):
        for y in range(num_divisions+1-x):
            yield vec3(
                x/num_divisions,
                y/num_divisions,
                (num_divisions-x-y) / num_divisions
            )

def draw_tri(p, origin, size):
    p.goto(*origin)
    p.lineto(origin.x + size, origin.y)
    p.lineto(origin.x + size/2, origin.y - SQRT_3*size/2)
    p.lineto(*origin)

def simplex_to_cart(pos, origin, size):
    ret = (
        pos[0] * origin +
        pos[1] * vec2(origin.x + size, origin.y) +
        pos[2] * vec2(origin.x + size/2, origin.y - SQRT_3*size/2)
    )
    return ret

def get_grad(pos, mat):
    s_x, s_y, s_z = pos
    W_x = s_x*mat[0,0] + s_y*mat[0,1] + s_z*mat[0,2]
    W_y = s_x*mat[1,0] + s_y*mat[1,1] + s_z*mat[1,2]
    W_z = s_x*mat[2,0] + s_y*mat[2,1] + s_z*mat[2,2]
    W_bar = s_x*W_x + s_y*W_y + s_z*W_z

    return vec3(
        float(s_x*(W_x-W_bar)),
        float(s_y*(W_y-W_bar)),
        float(s_z*(W_z-W_bar)),
    )

# line segments
# def draw_arrow(p, start, end):
#     if start == end:
#         p.dot(*start)
#         return
#     p.goto(*start)
#     p.lineto(*end)

# actual arrows
def draw_arrow(p, start, end):
    if start == end:
        p.dot(*start)
        return
    orth = (end-start).rotate(90).normalize()
    width = 0.1
    p.goto(*start+orth*width)
    p.lineto(*end)
    p.lineto(*start-orth*width)

def draw_mat(p, mat, origin, size):
    num_divisions = 10
    grads = {pos: get_grad(pos, mat) for pos in gen_simplex_coords(num_divisions)}
    max_grad = max(grad.mag() for grad in grads.values())
    
    linelength=(1/num_divisions)
    # spacing between flow and border
    spacing = 1
    draw_tri(p, origin, size)

    flow_origin = vec2(origin.x+spacing*SQRT_3, origin.y-spacing)
    flow_size = size-2*spacing*SQRT_3
    
    for pos, grad in grads.items():
        if max_grad != 0:
            grad /= max_grad

        start = simplex_to_cart(pos, flow_origin, flow_size)
        end = simplex_to_cart(pos + grad*linelength, flow_origin, flow_size)
        draw_arrow(p, start, end)

def main(p: Plot):
    p.plot_size = 11.69
    p.set_canvas_size(210, 297)
    p.setup()
    p.draw_bounding_box()

    mat_range = (0, 24)
    # mat_range = (24, 47)

    num_cols = 4
    spacing = 5
    size = (210 - spacing*(num_cols+1)) / num_cols
    vert_size = SQRT_3 * size/2
    text_size = vert_size/8
    for mat_num, mat in enumerate(MATS[mat_range[0]: mat_range[1]]):
        row = mat_num // num_cols
        col = mat_num % num_cols
        x = spacing + col * (size+spacing)
        y = vert_size + spacing + row * (vert_size+spacing)
        draw_mat(p, mat, vec2(x, y), size)
        draw_string(p, str(mat_range[0] + mat_num), vec2(x, y-vert_size), text_size)
