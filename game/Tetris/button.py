import pygame

class Button:
    def __init__(self,path_normal,path_click,x,y):

        self.size = [190,45] #Размер кнопки
        self.image_button = pygame.image.load(path_normal) #Загружаем изображение исходной кнопки
        self.x = x #Позиция х кнопки
        self.y = y #Позиция у кнопки
        self.rect_button = pygame.Rect(self.x,self.y,self.size[0],self.size[1]) #Прямоугольник для создания коллизии с курсором
        self.rect_image_button = self.image_button.get_rect()
        """Создание кнопки при нажатии на нее"""
        self.image_click = pygame.image.load(path_click)

    def create_button(self,settings,color):
        """Создает кнопку на экране"""
        text_button = settings.font_text.render(self.text,True,color) #Создаем изображение с текстом
        text_rect = text_button.get_rect() #Возвращаем прямоугольник который занимает текст
        text_rect.center = self.rect_image_button.center #Делаем текст посередине кнопки
        self.image_button.blit(text_button,text_rect)
        self.image_click.blit(text_button,text_rect)
        self.image_put_on_button.blit(text_button,text_rect)

    def draw_button(self,screen,control): #Рисует созданную кнопку на экране
       """Рисует кнопку в зависимости от флага,который берется из класса Control"""
       if self.rect_button.collidepoint(control.mouse_x,control.mouse_y) and control.flag == "CLICKED":

           screen.blit(self.image_click, (self.x, self.y)) #Если кликнули мышкой то рисуем кнопку нажатой

       elif control.flag == "NORMAL":

           screen.blit(self.image_button,(self.x,self.y)) #Если ничего не происходит,то рисуем обычную кнопку


class Button_Exit(Button):
    def __init__(self,path_normal,path_click,x,y):
        super().__init__(path_normal,path_click,x,y)

    def exit(self,control):
        """Выходит из игры"""
        if self.rect_button.collidepoint(control.mouse_x,control.mouse_y) and control.flag == "CLICKED":
            control.play = False

class Button_Play(Button):
    def __init__(self,path_normal,path_click,x,y):
        super().__init__(path_normal,path_click,x,y)

    def play(self,control,settings):
        """Запускает игру"""
        if self.rect_button.collidepoint(control.mouse_x, control.mouse_y) and control.flag == "CLICKED":
            settings.play_game = True

class Button_Pause(Button):
    def __init__(self,path_normal,path_click,x,y):
        super().__init__(path_normal, path_click, x, y)

    def pause(self,control,settings):
        """Останавливает игру при нажатии кнопки"""
        if self.rect_button.collidepoint(control.mouse_x, control.mouse_y) and control.flag == "CLICKED":
            settings.play_game = False