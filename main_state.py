import random
import json
import os
import Fisher_Class
import Float_Class
import Ship_Class
import Object_Class
import Fish_Class
import Class
import time
from pico2d import *

import game_framework
import gameover_state
import pause_state
import FishingUI_Class

ship = None
fisher = None
float = None
fish = None
bg = None
Objects = None
ui = None
game_time = None
running_time = None

name = "MainState"

def enter():
    global ship
    global fisher
    global float
    global fish
    global bg
    global Objects
    global ui
    global game_time

    ui = Class.UI()
    bg = Class.FixedTileBackground()
    Objects = [Object_Class.OBJECT(i) for i in range(bg.max_stone_id)]
    ship = Ship_Class.SHIP()
    fisher = Fisher_Class.FISHER(bg)
    float = Float_Class.FLOAT()
    fish = Fish_Class.FISH()
    bg.set_center_object(ship)
    ship.set_background(bg)
    fish.set_background(bg)

    for Object in Objects:
        Object.set_background(bg)

    game_time = time.clock()
    pass

def exit():
    pass

def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    global ship
    global fisher
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)
        else:
            ship.handle_event(fisher, event)
            fisher.handle_event(fisher, fish, ship, float, bg, event)
            FishingUI_Class.handle_events(event)



def update(frame_time):
    global ship
    global fisher
    global float
    global fish
    global Objects
    global ui
    global game_time
    global running_time

    handle_events(frame_time)

    bg.update(frame_time)
    ship.update(frame_time)
    fisher.update(ship, frame_time)
    float.update(fisher, frame_time)
    ui.upadte(fisher)
    fish.update(fisher, float)

    running_time = time.clock() - game_time

    if fisher.fisher_hunger <= 0:
        game_framework.change_state(gameover_state)
    if fisher.state == fisher.FIGHTING:
        FishingUI_Class.update(frame_time, fisher, fish, float)
        pass

def draw(frame_time):
    global ship
    global fisher
    global float
    global fish
    global Objects
    global ui
    global running_time

    clear_canvas()

    bg.draw(running_time)
    ship.draw()
    fisher.draw()
    if float.state != float.NONE:
        float.draw()
    for obj in Objects:
        obj.draw()
    ui.draw()

    if fisher.state == fisher.FIGHTING:
        FishingUI_Class.draw(fisher, fish)
    print(fish.fish_state)
    if(fish.fish_state == fish.DRAW):
        fish.draw(fisher)
    FishingUI_Class.draw_sys(fisher,fish)
    delay(0.03)
    update_canvas()

