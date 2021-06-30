import pygame
from pygame.locals import *
from section import Section

BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
ab_outer_coordinates = ({'x':45, 'y':450},
                        {'x':195, 'y':165},
                        {'x':580, 'y':35},
                        {'x':600, 'y':215},
                        {'x':450, 'y':275},
                        {'x':400, 'y':420})
cd_outer_coordinates = ({'x':610, 'y':35},
                        {'x':995, 'y':160},
                        {'x':1150, 'y':450},
                        {'x':795, 'y':420},
                        {'x':750, 'y':275},
                        {'x':600, 'y':215},)
a_middle_coordinates = ({'x':85, 'y':410},
                    {'x':195, 'y':210},
                    {'x':420, 'y':279},
                    {'x':410, 'y':300},
                    {'x':210, 'y':250},
                    {'x':121, 'y':380},
                    {'x':385, 'y':390},
                    {'x':385, 'y':400})
a_inner_coordinates = ({'x':180, 'y':340},
                    {'x':220, 'y':290},
                    {'x':400, 'y':315},
                    {'x':380, 'y':365})
b_middle_coordinates = ({'x':265, 'y':155},
                    {'x':550, 'y':65},
                    {'x':575, 'y':200},
                    {'x':560, 'y':200},
                    {'x':520, 'y':100},
                    {'x':335, 'y':155},
                    {'x':460, 'y':240},
                    {'x':448, 'y':250})
b_inner_coordinates = ({'x':405, 'y':155},
                    {'x':495, 'y':140},
                    {'x':540, 'y':205},
                    {'x':480, 'y':230})
c_middle_coordinates = ({'x':645, 'y':70},
                    {'x':925, 'y':150},
                    {'x':751, 'y':250},
                    {'x':740, 'y':240},
                    {'x':865, 'y':155},
                    {'x':675, 'y':105},
                    {'x':635, 'y':200},
                    {'x':615, 'y':200})
c_inner_coordinates = ({'x':700, 'y':145},
                    {'x':785, 'y':160},
                    {'x':720, 'y':230},
                    {'x':660, 'y':205})
d_middle_coordinates = ({'x':990, 'y':210},
                    {'x':1105, 'y':410},
                    {'x':820, 'y':405},
                    {'x':820, 'y':385},
                    {'x':1065, 'y':385},
                    {'x':990, 'y':260},
                    {'x':785, 'y':295},
                    {'x':780, 'y':280})
d_inner_coordinates = ({'x':970, 'y':295},
                    {'x':1010, 'y':345},
                    {'x':820, 'y':365},
                    {'x':800, 'y':315})


pygame.init()
width, height = 1200, 480
screen = pygame.display.set_mode((width, height))
running = True

img = pygame.image.load('sunburst7.jpg')
img.convert
rect = img.get_rect()
rect.center = width//2, height//2

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    screen.fill(GRAY)
    screen.blit(img, rect)

    ab1 = Section(screen, ab_outer_coordinates)
    cd1 = Section(screen, cd_outer_coordinates)
    a2 = Section(screen, a_middle_coordinates)
    a3 = Section(screen, a_inner_coordinates)
    b2 = Section(screen, b_middle_coordinates)
    b3 = Section(screen, b_inner_coordinates)
    c2 = Section(screen, c_middle_coordinates)
    c3 = Section(screen, c_inner_coordinates)
    d2 = Section(screen, d_middle_coordinates)
    d3 = Section(screen, d_inner_coordinates)

    pygame.display.flip()

pygame.quit()