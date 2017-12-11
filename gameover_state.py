import game_framework
import title_state
from pico2d import *


name = "Gameover_State"
image = None
bgm = None

def enter():
    global  image, bgm
    image = load_image('resource/gameover.png')
    bgm = load_music('resource/gameover_bgm.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()

def exit():
    global image, bgm
    del(bgm)
    del(image)


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(title_state)


def draw(frame_time):
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass



