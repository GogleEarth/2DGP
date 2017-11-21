from pico2d import *
import random
import Class_fishing

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



class FISH:
    image = None
    UN_DROW, DRAW = 0, 1
    def __init__(self):
        self.fish_id = random.randint(0,3)
        self.fish_level = random.randint(1,3)
        self.fish_size = random.randint(30,100)
        self.fish_heal = self.fish_size * 5
        self.fish_state = self.UN_DROW
        self.fish_y = 20
        if(FISH.image == None):
            FISH.image = load_image("resource/fishes.png")

    def update(self, fisher, float):
        i = random.randint(0,1000)
        print("random : ", i, "fish_level : ",(4 - self.fish_level) * 5 + fisher.fisher_luck)
        if i <= (4 - self.fish_level) * 5 + fisher.fisher_luck:
            float.state = float.FISING
            print("fishing start")
            fisher.state = fisher.FIGHTING
            self.reset()
            self.fish_state = self.UN_DROW
        if self.fish_state == self.DRAW:
            self.fish_y += 1
            if self.fish_y >= 30:
                self.fish_state = self.UN_DROW
        pass

    def draw(self, fisher):
        self.image.clip_draw(self.fish_id * 64,0,64,64,fisher.fisher_x,fisher.fisher_y + self.fish_y)
        pass

    def reset(self):
        self.fish_id = random.randint(0,3)
        self.fish_level = random.randint(1, 3)
        self.fish_size = random.randint(30, 100)
        self.fish_heal = self.fish_size * 5
        self.fish_state = self.UN_DROW
        self.fish_y = 20

class FISHER:
    PIXEL_PER_METER = (10.0 / 30) #10픽셀당 30cm
    RIGHT_DOWN,  RIGHT_UP, LEFT_UP, LEFT_DOWN = 0, 1, 2, 3
    STANDING, READY, FISHING, FIGHTING, FINISH = 0, 1, 2, 3, 4

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    image = None

    def __init__(self):
        self.fisher_x = 400
        self.fisher_y = 220
        self.fisher_frame = 0
        self.total_frames = 0.0
        self.fisher_hunger = 1000
        self.fisher_hungry = 10
        self.fisher_luck = random.randint(0, 20)
        self.fisher_str = random.randint(10, 20)
        self.state = self.STANDING
        self.dir = self.RIGHT_DOWN
        if(FISHER.image == None):
            FISHER.image = load_image("resource/fisher.png")
        pass

    def update(self, SHIP, frame_time):
        self.fisher_x = SHIP.ship_x
        self.fisher_y = SHIP.ship_y + 30
        if self.state == self.READY:
            self.total_frames += FISHER.FRAMES_PER_ACTION * FISHER.ACTION_PER_TIME * frame_time
            self.fisher_frame = int(self.total_frames) % 5
            if self.fisher_frame == 4:
                self.state = self.FISHING
        if self.state == self.FINISH:
            self.total_frames -= FISHER.FRAMES_PER_ACTION * FISHER.ACTION_PER_TIME * frame_time
            self.fisher_frame = int(self.total_frames) % 5
            if self.fisher_frame == 0:
                self.state = self.STANDING
        if self.state == self.FIGHTING:
            self.total_frames += FISHER.FRAMES_PER_ACTION * FISHER.ACTION_PER_TIME * frame_time
            self.fisher_frame = random.randint(1, int(self.total_frames) % 4+1)


    def draw(self):
        self.image.clip_draw(self.fisher_frame * 64, self.dir * 64 , 64, 64, self.fisher_x, self.fisher_y)
        pass

    def handle_event(self, SHIP, float, event):
        if event.type == SDL_MOUSEMOTION:
            print("Mouse position : ", event.x, "  ", 600 - event.y)
            if self.state == self.STANDING:
                if event.x >= self.fisher_x:
                    if event.y > self.fisher_y:
                        self.dir = self.LEFT_DOWN
                        float.float_des_x = event.x
                        float.float_des_y = 600 - event.y
                    else:
                        self.dir = self.LEFT_UP
                        float.float_des_x = event.x
                        float.float_des_y = 600 - event.y
                else:
                    if event.y > self.fisher_y:
                        self.dir = self.RIGHT_DOWN
                        float.float_des_x = event.x
                        float.float_des_y = 600 - event.y
                    else:
                        self.dir = self.RIGHT_UP
                        float.float_des_x = event.x
                        float.float_des_y = 600 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN:
            if SHIP.state_hor == SHIP.NONE_STATE and SHIP.state_vir == SHIP.NONE_STATE:
                if self.state == self.STANDING:
                    self.state = self.READY
                    float.state = float.READY
                    Class_fishing.init()
                if self.state == self.FISHING:
                    self.state = self.FINISH
                    float.float_y = self.fisher_y
                    float.float_x = self.fisher_x
                    float.state = float.NONE
                    Class_fishing.init()

                pass

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

class SHIP:
    PIXEL_PER_METER = (10.0 / 30) #10픽셀당 30cm
    SHIP_SPEED_KMPH = 20.0 # 시속 20km/h
    SHIP_SPEED_MPM = (SHIP_SPEED_KMPH * 1000.0 / 60.0) # 분속 333.333...m/m
    SHIP_SPEED_MPS = (SHIP_SPEED_MPM / 60.0) # 초속 5.555...m/s
    SHIP_SPEED_PPS = (SHIP_SPEED_MPS * PIXEL_PER_METER) # 초속 1.851851...p/s

    LEFT_RUN, RIGHT_RUN, UP_RUN, DOWN_RUN, NONE_STATE = 1, 2, 3, 4, 0
    ACC, BRK = 1,-1

    image = None

    def __init__(self):
        self.ship_x = 400
        self.ship_y = 200
        self.ship_frame = 0
        self.ship_acc = 1 # 가속도 1p/s
        self.ship_max_acc = 100 #최대 가속도 100p/s
        self.dir_hor = 0
        self.dir_vir = 0
        self.state_hor = self.NONE_STATE
        self.state_vir = self.NONE_STATE
        self.state_acc = self.BRK
        if SHIP.image == None:
            SHIP.image = load_image("resource/ship.png")

    def update(self, frame_time):
        distance = (self.SHIP_SPEED_PPS + self.ship_acc) * frame_time

        if self.state_hor == self.RIGHT_RUN:
            self.dir_hor = 1
        if self.state_hor == self.LEFT_RUN:
            self.dir_hor = -1
        if self.state_vir == self.UP_RUN:
            self.dir_vir = 1
        if self.state_vir == self.DOWN_RUN:
            self.dir_vir = -1

        if self.state_hor != self.NONE_STATE:
            self.ship_x += (self.dir_hor * distance)
        if self.state_vir != self.NONE_STATE:
            self.ship_y += (self.dir_vir * distance)

        if self.ship_acc <= self.ship_max_acc:
            self.ship_acc = max(0,self.ship_acc + self.state_acc)
        else:
            self.ship_acc = self.ship_max_acc - 1

        if self.ship_acc == 0:
            if self.state_vir != self.NONE_STATE:
                self.state_vir = self.NONE_STATE
            elif self.state_hor != self.NONE_STATE:
                self.state_hor = self.NONE_STATE

        print(self.ship_acc)

    def draw(self):
        if self.state_vir != self.NONE_STATE:
            self.image.clip_draw(0, (self.state_vir - 1) * 64, 64, 64, self.ship_x, self.ship_y)
        elif self.state_hor != self.NONE_STATE:
            self.image.clip_draw(0, (self.state_hor - 1) * 64, 64, 64, self.ship_x, self.ship_y)
        else:
            self.image.clip_draw(0, 0, 64, 64, self.ship_x, self.ship_y)

    def handle_event(self, fisher, event):
        if event.type == SDL_KEYDOWN:
            if fisher.state == fisher.STANDING:
                if event.key == SDLK_RIGHT:
                    self.state_hor = self.RIGHT_RUN
                    self.state_vir = self.NONE_STATE
                    self.state_acc = self.ACC
                elif event.key == SDLK_LEFT:
                    self.state_hor = self.LEFT_RUN
                    self.state_vir = self.NONE_STATE
                    self.state_acc = self.ACC
                elif event.key == SDLK_UP:
                    self.state_vir = self.UP_RUN
                    self.state_hor = self.NONE_STATE
                    self.state_acc = self.ACC
                elif event.key == SDLK_DOWN:
                    self.state_vir = self.DOWN_RUN
                    self.state_hor = self.NONE_STATE
                    self.state_acc = self.ACC
                elif event.key == SDLK_SPACE:
                    self.state_acc = self.BRK
        if event.type == SDL_KEYUP:
            if fisher.state == fisher.STANDING:
                if event.key == SDLK_RIGHT:
                    self.state_hor = self.RIGHT_RUN
                    self.state_vir = self.NONE_STATE
                    self.state_acc = self.ACC
                elif event.key == SDLK_LEFT:
                    self.state_hor = self.LEFT_RUN
                    self.state_vir = self.NONE_STATE
                    self.state_acc = self.ACC
                elif event.key == SDLK_UP:
                    self.state_vir = self.UP_RUN
                    self.state_hor = self.NONE_STATE
                    self.state_acc = self.ACC
                elif event.key == SDLK_DOWN:
                    self.state_vir = self.DOWN_RUN
                    self.state_hor = self.NONE_STATE
                    self.state_acc = self.ACC
                elif event.key == SDLK_SPACE:
                    self.state_acc = self.BRK

        print(self.ship_x, " " , self.ship_y)

class BACKGROUND:
    def __init__(self):
        self.image = load_image('resource/Background.png')
        pass

    def draw(self):
        self.image.draw(400, 700, 800,1600)
        pass

def handle_events():
    global running
    global ship
    global fisher
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            ship.handle_event(fisher, event)
            fisher.handle_event(ship, float, event)
    pass

current_time = 0.0


def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time


if __name__ == '__main__':
    main()