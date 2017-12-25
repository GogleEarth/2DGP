from pico2d import *
import random

class SHIP:
    PIXEL_PER_METER = (10.0 / 30) #10픽셀당 30cm
    SHIP_SPEED_KMPH = 20.0 # 시속 20km/h
    SHIP_SPEED_MPM = (SHIP_SPEED_KMPH * 1000.0 / 60.0) # 분속 333.333...m/m
    SHIP_SPEED_MPS = (SHIP_SPEED_MPM / 60.0) # 초속 5.555...m/s
    SHIP_SPEED_PPS = (SHIP_SPEED_MPS * PIXEL_PER_METER) # 초속 1.851851...p/s

    LEFT_RUN, RIGHT_RUN, UP_RUN, DOWN_RUN, NONE_STATE = 1, 2, 3, 4, 0
    ACCELATE, NONE, BREAK = 1, 0, -1

    image = None

    def __init__(self):
        self.ship_x = 0
        self.ship_y = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.ship_frame = 0
        self.ship_accelate = 2 # 가속도 2p/s
        self.ship_max_accelate = 200 #최대 가속도 200p/s
        self.direction_horizon = 0
        self.direction_virtical = 0
        self.state_horizon = self.NONE_STATE
        self.state_virtical = self.NONE_STATE
        self.state_accelate = self.NONE
        if SHIP.image == None:
            SHIP.image = load_image("resource/ship.png")

    def update(self, frame_time):
        distance = (self.SHIP_SPEED_PPS + self.ship_accelate) * frame_time

        if self.state_horizon == self.RIGHT_RUN:
            self.direction_horizon = 1
        if self.state_horizon == self.LEFT_RUN:
            self.direction_horizon = -1
        if self.state_virtical == self.UP_RUN:
            self.direction_virtical = 1
        if self.state_virtical == self.DOWN_RUN:
            self.direction_virtical = -1

        if self.state_horizon != self.NONE_STATE:
            self.ship_x += (self.direction_horizon * distance)
        if self.state_virtical != self.NONE_STATE:
            self.ship_y += (self.direction_virtical * distance)

        self.ship_x = clamp(0, self.ship_x, self.bg.w)
        self.ship_y = clamp(0, self.ship_y, self.bg.h)

        if self.ship_accelate <= self.ship_max_accelate:
            self.ship_accelate = max(0, self.ship_accelate + self.state_accelate)
        else:
            self.ship_accelate = self.ship_max_accelate - 1

        if self.ship_accelate == 0:
            if self.state_virtical != self.NONE_STATE:
                self.state_virtical = self.NONE_STATE
            elif self.state_horizon != self.NONE_STATE:
                self.state_horizon = self.NONE_STATE
            self.state_accelate = self.NONE

    def draw(self):
        if self.state_virtical != self.NONE_STATE:
            self.image.clip_draw(0, (self.state_virtical - 1) * 64, 64, 64, self.ship_x - self.bg.window_left, self.ship_y - self.bg.window_bottom)
        elif self.state_horizon != self.NONE_STATE:
            self.image.clip_draw(0, (self.state_horizon - 1) * 64, 64, 64, self.ship_x - self.bg.window_left, self.ship_y - self.bg.window_bottom)
        else:
            self.image.clip_draw(0, 0, 64, 64, self.ship_x - self.bg.window_left, self.ship_y - self.bg.window_bottom)


    def set_background(self, bg):
        self.bg = bg
        self.ship_x = self.bg.w / 2
        self.ship_y = self.bg.h / 2

    def get_bb(self):
        return self.ship_x - 32 - self.bg.window_left, self.ship_y - 32 - self.bg.window_bottom,\
               self.ship_x + 32 - self.bg.window_left, self.ship_y + 32 - self.bg.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, fisher, event):
        if event.type == SDL_KEYDOWN:
            if fisher.state == fisher.STANDING:
                if event.key == SDLK_d:
                    self.state_horizon = self.RIGHT_RUN
                    self.state_virtical = self.NONE_STATE
                    if self.state_accelate != self.BREAK:
                        self.state_accelate = self.ACCELATE
                elif event.key == SDLK_a:
                    self.state_horizon = self.LEFT_RUN
                    self.state_virtical = self.NONE_STATE
                    if self.state_accelate != self.BREAK:
                        self.state_accelate = self.ACCELATE
                elif event.key == SDLK_w:
                    self.state_virtical = self.UP_RUN
                    self.state_horizon = self.NONE_STATE
                    if self.state_accelate != self.BREAK:
                        self.state_accelate = self.ACCELATE
                elif event.key == SDLK_s:
                    self.state_virtical = self.DOWN_RUN
                    self.state_horizon = self.NONE_STATE
                    if self.state_accelate != self.BREAK:
                        self.state_accelate = self.ACCELATE
                elif event.key == SDLK_SPACE:
                    self.state_accelate = self.BREAK
        if event.type == SDL_KEYUP:
            if fisher.state == fisher.STANDING:
                if event.key == SDLK_d:
                    self.state_horizon = self.RIGHT_RUN
                    self.state_virtical = self.NONE_STATE
                    if self.state_accelate != self.BREAK:
                        self.state_accelate = self.ACCELATE
                elif event.key == SDLK_a:
                    self.state_horizon = self.LEFT_RUN
                    self.state_virtical = self.NONE_STATE
                    if self.state_accelate != self.BREAK:
                        self.state_accelate = self.ACCELATE
                elif event.key == SDLK_w:
                    self.state_virtical = self.UP_RUN
                    self.state_horizon = self.NONE_STATE
                    if self.state_accelate != self.BREAK:
                        self.state_accelate = self.ACCELATE
                elif event.key == SDLK_s:
                    self.state_virtical = self.DOWN_RUN
                    self.state_horizon = self.NONE_STATE
                    if self.state_accelate != self.BREAK:
                        self.state_accelate = self.ACCELATE
                elif event.key == SDLK_SPACE:
                    self.state_accelate = self.BREAK

