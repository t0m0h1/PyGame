import pygame
import sys
from player import Player # importing player class from player.py


class Game:
    def __init__(self, screen):  # Add the 'screen' parameter
        self.screen = screen
        player_sprite = Player((250, 430))
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.draw(self.screen) # objective is to update sprites and display them on screen



# initializing pygame
if __name__ == "__main__":
    pygame.init()
    swidth, sheight = 500, 500
    screen = pygame.display.set_mode((swidth, sheight))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()
    game = Game(screen=screen)

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



