from pico2d import *

import random

from Tilemap import load_tile_map

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



class FixedTileBackground:

    def __init__(self):
        self.tile_map = load_tile_map('resource/Sea_tilemap.json')
        self.max_stone_id = self.tile_map.max_stone_id
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.tile_map.width * self.tile_map.tilewidth
        self.h = self.tile_map.height * self.tile_map.tileheight
        print(self.w,self.h)
        self.bgm = load_music('resource/game_bgm.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()


    def set_center_object(self, ship):
        self.center_object = ship
        self.max_window_left = self.w - self.canvas_width
        self.max_window_bottom = self.h - self.canvas_height

    def draw(self):
        self.tile_map.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height, 0, 0)
        pass

    def update(self, frame_time):
        self.window_left = clamp(0, int(self.center_object.ship_x) - self.canvas_width//2, self.max_window_left)
        self.window_bottom = clamp(0, int(self.center_object.ship_y) - self.canvas_height//2, self.max_window_bottom)



