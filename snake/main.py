import pygame
import time
import random


# Initialize Pygame
pygame.init()

# variables and setup
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 165, 0)

swidth, sheight = 800, 600
screen = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

message_font = pygame.font.SysFont("ubuntu", 35)
game_font = pygame.font.SysFont("comicsansms", 35)

# function to display score
def display_score(score):
    value = game_font.render("Your Score: " + str(score), True, orange)
    screen.blit(value, [0, 0])

# function to display snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

def run():
    game_over = False
    game_close = False

    # initial position of snake
    x, y = swidth / 2, sheight / 2

    # initial velocity of snake
    x_change, y_change = 0, 0

    # snake body
    snake_pixels = []
    snake_length = 1

    # food position
    food_x = round(random.randrange(0, swidth - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, sheight - snake_block) / 10.0) * 10.0

    while not game_over:
        # game over screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # snake movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_block

        if x >= swidth or x < 0 or y >= sheight or y < 0:
            game_close = True

        x += x_change
        y += y_change

        screen.fill(black)
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])
        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True

        draw_snake(snake_block, snake_pixels)
        display_score(snake_length - 1)

        pygame.display.update()
        clock.tick(60)


pygame.quit()

