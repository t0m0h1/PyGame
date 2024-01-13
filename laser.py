import pygame

yellow = (255, 255, 0)

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(yellow)
        self.rect = self.image.get_rect(centre = pos)

    def move(self):
        self.rect.y -= 5