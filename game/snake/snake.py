import pygame
import sys

class Snake:
    def __init__(self,color):

        self.color = color # Цвет змеи
        self.route = "RIGHT"
        self.head = [45,45] #Позиция головы змеи,для управления ею
        self.body = [[45,45],[34,45],[23,45]] # Тело змеи
        self.speed = 10 # Чем выше значение тем ниже скорость

    def draw_snake(self,window):
        """Отрисовывает тело змеи"""
        for segment in self.body:
            pygame.draw.rect(window,self.color,pygame.Rect(segment[0],segment[1],10,10))

    def move(self,indicator):
        """Движение змеи, route это флаг направления. Мы удаляем с конца списка змеи сегмент,
        затем прибавляем в начало элемент головы. Мы тут также проверяем на столкновение с краем экрана"""

        if self.route == "RIGHT":
            self.head[0] += 11
            if self.head[0] == 419:
                self.head[0] = 23
                self.body.pop()
                indicator.pop()
        elif self.route == "LEFT":
            self.head[0] -= 11
            if self.head[0] == 12:
                self.head[0] = 419
                self.body.pop()
                indicator.pop()
        elif self.route == "UP":
            self.head[1] -= 11
            if self.head[1] == 23:
                self.head[1] = 419
                self.body.pop()
                indicator.pop()
        elif self.route == "DOWN":
            self.head[1] += 11
            if self.head[1] == 419:
                self.head[1] = 34
                self.body.pop()
                indicator.pop()

    def control(self,route):
        """Функция управления змеей,также делаем,чтобы
        если змея едет вправо,нельзя было поехать влево и так далее"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and route != "LEFT":
                    route = "RIGHT"
                elif event.key == pygame.K_LEFT and route != "RIGHT":
                    route = "LEFT"
                elif event.key == pygame.K_UP and route != "DOWN":
                    route = "UP"
                elif event.key == pygame.K_DOWN and route != "UP":
                    route = "DOWN"
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_KP_ENTER:
                    route = "ENTER"
            elif event.type == pygame.QUIT:
                sys.exit()
        return route

    def pick(self,food,gui):
        """Метод который реализует сбор еды змеей. Постоянно добавляем к списку тела змеи сегмент головы.
        Если еда съедена, то к телу прибавляется новый сегмент иначе мы с конца списка тела удаляем сегмент,
        предотвращая рост тела змеи"""
        self.body.insert(0, list(self.head))
        for segment in self.body[1:]: #Проверяем,если голова врезалась в сегмент тела,то удаляем сегмент и естественно из индикатора
            if self.head == segment:
                self.body.pop()
                gui.indicator.pop()
        """Тут проверяем,не врезались ли мы в препятствие"""
        for barrier in gui.barrier:
            if self.head == barrier:
                self.body.pop()
                gui.indicator.pop()

        if self.head == food.food_position:
            food.get_food_positon(gui) #Если съели еду,то получаем новые координаты еды
            gui.indicator.append([gui.indicator[-1][0] + 11,12]) #Добавляем к списку индикатора координаты для следующего квадрата
        else:
            self.body.pop()










