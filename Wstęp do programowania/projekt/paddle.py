import pygame

from colors import *

class Paddle(pygame.sprite.Sprite):

    def __init__(self, width, height, color) -> None:
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def move_left(self):
        self.rect.x -= 10

        # stop at the left side of the screen
        # self.rect.x = max(self.rect.x, 0)
        if self.rect.x < -50:
            self.rect.x = 750

    def move_right(self):
        self.rect.x += 10

        # stop at the right side of the screen
        # self.rect.x = min(self.rect.x, 700)
        if self.rect.x > 750:
            self.rect.x = -50