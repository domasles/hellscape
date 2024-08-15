from settings import *

import pygame, time

class Renderer:
    def __init__(self, engine):
        self.engine = engine
        self.data = engine.data
        self.vertexes = self.data.vertexes
        self.linedefs = self.data.linedefs

        self.min_x, self.max_x, self.min_y, self.max_y = self.get_map_bounds()
        self.vertexes = [pygame.math.Vector2(self.remap_x(v.x), self.remap_y(v.y)) for v in self.vertexes]

    def get_map_bounds(self):
        sorted_x = sorted(self.vertexes, key=lambda v: v.x)
        min_x, max_x = sorted_x[0].x, sorted_x[-1].x

        sorted_y = sorted(self.vertexes, key=lambda v: v.y)
        min_y, max_y = sorted_y[0].y, sorted_y[-1].y

        return min_x, max_x, min_y, max_y
    
    def remap_x(self, n, min_out=30, max_out=W-30):
        return (max(self.min_x, min(n, self.max_x)) - self.min_x) * (max_out - min_out) / (self.max_x - self.min_x) + min_out
    
    def remap_y(self, n, min_out=30, max_out=H-30):
        return H - (max(self.min_y, min(n, self.max_y)) - self.min_y) * (max_out - min_out) / (self.max_y - self.min_y) - min_out

    def draw(self):
        for l in self.linedefs:
            p1 = self.vertexes[l.start_vertex]
            p2 = self.vertexes[l.end_vertex]

            pygame.draw.line(self.engine.screen, "orange", p1, p2)

        for v in self.vertexes:
            pygame.draw.circle(self.engine.screen, "white", (v.x, v.y), 2)
