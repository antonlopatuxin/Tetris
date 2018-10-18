import pygame
import random

class Food():
    def __init__(self,color):
        self.color = color #Цвет квадрата еды
        self.food_position = [] #Список с текущей позицией еды

    def get_food_positon(self,gui):
        """Выдает рандомные позиции для еды"""
        self.food_position = list(random.choice(gui.field))

    def draw_food(self,window):
        """Рисуем еду на основе рандомных координат"""
        pygame.draw.rect(window,self.color,pygame.Rect(self.food_position[0],self.food_position[1],10,10))