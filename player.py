import pygame
from pygame.sprite import Sprite
from laser import Laser


class Player(Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("assets/player.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = 5
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 500

        self.lasers = pygame.sprite.Group()

    

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

        elif keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True

    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center))

    def update(self):
        self.get_input()
        self.recharge()




