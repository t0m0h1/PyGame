import pygame
import sys

# writing game class
class Game:
    def __init__(self):
        pass

    def run_game_loop(self):
        pass


# initializing pygame

pygame.init()
swidth, sheight = 500, 500
screen = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()

#Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))

    pygame.display.flip()
    clock.tick(60)