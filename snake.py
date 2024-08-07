import pygame
import time
import random

# Initialize the game
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Cute Snake Game')

# Colors
black = (0, 0, 0)
light_brown = (222, 184, 135)
red = (213, 50, 80)
green = (0, 255, 0)
dark_green = (34, 139, 34)

# Snake block size and speed
snake_block = 20
snake_head_block = 25
snake_speed = 10

# Game clock
clock = pygame.time.Clock()

# Font style
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Display score at the end
def display_final_score(score):
    value = score_font.render("Your Final Score: " + str(score), True, black)
    text_rect = value.get_rect(center=(width / 2, height / 2))
    window.blit(value, text_rect)

# Draw the snake
def draw_snake(snake_block, snake_head_block, snake_list):
    for i, x in enumerate(snake_list):
        if i == len(snake_list) - 1:
            pygame.draw.rect(window, dark_green, [x[0], x[1], snake_head_block, snake_head_block])
        else:
            pygame.draw.rect(window, green, [x[0], x[1], snake_block, snake_block])

# Display message
def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    text_rect = mesg.get_rect(center=(width / 2, height / 3))
    window.blit(mesg, text_rect)

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Food coordinates
    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    while not game_over:

        while game_close:
            window.fill(light_brown)
            display_message("You Lost! Press Q-Quit or C-Play Again", black)
            display_final_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(light_brown)
        pygame.draw.rect(window, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block, snake_head_block, snake_list)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
gameLoop()


