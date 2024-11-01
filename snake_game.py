import pygame
import time
import random

pygame.init()

# Define the colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Set display width and height
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Set snake properties
BLOCK_SIZE = 10
SNAKE_SPEED = 7

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game by Samyuktha')

# Create a clock object to control the speed of the game
clock = pygame.time.Clock()

# Set font for the game
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Display the player's score
def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, YELLOW)
    screen.blit(value, [0, 0])

# Draw the snake on the screen
def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], block_size, block_size])

# Display a message (used for Game Over messages)
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Snake starting position
    x_pos = SCREEN_WIDTH / 2
    y_pos = SCREEN_HEIGHT / 2
    x_change = BLOCK_SIZE
    y_change = 0

    # Snake body
    snake_list = []
    snake_length = 1

    # Food position
    food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0

    while not game_over:
        
        while game_close:
            screen.fill(BLUE)
            message("Game Over! Press Q-Quit or C-Play Again", RED)
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK_SIZE
                    x_change = 0

        if x_pos >= SCREEN_WIDTH or x_pos < 0 or y_pos >= SCREEN_HEIGHT or y_pos < 0:
            game_close = True
        x_pos += x_change
        y_pos += y_change
        screen.fill(BLACK)
        
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = [x_pos, y_pos]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collision with the snake itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_list)
        display_score(snake_length - 1)

        pygame.display.update()

        # Check if the snake has eaten the food
        if x_pos == food_x and y_pos == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

# Run the game
game_loop()
