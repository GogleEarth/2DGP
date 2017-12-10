from pico2d import *

class UI:
    image = None

    def __init__(self):
        self.frame = 0
        self.guage = 1000
        if(UI.image == None):
            UI.image = load_image("resource/Hungry.png")

    def upadte(self, fisher):
        self.frame = (1 + self.frame) % 60
        if self.frame == 9 and self.guage >= 0:
            fisher.fisher_hunger -= fisher.fisher_hungry
            fisher.fisher_hungry += 1
            self.guage = fisher.fisher_hunger
            print("hungry : ", self.guage)

    def draw(self):
        self.image.clip_draw(0,0,64,64,0,550,self.guage * 1.5,10)


class BACKGROUND:
    def __init__(self):
        self.image = load_image('resource/Background.png')
        pass

    def draw(self):
        self.image.draw(400, 700, 800,1600)
        pass

