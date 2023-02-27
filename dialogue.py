import pygame
from settings import *



class Dialogue():
    def __init__(self):
        self.font = pygame.font.SysFont("helvetica", 20)
        self.color = WHITE
        self.displaySurface = pygame.display.get_surface()


    def render(self, text, x, y):
        self.position = (x, y)
        self.rect = pygame.rect.Rect(self.position[0], self.position[1], 145, 20)
        dialogue = self.font.render(f"{text}", True, self.color)
        dialoguePosition = dialogue.get_rect(x=self.position[0], y=self.position[1])   # Position the dialogue
        self.displaySurface.blit(dialogue, dialoguePosition)

class Options():
    def __init__(self):
        self.font = pygame.font.SysFont("helvetica", 20)
        self.color = YELLOW
        self.displaySurface = pygame.display.get_surface()
        
    def render(self, text, x, y):
        self.position = (x, y)
        self.rect = pygame.rect.Rect(self.position[0], self.position[1], 145, 20)
        dialogue = self.font.render(f"{text}", True, self.color)
        dialoguePosition = dialogue.get_rect(x=self.position[0], y=self.position[1])   # Position the dialogue
        self.displaySurface.blit(dialogue, dialoguePosition)
