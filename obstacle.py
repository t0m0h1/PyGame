import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=(0, 0))

class Block(pygame.sprite.Sprite):
    def __init__(self, size, color, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        pass

    def shape(self):
        return [
            ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
            ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
        ]
    
