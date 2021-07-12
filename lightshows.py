import pygame
from colours import Colour
from itertools import cycle
from light import Light
from pygame.locals import *

def blink_all(light_list, color, time_between):
    for light in light_list:
        Light.turn_on(light, color)
    pygame.time.wait(time_between)
    for light in light_list:
        Light.turn_on(light, color)
    pygame.time.wait(time_between)
