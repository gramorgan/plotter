from functools import partial
from collections import namedtuple
import math
from numbers import Number
from collections.abc import Iterable

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
        if not isinstance(other, Number):
            return NotImplemented
        return vec2(other*self.x, other*self.y)
    def __rmul__(self, other):
        if not isinstance(other, Number):
            return NotImplemented
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
    def dot(self, other):
        return self.x*other.x + self.y*other.y
    def __repr__(self):
        return 'vec2({:.2f}, {:.2f})'.format(self.x, self.y)
    def __getattr__(self, swiz):
        if len(swiz) == 2:
            return vec2(*(getattr(self, a) for a in swiz))
        if len(swiz) == 3:
            return vec3(*(getattr(self, a) for a in swiz))
        if len(swiz) == 4:
            return vec4(*(getattr(self, a) for a in swiz))

    def rotate(self, angle):
        angle = math.radians(angle)
        c = math.cos(angle)
        s = math.sin(angle)
        return vec2(
            self.x*c - self.y*s,
            self.x*s + self.y*c,
        )

class vec3(namedtuple('vec3', ['x', 'y', 'z'])):

    def __new__(cls, x, y=None, z=None):
        y = x if y is None else y
        z = y if z is None else z
        return super().__new__(cls, x, y, z)
    def __add__(self, other):
        return vec3(self.x+other.x, self.y+other.y, self.z+other.z)
    def __mul__(self, other):
        if not isinstance(other, Number):
            return NotImplemented
        return vec3(other*self.x, other*self.y, other*self.z)
    def __rmul__(self, other):
        if not isinstance(other, Number):
            return NotImplemented
        return vec3(other*self.x, other*self.y, other*self.z)
    def __truediv__(self, other):
        return vec3(self.x/other, self.y/other, self.z/other)
    def __floordiv__(self, other):
        return vec3(self.x//other, self.y//other, self.z//other)
    def __sub__(self, other):
        return vec3(self.x-other.x, self.y-other.y, self.z-other.z)
    def __neg__(self):
        return vec3(-self.x, -self.y, -self.z)
    def mag(self):
        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
    def normalize(self):
        return self/self.mag()
    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z
    def cross(self, other):
        return vec3(
            self.y*other.z - self.z*other.y,
            self.z*other.x - self.x*other.z,
            self.x*other.y - self.y*other.x
        )
    def __repr__(self):
        return 'vec3({:.2f}, {:.2f}, {:.2f})'.format(self.x, self.y, self.z)
    def __getattr__(self, swiz):
        if len(swiz) == 2:
            return vec2(*(getattr(self, a) for a in swiz))
        if len(swiz) == 3:
            return vec3(*(getattr(self, a) for a in swiz))
        if len(swiz) == 4:
            return vec4(*(getattr(self, a) for a in swiz))

class vec4(namedtuple('vec4', ['x', 'y', 'z', 'w'])):

    def __new__(cls, x, y=None, z=None, w=None):
        y = x if y is None else y
        z = y if z is None else z
        w = r if w is None else w
        return super().__new__(cls, x, y, z, w)
    def __add__(self, other):
        return vec4(self.x+other.x, self.y+other.y, self.z+other.z, self.w+other.w)
    def __mul__(self, other):
        if not isinstance(other, Number):
            return NotImplemented
        return vec4(other*self.x, other*self.y, other*self.z, other*self.w)
    def __rmul__(self, other):
        if not isinstance(other, Number):
            return NotImplemented
        return vec4(other*self.x, other*self.y, other*self.z, other*self.w)
    def __truediv__(self, other):
        return vec4(self.x/other, self.y/other, self.z/other, self.w/other)
    def __floordiv__(self, other):
        return vec4(self.x//other, self.y//other, self.z//other, self.w//other)
    def __sub__(self, other):
        return vec4(self.x-other.x, self.y-other.y, self.z-other.z, self.w-other.w)
    def __neg__(self):
        return vec4(-self.x, -self.y, -self.z, -self.w)
    def mag(self):
        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z + self.w*self.w)
    def normalize(self):
        return self/self.mag()
    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z + self.w*other.w
    def __repr__(self):
        return 'vec4({:.2f}, {:.2f}, {:.2f}, {:.2f})'.format(self.x, self.y, self.z, self.w)
    def __getattr__(self, swiz):
        if len(swiz) == 2:
            return vec2(*(getattr(self, a) for a in swiz))
        if len(swiz) == 3:
            return vec3(*(getattr(self, a) for a in swiz))
        if len(swiz) == 4:
            return vec4(*(getattr(self, a) for a in swiz))
