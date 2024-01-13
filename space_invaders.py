import pygame
import sys

# writing game class
class Game:
    def __init__(self):
        pass

    def run(self):
        pass


# objective is to update sprites and display them on screen

# initializing pygame
if __name__ == "__main__":
    pygame.init()
    swidth, sheight = 500, 500
    screen = pygame.display.set_mode((swidth, sheight))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()
    game = Game()

    #Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0,0,0))
        game.run()

        pygame.display.flip()
        clock.tick(60)

        