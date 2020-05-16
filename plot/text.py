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
    '0': [(g, 0,20), (a, 20,0,90), (l, 30,0), (a, 50,20,90), (l, 50,80), (a, 30,100,90), (l, 20,100), (a, 0,80,90), (l, 0,20), (g, 44,6), (l, 6,94)],
    '1': [(g, 0,100), (l, 50,100), (g, 25,100), (l, 25,0), (a, 0,20,60)],
    '2': [(g, 0,25), (a, 50,25,180), (a, 20,65,40), (a, 0,100,-40), (l, 50,100)],
    '3': [(g, 0,20), (a, 48,20,150), (a, 20,55,110), (a, 50,75,80), (a, 0,75,180)],
    '4': [(g, 40,100), (l, 40,0), (l, 0,55), (l, 50,55)],
    '5': [(g, 50,0), (l, 0,0), (l, 0,55), (a, 25,100,225), (l, 0,100)],
    '6': [(g, 50,0), (a, 0,55,-90), (l, 0,75), (a, 50,75,-180), (l, 50,70), (a, 0,70,-180)],
    '7': [(g, 0,0), (l, 50,0), (l, 10,100), (g, 13,55), (l, 43,55)],
    '8': [(g, 25,0), (a, 25,55,160), (a, 25,100,-185), (a, 25,55,-185), (a, 25,0,160)],
    '9': [(g, 0,100), (a, 50,55,-90), (l, 50,25), (a, 0,25,-180), (l, 0,30), (a, 50,30,-180)],
    '<': [(g, 50,25), (l, 0,55), (l, 50,85)],
    '>': [(g, 0,25), (l, 50,55), (l, 0,85)],
}

def _draw_sequence(p: Plot, seq, origin, scale, angle):
    for f, x, y, *rest in seq:
        x, y = origin + scale*vec2(x, y).rotate(angle)/100
        f.__get__(p, Plot)(x, y, *rest)

def _draw_bounding_box(p, origin, scale):
    p.goto(*origin)
    p.lineto(origin.x + scale/2, origin.y)
    p.lineto(origin.x + scale/2, origin.y + scale)
    p.lineto(origin.x, origin.y + scale)
    p.lineto(*origin)

def draw_string(p: Plot, s, origin, scale, angle=0, **kwargs):
    kern = kwargs.get('kern', 1)
    for i, c in enumerate(s.upper()):
        if c not in CHAR_PATHS:
            continue
        char_origin = origin + i*(scale/2+kern)*vec2(1, 0).rotate(angle)

        # _draw_bounding_box(p, char_origin, scale)
        _draw_sequence(p, CHAR_PATHS[c], char_origin, scale, angle)

def draw_string_wrapped(p: Plot, s, width, origin, scale, angle=0, **kwargs):
    kern = kwargs.get('kern', 1)
    vert_spacing = kwargs.get('vert_spacing', 1)
    for i, c in enumerate(s.upper()):
        if c not in CHAR_PATHS:
            continue
        true_width = width-scale/2
        x = i*(scale/2+kern)
        y = (x // true_width) * (scale + vert_spacing)
        x = x % true_width
        char_origin = origin + vec2(x, y).rotate(angle)

        # _draw_bounding_box(p, char_origin, scale)
        _draw_sequence(p, CHAR_PATHS[c], char_origin, scale, angle)

def main(p: Plot):
    p.clipping = False
    p.plot_size = 4
    p.speed_pendown = 100
    p.setup()
    p.draw_bounding_box()
    size = 1.9
    # draw_string(p, '720 vert', vec2(100, 0), size, 90)
    # draw_string(p, 'tony hawk', vec2(100-(size+1), 0), size, 90)
    # draw_string(p, 'the quick brown fox jumps', vec2(0, 0), size)
    # draw_string(p, 'over the lazy dog', vec2(0, size+1), size)
    # draw_string(p, '0123456789><', vec2(0, 2*(size+1)), size)

    navy_seal = "What the fuck did you just fucking say about me you little bitch Ill have you know I graduated top of my class in the Navy Seals and Ive been involved in numerous secret raids on Al-Quaeda and I have over 300 confirmed kills I am trained in gorilla warfare and Im the top sniper in the entire US armed forces You are nothing to me but just another target I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth mark my fucking words You think you can get away with saying that shit to me over the Internet Think again fucker As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm maggot The storm that wipes out the pathetic little thing you call your life Youre fucking dead kid I can be anywhere anytime and I can kill you in over seven hundred ways and thats just with my bare hands Not only am I extensively trained in unarmed combat but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent you little shit If only you could have known what unholy retribution your little clever comment was about to bring down upon you maybe you would have held your fucking tongue But you couldnt you didnt and now youre paying the price you goddamn idiot I will shit fury all over you and you will drown in it Youre fucking dead kiddo"
    draw_string_wrapped(p, navy_seal, 100, vec2(0, 0), size)