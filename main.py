import pyxel
<<<<<<< HEAD
import classes
=======
from classes import *
>>>>>>> 364423ba4b62046cfac6d8309d87d8fd1a38a6e1


class Game:
    def __init__(self):
<<<<<<< HEAD
        pyxel.init(160, 120, title="pymagotchi", fps=60)
        pyxel.load("assets\music_loop.pyxres")
        pyxel.playm(0, 0, True)
        pyxel.load("assets\pet.pyxres")
        pyxel.mouse(True)
        self.x = 0
=======
        pyxel.init(120, 120, "pymagotchi", 60)
        pyxel.load("assets\music_loop.pyxres")
        pyxel.playm(0, 0, True)
        pyxel.load("assets\pet.pyxres")
        self.pet = Pet(55, 55, 8, 8, 10, 5, 10, 10, 5)
>>>>>>> 364423ba4b62046cfac6d8309d87d8fd1a38a6e1
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
<<<<<<< HEAD
        pyxel.blt(0, 0, 0, 0, 0, 8, 8)
=======
        self.pet.draw()
>>>>>>> 364423ba4b62046cfac6d8309d87d8fd1a38a6e1


Game()
