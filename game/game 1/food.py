import random
import pygame

class Food():
    def __init__(self,color,screen_width,screen_height):
        self.color = color
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.food_position = [random.randrange(1,screen_width/10,10),random.randrange(1,screen_height/10,10)]

    def draw_food(self,window):
        """Отображение еды"""
        pygame.draw.rect(window,self.color,pygame.Rect(self.food_position[0],self.food_position[1],10,10))

    def moove(self):
        self.food_position[0] += 10
