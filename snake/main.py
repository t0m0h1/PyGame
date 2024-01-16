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


# Game loop
while not game_over:
   # Event handling    
    while game_close == True:
        screen.fill(black)
        game_over_message = message_font.render("Game Over!", True, red)
        screen.blit(game_over_message, [swidth / 3, sheight / 3])
        display_score(snake_block - 1)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_r:
                    run()
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False

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

    # Game logic
    # (Your game logic code goes here)

    # Drawing code
    screen.fill((0, 0, 0))  # Fill the screen with black color

    # Update the display
    pygame.display.flip()
    clock.tick(60)  # 60 frames per second

# Clean up Pygame
pygame.quit()
