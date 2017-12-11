from pico2d import *
import random
import FishingUI_Class

class FISHER:
    PIXEL_PER_METER = (10.0 / 30) #10픽셀당 30cm
    RIGHT_DOWN,  RIGHT_UP, LEFT_UP, LEFT_DOWN = 0, 1, 2, 3
    STANDING, READY, FISHING, FIGHTING, FINISH = 0, 1, 2, 3, 4

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    image = None

    def __init__(self):
        self.fisher_x = 0
        self.fisher_y = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.fisher_frame = 0
        self.total_frames = 0.0
        self.fisher_hunger = 1000
        self.fisher_hungry = 10
        self.fisher_luck = random.randint(0, 20)
        self.fisher_str = random.randint(10, 20)
        self.state = self.STANDING
        self.dirrection = self.RIGHT_DOWN
        if(FISHER.image == None):
            FISHER.image = load_image("resource/fisher.png")
        pass

    def update(self, ship, frame_time):
        self.fisher_x = ship.ship_x
        self.fisher_y = ship.ship_y + 30
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
        self.image.clip_draw(self.fisher_frame * 64, self.dirrection * 64, 64, 64, self.fisher_x - self.bg.window_left, self.fisher_y - self.bg.window_bottom)
        pass

    def set_background(self, bg):
        self.bg = bg
        self.fisher_x = self.bg.w / 2
        self.fisher_y = self.bg.h / 2

    def handle_event(self,fisher, fish, ship, float, bg, event):
        if event.type == SDL_MOUSEMOTION:
            print("Mouse position : ", event.x, "  ", 600 - event.y)
            if self.state == self.STANDING:
                if event.x >= self.fisher_x:
                    if event.y > self.fisher_y:
                        self.dirrection = self.LEFT_DOWN
                        float.float_des_x = event.x
                        float.float_des_y = 600 - event.y
                    else:
                        self.dirrection = self.LEFT_UP
                        float.float_des_x = event.x
                        float.float_des_y = 600 - event.y
                else:
                    if event.y > self.fisher_y:
                        self.dirrection = self.RIGHT_DOWN
                        float.float_des_x = event.x
                        float.float_des_y = 600 - event.y
                    else:
                        self.dirrection = self.RIGHT_UP
                        float.float_des_x = event.x
                        float.float_des_y = 600 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN:
            if ship.state_horizon == ship.NONE_STATE and ship.state_virtical == ship.NONE_STATE:
                if self.state == self.STANDING:
                    self.state = self.READY
                    float.state = float.READY
                    FishingUI_Class.init(fisher, fish,bg)
                if self.state == self.FISHING:
                    self.state = self.FINISH
                    float.float_y = self.fisher_y
                    float.float_x = self.fisher_x
                    float.state = float.NONE
                    FishingUI_Class.init(fisher, fish,bg)

                pass
