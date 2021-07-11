import pygame
from pygame.locals import *

GRAY = (128, 128, 128)

class Light:
    light_list = []
    outer_list = []
    middle_list = []
    inner_list = []


    def __init__(self, surface, corners, section, level):
        self.corners = corners
        self.surface = surface
        self.section = section
        self.level = level
        
        Light.light_list.append(self)
        
        if self.level == 'outer':
            Light.outer_list.append(self)
        elif self.level == 'middle':
            Light.middle_list.append(self)
        elif self.level == 'inner':
            Light.inner_list.append(self)

    def turn_on(self, color):
        pygame.draw.polygon(self.surface, color, self.corners, 5)

    def turn_off(self):
        pygame.draw.polygon(self.surface, GRAY, self.corners, 5)



