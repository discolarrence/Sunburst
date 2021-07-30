import pygame
from colours import BLACK, WHITE


class Button(pygame.sprite.Sprite):
    """Creates button sprite

    Args:
        text (str): button text
        x (int): x-axis coordinate for button corner location
        y (int): y-axis coordinate for button corner location
        width (int): button width
        height (int): button height
        color (var): button color
        action (function): action clicked button performs

    Attributes:
        button_list (list): list of all buttons
    """
    button_list = pygame.sprite.Group()

    def __init__(self, text: str, x: int, y: int, width: int, height: int,
                 color, action):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        button_font = pygame.font.Font(None, 15)
        button_text = button_font.render(text, True, BLACK)
        button_text_rect = button_text.get_rect(center=self.rect.center)
        self.image.blit(button_text, button_text_rect)
        self.rect.topleft = x, y
        self.action = action

        Button.button_list.add(self)

    def is_clicked(self, event):
        """method that determines if a mouse click is on one of the buttons"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()
        return False


class LightShowButton(Button):
    """Child of button class creates light show buttons

    Args:
        text (str): button text
        x (int): x-axis coordinate for button corner location
        y (int): y-axis coordinate for button corner location
        action (function): action clicked button performs
    """
    def __init__(self, text: str, x: int, y: int, action):
        super().__init__(text, x, y, 150, 50, WHITE, action)
