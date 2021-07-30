import pygame


class Display:
    '''
    Display surface

    Args:
        width (int): width of display
        height (int): height of display
        fill_color (var): background color
        caption (str): caption for display window
        show (bool): state of lightshow
    '''
    def __init__(self, width, height, fill_color, caption, show=True):
        self.width = width
        self.height = height
        self.fill_color = fill_color
        self.caption = caption
        self.show = show

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(self.fill_color)
        pygame.display.set_caption(self.caption)
