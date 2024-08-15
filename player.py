from pygame.math import Vector2
from settings import *

import pygame

class Player:
    def __init__(self, engine):
        self.engine = engine
        self.thing = engine.data.things[0]
        self.pos = self.thing.pos
        self.angle = self.thing.angle

    def update(self):
        pass
