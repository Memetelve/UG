import pygame
from pygame.locals import *

from paddle import Paddle
from ball import Ball
from block import Block
from variables import *

pygame.init()


def write_score(score):
    # write score to file
    with open("score.txt", "a+") as f:
        f.write(str(score) + "\n")

def calculate_paddle_deflection_angle(paddle_x, paddle_width, ball_x):
    # more maths? do i like it? no (or maybe?)
    deflect_angle = 100 - ((paddle_x + paddle_width) - ball_x - 10) - 50
    deflect_angle = max(deflect_angle, -50) / 35
    return round(deflect_angle, 2)

def create_block(row, col, margin):
    block = Block(ROW_COLORS[row])
    block.rect.x = margin + (col * (BLOCK_WIDTH + BLOCK_GAP))
    block.rect.y = (BLOCK_HEIGHT + BLOCK_GAP) * row + margin
    return block

def calculate_blocks_per_row():
    return (WINDOWWIDTH + BLOCK_GAP) // (BLOCK_WIDTH + (BLOCK_GAP))

def calculate_margin(blocks_per_row):
    return (WINDOWWIDTH + BLOCK_GAP) % (blocks_per_row * (BLOCK_WIDTH + BLOCK_GAP)) / 2

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
blocks_per_row = calculate_blocks_per_row()
margin = calculate_margin(blocks_per_row)

# init blocks
all_blocks = pygame.sprite.Group()
for row in range(BLOCK_ROWS):
    for col in range(blocks_per_row):
        block = create_block(row, col, margin)
        all_sprites.add(block)
        all_blocks.add(block)


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
        ball.reset_position()

    # prevent ball from being stuck in paddle/walls
    if ball.just_hit > 0:
        ball.just_hit -= 1
    # bounce off paddle if not just hit
    if pygame.sprite.collide_rect(ball, paddle) and ball.just_hit == 0:
        ball.reflect()
        ball.move_vector[0] = calculate_paddle_deflection_angle(paddle.rect.x, paddle.width, ball.rect.x)


    block_collision_list = pygame.sprite.spritecollide(ball, all_blocks, False)
    for block in block_collision_list:
        ball.reflect()
        block.kill()
        score += 1
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
    screen.fill(BLACK)

    # draw stats
    font = pygame.font.Font(None, 34)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 575))
    text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(text, (700, 575))

    # draw all sprites
    all_sprites.draw(screen)

    pygame.display.update()

    if lives == 0:
        break

    # tick
    clock.tick(60)

write_score(score)

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        return True

font = pygame.font.Font(None, 74)
text = font.render(f"Score: {score}", 1, WHITE)
screen.blit(text, (300, 300))
pygame.display.flip()

while True:
    if checkForKeyPress():
        pygame.quit()
