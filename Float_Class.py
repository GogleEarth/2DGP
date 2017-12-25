from pico2d import *
import random

class FLOAT:
    image = None
    NONE, STANDING, READY, FISING, FIGHTING, FINISH = 0, 1, 2, 3, 4, 5

    PIXEL_PER_METER = (10.0 / 30)  # 10픽셀당 30cm
    FLOAT_SPEED_KMPH = 100.0  # 시속 100km/h
    FLOAT_SPEED_MPM = (FLOAT_SPEED_KMPH * 1000.0 / 60.0)  # 분속 1666.666...m/m
    FLOAT_SPEED_MPS = (FLOAT_SPEED_MPM / 60.0)  # 초속 27.777...m/s
    FLOAT_SPEED_PPS = (FLOAT_SPEED_MPS * PIXEL_PER_METER)  # 초속 9.259259...p/s

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    def __init__(self,fisher):
        self.float_des_x = 0
        self.float_des_y = 0
        self.float_x_org = fisher.fisher_x
        self.float_y_org = fisher.fisher_y
        self.float_x = fisher.fisher_x
        self.float_y = fisher.fisher_y
        self.state = self.NONE
        self.float_frame = 0
        self.total_frames = 0.0
        self.scale = 20
        if FLOAT.image == None:
            FLOAT.image = load_image("resource/float.png")

    def draw(self):
        self.image.clip_draw(0, 0, 64, 64, self.float_x - self.bg.window_left, self.float_y - self.bg.window_bottom, self.scale, self.scale)

    def update(self, fisher, frame_time):

        if self.state == self.NONE:
            self.float_x = fisher.fisher_x
            self.float_y = fisher.fisher_y
            self.float_x_org = fisher.fisher_x
            self.float_y_org = fisher.fisher_y

        if self.state == self.READY:
            self.state = self.READY
            if self.float_x_org >= self.float_des_x:
                self.float_x -= (self.float_x - self.float_des_x) / self.FLOAT_SPEED_PPS
            else:
                self.float_x += (self.float_des_x - self.float_x) / self.FLOAT_SPEED_PPS
            if self.float_y_org >= self.float_des_y:
                self.float_y -= (self.float_y - self.float_des_y) / self.FLOAT_SPEED_PPS
            else:
                self.float_y += (self.float_des_y - self.float_y) / self.FLOAT_SPEED_PPS
            if self.float_x >= self.float_des_x - 1 and self.float_x < self.float_des_x + 1:
                self.state = self.FISING


        if self.state == self.FINISH:
            self.state = self.FINISH
            if self.float_x_org >= self.float_x:
                self.float_x += (self.float_x_org - self.float_x) / self.FLOAT_SPEED_PPS
            else:
                self.float_x -= (self.float_x - self.float_x_org) / self.FLOAT_SPEED_PPS
            if self.float_y_org >= self.float_y:
                self.float_y += (self.float_y_org - self.float_y) / self.FLOAT_SPEED_PPS
            else:
                self.float_y -= (self.float_y - self.float_y_org) / self.FLOAT_SPEED_PPS
            if self.float_x >= self.float_x_org - 1 and self.float_x < self.float_x_org + 1:
                self.state = self.NONE

    def set_background(self, bg):
        self.bg = bg

    def get_bb(self):
        return self.float_x - self.scale / 2 - self.bg.window_left, self.float_x - self.scale / 2 - self.bg.window_bottom, self.float_x + self.scale / 2 - self.bg.window_left, self.float_y + self.scale / 2 - self.bg.window_bottom
