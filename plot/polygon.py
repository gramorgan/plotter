from __future__ import annotations
from typing import List, Tuple
from .utils import vec2

class Polygon():

    @staticmethod
    def _do_clip_intersection(cp1, cp2, sp1, sp2):
        d = (sp2.x-sp1.x) * (cp1.y-cp2.y) - (cp1.x-cp2.x) * (sp2.y-sp1.y)
        if d == 0:
            # lines are parallel
            return None
        t = ((cp1.y-cp2.y) * (cp1.x-sp1.x) + (cp2.x-cp1.x) * (cp1.y-sp1.y)) / d
        if t >= 0 and t <= 1:
            return sp1 + t * (sp2-sp1)
        return None
    
    @staticmethod
    def _inside_clip(cp1, cp2, point):
        P = (cp2.x-cp1.x) * (point.y-cp1.y) - (cp2.y - cp1.y) * (point.x-cp1.x)
        return P > 0

    def __init__(self, points: List[vec2]):
        self.points: List[vec2] = points
    
    def get_edges(self) -> List[Tuple[vec2, vec2]]:
        for i, point in enumerate(self.points):
            yield (point, self.points[(i+1) % len(self.points)])
    
    def clip(self, clip_poly: Polygon):
        for cp1, cp2 in clip_poly.get_edges():
            new_points = []
            for sp1, sp2 in self.get_edges():
                intersection = self._do_clip_intersection(cp1, cp2, sp1, sp2)
                if intersection is None:
                    if self._inside_clip(cp1, cp2, sp1):
                        new_points.append(sp1)
                    continue
                if self._inside_clip(cp1, cp2, sp2):
                    if not self._inside_clip(cp1, cp2, sp1):
                        new_points.append(intersection)
                    new_points.append(sp1)
                elif self._inside_clip(cp1, cp2, sp1):
                    new_points.append(intersection)
                
            print(new_points)
            self.points = new_points
