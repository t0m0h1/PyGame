import pygame
import sys

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