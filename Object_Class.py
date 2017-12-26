from pico2d import *
import random
from Tilemap import load_tile_map

class STONE:
    image = None

    def __init__(self,id):
        self.tile_map = load_tile_map('resource/Sea_tilemap.json')
        self.x = self.tile_map.object_stone[id]['x']
        self.y = self.tile_map.object_stone[id]['y']
        self.width = self.tile_map.object_stone[id]['width']
        self.height = self.tile_map.object_stone[id]['height']
        if STONE.image == None:
            STONE.image = load_image('resource/Stone.png')
        pass

    def draw(self):
        self.image.draw(self.x - self.bg.window_left, self.y - self.bg.window_bottom, self.width, self.height)
        pass

    def set_background(self, bg):
        self.bg = bg

    def get_bb(self):
        return self.x - self.width / 2 - self.bg.window_left, self.y - self.height / 2 - self.bg.window_bottom, self.x + self.width / 2 - self.bg.window_left, self.y + self.height / 2 - self.bg.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class VORTEX:
    image = None

    def __init__(self,id):
        self.tile_map = load_tile_map('resource/Sea_tilemap.json')
        self.x = self.tile_map.object_vortex[id]['x']
        self.y = self.tile_map.object_vortex[id]['y']
        self.width = self.tile_map.object_vortex[id]['width']
        self.height = self.tile_map.object_vortex[id]['height']
        if VORTEX.image == None:
            VORTEX.image = load_image('resource/Vortex.png')
        pass

    def draw(self):
        self.image.draw(self.x - self.bg.window_left, self.y - self.bg.window_bottom, self.width, self.height)
        pass

    def set_background(self, bg):
        self.bg = bg

    def get_bb(self):
        return self.x - self.width / 2 - self.bg.window_left, self.y - self.height / 2 - self.bg.window_bottom, self.x + self.width / 2 - self.bg.window_left, self.y + self.height / 2 - self.bg.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class LOCAL:

    def __init__(self,id):
        self.tile_map = load_tile_map('resource/Sea_tilemap.json')
        self.x = self.tile_map.object_loacl[id]['x']
        self.y = self.tile_map.object_loacl[id]['y']
        self.width = self.tile_map.object_loacl[id]['width']
        self.height = self.tile_map.object_loacl[id]['height']
        self.weight = random.randint(-40,40)
        pass

    def draw(self):
        pass

    def set_background(self, bg):
        self.bg = bg

    def get_bb(self):
        return self.x - self.width / 2 - self.bg.window_left, self.y - self.height / 2 - self.bg.window_bottom, self.x + self.width / 2 - self.bg.window_left, self.y + self.height / 2 - self.bg.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())