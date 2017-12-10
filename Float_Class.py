from pico2d import *
import random

class FLOAT:
    image = None
    NONE, STANDING, READY, FISING, FINISH = 0, 1, 2, 3, 4

    PIXEL_PER_METER = (10.0 / 30)  # 10픽셀당 30cm
    FLOAT_SPEED_KMPH = 100.0  # 시속 100km/h
    FLOAT_SPEED_MPM = (FLOAT_SPEED_KMPH * 1000.0 / 60.0)  # 분속 1666.666...m/m
    FLOAT_SPEED_MPS = (FLOAT_SPEED_MPM / 60.0)  # 초속 27.777...m/s
    FLOAT_SPEED_PPS = (FLOAT_SPEED_MPS * PIXEL_PER_METER)  # 초속 9.259259...p/s

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self):
        self.float_des_x = 0
        self.float_des_y = 0
        self.state = self.NONE
        self.float_frame = 0
        self.total_frames = 0.0
        if FLOAT.image == None:
            FLOAT.image = load_image("resource/float.png")

    def draw(self):
        self.image.clip_draw(0, 0, 64, 64, self.float_des_x, self.float_des_y, 5, 5)

    def update(self, fisher, frame_time):
        pass
    pass