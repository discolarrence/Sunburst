from itertools import cycle
import pygame
from pygame.locals import *


class Colour(Color):
    colour_list = []

    def __init__(self, red, green, blue):
        super().__init__(red, green, blue)

        Colour.colour_list.append(self)

    def next_colour(self):
        cycled_list = cycle(self.colour_list)
        return next(cycled_list)

