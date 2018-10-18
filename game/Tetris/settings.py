import pygame

class Settings:
    def __init__(self):

        self.window_size = [800,800] #Размер экрана
        self.caption_window = "Тетрис" #Название окна
        self.icon_window = pygame.image.load("images/icon.jpg") #Иконка окна
        """Различные цвета"""
        self.red = pygame.Color(255, 0, 0) #Красный
        self.green = pygame.Color(0, 255, 0) #Зеленый
        self.black = pygame.Color(0, 0, 0) #Черный
        self.white = pygame.Color(255, 255, 255) #Белый
        self.dark_green = pygame.Color(0, 100, 0) #Темнозеленый
        self.grey = pygame.Color(128, 128, 128) #Серый
        self.FPS = 60 #Частота кадров
        self.speed = 25 #Скорость падения фигуры
        self.var = 0 #Переменная для регулировки скорости
        self.play_game = False  # Флаг для реализации паузы и кнопки играть
