import pygame
from snake import Snake
from color import Color
from food import Food
from  gui import GUI

screen_width = 441
screen_height = 441
clock = pygame.time.Clock()

def main():
    pygame.init() #Инициализируем pygame
    window = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Змейка")
    color = Color()
    gui = GUI()
    gui.init_field()
    snake = Snake(color.green)
    food = Food(color.red)
    food.get_food_positon(gui)
    var = 0 #Переменная для изменеия скорости змеи

    while True:
        var += 1
        snake.route = snake.control(snake.route)
        window.fill(color.black)
        food.draw_food(window)
        snake.draw_snake(window)
        gui.draw_interface(window,color.green,snake)
        gui.draw_level(window,color.grey)
        if var % snake.speed == 0:
            snake.move(gui.indicator)
            snake.pick(food, gui)
        pygame.display.flip()
        clock.tick(60) # Данный метод задает сколько раз в секунду будет прогонятся цикл
main()