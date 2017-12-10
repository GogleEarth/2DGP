from pico2d import *
import random

class SHIP:
    PIXEL_PER_METER = (10.0 / 30) #10픽셀당 30cm
    SHIP_SPEED_KMPH = 20.0 # 시속 20km/h
    SHIP_SPEED_MPM = (SHIP_SPEED_KMPH * 1000.0 / 60.0) # 분속 333.333...m/m
    SHIP_SPEED_MPS = (SHIP_SPEED_MPM / 60.0) # 초속 5.555...m/s
    SHIP_SPEED_PPS = (SHIP_SPEED_MPS * PIXEL_PER_METER) # 초속 1.851851...p/s

    LEFT_RUN, RIGHT_RUN, UP_RUN, DOWN_RUN, NONE_STATE = 1, 2, 3, 4, 0
    ACCELATE, BREAK = 1, -1

    image = None

    def __init__(self):
        self.ship_x = 400
        self.ship_y = 200
        self.ship_frame = 0
        self.ship_acc = 1 # 가속도 1p/s
        self.ship_max_acc = 100 #최대 가속도 100p/s
        self.direction_horizon = 0
        self.direction_virtical = 0
        self.state_horizon = self.NONE_STATE
        self.state_virtical = self.NONE_STATE
        self.state_accelate = self.BREAK
        if SHIP.image == None:
            SHIP.image = load_image("resource/ship.png")

    def update(self, frame_time):
        distance = (self.SHIP_SPEED_PPS + self.ship_acc) * frame_time

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

        if self.ship_acc <= self.ship_max_acc:
            self.ship_acc = max(0, self.ship_acc + self.state_accelate)
        else:
            self.ship_acc = self.ship_max_acc - 1

        if self.ship_acc == 0:
            if self.state_virtical != self.NONE_STATE:
                self.state_virtical = self.NONE_STATE
            elif self.state_horizon != self.NONE_STATE:
                self.state_horizon = self.NONE_STATE

        print(self.ship_acc)

    def draw(self):
        if self.state_virtical != self.NONE_STATE:
            self.image.clip_draw(0, (self.state_virtical - 1) * 64, 64, 64, self.ship_x, self.ship_y)
        elif self.state_horizon != self.NONE_STATE:
            self.image.clip_draw(0, (self.state_horizon - 1) * 64, 64, 64, self.ship_x, self.ship_y)
        else:
            self.image.clip_draw(0, 0, 64, 64, self.ship_x, self.ship_y)

    def handle_event(self, fisher, event):
        if event.type == SDL_KEYDOWN:
            if fisher.state == fisher.STANDING:
                if event.key == SDLK_d:
                    self.state_horizon = self.RIGHT_RUN
                    self.state_virtical = self.NONE_STATE
                    self.state_accelate = self.ACCELATE
                elif event.key == SDLK_a:
                    self.state_horizon = self.LEFT_RUN
                    self.state_virtical = self.NONE_STATE
                    self.state_accelate = self.ACCELATE
                elif event.key == SDLK_w:
                    self.state_virtical = self.UP_RUN
                    self.state_horizon = self.NONE_STATE
                    self.state_accelate = self.ACCELATE
                elif event.key == SDLK_s:
                    self.state_virtical = self.DOWN_RUN
                    self.state_horizon = self.NONE_STATE
                    self.state_accelate = self.ACCELATE
                elif event.key == SDLK_SPACE:
                    self.state_accelate = self.BREAK
        if event.type == SDL_KEYUP:
            if fisher.state == fisher.STANDING:
                if event.key == SDLK_d:
                    self.state_horizon = self.RIGHT_RUN
                    self.state_virtical = self.NONE_STATE
                    self.state_accelate = self.ACCELATE
                elif event.key == SDLK_a:
                    self.state_horizon = self.LEFT_RUN
                    self.state_virtical = self.NONE_STATE
                    self.state_accelate = self.ACCELATE
                elif event.key == SDLK_w:
                    self.state_virtical = self.UP_RUN
                    self.state_horizon = self.NONE_STATE
                    self.state_accelate = self.ACCELATE
                elif event.key == SDLK_s:
                    self.state_virtical = self.DOWN_RUN
                    self.state_horizon = self.NONE_STATE
                    self.state_accelate = self.ACCELATE
                elif event.key == SDLK_SPACE:
                    self.state_accelate = self.BREAK

        print(self.ship_x, " " , self.ship_y)
