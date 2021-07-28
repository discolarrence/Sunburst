import pygame
from button import LightShowButton
from coordinates import light_shape_corner_coordinates
from colours import Colour, BLACK, WHITE
from light import *
from pygame.locals import *

#create color objects
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
width, height = 1200, 750
screen = pygame.display.set_mode((width, height))
running = True
screen.fill(BLACK)
pygame.display.set_caption('Sunburst--Click buttons for light effect demo. Close window or ESC to quit.')

#create light shapes
ab1 = Light(screen, light_shape_corner_coordinates[0], 'AB', 'top')
cd1 = Light(screen, light_shape_corner_coordinates[1], 'CD', 'top')
a2 = Light(screen, light_shape_corner_coordinates[2], 'A', 'middle') 
b2 = Light(screen, light_shape_corner_coordinates[3], 'B', 'middle')
c2 = Light(screen, light_shape_corner_coordinates[4], 'C', 'middle')
d2 = Light(screen, light_shape_corner_coordinates[5], 'D', 'middle')
a3 = Light(screen, light_shape_corner_coordinates[6], 'A', 'bottom')
b3 = Light(screen, light_shape_corner_coordinates[7], 'B', 'bottom')
c3 = Light(screen, light_shape_corner_coordinates[8], 'C', 'bottom')
d3 = Light(screen, light_shape_corner_coordinates[9], 'D', 'bottom')

#create light shows
def rainbow_levels_fast():
    colour_cycle_levels(Colour.colour_list, 16, 50)

def rainbow_in_to_out_slow():
    colour_cycle_inside_out(Colour.colour_list, 16, 250)

def rainbow_build_levels_med():
    colour_cycle_build_levels(Colour.colour_list, 16, 150)

def red_levels_med():
    colour_cycle_levels(Colour.red_list, 18, 150)

def blue_levels_med():
    colour_cycle_levels(Colour.blue_list, 18, 150)

def green_levels_med():
    colour_cycle_levels(Colour.green_list, 18, 150)

#create buttons
LightShowButton("rainbow levels fast", 25, 600, rainbow_levels_fast)
LightShowButton("rainbow in>out slow", 425, 600, rainbow_in_to_out_slow)
LightShowButton("rainbow build levels med", 225, 600, rainbow_build_levels_med)
LightShowButton("red levels med", 620, 600, red_levels_med)
LightShowButton("green levels med", 825, 600, green_levels_med)
LightShowButton("blue levels med", 1025, 600, blue_levels_med)

LightShowButton.button_list.draw(screen)

#start lightshow
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        
        elif event.type == MOUSEBUTTONDOWN:
            for button in LightShowButton.button_list:
                button.is_clicked(event)

        elif event.type == QUIT:
            running = False

        for light in Light.light_list:
            Light.turn_off(light)

pygame.quit()