import sys
import pygame
import time
from settings import *
from font_settings import *
from office_0 import office_0

pygame.init()

### Title Screen ###
title, title_rect = title_text()
WINDOW.blit(title, title_rect)


glitch1 = pygame.image.load("assets/computer/server_cabinets_glitch1.png")
glitch2 = pygame.image.load("assets/computer/server_cabinets_glitch2.png")


current_frame_index = 0
animation_frames = {0 : [glitch1, 2000], 1 : [glitch2, 100] , 2 : [glitch1, 50] , 3 :  [glitch2, 100] }
current_frame = animation_frames[current_frame_index][0]
frame_time = animation_frames[current_frame_index][1]
first_time = time.time()
flip_frame = pygame.event.custom_type()
pygame.time.set_timer(flip_frame, frame_time)


# Load title screen sound file to be played.
sound_effect = pygame.mixer.Sound("assets/sounds/title_screen.wav")
sound_effect.play(-1)

### Game loop ###
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if title_rect.collidepoint(event.pos):
                pygame.mixer.stop()                             # Stop the background music.
                office_0(WINDOW)                                # This will begin the game by taking you to your office.
                title_rect.topleft = (-100, -100)               # Remove clickable area from Title by putting it off screen.
        
        if event.type == flip_frame: 
            current_frame_index += 1
            current_frame_index = current_frame_index % len(animation_frames.keys())
            current_frame = animation_frames[current_frame_index][0]
            frame_time = animation_frames[current_frame_index][1]
            first_time = time.time()
            pygame.time.set_timer(flip_frame, frame_time)

    second_time = time.time()
    elapsed_time = (second_time - first_time) * 1000
    WINDOW.blit(current_frame, (0,0))

    pygame.display.update()

pygame.quit()
sys.exit()
