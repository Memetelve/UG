import pygame
import random

from variables import *


class Ball(pygame.sprite.Sprite):
    def __init__(self, color) -> None:
        super().__init__()

        self.image = pygame.Surface([10 * 2, 10 * 2])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.circle(self.image, color, (10, 10), 10)

        self.rect = self.image.get_rect()
        self.rect.x = WINDOWWIDTH / 2 - 10
        self.rect.y = WINDOWHEIGHT / 2 - 10

        self.move_vector = [0, 1]
        self.speed = BALL_SPEED

        # to avoid ball getting stuck in the paddle
        self.just_hit = 0

    def move(self):
        self.rect.x += self.move_vector[0] * self.speed
        self.rect.y += self.move_vector[1] * self.speed

        if self.rect.x < 0 or self.rect.x > WINDOWWIDTH - 20:
            self.move_vector[0] *= -1
        if self.rect.y < 0:
            self.move_vector[1] *= -1

    def reflect(self):
        if self.just_hit == 0:
            self.move_vector[1] *= -1
            self.just_hit = 10

    def reset_position(self):
        self.rect.x = WINDOWWIDTH / 2 - 10
        self.rect.y = WINDOWHEIGHT / 2 - 10
        self.move_vector = [0, 1]
        self.just_hit = 0
