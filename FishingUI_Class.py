from pico2d import *

white = None
yellow = None
red = None
key_down = False
time_limit = 0
fishing_state = True

class White_Zone:

    def __init__(self):
        self.image = load_image("resource/white_zone.png")

    def draw(self,fisher,fish):
        self.image.clip_draw(0,0,32,32,fisher.fisher_x-80,fisher.fisher_y,32,194)

class Yellow_Zone:

    def __init__(self):
        self.image = load_image("resource/Hungry.png")

    def draw(self,fisher,fish):
        self.image.clip_draw(0,0,32,32,fisher.fisher_x-80,fisher.fisher_y,32,(4 - fish.fish_level) * 32)


class Red_Line:

    def __init__(self,fisher):
        self.image = load_image("resource/red_line.png")
        self.x = fisher.fisher_x - 80
        self.y = fisher.fisher_y - 80

    def draw(self):
        self.image.clip_draw(0,0,32,32,self.x,self.y,)

    def update(self,fisher,fish):
        global key_down
        self.y = max(fisher.fisher_y - 95, self.y - (fish.fish_level + fish.fish_level)*1.5)
        if key_down == True:
            self.y = min(self.y + 5 + fisher.fisher_str, fisher.fisher_y + 95)
def init(fisher,fish):
    global white
    global yellow
    global red
    global fishing_state
    global time_limit

    time_limit = 0
    fishing_state = True
    if yellow == None:
        yellow = Yellow_Zone()
    else:
        del(yellow)
        yellow = Yellow_Zone()
    if white == None:
        white = White_Zone()
    else:
        del(white)
        white = White_Zone()
    if red == None:
        red = Red_Line(fisher)
    else:
        del(red)
        red = Red_Line(fisher)

    pass

def handle_events(event):
    global red
    global key_down

    if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
        if key_down == False:
           key_down = True
        else:
            key_down = False
    elif event.type == SDL_KEYUP and event.key == SDLK_SPACE:
        if key_down == True:
           key_down = False


def update(frame_time,fisher,fish,float):
    global red
    global key_down
    global time_limit
    global yellow
    global fishing_state

    red.update(fisher,fish)

    if key_down == True:
        key_down = False

    if fishing_state:
        time_limit += 1 / (frame_time * 60)
        print("Time_limit : ", 60 - time_limit)
        print("red y : ", red.y, " yellow y- :", fisher.fisher_y - 16 * (4-fish.fish_level), " yellow y+ : ", fisher.fisher_y + 16 * (4-fish.fish_level))
    if time_limit >= 45:
        if red.y >= fisher.fisher_y - 16 * (4-fish.fish_level) and red.y <= fisher.fisher_y + 16 * (4-fish.fish_level):
            print("fishing success")
            fishing_state = False
            if fish.fish_id != 3:
                fisher.fisher_str += fish.fish_level
                fisher.fisher_hunger = min(fisher.fisher_hunger + fish.fish_heal, 1000)
                fisher.fisher_hungry -= 5
                print("HEAL : ",fish.fish_heal)
            fisher.state = fisher.FINISH
            float.state = float.NONE
            fish.fish_state = fish.DRAW
        else:
            fisher.fisher_hunger -= fish.fish_level * 50
            fishing_state = False
            fisher.state = fisher.FINISH
            float.state = float.NONE
            fish.reset()


    pass

def draw(fisher, fish):
    global white
    global yellow
    global red

    white.draw(fisher, fish)
    yellow.draw(fisher, fish)
    red.draw()