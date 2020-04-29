from .plot import Plot
from .utils import vec2

g = Plot.goto
l = Plot.lineto
a = Plot.arcto

CHAR_PATHS = {
    'A': [(g, 0,100), (l, 15,7), (a, 35,7,130), (l, 50,100), (g, 42.5,55), (l, 7.5,55)],
    'B': [(g, 0,100), (l, 0,0), (l, 15,0), (a, 15,55,180), (l, 27.5,55), (a, 27.5,100,180), (l, 0,100)],
    'C': [(g, 50,100), (l, 30,100), (a, 0,70,90), (l, 0,30), (a, 30,0,90), (l, 50,0)],
    'D': [(g, 0,100), (l, 0,0), (l, 30,0), (a, 50,20,90), (l, 50,80), (a, 30,100,90), (l, 0,100)],
    'E': [(g, 50,0), (l, 20,0), (a, 0,20,-90), (l, 0,80), (a, 20,100,-90), (l, 50,100), (g, 30,55), (l, 0,55)],
    'F': [(g, 50,0), (l, 30,0), (a, 0,30,-90), (l, 0,100), (g, 30,55), (l, 0,55)],
    'G': [(g, 50,25), (a, 0,25,-180), (l, 0,75), (a, 50,75,-180), (l, 50,55), (l, 20, 55)],
    'H': [(g, 0,0), (l, 0,100), (g, 0,55), (l, 50,55), (g, 50,0), (l, 50,100)],
    'I': [(g, 0,0), (l, 50,0), (g, 25,0), (l, 25,100), (g, 0,100), (l, 50,100)],
    'J': [(g, 0,0), (l, 50,0), (g, 40,0), (l, 40,75), (a, 0,95,120)],
    'K': [(g, 0,0), (l, 0,100), (g, 0,70), (a, 50,0,-40), (g, 18,55), (a, 50,100,-40)],
    'L': [(g, 0,0), (l, 0,80), (a, 20,100,-90), (l, 50, 100)],
    'M': [(g, 0,100), (l, 0,0), (l, 25,55), (l, 50,0), (l, 50,100)],
    'N': [(g, 0,100), (l, 0,0), (l, 50,100), (l, 50,0)],
    'O': [(g, 0,20), (a, 20,0,90), (l, 30,0), (a, 50,20,90), (l, 50,80), (a, 30,100,90), (l, 20,100), (a, 0,80,90), (l, 0,20)],
    'P': [(g, 0,100), (l, 0,0), (l, 22,0), (a, 22,55,180), (l, 0,55)],
    'Q': [(g, 0,20), (a, 20,0,90), (l, 30,0), (a, 50,20,90), (l, 50,70), (a, 30,90,90), (l, 20,90), (a, 0,70,90), (l, 0,20), (g, 50,100), (a, 30,90,80)],
    'R': [(g, 0,100), (l, 0,0), (l, 22,0), (a, 22,55,180), (l, 0,55), (g, 18,55), (a, 50,100,-40)],
    'S': [(g, 50,0), (l, 25,0), (a, 25,50,-180), (a, 25,100,180), (l, 0,100)],
    'T': [(g, 0,0), (l, 50,0), (g, 25,0), (l, 25,100)],
    'U': [(g, 0,0), (l, 0,80), (a, 20,100,-90), (l, 30,100), (a, 50,80,-90), (l, 50,0)],
    'V': [(g, 0,0), (l, 25,100), (l, 50,0)],
    'W': [(g, 0,0), (l, 0,100), (l, 25,55), (l, 50,100), (l, 50, 0)],
    'X': [(g, 0,0), (l, 50,100), (g, 0,100), (l, 50,0)],
    'Y': [(g, 0,0), (l, 25,55), (l, 50,0), (g, 25,55), (l, 25,100)],
    'Z': [(g, 0,0), (l, 50,0), (l, 0,100), (l, 50,100)],
}

def _draw_sequence(p: Plot, seq, origin, scale):
    for f, x, y, *rest in seq:
        x = origin.x + scale * x/100
        y = origin.y + scale * y/100
        f.__get__(p, Plot)(x, y, *rest)

KERN = 0.1

def _draw_bounding_box(p, origin, scale):
    p.goto(*origin)
    p.lineto(origin.x + scale/2, origin.y)
    p.lineto(origin.x + scale/2, origin.y + scale)
    p.lineto(origin.x, origin.y + scale)
    p.lineto(*origin)

def draw_string(p: Plot, s, origin, scale):
    for i, c in enumerate(s.upper()):
        if c not in CHAR_PATHS:
            continue
        char_origin = origin+i*scale*vec2(0.5+KERN, 0)

        # _draw_bounding_box(p, char_origin, scale)
        _draw_sequence(p, CHAR_PATHS[c], char_origin, scale)

def main(p: Plot):
    p.clipping = False
    p.plot_size = 8
    p.setup()
    size = 5
    draw_string(p, 'the quick brown fox jumps', vec2(0, 0), size)
    draw_string(p, 'over the lazy dog', vec2(0, size+1), size)