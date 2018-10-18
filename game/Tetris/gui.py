import pygame

class GUI:
    def __init__(self):

        self.border_brick = pygame.image.load("images/borderends.png")
        self.border = pygame.image.load("images/border.bmp")
        self.interface = pygame.image.load("images/gui.png")
        self.indicator = pygame.image.load("images/indicator.jpg")
        self.indicator_segment = pygame.image.load("images/indicator_segment.jpg")
        self.indicator_segment_list = []
        self.interface.set_colorkey((0,0,0))
        self.interface_rect = self.interface.get_rect()
        self.interface2 = pygame.image.load("images/gui2.png")
        self.interface_rect2 = self.interface2.get_rect()
        self.gui = [] #Список с координатами всех блоков интерфейса
        self.grid = pygame.image.load("images/grid.png")
        self.menu_window = pygame.image.load("images/window.jpg")
        self.font_text = pygame.font.SysFont("micra", 22)
        self.score = 0
        self.text_score = self.font_text.render("Счет:",True,(0, 255, 255))
        """Координаты для отображения в окне интерфейса следующей фигуры"""
        self.t_shape = [[650,275],[650,250],[650,225],[625,250]]
        self.cube_shape = [[625,250],[650,250],[625,275],[650,275]]
        self.s_shape = [[650,250],[675,250],[650,275],[625,275]]
        self.l_shape = [[625,275],[625,250],[625,225],[650,275]]
        self.band_shape = [[650,275],[650,250],[650,225],[650,300]]

    def draw_indicator(self,screen):
        """Отображает индикатор прохождения уровня"""
        screen.blit(self.indicator,(575,464))

    def add_segment_indicator(self):
        """Заполняет индикатор"""
        if self.score == 200:
            self.indicator_segment_list.append([600,468])
        elif self.score % 200 == 0:
            self.indicator_segment_list.append([self.indicator_segment_list[len(self.indicator_segment_list) - 1][0] + 4,468])


    def draw_segment_indicator(self,screen):
        """Отображает сегменты индикатора"""
        for segment in self.indicator_segment_list:
            screen.blit(self.indicator_segment,segment)

    def draw_next_shape(self,screen,shape):
        """Отображает на панели интерфейса следующую фигуру"""
        if shape.next_shape == "Shape_Band":
            for brick in self.band_shape:
                screen.blit(shape.next_color,brick)
        elif shape.next_shape == "Shape_S":
            for brick in self.s_shape:
                screen.blit(shape.next_color,brick)
        elif shape.next_shape == "Shape_L":
            for brick in self.l_shape:
                screen.blit(shape.next_color,brick)
        elif shape.next_shape == "Shape_Cube":
            for brick in self.cube_shape:
                screen.blit(shape.next_color,brick)
        elif shape.next_shape == "Shape_T":
            for brick in self.t_shape:
                screen.blit(shape.next_color,brick)

    def draw_score(self,screen):
        """Выводит на экран надпись счёт"""
        screen.blit(self.text_score,(560,80))
        number_score = self.font_text.render(str(self.score), True, (0, 255, 255))
        screen.blit(number_score,(650,80))

    def add_score(self):
        """Увеличивает счет"""
        self.score += 100
        self.add_segment_indicator()

    def init_gui(self):
        """Инициализирует координаты блоков для интерфейса"""

        for y in range(0,1000,25):
            for x in range(0,500,25):
                if x == 0 or x == 475 and 0 <= y <= 975:
                    self.gui.append([x,y])
                if y == 0 or y == 975 and 0 <= x <= 475:
                    self.gui.append([x,y])

    def draw_gui(self,surf):
        """Создает изображение интерфейса,которое сохраняет в виде картинки"""
        for y in range(0, 825, 25):
            for x in range(0, 525, 25):
                print(x, y)
                if y == 0 and 0 <= x <= 500:  # Если мы рисуем верхнюю линию,то поворачиваем тайл на 90 градусов
                    if x == 0 or x == 25 or x == 450 or x == 475:
                        surf.blit(self.border_brick, (x, y))
                    else:
                        new_border = pygame.transform.rotate(self.border, 90)  # Поворот тайла на 90 градусов
                        surf.blit(new_border, (x, y))

                elif x == 0 and 25 <= y <= 750:
                    if y == 25 or y == 750:
                        surf.blit(self.border_brick, (x, y))
                    else:
                        surf.blit(self.border, (x, y))
                elif x == 475 and 25 <= y <= 750:
                    if y == 25 or y == 750:
                        surf.blit(self.border_brick, (x, y))
                    else:
                        surf.blit(self.border, (x, y))

                elif y == 775 and 0 <= x <= 500:  # Если мы рисуем верхнюю линию,то поворачиваем тайл на 90 градусов
                    if x == 0 or x == 25 or x == 450 or x == 475:
                        surf.blit(self.border_brick, (x, y))
                    else:
                        new_border = pygame.transform.rotate(self.border, 90)  # Поворот тайла на 90 градусов
                        surf.blit(new_border, (x, y))

        pygame.image.save(surf, "images/gui.png")