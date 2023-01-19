import pygame
import math

from pygame.locals import *

from paddle import Paddle
from ball import Ball
from block import Block
from variables import *

pygame.init()


def write_score(score):
    # write score to file
    with open("score.txt", "w") as f:
        f.write(str(score) + "\n")


# game stats
score = 0
lives = 3

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

# init ball
ball = Ball(WHITE)

# add paddle to sprite group
all_sprites.add(paddle)
all_sprites.add(ball)

# MATHS (aaaaaaaa)
# calculate brics per row
blocks_per_row = (WINDOWWIDTH + BLOCK_GAP) // (BLOCK_WIDTH + (BLOCK_GAP))
# calculate left (and right) margin
margin = (WINDOWWIDTH + BLOCK_GAP) % (blocks_per_row * (BLOCK_WIDTH + BLOCK_GAP)) / 2

# init blocks
all_blocks = pygame.sprite.Group()

for row in range(BLOCK_ROWS):
    for col in range(blocks_per_row):
        brick = Block(ROW_COLORS[row])
        brick.rect.x = margin + (col * (BLOCK_WIDTH + BLOCK_GAP))
        brick.rect.y = (BLOCK_HEIGHT + BLOCK_GAP) * row + margin
        all_sprites.add(brick)
        all_blocks.add(brick)


# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # ball logic
    ball.move()

    if ball.rect.y > WINDOWHEIGHT:
        lives -= 1
        if lives == 0:
            break
        else:
            ball.rect.x = 400 - 10
            ball.rect.y = 300
            ball.move_vector = [0, 1]
            ball.speed = 5
            ball.just_hit = 0

    # i don't even know
    if ball.just_hit > 0:
        ball.just_hit -= 1
    # bounce off paddle if not just hit
    if pygame.sprite.collide_rect(ball, paddle) and ball.just_hit == 0:
        ball.reflect()

        # more maths? do i like it? no (or maybe?)
        deflect_angle = 100 - ((paddle.rect.x + paddle.width) - ball.rect.x - 10) - 50
        deflect_angle = max(deflect_angle, -50) / 35
        print(deflect_angle)
        ball.move_vector[0] = round(deflect_angle, 3)

    brick_collision_list = pygame.sprite.spritecollide(ball, all_blocks, False)
    for brick in brick_collision_list:
        ball.reflect()
        score += 1
        brick.kill()

        ball.speed += 0.1

        if len(all_blocks) == 0:
            break

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

    # draw stats
    font = pygame.font.Font(None, 34)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 575))
    text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(text, (700, 575))

    # draw all sprites
    all_sprites.draw(screen)

    pygame.display.update()

    # tick
    clock.tick(60)

write_score(score)


def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        return True


while True:
    font = pygame.font.Font(None, 74)
    text = font.render(f"Score: {score}", 1, WHITE)
    screen.blit(text, (200, 300))
    pygame.display.flip()

    while True:
        if checkForKeyPress():
            pygame.quit()
