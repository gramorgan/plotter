import turtle as t
from pyaxidraw import axidraw
import math
import subprocess
import atexit

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

def _line_segment_intersection(p1, p2, p3, p4):
    ta = (
        ((p3[1]-p4[1]) * (p1[0]-p3[0]) + (p4[0]-p3[0]) * (p1[1]-p3[1])) /
        ((p4[0]-p3[0]) * (p1[1]-p2[1]) - (p1[0]-p2[0]) * (p4[1]-p3[1]))
    )
    tb = (
        ((p1[1]-p2[1]) * (p1[0]-p3[0]) + (p2[0]-p1[0]) * (p1[1]-p3[1])) /
        ((p4[0]-p3[0]) * (p1[1]-p2[1]) - (p1[0]-p2[0]) * (p4[1]-p3[1]))
    )
    if ta >= 0 and ta <= 1 and tb >= 0 and tb <= 1:
        return (
            p1[0] + ta * (p2[0]-p1[0]),
            p1[1] + ta * (p2[1]-p1[1])
        )
    return None

class Plot:

    def __init__(self):
        self.canvas_size = 100
        self.plot_size = 4
        self.plot_origin = (0, 0)
        self.plotter_enabled = False

        self.clipping = True
        self._out_pos = None

        self.ad = None
        self.options = None
    
    def setup(self):
        t.setworldcoordinates(0, self.canvas_size, self.canvas_size, 0)
        t.hideturtle()
        t.tracer(500, 0)

        if self.plotter_enabled:
            self.ad = axidraw.AxiDraw()
            self.ad.interactive()
            self.ad.options.const_speed = True
            self.ad.connect()

            self.options = self.ad.options

            # prevent screen from sleeping
            self.caff_proc = subprocess.Popen(['caffeinate', '-d'])
            atexit.register(self.caff_proc.terminate)
    
    def done(self):
        if self.plotter_enabled:
            self.ad.moveto(0, 0)
            self.ad.plot_setup()
            self.ad.options.mode = 'align'
            self.ad.plot_run()
            self.ad.disconnect()

            self.caff_proc.terminate()

        t.update()
        t.done()
    
    def draw_bounding_box(self, plot=False):
        old_plot_enabled = self.plotter_enabled
        if not plot:
            self.plotter_enabled = False
        self.goto(0, 0)
        self.lineto(self.canvas_size, 0)
        self.lineto(self.canvas_size, self.canvas_size)
        self.lineto(0, self.canvas_size)
        self.lineto(0, 0)
        self.plotter_enabled = old_plot_enabled
    
    def goto(self, x, y):
        if self.clipping and not self.in_bounds(x, y):
            self._out_pos = (x, y)
            return
        self._out_pos = None
        self._goto(x, y)

    def _goto(self, x, y):
        t.penup()
        t.goto(x, y)
        if self.plotter_enabled:
            t.update()
            self.ad.moveto(
                self.plot_origin[0] + (x/self.canvas_size)*self.plot_size,
                self.plot_origin[1] + (y/self.canvas_size)*self.plot_size
            )
    
    def lineto(self, x, y):
        if self.clipping and not self.in_bounds(x, y):
            old_out_pos = self._out_pos
            self._out_pos = (x, y)
            if old_out_pos is None:
                ex, ey = self.calc_box_intersection(*t.pos())
                self._lineto(ex, ey)
            return
        if self._out_pos is not None:
            ex, ey = self.calc_box_intersection(x, y)
            self._goto(ex, ey)
            self._out_pos = None
        self._lineto(x, y)

    def _lineto(self, x, y):
        t.pendown()
        t.goto(x, y)
        if self.plotter_enabled:
            t.update()
            self.ad.lineto(
                self.plot_origin[0] + (x/self.canvas_size)*self.plot_size,
                self.plot_origin[1] + (y/self.canvas_size)*self.plot_size
            )

    def penup(self):
        t.penup()
        if self.plotter_enabled:
            self.ad.penup()

    def pendown(self):
        t.pendown()
        if self.plotter_enabled:
            self.ad.pendown()
    
    def inches_to_units(self, a):
        return (a / self.plot_size) * self.canvas_size
    
    def in_bounds(self, x, y):
        return (
                x >= 0
            and x <= self.canvas_size
            and y >= 0
            and y <= self.canvas_size
        )
    
    def calc_box_intersection(self, x, y):
        edges = [
            ((0, 0), (0, self.canvas_size)),
            ((0, self.canvas_size), (self.canvas_size, self.canvas_size)),
            ((self.canvas_size, self.canvas_size), (self.canvas_size, 0)),
            ((self.canvas_size, 0), (0, 0)),
        ]
        for edge in edges:
            pos = _line_segment_intersection(
                edge[0], edge[1],
                self._out_pos, (x, y)
            )
            if pos is not None:
                return pos
        return None
    