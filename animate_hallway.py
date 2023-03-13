import sys
import pygame
from settings import *


def animate_hallway(WINDOW):

    # Load the PNG files
    frames = []
    for i in range(0, 7):
        filename = f"assets/hallway/hallway_{i}.png"
        frame = pygame.image.load(filename).convert_alpha()
        frames.append(frame)


    # Set up the animation parameters
    frame_duration = 500                        # milliseconds per frame
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
            if current_frame >= num_frames:
                running = False
                break

            time_since_last_frame = 0
        last_tick = pygame.time.get_ticks()             # Update last_tick variable

        WINDOW.blit(frames[current_frame], (0, 0))      # Draw the current frame
        pygame.display.update()
