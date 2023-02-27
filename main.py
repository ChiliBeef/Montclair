import pygame
from settings import *
from dialogue import *

pygame.init()



### First dialogue ###
dialogue = Dialogue()
dialogue.render("Here we have some standard text and dialogue.", 20, 10)
dialogue.render("Here we have some standard text and dialogue.", 20, 30)

### First set of choices ###
option1 = Options()
option2 = Options()

option1.render("This is Option 1.", 20, 80)
option2.render("This is Option 2.", 20, 100)


### Game loop ###
run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if option1.rect.collidepoint(mouse_pos):
                    WINDOW.fill(BLACK)
                    option1_text = option1.render("Welcome to Option 1", 300, 300)
                    print("You clicked on Option 1.")
                    option1.rect.topleft = (-100, -100)  # Remove clickable area from Option 1 by putting it off screen.
                    option2.rect.topleft = (-100, -100)  # Remove clickable area from Option 2 by putting it off screen.

                elif option2.rect.collidepoint(mouse_pos):
                    WINDOW.fill(BLACK)
                    option2_text = option2.render("Welcome to Option 2", 300, 300)
                    print("You clicked on Option 2.")
                    option1.rect.topleft = (-100, -100)  # Remove clickable area from Option 1 by putting it off screen.
                    option2.rect.topleft = (-100, -100)  # Remove clickable area from Option 2 by putting it off screen.


    pygame.display.flip()
