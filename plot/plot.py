import turtle as t
from pyaxidraw import axidraw
import math
from functools import partial
from .utils import vec2

FLOAT_EPSILON =  0.001

def _dist_between(a, b):
    x_dist = a.x - b.x
    y_dist = a.y - b.y
    return math.sqrt(x_dist*x_dist + y_dist*y_dist)

def _line_segment_intersection(p1, p2, p3, p4):
    d = (p4.x-p3.x) * (p1.y-p2.y) - (p1.x-p2.x) * (p4.y-p3.y)
    if d == 0:
        # lines are parallel
        return None
    ta = ((p3.y-p4.y) * (p1.x-p3.x) + (p4.x-p3.x) * (p1.y-p3.y)) / d
    tb = ((p1.y-p2.y) * (p1.x-p3.x) + (p2.x-p1.x) * (p1.y-p3.y)) / d
    if ta >= 0 and ta <= 1 and tb >= 0 and tb <= 1:
        return vec2(
            p1.x + ta * (p2.x-p1.x),
            p1.y + ta * (p2.y-p1.y)
        )
    return None

class dotdict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

class Plot():

    DEFAULT_POS = vec2(0)
    DEFAULT_HEADING = vec2(0, -1)
    DEFAULT_PENUP = True

    def __init__(self, plotter_enabled=False):
        self.set_canvas_size(100, 100)

        self.plot_size = 4
        self.plotter_enabled = plotter_enabled

        self.clipping = True
        self.cull_empty_at_edges = True

        self._reset_plot_state()
        self._real_pos = self.DEFAULT_POS

        self.ad = None
        self.options = dotdict()

        t.hideturtle()
        t.tracer(1000, 0)
    
    def set_canvas_size(self, xsize, ysize):
        self.canvas_size = vec2(xsize, ysize)
        self._max_canvas_size = max(self.canvas_size)
        t.setworldcoordinates(0, self._max_canvas_size, self._max_canvas_size, 0)
    
    def setup(self):
        t.clear()
        self._reset_plot_state()

        if self.plotter_enabled:
            self.ad = axidraw.AxiDraw()
            self.ad.interactive()
            self.ad.options.const_speed = True
            for k, v in self.options.items():
                setattr(self.ad.options, k, v)
            if not self.ad.connect():
                raise RuntimeError('plotter not connected')

            self.options = self.ad.options
    
    def _reset_plot_state(self):
        self._current_pos = self.DEFAULT_POS
        self._current_heading = self.DEFAULT_HEADING
        self._current_penup = self.DEFAULT_PENUP
    
    def done(self):
        if self.plotter_enabled:
            self.ad.moveto(0, 0)
            self.ad.plot_setup()
            self.ad.options.mode = 'align'
            self.ad.plot_run()
            self.ad.disconnect()

        t.update()
        t.done()
    
    def draw_bounding_box(self, plot=False):
        old_plot_enabled = self.plotter_enabled
        if not plot:
            self.plotter_enabled = False
        self.goto(0, 0)
        self.lineto(self.canvas_size.x, 0)
        self.lineto(self.canvas_size.x, self.canvas_size.y)
        self.lineto(0, self.canvas_size.y)
        self.lineto(0, 0)
        self.plotter_enabled = old_plot_enabled
    
    def goto(self, x, y):
        self._current_pos = vec2(x, y)
        self._current_penup = True

    def _goto(self, x, y):
        if self.clipping:
            x = max(x, 0)
            y = max(y, 0)

        t.penup()
        t.goto(x, y)
        self._real_pos = vec2(x, y)
        if self.plotter_enabled:
            t.update()
            self.ad.moveto(
                (x/self._max_canvas_size)*self.plot_size,
                (y/self._max_canvas_size)*self.plot_size
            )
    
    def lineto(self, x, y):
        old_in_bounds = self.in_bounds(*self._current_pos)
        new_in_bounds = self.in_bounds(x, y)
        if self.clipping and old_in_bounds and new_in_bounds:
            self._lineto(x, y)
        elif self.clipping:
            edge_intersections = self.get_edge_intersections(self._current_pos, vec2(x, y))
            if len(edge_intersections) == 1 and new_in_bounds:
                if not (self.cull_empty_at_edges and _dist_between(vec2(x, y), edge_intersections[0]) < FLOAT_EPSILON):
                    self.goto(*edge_intersections[0])
                    self._lineto(x, y)
            elif len(edge_intersections) == 1 and not new_in_bounds:
                if not (self.cull_empty_at_edges and _dist_between(self._current_pos, edge_intersections[0]) < FLOAT_EPSILON):
                    self._lineto(*edge_intersections[0])
            elif len(edge_intersections) == 2:
                close = min(edge_intersections, key=partial(_dist_between, self._real_pos))
                far   = max(edge_intersections, key=partial(_dist_between, self._real_pos))
                self.goto(*close)
                self._lineto(*far)
            elif len(edge_intersections) > 2:
                print('error: more than 2 edge intersections. time to fix this')
        else:
            self._lineto(x, y)
        self._current_penup = False
        self._current_pos = vec2(x, y)

    def _lineto(self, x, y):
        if self.clipping:
            x = max(x, 0)
            y = max(y, 0)

        if self._real_pos != self._current_pos:
            self._goto(*self._current_pos)
        t.pendown()
        t.goto(x, y)
        self._real_pos = vec2(x, y)
        if self.plotter_enabled:
            t.update()
            self.ad.lineto(
                (x/self._max_canvas_size)*self.plot_size,
                (y/self._max_canvas_size)*self.plot_size
            )
    
    def penup(self):
        self._current_penup = True
    def pendown(self):
        self._current_penup = False
    def forward(self, dist):
        new_pos = self._current_pos + self._current_heading * dist
        if self._current_penup:
            self.goto(*new_pos)
        else:
            self.lineto(*new_pos)
    def set_angle(self, angle):
        self._current_heading = self.DEFAULT_HEADING.rotate(angle)
    def right(self, angle):
        self._current_heading = self._current_heading.rotate(angle)
    def left(self, angle):
        self._current_heading = self._current_heading.rotate(-angle)
    
    def inches_to_units(self, a):
        return (a / self.plot_size) * self._max_canvas_size
    
    def in_bounds(self, x, y):
        return (
                x >= 0
            and x <= self.canvas_size.x
            and y >= 0
            and y <= self.canvas_size.y
        )
    
    def get_edge_intersections(self, old_pos, new_pos):
        topleft = vec2(0)
        topright = vec2(self.canvas_size.x, 0)
        bottomleft = vec2(0, self.canvas_size.y)
        bottomright = self.canvas_size
        edges = [
            (topleft, topright),
            (topright, bottomright),
            (bottomright, bottomleft),
            (bottomleft, topleft),
        ]
        return list(filter(None, [_line_segment_intersection(old_pos, new_pos, e[0], e[1]) for e in edges]))
    
    def pen_change(self):
        if self.plotter_enabled:
            self.ad.penup()
        t.update()
        input()
    
    def circle(self, origin, radius, len_segments_inches=0.02):
        len_segments = self.inches_to_units(len_segments_inches)
        num_divisions = max(3, round((2*math.pi*radius)/len_segments))
        self.goto(origin[0]+radius, origin[1])
        for t in range(1, num_divisions+1):
            x = origin[0] + radius*math.cos((t/num_divisions)*(2*math.pi))
            y = origin[1] + radius*math.sin((t/num_divisions)*(2*math.pi))
            self.lineto(x, y)
    
    def arc(self, radius, angle, left=False, len_segments_inches=0.02):
        if left:
            radius *= -1
            angle *= -1

        center = self._current_pos + self._current_heading.rotate(90) * radius
        offset = self._current_pos - center

        len_segments = self.inches_to_units(len_segments_inches)
        num_divisions = max(3, round(2*math.pi*abs(radius)*(abs(angle)/360)/len_segments))
        for t in range(1, num_divisions+1):
            cur_offset = offset.rotate(t*angle/num_divisions)
            self.lineto(*(center+cur_offset))
        self.right(angle)
    
    def arcto(self, x, y, angle, len_segments_inches=0.02):
        sign = 1 if angle > 0 else -1
        angle = abs(angle) % 360
        if angle == 0:
            self.lineto(x, y)
            return
        
        d = _dist_between(self._current_pos, vec2(x, y))
        r = abs(d / (2 * math.cos(math.pi/2 - math.radians(angle/2))))
        offset = -(vec2(x, y) - self._current_pos).normalize().rotate(sign*(90-angle/2))*r
        center = self._current_pos - offset

        len_segments = self.inches_to_units(len_segments_inches)
        num_divisions = max(3, round((2*math.pi*r * (angle/360)) / len_segments))
        for t in range(1, num_divisions+1):
            cur_offset = offset.rotate(sign*t*angle/num_divisions)
            self.lineto(*(center+cur_offset))
