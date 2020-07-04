from plot import Plot
import numpy as np
from skimage import measure

def remap(a, orig_lo, orig_hi, new_lo, new_hi):
    return new_lo + (new_hi - new_lo) * ((a - orig_lo) / (orig_hi - orig_lo))

def main(p: Plot):
    p.setup()
    x, y = np.ogrid[-np.pi:1:100j, -np.pi:np.pi:100j]
    r = np.cos(np.exp((np.sin(x)**4 + np.cos(y)**3)))
    num_steps = 10

    for i in range(num_steps+1):
        c = -1 + 2*i / num_steps
        contours = measure.find_contours(r, c)
        for contour in contours:
            p.goto(*contour[0])
            for point in contour[1:]:
                p.lineto(*point)