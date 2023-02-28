import pygame
from settings import *



def title_font():
    title_font = pygame.font.SysFont("helvetica", 60, False, True)
    title = title_font.render("MONTCLAIR", True, WHITE)
    title_rect = title.get_rect(center=(WIDTH/2, HEIGHT/2))
    return title, title_rect


class Dialogue():
    def __init__(self):
        self.font = pygame.font.SysFont("helvetica", 20)
        self.color = WHITE
        self.displaySurface = pygame.display.get_surface()

    def render(self, text, x, y):
        dialogue = self.font.render(f"{text}", True, self.color)
        self.displaySurface.blit(dialogue, (x, y))


class Options():
    def __init__(self):
        self.font = pygame.font.SysFont("helvetica", 20)
        self.color = YELLOW
        self.displaySurface = pygame.display.get_surface()
        
    def render(self, text, x, y):
        options = self.font.render(f"{text}", True, self.color)
        options_rect = options.get_rect()                           # Get a rectangle and draw it around the Options text.
        options_rect.height = self.font.get_height()                # Set the height of the rect to be the same as the font size.
        options_rect.width = options.get_width()                    # Set the width of the rect to be the same as the width of the rendered text.
        options_rect.topleft = (x, y)                               # Draw the rect starting in the top left corner using the x, y coordinates.
        self.rect = options_rect                                    # Declare that the drawn rect belongs to 'options_rect' and its other instance attributes.
        self.displaySurface.blit(options, options_rect)
                   
