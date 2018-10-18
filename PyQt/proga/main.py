from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv) #Создаем объект приложения которым управляем им
window = QtWidgets.QWidget() #Создаем объект окна
window.setWindowTitle("Моя прога") #Название окна
window.resize(300,70) #Размер окна
label = QtWidgets.QLabel("<center>Antoxa</center>") #Текст в окне
btn_Quit = QtWidgets.QPushButton("&Выход")
vbox = QtWidgets.QVBoxLayout() #Вертикальный контейнер
vbox.addWidget(label) #Добавляем в контейнер надпись
vbox.addWidget(btn_Quit) #Добавляем кнопку в контейнер
window.setLayout(vbox) #Добавляем контейнер в окно
btn_Quit.clicked.connect(app.quit) #Назначаем на кнопку обработчик сигнала
window.show() #Вывод окна на экран
sys.exit(app.exec_()) #Бесконечный цикл обработки событий
