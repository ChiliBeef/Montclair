import sys
import pygame
from settings import *


def computer_console_0(WINDOW):
    WINDOW.fill(BLACK)
    # Load the .png files used for animation sequence.
    frames = []
    for i in range(0, 8):
        filename = f"assets/computer/monitor_{i}.png"
        frame = pygame.image.load(filename)
        frames.append(frame)

    server_rack_icon = pygame.image.load("assets/computer/server_rack_icon.png")
    icon_width, icon_height = server_rack_icon.get_width(), server_rack_icon.get_height()
    icon_rect = pygame.Rect(80, 70, icon_width, icon_height)

    # Load computer startup sound file to be played.
    sound_effect = pygame.mixer.Sound("assets/sounds/computer_startup.wav")
    sound_effect.play()

    # Set up the animation parameters.
    frame_duration = 200                        # milliseconds per frame
    num_frames = len(frames)
    current_frame = 0
    time_since_last_frame = 0
    last_tick = pygame.time.get_ticks()         # Define last_tick variable


    # Animation loop
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        # Update the animation
        time_since_last_frame += pygame.time.get_ticks() - last_tick
        if time_since_last_frame >= frame_duration:
            current_frame += 1
            time_since_last_frame = 0
        last_tick = pygame.time.get_ticks()         # Update last_tick variable

        if current_frame < num_frames:
            WINDOW.blit(frames[current_frame], (0, 0))

        else:
            WINDOW.blit(server_rack_icon, (80, 70))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if icon_rect.collidepoint(event.pos):
                    print("You clicked on the icon!")
                    computer_console_0(WINDOW)
                    icon_rect.topleft = (-100, -100)

        pygame.display.update()
