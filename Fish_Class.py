from pico2d import *
import random

class FISH:
    image = None
    UN_DROW, DRAW = 0, 1
    def __init__(self):
        self.fish_id = random.randint(0,4)
        self.fish_level = random.randint(1,3)
        self.fish_size = random.randint(30,100)
        self.fish_heal = self.fish_size * 2
        self.fish_state = self.UN_DROW
        self.fish_y = 20
        self.weight = 0
        if(FISH.image == None):
            FISH.image = load_image("resource/fishes.png")

    def update(self, fisher, float):
        if float.state == float.FISING:
            i = random.randint(0,100)
            if i <= 4 - self.fish_level + fisher.fisher_luck + self.weight:
                float.state = float.FIGHTING
                fisher.state = fisher.FIGHTING
                self.reset()
                self.fish_state = self.UN_DROW
        if self.fish_state == self.DRAW:
            self.fish_y = self.fish_y + 1
            if self.fish_y >= 30:
                self.fish_state = self.UN_DROW
        pass

    def draw(self, fisher):
        self.image.clip_draw(self.fish_id * 64,0,64,64,fisher.fisher_x - self.bg.window_left,fisher.fisher_y + self.fish_y - self.bg.window_bottom)
        pass

    def reset(self):
        self.fish_id = random.randint(0,4)
        self.fish_level = random.randint(1, 3)
        self.fish_size = random.randint(30, 100)
        self.fish_heal = self.fish_size * 2
        self.fish_state = self.UN_DROW
        self.fish_y = 20

    def set_background(self, bg):
        self.bg = bg