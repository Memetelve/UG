import pygame

from variables import *


class Block(pygame.sprite.Sprite):
    def __init__(self, color) -> None:
        super().__init__()

        self.image = pygame.Surface([BLOCK_WIDTH, BLOCK_HEIGHT])
        self.image.fill(color)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, BLOCK_WIDTH, BLOCK_HEIGHT])

        self.rect = self.image.get_rect()
