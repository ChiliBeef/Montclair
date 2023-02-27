import pygame
from settings import *



class Dialogue(pygame.surface.Surface):
    def __init__(self):
        self.font = pygame.font.SysFont("helvetica", 20)
        self.color = WHITE
    
    def render(self, text):
        self.font.render(f"{text}", True, self.color)

class Options(pygame.surface.Surface):
    def __init__(self):
        self.font = pygame.font.SysFont("helvetica", 20)
        self.color = YELLOW

    def render(self, text):
        self.font.render(f"{text}", True, self.color)
