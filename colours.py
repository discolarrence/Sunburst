from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)


class Colour(Color):
    '''
    Child of pygame Color class to append new color objects to lists

    Args:
        red (int): stores red RGB value
        green (int): stores green RGB value
        blue (int): stores blue RGB value

    Attributes:
        colour_list (list): list of all colors
        red_list (list): list of all colors with a red RGB value of 255
        green_list (list): list of all colors with a green RGB value of 255
        blue_list (list): list of all colors with a blue RGB value of 255
    '''
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
        if self.green == 255:
            Colour.green_list.append(self)
        if self.blue == 255:
            Colour.blue_list.append(self)
