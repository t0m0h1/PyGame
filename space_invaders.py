import pygame
import sys
import pygame
import sys
from player import Player # importing player class from player.py
import obstacle # importing obstacle module


class Game:
    def __init__(self, screen):  # Add the 'screen' parameter
        self.screen = screen

        # player setup
        player_sprite = Player((screen.get_width() // 2, screen.get_height() - 8)) # creating player sprite position
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # obstacle setup
        self.shape = obstacle.shape # calling shape attribute from Block class
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_positions = [num * (self.screen.get_width() // (self.obstacle_amount + 1)) for num in range(1, self.obstacle_amount + 1)]
        self.create_multiple_obstacles(*self.obstacle.x_positions, x_start=screen.get_width() / 15, y_start=480) # calling create_obstacle method


    def create_obstacle(self):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == x:
                    x = col_index * self.block_size
                    y = row_index * self.block_size
                    block = obstacle.Block(self.block_size, (241, 79, 80), x, y)

    def create_multiple_obstacles(self, *offset, x_start, y_start):
        for x in offset:
            self.create_obstacle(x_start, y_start, offset_x=x)


    def run(self):
        self.player.update()
        self.player.draw(self.screen) # objective is to update sprites and display them on screen
        self.player.sprite.lasers.draw(self.screen) # objective is to male lasers visible on screen
        for laser in self.player.sprite.lasers:
            laser.rect.y -= 5
            if laser.rect.y <= 0:
                laser.kill()


# initialising pygame
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


from player import Player # importing player class from player.py
import obstacle # importing obstacle module


class Game:
    def __init__(self, screen):  # Add the 'screen' parameter
        self.screen = screen

        # player setup
        player_sprite = Player((screen.get_width() // 2, screen.get_height() - 8)) # creating player sprite position
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # obstacle setup
        self.shape = obstacle.shape # 
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_positions = [num * (self.screen.get_width() // (self.obstacle_amount + 1)) for num in range(1, self.obstacle_amount + 1)]
        self.create_multiple_obstacles(*self.obstacle.x_positions, x_start=screen.get_width() / 15, y_start=480) # calling create_obstacle method


    def create_obstacle(self, x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == x:
                    x = col_index * self.block_size
                    y = row_index * self.block_size
                    block = obstacle.Block(self.block_size, (241, 79, 80), x, y)
                    self.blocks.add(block)

    def create_multiple_obstacles(self, *offset, x_start, y_start):
        for x in offset:
            self.create_obstacle(x_start, y_start, offset_x=x)


    def run(self):
        self.player.update()
        self.player.draw(self.screen) # objective is to update sprites and display them on screen
        self.player.sprite.lasers.draw(self.screen) # objective is to male lasers visible on screen
        for laser in self.player.sprite.lasers:
            laser.rect.y -= 5
            if laser.rect.y <= 0:
                laser.kill()

        self.blocks.draw(self.screen)


# initialising pygame
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



