import pygame
import sys

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


def calculate_paddle_deflection_angle(
    paddle_x, ball_x, paddle_width=PADDLE_WIDTH
) -> float:
    # more maths? do i like it? no (or maybe?)

    # paddle center
    paddle_center = paddle_x + paddle_width / 2
    # ball center
    ball_center = ball_x + 10

    angle = (ball_center - paddle_center) / 40
    print(angle)

    return angle


def create_block(row, col, margin):
    block = Block(ROW_COLORS[row])
    block.rect.x = margin + (col * (BLOCK_WIDTH + BLOCK_GAP))
    block.rect.y = (BLOCK_HEIGHT + BLOCK_GAP) * row + margin
    return block


def calculate_blocks_per_row(
    window_width=WINDOWWIDTH, block_gap=BLOCK_GAP, block_width=BLOCK_WIDTH
) -> int:
    return (window_width + block_gap) // (block_width + block_gap)


def calculate_margin(
    blocks_per_row,
    window_width=WINDOWWIDTH,
    block_gap=BLOCK_GAP,
    block_width=BLOCK_WIDTH,
) -> int:
    return int(
        (window_width + block_gap) % (blocks_per_row * (block_width + block_gap)) / 2
    )


def terminate():
    pygame.quit()
    sys.exit()


def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def drawPressKeyMsg(screen, font):
    pressKeySurf = font.render("Press a key to play.", True, WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.midtop = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
    screen.blit(pressKeySurf, pressKeyRect)


def show_score_screen(screen, score, won):

    if won:
        text = "You won!"
    else:
        text = "Game Over"

    text_score = f"Score: {str(score)}"

    gameOverFont = pygame.font.Font("freesansbold.ttf", 70)
    gameSurf = gameOverFont.render(text, True, WHITE)
    overSurf = gameOverFont.render(text_score, True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    screen.blit(gameSurf, gameRect)
    screen.blit(overSurf, overRect)
    drawPressKeyMsg(screen, gameOverFont)
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress()  # clear out any key presses in the event queue

    while True:
        if checkForKeyPress():
            pygame.event.get()  # clear event queue
            return


def place_blocks():
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

    return all_blocks


def game_loop(ball, paddle, all_sprites, score=0, lives=3):
    all_blocks = place_blocks()

    print(len(all_blocks))

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
            ball.move_vector[0] = calculate_paddle_deflection_angle(
                paddle.rect.x, ball.rect.x
            )

        block_collision_list = pygame.sprite.spritecollide(ball, all_blocks, False)
        for block in block_collision_list:
            ball.reflect()
            block.kill()
            score += 1
            ball.speed += 0.2

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

        if lives == 0 or len(all_blocks) == 0:

            for block in all_blocks:
                block.kill()

            return score, lives

        # draw all sprites
        all_sprites.draw(screen)

        pygame.display.update()

        # tick
        clock.tick(60)


if __name__ == "__main__":
    # init screen
    font = pygame.font.SysFont(None, 14)
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    # init clock
    clock = pygame.time.Clock()

    # init sprites
    all_sprites = pygame.sprite.Group()

    # init paddle
    paddle = Paddle(10, WHITE)
    paddle.rect.x = 350
    paddle.rect.y = 560

    # init ball
    ball = Ball(WHITE)

    # add paddle to sprite group
    all_sprites.add(paddle)
    all_sprites.add(ball)

    # set initial stats
    score = 0
    lives = 3

    while True:

        score, lives = game_loop(ball, paddle, all_sprites, score, lives)
        write_score(score)

        won = lives != 0

        ball.reset_position()
        show_score_screen(screen, score, won)

        if not won:
            # reset ball speed
            ball.speed = BALL_SPEED

            score = 0
            lives = 3
