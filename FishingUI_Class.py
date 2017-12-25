from pico2d import *

white = None
yellow = None
red = None
key_down = False
time_limit = 0
fishing_state = True
font = None
fishing = None
trash = None

class White_Zone:

    def __init__(self):
        self.image = load_image("resource/white_zone.png")

    def draw(self,fisher,fish):
        self.image.clip_draw(0,0,32,32,fisher.fisher_x-40-self.bg.window_left,fisher.fisher_y-self.bg.window_bottom,32,194)

    def set_background(self, bg):
        self.bg = bg
class Yellow_Zone:

    def __init__(self):
        self.image = load_image("resource/Hungry.png")

    def draw(self,fisher,fish):
        self.image.clip_draw(0,0,32,32,fisher.fisher_x-40-self.bg.window_left,fisher.fisher_y-self.bg.window_bottom,32,(4 - fish.fish_level) * 32)

    def set_background(self, bg):
        self.bg = bg

class Red_Line:

    def __init__(self,fisher):
        self.image = load_image("resource/red_line.png")
        self.x = fisher.fisher_x
        self.y = fisher.fisher_y

    def draw(self):
        self.image.clip_draw(0,0,32,32,self.x-40-self.bg.window_left,self.y-self.bg.window_bottom)

    def update(self,fisher,fish):
        global key_down
        self.y = max(fisher.fisher_y - 95, self.y - (fish.fish_level + fish.fish_level)*1.5)
        if key_down == True:
            self.y = min(self.y + 5 + fisher.fisher_str, fisher.fisher_y + 95)

    def set_background(self, bg):
        self.bg = bg

def init(fisher,fish,bg):
    global white
    global yellow
    global red
    global fishing_state
    global time_limit
    global font
    global fishing
    global trash

    fishing = None
    trash = None
    time_limit = 0
    fishing_state = True
    if font == None:
        font = load_font('resource/ENCR10B.TTF')

    if yellow == None:
        yellow = Yellow_Zone()
        yellow.set_background(bg)
    else:
        del(yellow)
        yellow = Yellow_Zone()
        yellow.set_background(bg)
    if white == None:
        white = White_Zone()
        white.set_background(bg)
    else:
        del(white)
        white = White_Zone()
        white.set_background(bg)
    if red == None:
        red = Red_Line(fisher)
        red.set_background(bg)
    else:
        del(red)
        red = Red_Line(fisher)
        red.set_background(bg)


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
    global font
    global fishing
    global trash

    red.update(fisher,fish)

    if key_down == True:
        key_down = False

    if fishing_state:
        time_limit += 1 / (frame_time * 60)
        print("Time_limit : ", 60 - time_limit)
    if time_limit >= 45:
        if red.y >= fisher.fisher_y - 16 * (4-fish.fish_level) and red.y <= fisher.fisher_y + 16 * (4-fish.fish_level):
            fishing_state = False
            if fish.fish_id != 3:
                trash = False
                fisher.fisher_str += fish.fish_level
                fisher.fisher_hunger = min(fisher.fisher_hunger + fish.fish_heal, 1000)
                if(fisher.fisher_hungry > 5):
                    fisher.fisher_hungry -= 5
                fisher.eat_fish()
            else:
                trash = True
            fisher.number_of_fishes[fish.fish_id][fish.fish_id] += 1
            fisher.state = fisher.FINISH
            float.state = float.FINISH
            fish.fish_state = fish.DRAW
            fishing = True
            fisher.fishing += 1
        else:
            fisher.fisher_hunger -= fish.fish_level * 50
            fishing_state = False
            fisher.state = fisher.FINISH
            float.state = float.NONE
            fish.reset()
            fishing = False

    pass

def draw(fisher, fish):
    global white
    global yellow
    global red
    global font
    global time_limit

    font.draw(fisher.bg.canvas_width / 2 - 125, 25, 'time_limit : %3.2f' % (45-time_limit), (255, 255, 0))
    white.draw(fisher, fish)
    yellow.draw(fisher, fish)
    red.draw()

def draw_sys(fisher, fish):
    global time_limit
    global fishing
    global trash
    global font

    if time_limit >= 45:
        if fishing:
            font.draw(fisher.bg.canvas_width / 2 - 125, 35, '<sys>fishing succesee',(255, 255, 0))
            if not trash:
                font.draw(fisher.bg.canvas_width / 2 - 125, 15, '<sys>healing : %d' % fish.fish_heal , (255, 255, 0))
        else:
            font.draw(fisher.bg.canvas_width / 2-125, 25, '<sys>fishing fail',(255, 255, 0))
