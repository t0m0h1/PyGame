import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=(0, 0))


    

class Block:
    def __init__(self, block_size, color, x, y):
        super().__init__()
        self.block_size = block_size
        self.color = color
        self.x = x
        self.y = y

    def shape(self, x):
        # Define the shape based on the value of x
        if x == 1:
            return [[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]]
        elif x == 2:
            return [[2, 2, 2],
                    [2, 2, 2],
                    [2, 2, 2]]
        else:
            return [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
    
