from pico2d import *
import random
from Tilemap import load_tile_map

class OBJECT:
    image = None

    def __init__(self,id):
        self.tile_map = load_tile_map('resource/Sea_tilemap.json')
        self.x = self.tile_map.object_stone[id]['x']
        self.y = self.tile_map.object_stone[id]['y']
        self.width = self.tile_map.object_stone[id]['width']
        self.height = self.tile_map.object_stone[id]['height']
        if OBJECT.image == None:
            OBJECT.image = load_image('resource/Stone.png')
        pass

    def draw(self):
        self.image.draw(self.x - self.bg.window_left, self.y - self.bg.window_bottom, self.width, self.height)
        pass

    def set_background(self, bg):
        self.bg = bg
        self.y = bg.h - self.y