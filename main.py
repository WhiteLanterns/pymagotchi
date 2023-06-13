import pyxel

class Game():
    def __init__(self):
        pyxel.init(640, 480, "pymagotchi", 60)
        pyxel.load("assets\music_loop.pyxres")
        pyxel.playm(0, 0, True)
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)


Game()