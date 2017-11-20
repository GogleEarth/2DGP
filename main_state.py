import random
import json
import os
import Class

from pico2d import *

import game_framework
import title_state
import Class_fishing

running = None
ship = None
fisher = None
float = None
fish = None
current_time = None
bg = None
Objects = None
ui = None

name = "MainState"

def enter():
    global ship
    global running
    global current_time
    global fisher
    global float
    global fish
    global bg
    global Objects
    global ui

    running = True
    current_time = get_time()

    ui = Class.UI()
    bg = Class.BACKGROUND()
    Objects = [Class.OBJECT() for i in range(10)]
    ship = Class.SHIP()
    fisher = Class.FISHER()
    float = Class.FLOAT()
    fish = Class.FISH()

    pass

def exit():
    pass

def pause():
    pass


def resume():
    pass


def handle_events():
    global ship
    global fisher
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            ship.handle_event(fisher, event)
            fisher.handle_event(ship, float, event)
            Class_fishing.handle_events(event)



def update():
    global ship
    global running
    global current_time
    global fisher
    global float
    global fish
    global bg
    global Objects
    global ui

    frame_time = Class.get_frame_time()
    handle_events()

    ship.update(frame_time)
    fisher.update(ship, frame_time)
    float.update(fisher, frame_time)
    ui.upadte(fisher)
    if float.state == float.READY:
        fish.update(fisher, float)
    if fisher.fisher_hunger <= 0:
        game_framework.change_state(title_state)
    if fisher.state == fisher.FIGHTING:
        Class_fishing.update(frame_time,fisher,fish,float)
        pass

def draw():
    global ship
    global running
    global current_time
    global fisher
    global float
    global fish
    global bg
    global Objects
    global ui

    clear_canvas()

    bg.draw()
    ship.draw()
    fisher.draw()
    if float.state != float.NONE:
        float.draw()
    for obj in Objects:
        obj.draw()
    ui.draw()
    if fisher.state == fisher.FIGHTING:
        Class_fishing.draw()
    print(fish.fish_state)
    if(fish.fish_state == fish.DRAW):
        fish.draw(fisher)

    delay(0.03)
    update_canvas()