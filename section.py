import pygame
from pygame.locals import *

BLACK = (0, 0, 0)

class Section:
    color = BLACK

    def __init__(self, surface, corners):
        counter = 0
        for _ in range(len(corners)):
            start = counter
            if start == len(corners)-1:
                end = 0
            else:
                end = start + 1
            pygame.draw.line(surface, self.color, (corners[start]['x'], corners[start]['y']), (corners[end]['x'], corners[end]['y']), 3)
            counter += 1