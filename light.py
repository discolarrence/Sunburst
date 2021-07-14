import pygame
from pygame.locals import *
from colours import GRAY

class Light:
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

    




