import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("assets/player.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)

