import pygame
import time
import random

pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake properties
snake_block = 10
snake_speed = 15

# Snake body
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(WIN, GREEN, [x[0], x[1], snake_block, snake_block])

def gameLoop():
    game_over = False
    game_close = False

    x1, y1 = WIDTH // 2, HEIGHT // 2
    x1_change, y1_change = 0, 0

    snake_List = []
    Length_of_snake = 1

    # Random position for food
    foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            WIN.fill(WHITE)
            font_style = pygame.font.SysFont(None, 50)
            message = font_style.render("You Lost! Press 'Q'-Quit or 'C'-Play Again", True, RED)
            WIN.blit(message, [WIDTH // 6, HEIGHT // 3])
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

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        WIN.fill(WHITE)
        pygame.draw.rect(WIN, RED, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake(snake_block, snake_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # Adjust the speed of the snake
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
