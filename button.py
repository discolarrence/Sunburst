import pygame
from colours import BLACK, WHITE

class Button(pygame.sprite.Sprite):
    button_list = pygame.sprite.Group()
    
    def __init__(self, text:str, x:int, y:int, width:int, height:int, color, action):
        super().__init__()
        self.image= pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        button_font = pygame.font.Font(None, 15)
        button_text = button_font.render(text, True, BLACK)
        button_text_rect = button_text.get_rect(center = self.rect.center)
        self.image.blit(button_text, button_text_rect)
        self.rect.topleft = x, y
        self.action = action

        Button.button_list.add(self)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()
        return False

class LightShowButton(Button):
    def __init__(self, text:str, x:int, y:int, action):
        super().__init__(text, x, y, 150, 50, WHITE, action)
    