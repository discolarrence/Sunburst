import pygame
from colours import BLACK, WHITE

class Button:
    button_list = []
    
    def __init__(self, surface, text:str, position_x:int, position_y:int, width:int, height:int, color):
        self.surface = surface
        self.text = text
        self.color = color
        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height = height
        self.outline = [position_x, position_y, width, height]

        Button.button_list.append(self)

        pygame.draw.rect(self.surface, self.color, self.outline)
        button_font = pygame.font.Font(pygame.font.get_default_font(), 20)
        button_text = button_font.render(text, True, BLACK)
        button_text_shape = button_text.get_rect()
        button_text_shape.center = ( (self.position_x+(self.width/2)), 
                                (self.position_y+(self.height/2)) )
        self.surface.blit(button_text, button_text_shape)
        pygame.display.update


class LightshowButton(Button):
    def __init__(self, surface, text:str, position_x:int, position_y:int):
        super().__init__(surface, text, position_x, position_y, 100, 50, WHITE)
    