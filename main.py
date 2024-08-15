from renderer import Renderer
from wad_data import WADData
from player import Player
from settings import *
from bsp import BSP

import pygame, sys

class Engine:
    def __init__(self):
        self.wad = self.get_wad()
        self.screen = pygame.display.set_mode(WIN_RES)
        self.clock = pygame.time.Clock()
        self.running = True
        self.d_time = 1 / 60

        self.on_init()

    def on_init(self):
        self.data = WADData(self, "E1M1")
        self.renderer = Renderer(self)
        self.player = Player(self)
        self.bsp = BSP(self)

    def update(self):
        self.player.update()
        self.bsp.update()

        self.d_time = self.clock.tick()

        pygame.display.set_caption(f"{self.clock.get_fps()}")

    def draw(self):
        self.screen.fill("black")
        self.renderer.draw()

        pygame.display.flip()

    def get_wad(self):
        if len(sys.argv) != 2:
            print("Usage: python main.py <wad_file>")
            sys.exit()

        return sys.argv[1]

    def check_events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False

    def run(self):
        while self.running:
            self.check_events()
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    engine = Engine()
    engine.run()
