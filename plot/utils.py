from collections import namedtuple
import math

SQRT_2 = 1.41421356237
SQRT_3 = 1.73205080757

def lerp(a, b, t):
    return a*(1-t) + b*t

def clamp(a, lo, hi):
    return min(hi, max(lo, a))

def smoothstep(x, lo, hi):
    x = clamp((x - lo) / (hi - lo), 0, 1)
    return x*x * (3 - 2 * x)

def smin(a, b, k):
    h = max(k-abs(a-b), 0)
    return min(a, b) - (h*h)/(4*k)

def smax(a, b, k):
    h = max(k-abs(a-b), 0)
    return max(a, b) + (h*h)/(4*k)


class vec2(namedtuple('vec2', ['x', 'y'])):

    def __new__(cls, x, y=None):
        y = x if y is None else y
        return super().__new__(cls, x, y)
    def __add__(self, other):
        return vec2(self.x+other.x, self.y+other.y)
    def __mul__(self, other):
        if isinstance(other, vec2):
            return self.x+other.x + self.y+other.y
        return vec2(other*self.x, other*self.y)
    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return vec2(other*self.x, other*self.y)
    def __truediv__(self, other):
        return vec2(self.x/other, self.y/other)
    def __floordiv__(self, other):
        return vec2(self.x//other, self.y//other)
    def __sub__(self, other):
        return vec2(self.x-other.x, self.y-other.y)
    def __neg__(self):
        return vec2(-self.x, -self.y)
    def mag(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
    def normalize(self):
        return self/self.mag()
    def __repr__(self):
        return '({:.2f}, {:.2f})'.format(self.x, self.y)

    def rotate(self, angle):
        angle = math.radians(angle)
        return vec2(
            self.x*math.cos(angle) - self.y*math.sin(angle),
            self.x*math.sin(angle) + self.y*math.cos(angle),
        )
