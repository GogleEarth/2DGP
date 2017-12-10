from pico2d import *
import random

class FISH:
    image = None
    UN_DROW, DRAW = 0, 1
    def __init__(self):
        self.fish_id = random.randint(0,3)
        self.fish_level = random.randint(1,3)
        self.fish_size = random.randint(30,100)
        self.fish_heal = self.fish_size * 2
        self.fish_state = self.UN_DROW
        self.fish_y = 20
        if(FISH.image == None):
            FISH.image = load_image("resource/fishes.png")

    def update(self, fisher, float):
        i = random.randint(0,1000)
        print("random : ", i, "fish_level : ",(4 - self.fish_level) * 5 + fisher.fisher_luck)
        if i <= (4 - self.fish_level) * 5 + fisher.fisher_luck:
            float.state = float.FISING
            print("fishing start")
            fisher.state = fisher.FIGHTING
            self.reset()
            self.fish_state = self.UN_DROW
        if self.fish_state == self.DRAW:
            self.fish_y += 1
            if self.fish_y >= 30:
                self.fish_state = self.UN_DROW
        pass

    def draw(self, fisher):
        self.image.clip_draw(self.fish_id * 64,0,64,64,fisher.fisher_x,fisher.fisher_y + self.fish_y)
        pass

    def reset(self):
        self.fish_id = random.randint(0,3)
        self.fish_level = random.randint(1, 3)
        self.fish_size = random.randint(30, 100)
        self.fish_heal = self.fish_size * 5
        self.fish_state = self.UN_DROW
        self.fish_y = 20