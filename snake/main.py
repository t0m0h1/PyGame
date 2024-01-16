import pygame
import time
import random


# Initialize Pygame
pygame.init()

# variables and setup
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 165, 0)

swidth, sheight = 800, 600
screen = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
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
    clock.tick(60)  # 60 frames per second

     

# Clean up Pygame
pygame.quit()

