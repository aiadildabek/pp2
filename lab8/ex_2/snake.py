# Extend example project from lecture and add the following functionality:
# 
# Checking for border (wall) collision and whether the snake is leaving the playing area
# Generate random position for food, so that it does not fall on a wall or a snake
# Add levels. For example, when the snake receives 3-4 foods or depending on score 
# Increase speed when the user passes to the next level
# Add counter to score and level
# Comment your code

import pygame
import sys
from random import randrange


WINDOW = 500
TILE_SIZE = 25
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]

snake = pygame.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)

food = snake.copy()
food.center = get_random_position()

wall = snake.copy()
wall.center = get_random_position()

time, time_step = 0, 110
screen = pygame.display.set_mode([WINDOW] * 2)
clock = pygame.time.Clock()

dirs = {
    pygame.K_w: 1,
    pygame.K_s: 1,
    pygame.K_d: 1,
    pygame.K_a: 1
}

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and dirs[pygame.K_w]:
                snake_dir = (0, -TILE_SIZE)
                dirs = {
                    pygame.K_w: 1,
                    pygame.K_s: 0,
                    pygame.K_d: 1,
                    pygame.K_a: 1
                }
            if event.key == pygame.K_s and dirs[pygame.K_s]:
                snake_dir = (0, TILE_SIZE)
                dirs = {
                    pygame.K_w: 0,
                    pygame.K_s: 1,
                    pygame.K_d: 1,
                    pygame.K_a: 1
                }
            if event.key == pygame.K_a and dirs[pygame.K_a]:
                snake_dir = (-TILE_SIZE, 0)
                dirs = {
                    pygame.K_w: 1,
                    pygame.K_s: 1,
                    pygame.K_d: 0,
                    pygame.K_a: 1
                }
            if event.key == pygame.K_d and dirs[pygame.K_d]:
                snake_dir = (TILE_SIZE, 0)
                dirs = {
                    pygame.K_w: 1,
                    pygame.K_s: 1,
                    pygame.K_d: 1,
                    pygame.K_a: 0
                }
    
    screen.fill('black')

    if length % 3 == 0:
        time_step = max(60, time_step - 10)

    self_eating = pygame.Rect.collidelist(snake, segments[-2::-1]) != -1
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating or snake.center == wall.center:
        snake.center, food.center, wall.center = get_random_position(), get_random_position(), get_random_position()
        length, snake_dir = 1, (0, 0)
        segments = [snake.copy()]

    if snake.center == food.center:
        food.center = get_random_position()
        length += 1


    pygame.draw.rect(screen, 'red', food)

    pygame.draw.rect(screen, 'white', wall)

    [pygame.draw.rect(screen, 'green', segment) for segment in segments]

    time_now = pygame.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]

    pygame.display.flip()
    clock.tick(60)