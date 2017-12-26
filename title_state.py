import game_framework
import main_state
import manual_state

from pico2d import *


name = "TitleState"
image = None
bgm = None

def enter():
    global  image, bgm
    image = load_image('resource/title.png')
    bgm = load_music('resource/title_bgm.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()

def exit():
    global image, bgm
    del(image)
    del(bgm)


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F1:
            game_framework.change_state(manual_state)
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)


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






