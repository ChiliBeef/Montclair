import sys
import pygame
from settings import *
from font_settings import *
from office_0 import office_0

pygame.init()



### Title Screen ###
title, title_rect = title_text()
WINDOW.blit(title, title_rect)


### Game loop ###
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if title_rect.collidepoint(event.pos):
                office_0(WINDOW)                    # This will begin the game by taking you to your office.
                title_rect.topleft = (-100, -100)   # Remove clickable area from Title by putting it off screen.


    pygame.display.update()

pygame.quit()
sys.exit()
