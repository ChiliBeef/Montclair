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


# Load title screen background image and glitch vfx files to be played.
glitch1 = pygame.image.load("assets/computer/server_cabinets_glitch1.png")
glitch2 = pygame.image.load("assets/computer/server_cabinets_glitch2.png")

# Load title screen background sound and glitch sfx file to be played.
bg_sound = pygame.mixer.Sound("assets/sounds/title_screen.wav")
glitch_sound = pygame.mixer.Sound("assets/sounds/glitch_sfx.wav")
bg_sound.play(-1)

# Set up animation sequence of background image and glitch vfx.
current_frame_index = 0
animation_frames = {0 : [glitch1, 2000, None], 1 : [glitch2, 100, glitch_sound] , 2 : [glitch1, 1500, None] , 3 :  [glitch2, 100, glitch_sound] }
current_frame = animation_frames[current_frame_index][0]
frame_time = animation_frames[current_frame_index][1]
first_time = time.time()
flip_frame = pygame.event.custom_type()
pygame.time.set_timer(flip_frame, frame_time)




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

            if animation_frames[current_frame_index][2] is not None:
                sound_2_play = animation_frames[current_frame_index][2]
                sound_2_play.play()
                print("change")

            pygame.time.set_timer(flip_frame, frame_time)


    second_time = time.time()
    elapsed_time = (second_time - first_time) * 1000
    WINDOW.blit(current_frame, (0,0))

    pygame.display.update()

pygame.quit()
sys.exit()
