import pygame
from colours import GRAY
from itertools import cycle
from light import Light
from pygame.locals import *

def screen_update_and_wait(wait_time: int):
    pygame.display.flip()
    pygame.time.wait(wait_time)

def colour_cycle_levels(colour_list: list, reps: int, wait_time: int):
    bottom_colour = middle_colour = top_colour = GRAY
    colour_cycle = cycle(colour_list)
    for _ in range(0, reps):
        for light in Light.bottom_list:
            Light.turn_on(light, bottom_colour)
        for light in Light.middle_list:
            Light.turn_on(light, middle_colour)
        for light in Light.top_list:
            Light.turn_on(light, top_colour)
        screen_update_and_wait(wait_time)
        top_colour = middle_colour
        middle_colour = bottom_colour
        bottom_colour = next(colour_cycle)
    

def colour_cycle_inside_out(colour_list: list, reps: int, wait_time: int):
    inside_colour = outside_colour = top_colour = GRAY
    colour_cycle = cycle(colour_list)
    for _ in range(0, reps):
        for light in Light.top_list:
            Light.turn_on(light, top_colour)
        for light in Light.a_list:
            Light.turn_on(light, outside_colour)
        for light in Light.d_list:
            Light.turn_on(light, outside_colour)
        for light in Light.b_list:
            Light.turn_on(light, inside_colour)
        for light in Light.c_list:
            Light.turn_on(light, inside_colour)
        screen_update_and_wait(wait_time)
        top_colour = outside_colour
        outside_colour = inside_colour
        inside_colour = next(colour_cycle)

def colour_cycle_build_levels(colour_list: list, reps: int, wait_time: int):
    colour = GRAY
    colour_cycle = cycle(colour_list)
    for _ in range(0, reps):
        for light in Light.bottom_list:
            Light.turn_on(light, colour)
        screen_update_and_wait(wait_time)
        for light in Light.middle_list:
            Light.turn_on(light, colour)
        screen_update_and_wait(wait_time)
        for light in Light.top_list:
            Light.turn_on(light, colour)
        screen_update_and_wait(wait_time)
        colour = next(colour_cycle)
