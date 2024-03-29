import pygame

from variables import *


class Paddle(pygame.sprite.Sprite):
    def __init__(self, height, color) -> None:
        super().__init__()

        self.width = PADDLE_WIDTH

        self.image = pygame.Surface([self.width, height])
        self.image.fill(color)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, self.width, height])

        self.rect = self.image.get_rect()

    def move_left(self):
        self.rect.x -= 10

        if self.rect.x < -50:
            self.rect.x = WINDOWWIDTH - 50

    def move_right(self):
        self.rect.x += 10

        if self.rect.x > WINDOWWIDTH - 50:
            self.rect.x = -50
