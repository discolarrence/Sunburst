import pygame
from coordinates import list_of_coordinates_lists
from colours import Colour, BLACK
from light import Light
from lightshows import *
from pygame.locals import *

# create color objects
white = Colour(255, 255, 255)
fuchsia = Colour(255, 0, 255)
salmon = Colour(255, 0, 128)
red = Colour(255, 0, 0)
yellow = Colour(255, 255, 0)
orange = Colour(255, 128, 0)
olive = Colour(128, 128, 0)
green = Colour(128, 255, 0)
lime = Colour(0, 255, 0)
teal = Colour(0, 128, 128)
cornflower = Colour(0, 128, 255)
aqua = Colour(0, 255, 255)
lt_green = Colour(0, 255, 128)
blue = Colour(0, 0, 255)
lt_purple = Colour(128, 0, 255)
purple = Colour(128, 0, 128)

#set up surface
pygame.init()
width, height = 1200, 480
screen = pygame.display.set_mode((width, height))
running = True

#create light shapes
ab1 = Light(screen, list_of_coordinates_lists[0], 'AB', 'outer')
cd1 = Light(screen, list_of_coordinates_lists[1], 'CD', 'outer')
a2 = Light(screen, list_of_coordinates_lists[2], 'A', 'middle')
a3 = Light(screen, list_of_coordinates_lists[3], 'A', 'inner')
b2 = Light(screen, list_of_coordinates_lists[4], 'B', 'middle')
b3 = Light(screen, list_of_coordinates_lists[5], 'B', 'inner')
c2 = Light(screen, list_of_coordinates_lists[6], 'C', 'middle')
c3 = Light(screen, list_of_coordinates_lists[7], 'C', 'inner')
d2 = Light(screen, list_of_coordinates_lists[8], 'D', 'middle')
d3 = Light(screen, list_of_coordinates_lists[9], 'D', 'inner')

#start lightshow
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_1:
                colour_cycle_levels(Colour.colour_list, 160, 50)
            elif event.key == K_2:
                colour_cycle_inside_out(Colour.colour_list, 160, 150)
            elif event.key == K_3:
                colour_cycle_build_levels(Colour.colour_list, 160, 250)

        elif event.type == QUIT:
            running = False
    
    #default screen
    screen.fill(BLACK)

pygame.quit()