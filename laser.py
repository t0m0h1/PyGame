import pygame

light_yellow = (255, 255, 102)

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((3, 15))
        self.image.fill(light_yellow)
        self.rect = self.image.get_rect(center=pos)


