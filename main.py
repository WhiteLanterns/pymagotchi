import pyxel


class Game:
    def __init__(self):
        pyxel.init(120, 120, "pymagotchi", 60)
        pyxel.load("assets\music_loop.pyxres")
        pyxel.playm(0, 0, True)
        pyxel.load("assets\pet.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(55, 55, 0, 8, 0, 8, 8)


Game()
