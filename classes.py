import pyxel


class Pet:
    def __init__(self, x, y, w, h, health, fun, hunger, energy, mood):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.health = health
        self.fun = fun
        self.hunger = hunger
        self.energy = energy
        self.mood = mood
        self.sprite_2 = 0

    def draw(self):
        sprite_1 = 8
        if pyxel.frame_count % 60 == 0:
            if self.sprite_2 == 8:
                self.sprite_2 = 0
            else:
                self.sprite_2 = 8
        pyxel.blt(self.x, self.y, 0, sprite_1, self.sprite_2, self.w, self.h)
