from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtWidgets import QLineEdit, QMainWindow
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QInputDialog
from PyQt5 import uic
from PyQt5.QtGui import QPalette, QImage, QBrush, QPixmap, QIcon
import os
import sqlite3
import sys


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('data/Ui.ui', self)
        palette = QPalette()
        oImage = QImage("data/tetris_super.jpg")
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)
        self.rec.clicked.connect(self.record)
        self.exi.clicked.connect(self.vihod)
        self.play.clicked.connect(self.playing)

    def record(self):
        i, okBtnPressed = QInputDialog.getText(self, "Поле", "100000000000000000000")

    def vihod(self):
        exit()

    def playing(self):
        i, okBtnPressed = QInputDialog.getInt(self, "Введите Уровень",
                                              "Ввод уровня",
                                              1, 2, 3)
        os.startfile('norm.py')
        my_file = open("some.txt", "w")
        my_file.write(str(i))
        my_file.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Menu()
    win.show()
    sys.exit(app.exec_())
