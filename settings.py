import pygame


### Display Setup ###
pygame.display.set_caption("Montclair")
WIDTH = 1280
HEIGHT = 720
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pygame.time.Clock()
clock.tick(FPS)


### Colors ###
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
