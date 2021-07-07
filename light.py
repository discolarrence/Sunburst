import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

class Light:
    light_list = []

    def __init__(self, surface, corners, section, level):
        self.corners = corners
        self.surface = surface
        self.section = section
        self.level = level
        
        Light.light_list.append(self)

    def turn_on(self):
        pygame.draw.polygon(self.surface, WHITE, self.corners, 5)


    def turn_off(self):
        pygame.draw.polygon(self.surface, GRAY, self.corners, 5)


    def change_color(self, color):
        pygame.draw.polygon(self.surface, color, self.corners, 5)

    @property
    def section(self):
        return self._section

    @property
    def level(self):
        return self._level
    
    



