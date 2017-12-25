
import json

from pico2d import *

class TileSet:

    def __init__(self):
        self.firstgid = 0

    def load(self, file_name):
        f = open(file_name)
        data = json.load(f)
        f.close()
        self.__dict__.update(data)
        self.base_image = load_image(self.image)
        self.tile_images = []
        image = self.base_image.clip_image(0, 0, self.tilewidth, self.tileheight)
        self.tile_images.append(image)
        pass


def load_tile_set(file_name):
    tile_set = TileSet()
    tile_set.load(file_name)

    return tile_set
    pass