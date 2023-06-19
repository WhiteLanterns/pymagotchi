import pyxel
from classes import *


class Game:
    def __init__(self):
        pyxel.init(120, 120, "pymagotchi", 60)
        pyxel.load("assets\music_loop.pyxres")
        pyxel.playm(0, 0, True)
        pyxel.load("assets\pet.pyxres")
        self.pet = Pet(55, 55, 8, 8, 10, 5, 10, 10, 5)
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        self.pet.draw()


Game()
