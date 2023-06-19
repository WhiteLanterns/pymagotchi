import pyxel
import classes

class Game():
    def __init__(self):
        pyxel.init(160, 120, title="pymagotchi", fps=60)
        pyxel.load("assets\music_loop.pyxres")
        pyxel.playm(0, 0, True)
        pyxel.load("assets\pet.pyxres")
        pyxel.mouse(True)
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0, 0, 0, 0, 0, 8, 8)


Game()