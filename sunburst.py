import pygame
from coordinates import list_of_coordinates_lists
from colours import Colour, BLACK
from light import Light
from lightshows import *
from pygame.locals import *

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

#set up surface & terminal instructions
pygame.init()
width, height = 1200, 480
screen = pygame.display.set_mode((width, height))
running = True
screen.fill(BLACK)
print('Type 1, 2, or 3 to watch different light shows. ESC to quit.')
print(Fore.RED + 'This text is red in color')

#create light shapes
ab1 = Light(screen, list_of_coordinates_lists[0], 'AB', 'top')
cd1 = Light(screen, list_of_coordinates_lists[1], 'CD', 'top')
a2 = Light(screen, list_of_coordinates_lists[2], 'A', 'middle') 
a3 = Light(screen, list_of_coordinates_lists[3], 'A', 'bottom')
b2 = Light(screen, list_of_coordinates_lists[4], 'B', 'middle')
b3 = Light(screen, list_of_coordinates_lists[5], 'B', 'bottom')
c2 = Light(screen, list_of_coordinates_lists[6], 'C', 'middle')
c3 = Light(screen, list_of_coordinates_lists[7], 'C', 'bottom')
d2 = Light(screen, list_of_coordinates_lists[8], 'D', 'middle')
d3 = Light(screen, list_of_coordinates_lists[9], 'D', 'bottom')

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

        for light in Light.light_list:
            Light.turn_off(light)

pygame.quit()