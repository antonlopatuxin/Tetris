from PyQt5 import QtCore,QtWidgets

class MyWindow(QtWidgets.QWidget):
    def __init__(self,parent = None): # Конструктор класса
        QtWidgets.QWidget.__init__(self,parent) # Вызываем конструктор базового класса
        self.label = QtWidgets.QLabel("Hello") # СОздаем объект надписи в окне
        self.label.setAlignment(QtCore.Qt.AlignHCenter) # Выравниваем текст по центру
        self.btnQuit = QtWidgets.QPushButton("&Quit") # Создаем объект кнопки, символ & создает кнопку быстрого доступа,что это?
        self.vbox = QtWidgets.QVBoxLayout() # Создаем вертикальный контейнер
        self.vbox.addWidget(self.label) # Добавляем надпись в контейнер,становится потомком контейнера
        self.vbox.addWidget(self.btnQuit) # Аналогично для кнопки
        self.setLayout(self.vbox)  # Добавляет контейнер в основное окно, контейнер становится потомком окна
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit) # Назначает обработчик сигнала кнопки при ее нажатии

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv) # Создаем объект приложения,необходим для управления программой
    window = MyWindow() # Экземпляр класса
    window.setWindowTitle("Окошечко") # Задаем название окна
    window.resize(300,70) # Задаем размеры окна,являются инструкциями,которые не всегда выполняются
    window.show() # Отображаем окно на экране
    sys.exit(app.exec_()) # Запускаем цикл обработки событий