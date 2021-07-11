import pygame
import random
from colours import Colour
from itertools import cycle
from light import Light
from pygame.locals import *



BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

ab_outer_coordinates = [[45, 450],
                    [80, 270],
                    [195, 165],
                    [390, 55],
                    [580, 35],
                    [595, 215],
                    [515, 235],
                    [450, 275],
                    [410, 345],
                    [400, 420]]
cd_outer_coordinates = [[610, 35],
                    [795, 50],
                    [995, 160],
                    [1110, 285],
                    [1150, 450],
                    [795, 420],
                    [790, 345,],
                    [750, 275],
                    [680,235],
                    [605, 215]]
a_middle_coordinates = [[85, 410],
                    [120, 295],
                    [195, 210],
                    [420, 279],
                    [410, 300],
                    [210, 250],
                    [155,300],
                    [120, 380],
                    [385, 390],
                    [385, 400]]
a_inner_coordinates = [[180, 340],
                    [220, 290],
                    [400, 315],
                    [380, 365]]
b_middle_coordinates = [[265, 155],
                    [420, 85],
                    [550, 65],
                    [575, 200],
                    [560, 200],
                    [520, 100],
                    [435, 115],
                    [335, 155],
                    [460, 240],
                    [450, 250]]
b_inner_coordinates = [[405, 155],
                    [495, 140],
                    [540, 205],
                    [480, 230]]
c_middle_coordinates = [[645, 70],
                    [780, 80],
                    [925, 150],
                    [750, 250],
                    [740, 240],
                    [865, 155],
                    [770, 115],
                    [675, 105],
                    [635, 200],
                    [615, 200]]
c_inner_coordinates = [[700, 145],
                    [785, 160],
                    [720, 230],
                    [660, 205]]
d_middle_coordinates = [[990, 210],
                    [1060, 285],
                    [1105, 410],
                    [820, 405],
                    [820, 385],
                    [1065, 385],
                    [1030, 310],
                    [990, 260],
                    [785, 295],
                    [780, 280]]
d_inner_coordinates = [[970, 295],
                    [1010, 345],
                    [820, 365],
                    [800, 315]]

inner_colour = GRAY
outer_colour = GRAY 
middle_colour = GRAY

pygame.init()
width, height = 1200, 480
screen = pygame.display.set_mode((width, height))
running = True

# img = pygame.image.load('sunburst7.jpg')
# img.convert
# rect = img.get_rect()
# rect.center = width//2, height//2

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    
    screen.fill(BLACK)
    
    red = Colour(255, 0, 0)
    lime = Colour(0, 255, 0)
    blue = Colour(0, 0, 255)
    fuchsia = Colour(255, 0, 255)
    aqua = Colour(0, 255, 255)
    yellow = Colour(255, 255, 0)
    olive = Colour(128, 128, 0)
    purple = Colour(128, 0, 128)
    teal = Colour(0, 128, 128)
    orange = Colour(255, 128, 0)
    salmon = Colour(255, 0, 128)
    green = Colour(128, 255, 0)
    lt_purple = Colour(128, 0, 255)
    cornflower = Colour(0, 128, 255)
    lt_green = Colour(0, 255, 128)
    white = Colour(255, 255, 255)

    ab1 = Light(screen, ab_outer_coordinates, 'AB', 'outer')
    cd1 = Light(screen, cd_outer_coordinates, 'CD', 'outer')
    a2 = Light(screen, a_middle_coordinates, 'A', 'middle')
    a3 = Light(screen, a_inner_coordinates, 'A', 'inner')
    b2 = Light(screen, b_middle_coordinates, 'B', 'middle')
    b3 = Light(screen, b_inner_coordinates, 'B', 'inner')
    c2 = Light(screen, c_middle_coordinates, 'C', 'middle')
    c3 = Light(screen, c_inner_coordinates, 'C', 'inner')
    d2 = Light(screen, d_middle_coordinates, 'D', 'middle')
    d3 = Light(screen, d_inner_coordinates, 'D', 'inner')

    colour_cycle = cycle(Colour.colour_list)
    
    for _ in range(1,10):
        for light in Light.inner_list:
            Light.turn_on(light, inner_colour)
        for light in Light.middle_list:
            Light.turn_on(light, middle_colour)
        for light in Light.outer_list:
            Light.turn_on(light, outer_colour)
        pygame.display.flip()
        pygame.time.wait(250)
        outer_colour = middle_colour
        middle_colour = inner_colour
        inner_colour = next(colour_cycle)

        


pygame.quit()