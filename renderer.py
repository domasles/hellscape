from settings import *

import pygame, random

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
    
    def get_color(self, seed):
        random.seed(seed)

        rnd = random.randrange
        rng = 100, 256

        return rnd(*rng), rnd(*rng), rnd(*rng)

    def draw(self):
        def lines():
            for l in self.linedefs:
                p1 = self.vertexes[l.start_vertex]
                p2 = self.vertexes[l.end_vertex]

                pygame.draw.line(self.engine.screen, (70, 70, 70), p1, p2)

        def vertexes():
            for v in self.vertexes:
                pygame.draw.circle(self.engine.screen, "white", (v.x, v.y), 2)

        def bounds(bound, color):
            x, y = self.remap_x(bound.left), self.remap_y(bound.top)
            w, h = self.remap_x(bound.right) - x, self.remap_y(bound.bottom) - y

            pygame.draw.rect(self.engine.screen, color, (x, y, w, h), 2)

        def node(node):
            node = self.engine.data.nodes[node]

            bounds_right = node.bounds["right"]
            bounds_left = node.bounds["left"]

            bounds(bounds_right, "green")
            bounds(bounds_left, "red")

            x1, y1 = self.remap_x(node.x_part), self.remap_y(node.y_part)
            x2 =self.remap_x(node.x_part + node.dx_part)
            y2 =self.remap_y(node.y_part + node.dy_part)

            pygame.draw.line(self.engine.screen, "blue", (x1, y1), (x2, y2), 4)

        def player():
            pos = self.engine.player.pos
            x = self.remap_x(pos.x)
            y = self.remap_y(pos.y)

            pygame.draw.circle(self.engine.screen, "orange", (x, y), 5)

        lines()
        player()
        node(self.engine.bsp.root_node)

    def draw_segment(self, segment, sub_sector):
        v1 = self.vertexes[segment.start_vertex]
        v2 = self.vertexes[segment.end_vertex]

        pygame.draw.line(self.engine.screen, self.get_color(sub_sector), v1, v2, 4)
        pygame.display.flip()
        pygame.time.wait(1)
