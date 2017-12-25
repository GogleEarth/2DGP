import game_framework
import main_state
import Fish_Class
from pico2d import *



name = "PauseState"
image = None
fishimage = None
font = None

def enter():
    global image, fishimage, font
    image = load_image('resource/pause.png')
    fishimage = load_image('resource/fishes.png')
    font = load_font('resource/ENCR10B.TTF')

def exit():
    global image, fishimage, font
    del(image)
    del(fishimage)
    del(font)

def update(frame_time):
    main_state.ui.upadte(main_state.fisher,frame_time)
    pass

def draw(frame_time):
    global image,fishimage,font
    clear_canvas()
    image.draw(400, 300, 800, 600)
    for i in range(0,5):
        fishimage.clip_draw(i * 64, 0, 64, 64, 600, i * 64 + 128)
        font.draw(650, i * 64 + 128, 'X: %d' % main_state.fisher.number_of_fishes[i][i], (0, 0, 0))

    font.draw(100, 400, 'STR: %d' % main_state.fisher.fisher_str, (0, 0, 0))
    font.draw(100, 350, 'LUCK: %d' % main_state.fisher.fisher_luck, (0, 0, 0))
    font.draw(100, 300, 'HUNGER: %d' % main_state.fisher.fisher_hunger, (0, 0, 0))
    font.draw(100, 250, 'HUNGER SENSATION: %d' % main_state.fisher.fisher_hungry, (0, 0, 0))

    update_canvas()

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_state()
    pass


def pause(): pass


def resume(): pass




