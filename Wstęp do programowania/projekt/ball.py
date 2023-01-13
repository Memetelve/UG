import pygame

from colors import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, color) -> None:
        super().__init__()

        self.image = pygame.Surface([radius*2, radius*2])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.circle(self.image, color, (radius, radius), radius)

        self.rect = self.image.get_rect()

        self.speed = 10
        self.direction = 1