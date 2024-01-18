import pygame
import random

swidth, sheight = 600, 600
block_size = 20

pygame.font.init()
score_font = pygame.font.SysFont('Arial', 30)
score = 0

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

pygame.init()

screen = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

# Snake food and snake initial position
snake_pos = [[swidth/2, sheight/2]]
snake_speed = [0, block_size]

teleport = True

def generate_food():
# Generates the position of the snake's food.
    
# Returns:
# food_pos (list): The position of the food as a list [x, y].
    x = random.randint(0, (swidth - block_size) // block_size) * block_size
    y = random.randint(0, (sheight - block_size) // block_size) * block_size
    food_pos = [x, y]
    if food_pos in snake_pos:
        return food_pos


