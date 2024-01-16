import pygame
import time
import random


# Initialize Pygame
pygame.init()

# Set up the display
swidth, sheight = 800, 600
screen = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption("Snake Game")

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic

    # Drawing code
    screen.fill((0, 0, 0))  # Fill the screen with black color

    # Update the display
    pygame.display.flip()

# Clean up Pygame
pygame.quit()

