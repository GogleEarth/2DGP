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
    eat_sound = None

    def __init__(self,bg):
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.fisher_frame = 0
        self.total_frames = 0.0
        self.fisher_hunger = 1000
        self.fisher_hungry = 10
        self.fisher_luck = random.randint(-10, 10)
        self.fisher_str = random.randint(10, 20)
        self.state = self.STANDING
        self.dirrection = self.RIGHT_DOWN
        self.bg = bg
        self.fisher_x = self.bg.w / 2
        self.fisher_y = self.bg.h / 2
        self.number_of_fishes = [{0:0},{1:0},{2:0},{3:0},{4:0}]
        self.fishing = 0
        if(FISHER.image == None):
            FISHER.image = load_image("resource/fisher.png")

        if FISHER.eat_sound == None:
            FISHER.eat_sound = load_wav('resource/eat_sound.wav')
            FISHER.eat_sound.set_volume(32)
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

    def eat_fish(self):
        self.eat_sound.play()

    def handle_event(self,fisher, fish, ship, float, bg, event):
        if event.type == SDL_MOUSEMOTION:
            if self.state == self.STANDING and float.state == float.NONE:
                if fisher.fisher_x + event.x - 400 >= self.fisher_x:
                    if fisher.fisher_y + 600 - event.y - 300 > self.fisher_y:
                        self.dirrection = self.LEFT_DOWN
                        float.float_x = fisher.fisher_x
                        float.float_y = fisher.fisher_y
                        float.float_des_x = fisher.fisher_x + event.x - 400
                        float.float_des_y = fisher.fisher_y + 600 - event.y - 330
                    else:
                        self.dirrection = self.LEFT_UP
                        float.float_x = fisher.fisher_x
                        float.float_y = fisher.fisher_y
                        float.float_des_x = fisher.fisher_x + event.x - 400
                        float.float_des_y = fisher.fisher_y + 600 - event.y - 330
                else:
                    if fisher.fisher_y + 600 - event.y - 300 > self.fisher_y:
                        self.dirrection = self.RIGHT_DOWN
                        float.float_x = fisher.fisher_x
                        float.float_y = fisher.fisher_y
                        float.float_des_x = fisher.fisher_x + event.x - 400
                        float.float_des_y = fisher.fisher_y + 600 - event.y - 330
                    else:
                        self.dirrection = self.RIGHT_UP
                        float.float_x = fisher.fisher_x
                        float.float_y = fisher.fisher_y
                        float.float_des_x = fisher.fisher_x + event.x - 400
                        float.float_des_y = fisher.fisher_y + 600 - event.y - 330

        elif event.type == SDL_MOUSEBUTTONDOWN:
            if ship.state_horizon == ship.NONE_STATE and ship.state_virtical == ship.NONE_STATE:
                if self.state == self.STANDING:
                    self.state = self.READY
                    float.state = float.READY
                    FishingUI_Class.init(fisher, fish,bg)
                if self.state == self.FISHING:
                    self.state = self.FINISH
                    float.state = float.FINISH
                    FishingUI_Class.init(fisher, fish,bg)

                pass
