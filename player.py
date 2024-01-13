import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("assets/player.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = 5

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.x <= 0:
                self.rect.x = 0

        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            if self.rect.x >= 450:
                self.rect.x = 450

    def update(self):
        self.get_input()

