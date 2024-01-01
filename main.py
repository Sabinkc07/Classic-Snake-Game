import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game - Designed by Sabin KC")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake initial position and size
snake_block_size = 20
snake_speed = 15
snake_x = screen_width // 2
snake_y = screen_height // 2
snake_x_change = 0
snake_y_change = 0
snake_length = 1
snake_body = []

# Food position
food_x = round(random.randrange(0, screen_width - snake_block_size) / 20.0) * 20.0
food_y = round(random.randrange(0, screen_height - snake_block_size) / 20.0) * 20.0

# Score
score = 0

# Game over flag
game_over = False

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_block_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_block_size
                snake_x_change = 0

    # Update snake position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check if snake crosses the screen boundaries
    if snake_x >= screen_width:
        snake_x = 0
    elif snake_x < 0:
        snake_x = screen_width - snake_block_size
    if snake_y >= screen_height:
        snake_y = 0
    elif snake_y < 0:
        snake_y = screen_height - snake_block_size

    # Clear the game window
    game_window.fill(black)

    # Draw the snake
    snake_head = [snake_x, snake_y]
    snake_body.append(snake_head)
    if len(snake_body) > snake_length:
        del snake_body[0]

    for part in snake_body:
        pygame.draw.rect(game_window, green, [part[0], part[1], snake_block_size, snake_block_size])

    # Draw the food
    pygame.draw.rect(game_window, red, [food_x, food_y, snake_block_size, snake_block_size])

    # Check if snake eats the food
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, screen_width - snake_block_size) / 20.0) * 20.0
        food_y = round(random.randrange(0, screen_height - snake_block_size) / 20.0) * 20.0
        snake_length += 1
        score += 1

    # Display the score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, white)
    game_window.blit(text, (10, 10))

    # Update the game window
    pygame.display.update()

    # Set the game speed
    clock = pygame.time.Clock()
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
