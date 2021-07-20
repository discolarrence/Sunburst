from itertools import cycle
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

#child of pygame Color class to append new color objects to a list of all colors on initialization
class Colour(Color):
    colour_list = []

    def __init__(self, red, green, blue):
        super().__init__(red, green, blue)

        Colour.colour_list.append(self)

    def next_colour(self):
        cycled_list = cycle(self.colour_list)
        return next(cycled_list)

