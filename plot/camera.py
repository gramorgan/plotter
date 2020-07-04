from .utils import vec2, vec3, vec4
from collections import namedtuple
import math

class mat4(namedtuple('mat4', [f'e{ i//4 }{ i%4 }' for i in range(16)])):

    @classmethod
    def ident(cls):
        return cls(
            1, 0, 0, 0,
            0, 1, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1
        )
    
    @classmethod
    def scale(cls, sx, sy, sz):
        return cls(
            sx, 0 , 0 , 0,
            0 , sy, 0 , 0,
            0 , 0 , sz, 0,
            0 , 0 , 0 , 1
        )

    @classmethod
    def translate(cls, tx, ty, tz):
        return cls(
            1, 0, 0, tx,
            0, 1, 0, ty,
            0, 0, 1, tz,
            0, 0, 0, 1
        )

    def get(self, r, c):
        return self[r*4 + c]

    # opengl column-major convention (no rmul)
    def __mul__(self, other):
        if not isinstance(other, vec4):
            return NotImplemented
        return vec4(
            other.x*self.e00 + other.y*self.e01 + other.z*self.e02 + other.w*self.e03,
            other.x*self.e10 + other.y*self.e11 + other.z*self.e12 + other.w*self.e13,
            other.x*self.e20 + other.y*self.e21 + other.z*self.e22 + other.w*self.e23,
            other.x*self.e30 + other.y*self.e31 + other.z*self.e32 + other.w*self.e33,
        )

    def __matmul__(self, other):
        if not isinstance(other, mat4):
            return NotImplemented
        return mat4(
            self.e00*other.e00 + self.e01*other.e10 + self.e02*other.e20 + self.e03*other.e30,
            self.e00*other.e01 + self.e01*other.e11 + self.e02*other.e21 + self.e03*other.e31,
            self.e00*other.e02 + self.e01*other.e12 + self.e02*other.e22 + self.e03*other.e32,
            self.e00*other.e03 + self.e01*other.e13 + self.e02*other.e23 + self.e03*other.e33,
            self.e10*other.e00 + self.e11*other.e10 + self.e12*other.e20 + self.e13*other.e30,
            self.e10*other.e01 + self.e11*other.e11 + self.e12*other.e21 + self.e13*other.e31,
            self.e10*other.e02 + self.e11*other.e12 + self.e12*other.e22 + self.e13*other.e32,
            self.e10*other.e03 + self.e11*other.e13 + self.e12*other.e23 + self.e13*other.e33,
            self.e20*other.e00 + self.e21*other.e10 + self.e22*other.e20 + self.e23*other.e30,
            self.e20*other.e01 + self.e21*other.e11 + self.e22*other.e21 + self.e23*other.e31,
            self.e20*other.e02 + self.e21*other.e12 + self.e22*other.e22 + self.e23*other.e32,
            self.e20*other.e03 + self.e21*other.e13 + self.e22*other.e23 + self.e23*other.e33,
            self.e30*other.e00 + self.e31*other.e10 + self.e32*other.e20 + self.e33*other.e30,
            self.e30*other.e01 + self.e31*other.e11 + self.e32*other.e21 + self.e33*other.e31,
            self.e30*other.e02 + self.e31*other.e12 + self.e32*other.e22 + self.e33*other.e32,
            self.e30*other.e03 + self.e31*other.e13 + self.e32*other.e23 + self.e33*other.e33,
        )
    
    # stolen from https://stackoverflow.com/a/44446912/12888157
    def inverse(self):
        A2323 = self.e22 * self.e33 - self.e23 * self.e32 
        A1323 = self.e21 * self.e33 - self.e23 * self.e31 
        A1223 = self.e21 * self.e32 - self.e22 * self.e31 
        A0323 = self.e20 * self.e33 - self.e23 * self.e30 
        A0223 = self.e20 * self.e32 - self.e22 * self.e30 
        A0123 = self.e20 * self.e31 - self.e21 * self.e30 
        A2313 = self.e12 * self.e33 - self.e13 * self.e32 
        A1313 = self.e11 * self.e33 - self.e13 * self.e31 
        A1213 = self.e11 * self.e32 - self.e12 * self.e31 
        A2312 = self.e12 * self.e23 - self.e13 * self.e22 
        A1312 = self.e11 * self.e23 - self.e13 * self.e21 
        A1212 = self.e11 * self.e22 - self.e12 * self.e21 
        A0313 = self.e10 * self.e33 - self.e13 * self.e30 
        A0213 = self.e10 * self.e32 - self.e12 * self.e30 
        A0312 = self.e10 * self.e23 - self.e13 * self.e20 
        A0212 = self.e10 * self.e22 - self.e12 * self.e20 
        A0113 = self.e10 * self.e31 - self.e11 * self.e30 
        A0112 = self.e10 * self.e21 - self.e11 * self.e20 

        det = ( self.e00 * ( self.e11 * A2323 - self.e12 * A1323 + self.e13 * A1223 ) 
              - self.e01 * ( self.e10 * A2323 - self.e12 * A0323 + self.e13 * A0223 ) 
              + self.e02 * ( self.e10 * A1323 - self.e11 * A0323 + self.e13 * A0123 ) 
              - self.e03 * ( self.e10 * A1223 - self.e11 * A0223 + self.e12 * A0123 ) )
        if det == 0:
            raise ValueError('matrix is not invertible')
        det = 1 / det

        return mat4(
            det *   ( self.e11 * A2323 - self.e12 * A1323 + self.e13 * A1223 ),
            det * - ( self.e01 * A2323 - self.e02 * A1323 + self.e03 * A1223 ),
            det *   ( self.e01 * A2313 - self.e02 * A1313 + self.e03 * A1213 ),
            det * - ( self.e01 * A2312 - self.e02 * A1312 + self.e03 * A1212 ),
            det * - ( self.e10 * A2323 - self.e12 * A0323 + self.e13 * A0223 ),
            det *   ( self.e00 * A2323 - self.e02 * A0323 + self.e03 * A0223 ),
            det * - ( self.e00 * A2313 - self.e02 * A0313 + self.e03 * A0213 ),
            det *   ( self.e00 * A2312 - self.e02 * A0312 + self.e03 * A0212 ),
            det *   ( self.e10 * A1323 - self.e11 * A0323 + self.e13 * A0123 ),
            det * - ( self.e00 * A1323 - self.e01 * A0323 + self.e03 * A0123 ),
            det *   ( self.e00 * A1313 - self.e01 * A0313 + self.e03 * A0113 ),
            det * - ( self.e00 * A1312 - self.e01 * A0312 + self.e03 * A0112 ),
            det * - ( self.e10 * A1223 - self.e11 * A0223 + self.e12 * A0123 ),
            det *   ( self.e00 * A1223 - self.e01 * A0223 + self.e02 * A0123 ),
            det * - ( self.e00 * A1213 - self.e01 * A0213 + self.e02 * A0113 ),
            det *   ( self.e00 * A1212 - self.e01 * A0212 + self.e02 * A0112 ),
        )

class Camera():

    def __init__(self):
        self.view = mat4.ident()
        self.proj = mat4.ident()
        self.ndc = mat4.ident()

        self.screen = mat4.ident()
        # default screen transform to Plot defaults
        self.set_screen(vec2(100, 0), vec2(0, 100))
    
    def _update_ndc(self):
        self.ndc = self.proj @ self.view
    
    def set_view(self, eye: vec3, lookat: vec3, up: vec3 = vec3(0, 1, 0)):
        cz = (eye - lookat).normalize()
        cx = up.cross(cz).normalize()
        cy = cz.cross(cx)
        self.view = mat4(
            cx.x, cx.y, cx.z, 0,
            cy.x, cy.y, cy.z, 0,
            cz.x, cz.y, cz.z, 0,
            0,    0,    0,    1
        )
        self.view @= mat4.translate(*-eye)
        self._update_ndc()
    
    # projection matrices are from
    # https://www.scratchapixel.com/lessons/3d-basic-rendering/perspective-and-orthographic-projection-matrix/
    def set_proj_orth(self, width, near, far):
        self.proj = mat4(
            2 / width , 0         , 0               , 0,
            0         , 2 / width , 0               , 0,
            0         , 0         , -2 / (far-near) , -(far+near)   / (far-near),
            0         , 0         , 0               , 1
        )
        self._update_ndc()
    
    def set_proj_persp(self, fov, near, far):
        fov = math.radians(fov)
        scale = 1 / math.tan(fov/2)
        self.proj = mat4(
            scale , 0     , 0                 , 0,
            0     , scale , 0                 , 0,
            0     , 0     , -far / (far-near) , -far*near / (far-near),
            0     , 0     , -1                , 0
        )
        self._update_ndc()
    
    def set_screen(self, topright: vec2, bottomleft: vec2):
        half_size = (topright - bottomleft) / 2
        center = (topright + bottomleft) / 2
        self.screen = mat4.translate(*center, 0) @ mat4.scale(*half_size, 1)
        self._update_ndc()
    
    def eval(self, point: vec3) -> vec3:
        point4 = vec4(*point, 1)
        point4 = self.ndc * point4
        point4 /= point4.w
        point4 = self.screen * point4
        return point4.xyz
    