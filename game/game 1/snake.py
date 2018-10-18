import pygame

class Snake():
    def __init__(self,color):
        self.color = color
        self.body = [[100,50],[90,50],[80,50]]

    def draw_snake(self,window,window_color):
        """Рисует сегменты змеи"""
        window.fill(window_color)
        for segment in self.body:
            pygame.draw.rect(window,self.color,pygame.Rect(segment[0],segment[1],10,10))