import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Light:
    def __init__(self, surface, corners, section, level):
        self.corners = corners
        self.surface = surface
        self.section = section
        self.level = level
        

    def turn_on(self):
        pygame.draw.polygon(self.surface, WHITE, self.corners, 5)


    def turn_off(self):
        pygame.draw.polygon(self.surface, BLACK, self.corners, 5)


    def change_color(self, color):
        pygame.draw.polygon(self.surface, color, self.corners, 5)
