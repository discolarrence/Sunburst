import pygame
from colours import GRAY
from itertools import cycle
from pygame.locals import *


class Light:
    """"""
    light_list = []
    top_list = []
    middle_list = []
    bottom_list = []
    a_list = []
    b_list = []
    c_list = []
    d_list = [] 

    def __init__(self, surface, corners, section, level):
        self.surface = surface
        self.corners = corners
        self.section = section
        self.level = level
        
        Light.light_list.append(self)
        
        if self.level == 'top':
            Light.top_list.append(self)
        elif self.level == 'middle':
            Light.middle_list.append(self)
        elif self.level == 'bottom':
            Light.bottom_list.append(self)

        if self.section == 'A':
            Light.a_list.append(self)
        elif self.section == 'B':
            Light.b_list.append(self)
        elif self.section == 'C':
            Light.c_list.append(self)
        elif self.section == 'D':
            Light.d_list.append(self)

    def turn_on(self, color):
        pygame.draw.polygon(self.surface, color, self.corners, 5)

    def turn_off(self):
        pygame.draw.polygon(self.surface, GRAY, self.corners, 5)
        pygame.display.flip()

#  light effect functions
def screen_update_and_wait(wait_time: int):
    """update display contents and wait

    Parameters
    ----------
    wait_time : int
        time to wait in microseconds
    """
    pygame.display.flip()
    pygame.time.wait(wait_time)


def colour_cycle_levels(colour_list: list, reps: int, wait_time: int):
    """cycle through list to change light color by level grouping

    Parameters
    ----------
    colour_list : list
        list of colors
    reps : int
        number of repetions
    wait_time : int
        time to wait in microseconds
    """
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
    """cycle through list to change light color from inner to outer sections

    Parameters
    ----------
    colour_list : list
        list of colors
    reps : int
        number of repetions
    wait_time : int
        time to wait in microseconds
    """
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
    """cycle through list to change level color one level at a time

    Parameters
    ----------
    colour_list : list
        list of colors
    reps : int
        number of repetions
    wait_time : int
        time to wait in microseconds
    """
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
