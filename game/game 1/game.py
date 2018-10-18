import sys
import pygame
from food import Food
from color import Color
from snake import Snake

def run_game():
    pygame.init()
    screen_width = 800
    screen_height = 600
    window = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Змейка")
    my_color = Color()
    food = Food(my_color.red,screen_width,screen_height)
    snake = Snake(my_color.green)
    print(food.food_position)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        snake.draw_snake(window,my_color.black)
        food.draw_food(window)


        pygame.display.flip()  # Отображение последнего отрисованного экрана

run_game()
