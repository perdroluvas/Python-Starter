
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_COLOR = (0, 0, 0)
WINDOW_TITLE = 'Pong'
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

# Set up the ball
BALL_SIZE = 10
BALL_COLOR = (255, 255, 255)
BALL_SPEED = 3
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2
ball_dx = BALL_SPEED
ball_dy = BALL_SPEED

# Set up the paddles
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 80
PADDLE_COLOR = (255, 255, 255)
PADDLE_SPEED = 5
paddle_a_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle_b_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_a_y > 0:
        paddle_a_y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle_a_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        paddle_a_y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle_b_y > 0:
        paddle_b_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle_b_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        paddle_b_y += PADDLE_SPEED

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Border checking
    if ball_y > WINDOW_HEIGHT - BALL_SIZE or ball_y < 0:
        ball_dy *= -1
    if ball_x > WINDOW_WIDTH - BALL_SIZE or ball_x < 0:
        ball_dx *= -1

    # Paddle and ball collisions
    if ball_y < paddle_a_y + PADDLE_HEIGHT and ball_y + BALL_SIZE > paddle_a_y and ball_x > WINDOW_WIDTH // 2:
        ball_dx *= -1
    if ball_y + BALL_SIZE > paddle_b_y + PADDLE_HEIGHT and ball_y < paddle_b_y and ball_x < WINDOW_WIDTH // 2:
        ball_dx *= -1

    # Draw everything
    window.fill(WINDOW_COLOR)
    pygame.draw.rect(window, PADDLE_COLOR, (WINDOW_WIDTH // 2, paddle_a_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(window, PADDLE_COLOR, (WINDOW_WIDTH // 2 - PADDLE_WIDTH, paddle_b_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(window, BALL_COLOR, (ball_x, ball_y), BALL_SIZE)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
