from pico2d import *
import random

running = None

class FISH:
    image = None

    def __init__(self):
        self.fish_id = random.randint(0,2)
        self.fish_level = 0
        self.fish_size = random.randint(5,30)
        self.fish_heal = self.fish_size * 10
        if(FISH.image == None):
            image = load_image("resource/fishes.png")
        pass

class FISHER:
    def __init__(self):
        self.fisher_x = 400
        self.fisher_y = 200
        self.fisher_frame = 0
        self.fisher_hunger = 1000
        self.fisher_hungry = 10
        self.fisher_luck = random.randint(10, 50)
        self.fisher_str = random.randint(10, 20)
        self.image = load_image("resource/fisher.png")
        pass

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.fisher_frame, 0, 45, 45, self.fisher_x, self.fisher_y)
        pass

class OBJECT:
    image = None

    def __init__(self):
        self.object_x = random.randint(0,800)
        self.object_y = random.randint(0,300)
        if OBJECT.image == None:
            OBJECT.image = load_image('resource/Stone.png')
        pass

    def draw(self):
        self.image.draw(self.object_x, self.object_y)
        pass

class BACKGROUND:
    def __init__(self):
        self.image = load_image('resource/Background.png')
        pass

    def draw(self):
        self.image.draw(400, 300, 800,600)
        pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def main():

    open_canvas()

    global running
    running = True

    bg = BACKGROUND()
    fisher = FISHER()
    Objects = [OBJECT() for i in range(10)]

    while running:
        handle_events()

        bg.draw()
        fisher.draw()
        for obj in Objects:
            obj.draw()

        update_canvas()
        delay(0.05)


    close_canvas()
    pass

if __name__ == '__main__':
    main()