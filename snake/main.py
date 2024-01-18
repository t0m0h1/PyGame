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

teleport = False
# teleport = False means that the snake will die if it hits the wall

def generate_food():
# Generates the position of the snake's food.
    
# We want the food to be at a random position within the screen, but not where the snake currently is.
    x = random.randint(0, (swidth - block_size) // block_size) * block_size
    y = random.randint(0, (sheight - block_size) // block_size) * block_size
    food_pos = [x, y]
    if food_pos not in snake_pos:
        return food_pos



food_pos = generate_food()

def draw_objects():
    screen.fill(black)
    for pos in snake_pos:
        pygame.draw.rect(screen, white, (pos[0], pos[1], block_size, block_size))
    pygame.draw.rect(screen, red, (food_pos[0], food_pos[1], block_size, block_size))
    score_text = score_font.render(f'Score: {score}', True, white)
    screen.blit(score_text, (10, 10))


def move_snake():
    global food_pos, score
    new_head = [snake_pos[0][0] + snake_speed[0], snake_pos[0][1] + snake_speed[1]]

    if teleport:
        if new_head[0] < 0:
            new_head[0] = swidth - block_size
        elif new_head[0] >= swidth:
            new_head[0] = 0
        if new_head[1] < 0:
            new_head[1] = sheight - block_size
        elif new_head[1] >= sheight:
            new_head[1] = 0

    if new_head in snake_pos[1:]:
        game_over_screen()  # Game should end when the snake hits itself
        return
    else:
        snake_pos.insert(0, new_head)  # Insert the new head of the snake

    if new_head == food_pos:  # Snake eats the food
        food_pos = generate_food()
        score += 1
    else:
        snake_pos.pop()  # Remove the tail of the snake if it doesn't eat food


# game over condition
    
def game_over():
    if teleport:
        return False
    else:
        return snake_pos[0][0] < 0 or snake_pos[0][0] >= swidth or snake_pos[0][1] < 0 or snake_pos[0][1] >= sheight or snake_pos[0] in snake_pos[1:]
    

def game_over_screen():
    screen.fill(black)
    game_over_text = score_font.render('Game Over', True, white)
    screen.blit(game_over_text, (swidth/2 - game_over_text.get_width()/2, sheight/2 - game_over_text.get_height()/2))
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    run()
                    return
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                    return
        



# main game loop
def run():
    global snake_speed, snake_pos, food_pos, score, teleport
    snake_pos = [[swidth/2, sheight/2]]
    snake_speed = [block_size, 0]
    food_pos = generate_food()
    score = 0
    teleport = False
    running = True
    while running:
        pygame.event.pump()  # Allow event handling to continue

        clock.tick(10)  # Control the game speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:  # Handle key presses
                if event.key == pygame.K_UP and snake_speed[1] != block_size:
                    snake_speed = [0, -block_size]
                elif event.key == pygame.K_DOWN and snake_speed[1] != -block_size:
                    snake_speed = [0, block_size]
                elif event.key == pygame.K_LEFT and snake_speed[0] != block_size:
                    snake_speed = [-block_size, 0]
                elif event.key == pygame.K_RIGHT and snake_speed[0] != -block_size:
                    snake_speed = [block_size, 0]

        move_snake()

        if game_over():
            game_over_screen()
            return

        screen.fill(black)  # Clear the screen

        draw_objects()  # Draw the game objects

        pygame.display.update()  # Update the display

    pygame.quit()  # Quit the game


# Run the game
if __name__ == '__main__':
    run()