import pygame
from pygame.locals import *

class Control:
    def __init__(self):
        self.play = True  # Переменная для остановки игрового цикла
        self.mouse_x = 0 #Позиция х курсора
        self.mouse_y = 0 #Позиция у курсора
        self.flag = "NORMAL" #Флаг для отрисовки кнопок
        self.speed_variable = 20 #Этой переменной регулируем скорость падения фигур

    def drop_shape(self):
        """Ускоряет падение фигуры"""
        self.speed_variable = 1

    def normal_speed(self):
        """Возвращает начальную скорость"""
        self.speed_variable = 20

    def control_game(self,shape):
        """Все управление игрой"""
        for event in pygame.event.get():

            if event.type == QUIT:
                self.play = False

            elif event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    self.play = False
                elif event.key == K_LEFT:
                   shape.direction = "Left"
                elif event.key == K_RIGHT:
                    shape.direction = "Right"
                elif event.key == K_UP:
                    shape.shape_form.rotate()
                elif event.key == K_DOWN:
                    self.drop_shape()

            elif event.type == KEYUP:

                if event.key == K_LEFT:
                    shape.direction = "Normal"
                elif event.key == K_RIGHT:
                    shape.direction = "Normal"
                elif event.key == K_DOWN:
                    self.normal_speed()

            elif event.type == MOUSEBUTTONDOWN:

                self.mouse_x,self.mouse_y = pygame.mouse.get_pos()
                self.flag = "CLICKED"

            elif event.type == MOUSEBUTTONUP:

                self.flag = "NORMAL"



