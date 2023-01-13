import pygame

from paddle import Paddle
from colors import *

pygame.init()


# screen
WINDOWWIDTH = 800
WINDOWHEIGHT = 600

# game stats
score = 0
lives = 1

# init screen
font = pygame.font.SysFont(None, 14)
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

# init clock
clock = pygame.time.Clock()

# init sprites
all_sprites = pygame.sprite.Group()

# init paddle
paddle = Paddle(100, 10, WHITE)
paddle.rect.x = 350
paddle.rect.y = 560

# add paddle to sprite group
all_sprites.add(paddle)

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move_left()
    if keys[pygame.K_RIGHT]:
        paddle.move_right()

    # update sprites
    all_sprites.update()

    # draw background
    screen.fill(GREY)

    font = pygame.font.Font(None, 34)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10,575))
    text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(text, (700,575))

    # draw all sprites
    all_sprites.draw(screen)

    pygame.display.update()

    # tick
    clock.tick(60)
