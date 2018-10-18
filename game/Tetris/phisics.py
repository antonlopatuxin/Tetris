import operator
import pygame

class Physics:
    def __init__(self):
        self.blast = pygame.image.load("images/blast.jpg")
        self.blast1 = pygame.image.load("images/blast1.jpg")
        self.blast2 = pygame.image.load("images/blast2.jpg")
        self.blast3 = pygame.image.load("images/blast3.jpg")
        self.blast4 = pygame.image.load("images/blast4.jpg")
        self.blast5 = pygame.image.load("images/blast5.jpg")
        self.blast6 = pygame.image.load("images/blast6.jpg")
        self.blast_list = [self.blast,self.blast1,self.blast2,self.blast3,self.blast4,self.blast5,self.blast6] #Список с изображениями взрывов
        self.blast_coordinate = [] #Список с координатами для взрыва
        self.bottom = "Move" #Флаг,для отслеживания достижения края экрана
        self.brick_list = [] #Здесь храняться кирпичи фигур,которые уже приземлились
        self.flag = 0 #Флаг который хранит номер ячейки списка,которую надо удалять при полной линии
        self.flag_delete = False #Флаг который указывает нужно ли удалять линию


    def check_bottom(self,shape,control):
        """Отслеживает не достигла ли фигура низа экрана"""
        for brick in shape.shape_form.list_coordinate:
            if brick[1] > 725:
                self.bottom = "End"
                control.speed_variable = 20

    def add_brick_list(self,shape):
        """Если фигура остановилась то записываем ее в список"""
        if self.bottom == "End":
            for brick in shape.shape_form.list_coordinate:
                self.brick_list.append([shape.shape_color,brick[0],brick[1]]) #Также добавляем цвет кирпича,чтобы адекватно отрисовывать их
            self.bottom = "Move"
            self.brick_list = sorted(self.brick_list,key=operator.itemgetter(2,1)) #Сортируем список,чтобы была возможность отслеживать заполненные линии
            shape.shape_color = shape.next_color
            shape.shape_name = shape.next_shape
            shape.shape_form = shape.get_shape()
            shape.next_color = shape.get_color()
            shape.next_shape = shape.get_shape_form()

    def draw_bottom_brick(self,screen):
        """Рисует из списка кирпичей сложенные кирпичи"""
        for brick in self.brick_list:
            screen.blit(brick[0],(brick[1],brick[2]))

    def check_collision(self,shape,control):
        """Отслеживает столкновение с фигурами"""
        for brick in shape.shape_form.list_coordinate:
            for brick_bottom in self.brick_list:
                if brick == [brick_bottom[1],brick_bottom[2] - 25]:
                    self.bottom = "End"
                    control.speed_variable = 20
                elif brick == [brick_bottom[1] - 25,brick_bottom[2]]: #Тут мы исключаем наезд на фигуры сбоку
                    shape.direction = None
                elif brick == [brick_bottom[1] + 25,brick_bottom[2]]:
                    shape.direction = None

    def delete_line(self):
        """Удаляет заполненную линию"""
        i = 0
        while i < 18:
            i += 1
            self.blast_coordinate.append([self.brick_list[self.flag][1],self.brick_list[self.flag][2]])
            del self.brick_list[self.flag]

    def shift_bricks(self):
        """Если линию удалили,то сдвигаем верхнии кирпичи вниз"""
        iteration = 0
        while iteration < self.flag:
            self.brick_list[iteration][2] += 25
            iteration += 1

    def create_blast(self,screen):
        """Создает серию взрывов"""
        for blast in self.blast_list:
            for coord in self.blast_coordinate:
                screen.blit(blast,coord)

    def check_full_line(self):
        """Проверяет,есть ли заполненные линии"""
        x = 25
        iteration = 0
        for brick in self.brick_list:
            if brick[1] == x:
                if x == 25:
                    self.flag = iteration
                x += 25
            else:
                x = 25

            if x == 475: #Если линия заполнена то удаляем ее
                self.flag_delete = True
                break
            else:
                self.flag_delete = False
            iteration += 1

    def logic_game(self,screen,gui):
        """Логика игры"""
        self.check_full_line()
        while self.flag_delete:
            self.delete_line()
            self.create_blast(screen)
            gui.add_score()
            self.shift_bricks()
            self.check_full_line()