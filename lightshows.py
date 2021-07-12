import pygame
from colours import GRAY
from itertools import cycle
from light import Light
from pygame.locals import *

def colour_cycle_levels(colour_list, reps, time_between):
    inner_colour = middle_colour = outer_colour = GRAY
    colour_cycle = cycle(colour_list)
    for _ in range(0, reps):
        for light in Light.inner_list:
            Light.turn_on(light, inner_colour)
        for light in Light.middle_list:
            Light.turn_on(light, middle_colour)
        for light in Light.outer_list:
            Light.turn_on(light, outer_colour)
        pygame.display.flip()
        pygame.time.wait(time_between)
        outer_colour = middle_colour
        middle_colour = inner_colour
        inner_colour = next(colour_cycle)

def colour_cycle_inside_out(colour_list, reps, time_between):
    inside_colour = outside_colour = outer_colour = GRAY
    colour_cycle = cycle(colour_list)
    for _ in range(0, reps):
        for light in Light.outer_list:
            Light.turn_on(light, outer_colour)
        for light in Light.a_list:
            Light.turn_on(light, outside_colour)
        for light in Light.d_list:
            Light.turn_on(light, outside_colour)
        for light in Light.b_list:
            Light.turn_on(light, inside_colour)
        for light in Light.c_list:
            Light.turn_on(light, inside_colour)
        pygame.display.flip()
        pygame.time.wait(time_between)
        outer_colour = outside_colour
        outside_colour = inside_colour
        inside_colour = next(colour_cycle)

def colour_cycle_build_levels(colour_list, reps, time_between):
    colour = GRAY
    colour_cycle = cycle(colour_list)
    for _ in range(0, reps):
        for light in Light.inner_list:
            Light.turn_on(light, colour)
        pygame.display.flip()
        pygame.time.wait(time_between)
        for light in Light.middle_list:
            Light.turn_on(light, colour)
        pygame.display.flip()
        pygame.time.wait(time_between)
        for light in Light.outer_list:
            Light.turn_on(light, colour)
        pygame.display.flip()
        pygame.time.wait(time_between)
        colour = next(colour_cycle)
    