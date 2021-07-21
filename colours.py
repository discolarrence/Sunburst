from itertools import cycle
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

#child of pygame Color class to append new color objects to a list of all colors on initialization
class Colour(Color):
    colour_list = []
    red_list = []
    green_list = []
    blue_list = []
    

    def __init__(self, red, green, blue):
        super().__init__(red, green, blue)
        self.red = red
        self.green = green
        self.blue = blue
        
        Colour.colour_list.append(self)

        if self.red == 255:
            Colour.red_list.append(self)
        if self.green ==255:
            Colour.green_list.append(self)
        if self.blue == 255:
            Colour.blue_list.append(self)

    def next_colour(self, list):
        cycled_list = cycle(list)
        return next(cycled_list)

