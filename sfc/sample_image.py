import math

def lerp(a, b, t):
    return (1-t)*a + t*b

def clamp(a, lo, hi):
    return max(min(a, hi), lo)

def sample_image(img, x, y):
    width, height = img.size

    left_ind = clamp(math.floor(x*width), 0, width-1)
    right_ind = clamp(math.ceil(x*width), 0, width-1)
    top_ind = clamp(math.floor(y*height), 0, height-1)
    bottom_ind = clamp(math.ceil(y*height), 0, height-1)

    topleft = img.getpixel( (left_ind, top_ind) )[0]
    topright = img.getpixel( (right_ind, top_ind) )[0]
    bottomleft = img.getpixel( (left_ind, bottom_ind) )[0]
    bottomright = img.getpixel( (right_ind, bottom_ind) )[0]

    t_x, _ = math.modf(x*width)
    t_y, _ = math.modf(y*height)

    top = lerp(topleft, topright, t_x)
    bottom = lerp(bottomleft, bottomright, t_x)

    return lerp(top, bottom, t_y) / 255
