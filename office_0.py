import sys
import pygame
from settings import *
from font_settings import *
from computer_console_0 import computer_console_0
from animate_hallway import animate_hallway


def office_0(WINDOW):
    WINDOW.fill(BLACK)

    ### Dialogue ###
    dialogue = Dialogue()
    dialogue.render("Here we have some dialogue about how it's your first evening shift at the Montclair datacenter.", 20, 10)
    dialogue.render("Here we have even more dialogue about checking any messages or error reports.", 20, 30)


    ### Options ###
    option1 = Options()
    option1.render("Check the system log.", 20, 80)

    option2 = Options()
    option2.render("Investigate the server room.", 20, 100)
    
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if option1.rect.collidepoint(event.pos):
                    computer_console_0(WINDOW)
                    option1.rect.topleft = (-100, -100)
                    option2.rect.topleft = (-100, -100)

                elif option2.rect.collidepoint(event.pos):
                    animate_hallway(WINDOW)
                    option1.rect.topleft = (-100, -100)
                    option2.rect.topleft = (-100, -100)

        pygame.display.update()
