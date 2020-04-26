from collections import Iterable
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


class _vec(tuple):

    @staticmethod
    def _flatten(seq):
        for e in seq:
            if isinstance(e, Iterable):
                yield from e
            else:
                yield e

    def __add__(self, other):
        return self.__class__(a+b for a, b in zip(self, other))
    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return sum(a*b for a, b in zip(self, other))
        return self.__class__(a*other for a in self)
    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.__class__(other*a for a in self)
    def __truediv__(self, other):
        return self.__class__(a/other for a in self)
    def __floordiv__(self, other):
        return self.__class__(a//other for a in self)
    def __sub__(self, other):
        return self.__class__(a-b for a, b in zip(self, other))
    def __neg__(self):
        return self.__class__(-a for a in self)
    def mag(self):
        return math.sqrt(sum(a*a for a in self))
    def normalize(self):
        return self/self.mag()
    def __getnewargs__(self):
        return tuple(*self)
    def __repr__(self):
        return '({})'.format(', '.join('{:.2f}'.format(s) for s in self))
    def __getattr__(self, attr):
        if len(attr) == 1:
            return self[self.swiz_indices[attr]]
        return self.__class__(self[self.swiz_indices[e]] for e in attr)


class vec2(_vec):
    swiz_indices = {
        'x': 0, 'y': 1,
    }

    def __new__(cls, *args):
        args = tuple(cls._flatten(args))
        if len(args) == 1:
            return super().__new__(cls, args*2)
        elif len(args) == 2:
            return super().__new__(cls, args)
        raise ValueError('cannot create {} from {} arguments'.format(cls.__name__, len(args)))

    def rotate(self, angle):
        assert len(self) == 2, 'can only rotate vectors of dimension 2'
        perp = self.__class__(*(-self[1], self[0]))
        angle = angle * math.pi / 180.0
        c, s = math.cos(angle), math.sin(angle)
        return self.__class__(self[0]*c+perp[0]*s, self[1]*c+perp[1]*s)


class vec3(_vec):
    swiz_indices = {
        'x': 0, 'y': 1, 'z': 2,
        'r': 0, 'g': 1, 'b': 2,
    }

    def __new__(cls, *args):
        args = tuple(cls._flatten(args))
        if len(args) == 1:
            return super().__new__(cls, args*3)
        elif len(args) == 3:
            return super().__new__(cls, args)
        raise ValueError('cannot create {} from {} arguments'.format(cls.__name__, len(args)))


class vec4(_vec):
    swiz_indices = {
        'x': 0, 'y': 1, 'z': 2, 'w': 3,
        'r': 0, 'g': 1, 'b': 2, 'a': 3,
    }

    def __new__(cls, *args):
        args = tuple(cls._flatten(args))
        if len(args) == 1:
            return super().__new__(cls, args*4)
        elif len(args) == 4:
            return super().__new__(cls, args)
        raise ValueError('cannot create {} from {} arguments'.format(cls.__name__, len(args)))
