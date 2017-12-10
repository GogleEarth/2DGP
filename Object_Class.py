from pico2d import *
import random

class OBJECT:
    image = None

    def __init__(self):
        self.object_x = random.randint(0,800)
        self.object_y = random.randint(0,600)
        if OBJECT.image == None:
            OBJECT.image = load_image('resource/Stone.png')
        pass

    def draw(self):
        self.image.draw(self.object_x, self.object_y)
        pass
