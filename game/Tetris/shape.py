import pygame
import random

class Shape:
    def __init__(self):
        """Загружаем блоки фигур разного цвета и записываем их для удобства в список"""

        self.color_blue = pygame.image.load("images/bluebrick.png")
        self.color_green = pygame.image.load("images/greenbrick.png")
        self.color_red = pygame.image.load("images/redbrick.png")
        self.color_yellow = pygame.image.load("images/yellowbrick.png")
        self.color_teal = pygame.image.load("images/tealbrick.png")
        self.color_orange = pygame.image.load("images/orangebrick.png")
        self.color_purple = pygame.image.load("images/purplebrick.png")
        self.color = [self.color_blue,self.color_green,self.color_orange,self.color_purple,self.color_red,
                      self.color_teal,self.color_yellow]
        self.shape_list = ["Shape_T","Shape_Cube","Shape_L","Shape_S","Shape_Band"] #Данный список нужен для получения рандомной фигуры
        self.shape_name = None #Форма фигуры из списка выше
        self.next_shape = None #Следующая фигура
        self.next_color = None
        self.x = 250
        self.y = 25
        self.shape_form = None #Форма фигуры
        self.direction = None #Нарпавление фигуры
        self.shape_color = None #Цвет фигуры

    def get_color(self):
        """Выдает сегмент фигуры случайного цвета"""
        return random.choice(self.color)

    def get_shape_form(self):
        """Выдает из списка рандомную форму фигуры"""
        return random.choice(self.shape_list)

    def get_shape(self):
        """Выдает из списка рандомное значение для определения фигуры"""

        name = self.shape_name
        if name == "Shape_T":
            shape = Shape_T()
        elif name == "Shape_Cube":
            shape = Shape_Cube()
        elif name == "Shape_L":
            shape = Shape_L()
        elif name == "Shape_S":
            shape = Shape_S()
        elif name == "Shape_Band":
            shape = Shape_Band()
        return shape

    def shape_moove(self,settings,physics):
        """Движение фигуры"""
        if physics.bottom == "Move":
            self.shape_form.list_coordinate[0][1] += settings.speed
            self.shape_form.list_coordinate[1][1] += settings.speed
            self.shape_form.list_coordinate[2][1] += settings.speed
            self.shape_form.list_coordinate[3][1] += settings.speed

    def shape_control(self):
        """Метод управления фигурой с помощью флага,который мы получаем при нажатии клавиш"""
        if self.direction == "Left":
            if (self.shape_form.list_coordinate[0][0] > 25 and self.shape_form.list_coordinate[1][0] > 25 and
                self.shape_form.list_coordinate[2][0] > 25 and self.shape_form.list_coordinate[3][0] > 25):

                self.shape_form.list_coordinate[0][0] -= 25
                self.shape_form.list_coordinate[1][0] -= 25
                self.shape_form.list_coordinate[2][0] -= 25
                self.shape_form.list_coordinate[3][0] -= 25
        elif self.direction == "Right":
            if (self.shape_form.list_coordinate[0][0] < 450 and self.shape_form.list_coordinate[1][0] < 450 and
                self.shape_form.list_coordinate[2][0] < 450 and self.shape_form.list_coordinate[3][0] < 450):

                self.shape_form.list_coordinate[0][0] += 25
                self.shape_form.list_coordinate[1][0] += 25
                self.shape_form.list_coordinate[2][0] += 25
                self.shape_form.list_coordinate[3][0] += 25

    def draw_shape(self,brick,screen):
        """Рисует фигуру на экране"""
        for brick_coord in self.shape_form.list_coordinate:
            screen.blit(brick,(brick_coord[0],brick_coord[1]))

class Shape_T(Shape):
    def __init__(self):
        super().__init__()
        self.list_coordinate = [[self.x,self.y],[self.x - 25,self.y - 25],[self.x,self.y - 50],[self.x,self.y - 25]]
        self.position = "Left" #Положение фигуры,то есть вертикально влево стоит или горизонтально
        self.rotate_resolution = True #Это флаг с помощью которого мы отслеживаем положение фигуры и разрешаем поворот

    def check_rotate_resolution(self):
        """Проверяет можно ли повернуть фигуру,для того чтобы концы фигуры не заехали за край экрана"""
        if self.position == "Left":
            if self.list_coordinate[0][0] > 426:
                self.rotate_resolution = False
            elif self.list_coordinate[0][0] < 426:
                self.rotate_resolution = True
        elif self.position == "Right":
            if self.list_coordinate[3][0] < 49:
                self.rotate_resolution = False
            elif self.list_coordinate[3][0] > 49:
                self.rotate_resolution = True

    def rotate(self):
        """Переворачивает фигуру на 90 градусов"""
        if self.position == "Left" and self.rotate_resolution:
            self.list_coordinate[0] = [self.list_coordinate[0][0] + 25,self.list_coordinate[0][1] - 25]
            self.position = "Up"
        elif self.position == "Up":
            self.list_coordinate[1] = [self.list_coordinate[1][0] + 25,self.list_coordinate[1][1] + 25]
            self.position = "Right"
        elif self.position == "Right" and self.rotate_resolution:
            self.list_coordinate[2] = [self.list_coordinate[2][0] - 25,self.list_coordinate[2][1] + 25]
            self.position = "Down"
        elif self.position == "Down":
            self.list_coordinate[0] = list(self.list_coordinate[1])
            self.list_coordinate[1] = list(self.list_coordinate[2])
            self.list_coordinate[2] = [self.list_coordinate[2][0] + 25,self.list_coordinate[2][1] - 25]
            self.position = "Left"

class Shape_Cube(Shape):
    def __init__(self):
        super().__init__()
        self.list_coordinate =[[self.x,self.y],[self.x + 25,self.y],[self.x,self.y - 25],[self.x + 25,self.y - 25]]
        self.position = None
        self.rotate_resolution = True #Это флаг с помощью которого мы отслеживаем положение фигуры и разрешаем поворот

    def check_rotate_resolution(self):
       pass

    def rotate(self):
        pass

class Shape_L(Shape):
    def __init__(self):
        super().__init__()
        self.list_coordinate = [[self.x + 25,self.y],[self.x,self.y],[self.x,self.y - 25],[self.x,self.y - 50]]
        self.position = "Right"
        self.rotate_resolution = True #Это флаг с помощью которого мы отслеживаем положение фигуры и разрешаем поворот

    def check_rotate_resolution(self):
        """Проверяет можно ли повернуть фигуру,для того чтобы концы фигуры не заехали за край экрана"""
        if self.position == "Right":
            if self.list_coordinate[1][0] < 49:
                self.rotate_resolution = False
            elif 49 < self.list_coordinate[0][0] > 49:
                self.rotate_resolution = True
        elif self.position == "Left":
            if self.list_coordinate[1][0] > 426:
                self.rotate_resolution = False
            elif self.list_coordinate[1][0] < 426:
                self.rotate_resolution = True

    def rotate(self):
        """Переворачивает фигуру на 90 градусов"""
        if self.position == "Right" and self.rotate_resolution:
            self.list_coordinate[3] = [self.list_coordinate[3][0] + 25,self.list_coordinate[3][1] + 25]
            self.list_coordinate[0][0] -= 50
            self.list_coordinate[1] = [self.list_coordinate[1][0] - 25,self.list_coordinate[1][1] - 25]
            self.position = "Down"
        elif self.position == "Down":
            self.list_coordinate[3] = [self.list_coordinate[3][0] - 25,self.list_coordinate[3][1] + 25]
            self.list_coordinate[0][1] -= 50
            self.list_coordinate[1] = [self.list_coordinate[1][0] + 25,self.list_coordinate[1][1] - 25]
            self.position = "Left"
        elif self.position == "Left" and self.rotate_resolution:
            self.list_coordinate[0][0] += 50
            self.list_coordinate[1] = [self.list_coordinate[1][0] + 25,self.list_coordinate[1][1] + 25]
            self.list_coordinate[3] = [self.list_coordinate[3][0] - 25,self.list_coordinate[3][1] - 25]
            self.position = "Up"
        elif self.position == "Up":
            self.list_coordinate[0][1] += 50
            self.list_coordinate[1] = [self.list_coordinate[1][0] - 25,self.list_coordinate[1][1] + 25]
            self.list_coordinate[3] = [self.list_coordinate[3][0] + 25,self.list_coordinate[3][1] - 25]
            self.position = "Right"

class Shape_S(Shape):
    def __init__(self):
        super().__init__()
        self.list_coordinate = [[self.x,self.y],[self.x,self.y - 25],[self.x - 25,self.y - 25],[self.x - 25,self.y - 50]]
        self.position = "Up"
        self.rotate_resolution = True #Это флаг с помощью которого мы отслеживаем положение фигуры и разрешаем поворот

    def check_rotate_resolution(self):
        """Проверяет можно ли повернуть фигуру,для того чтобы концы фигуры не заехали за край экрана"""
        if self.position == "Up":
            if self.list_coordinate[2][0] < 50:
                self.rotate_resolution = False
            elif self.list_coordinate[2][0] > 49:
                self.rotate_resolution = True

    def rotate(self):
        """Переворачивает фигуру на 90 градусов"""
        if self.position == "Up" and self.rotate_resolution:
            self.list_coordinate[0][0] -= 50
            self.list_coordinate[3][1] += 50
            self.position = "Down"
        elif self.position == "Down":
            self.list_coordinate[0][0] += 50
            self.list_coordinate[3][1] -= 50
            self.position = "Up"

class Shape_Band(Shape):
    def __init__(self):
        super().__init__()
        self.list_coordinate = [[self.x,self.y],[self.x,self.y - 25],[self.x,self.y - 50],[self.x,self.y - 75]]
        self.position = "Up"
        self.rotate_resolution = True #Это флаг с помощью которого мы отслеживаем положение фигуры и разрешаем поворот

    def check_rotate_resolution(self):
        """Проверяет можно ли повернуть фигуру,для того чтобы концы фигуры не заехали за край экрана"""
        if self.position == "Up":
            if self.list_coordinate[0][0] < 75 or self.list_coordinate[0][0] > 425:
                self.rotate_resolution = False
            elif 49 < self.list_coordinate[0][0] < 426:
                self.rotate_resolution = True

    def rotate(self):
        """Переворачивает фигуру на 90 градусов"""
        if self.position == "Up" and self.rotate_resolution:
            self.list_coordinate[0] = [self.list_coordinate[0][0] - 50,self.list_coordinate[0][1] - 50]
            self.list_coordinate[1] = [self.list_coordinate[1][0] - 25,self.list_coordinate[1][1] - 25]
            self.list_coordinate[3] = [self.list_coordinate[3][0] + 25,self.list_coordinate[3][1] + 25]
            self.position = "Down"
        elif self.position == "Down":
            self.list_coordinate[0] = [self.list_coordinate[0][0] + 50, self.list_coordinate[0][1] + 50]
            self.list_coordinate[1] = [self.list_coordinate[1][0] + 25, self.list_coordinate[1][1] + 25]
            self.list_coordinate[3] = [self.list_coordinate[3][0] - 25, self.list_coordinate[3][1] - 25]
            self.position = "Up"

