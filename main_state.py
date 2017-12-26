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
Locals = None

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
    global Locals

    ui = Class.UI()
    bg = Class.FixedTileBackground()
    Locals = [Object_Class.LOCAL(i) for i in range(bg.local-bg.max_vortex_id)]
    Objects = [Object_Class.STONE(i) for i in range(bg.max_stone_id)]
    Voretx = [Object_Class.VORTEX(i) for i in range(0, bg.max_vortex_id-bg.max_stone_id)]
    Objects = Objects + Voretx
    ship = Ship_Class.SHIP()
    fisher = Fisher_Class.FISHER(bg)
    float = Float_Class.FLOAT(fisher)
    fish = Fish_Class.FISH()
    bg.set_center_object(ship)
    ship.set_background(bg)
    fish.set_background(bg)
    float.set_background(bg)

    for Object in Objects:
        Object.set_background(bg)

    for local in Locals:
        local.set_background(bg)


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
        if event.type == SDL_QUIT:
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
    global Locals

    handle_events(frame_time)

    bg.update(frame_time)
    ship.update(frame_time)
    fisher.update(ship, frame_time)
    float.update(fisher, frame_time)
    ui.upadte(fisher, frame_time)
    fish.update(fisher, float)

    running_time = time.clock() - game_time

    if fisher.fisher_hunger <= 0:
        game_framework.change_state(gameover_state)
    if fisher.state == fisher.FIGHTING:
        FishingUI_Class.update(frame_time, fisher, fish, float)
        pass

    for obj in Objects:
        if ship.ship_x - obj.x > -100 and ship.ship_x - obj.x < 100:
            if ship.ship_y - obj.y > -100 and ship.ship_y - obj.y < 100:
                if collide(ship, obj):
                    fisher.fisher_hunger -= ship.ship_accelate
                    ship.state_accelate = ship.NONE
                    ship.ship_accelate = 0
                    if obj.x >= ship.ship_x:
                        ship.ship_x -= 20
                    elif obj.x <= ship.ship_x:
                        ship.ship_x += 20
                    if obj.y >= ship.ship_y:
                        ship.ship_y -= 20
                    elif obj.y <= ship.ship_y:
                        ship.ship_y += 20

    for loc in Locals:
        if collide(float,loc):
            fish.weight = loc.weight

    if fisher.fishing > 5:
        fisher.fishing = 0
        for loc in Locals:
            loc.weight = random.randint(-40,40)


def draw(frame_time):
    global ship
    global fisher
    global float
    global fish
    global Objects
    global ui
    global running_time
    global Locals

    clear_canvas()

    bg.draw()

    for obj in Objects:
        obj.draw()
        #obj.draw_bb()

    #for local in Locals:
    #    local.draw_bb()

    bg.draw_bg_ui(running_time)

    ship.draw()
    #ship.draw_bb()

    fisher.draw()

    if float.state != float.NONE:
        float.draw()

    ui.draw()

    if fisher.state == fisher.FIGHTING:
        FishingUI_Class.draw(fisher, fish)

    if(fish.fish_state == fish.DRAW):
        fish.draw(fisher)

    FishingUI_Class.draw_sys(fisher,fish)

    delay(0.03)
    update_canvas()

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False

    if right_a < left_b:
        return False

    if top_a < bottom_b:
        return False

    if bottom_a > top_b:
        return  False

    return True
    pass