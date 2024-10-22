import pygame
import time
import random

pygame.init()

# Window dimensions
width = 800
height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake block size
block_size = 20
snake_speed = 15

# Font
font_style = pygame.font.SysFont("bahnschrift", 25)

# Initialize the window
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Snake direction
direction = "RIGHT"

# Score
score = 0

# Function to draw the snake
def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, black, [x[0], x[1], block_size, block_size])

# Function to display message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [width / 6, height / 3])

# Main function
def game_loop():
    global direction
    global score

    game_over = False
    game_close = False

    # Starting position of the snake
    lead_x = width / 2
    lead_y = height / 2

    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    snake_length = 1

    # Initial position of the food
    food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close == True:
            game_display.fill(white)
            message("You lost! Press Q-Quit or C-Play Again", red)
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
                    direction = "LEFT"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "RIGHT"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "UP"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "DOWN"
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= width or lead_x < 0 or lead_y >= height or lead_y < 0:
            game_close = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        game_display.fill(blue)
        pygame.draw.rect(game_display, green, [food_x, food_y, block_size, block_size])

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        pygame.display.update()

        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            snake_length += 1
            score += 10

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
