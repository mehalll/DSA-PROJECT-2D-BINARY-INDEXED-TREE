import sys
from PyQt5.QtCore import pyqtSlot, QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets, QtGui


class MainPage(QMainWindow):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('DS_PROJECT_1.ui',self)
        self.pushButton.clicked.connect(self.move)

        label_10 = QLabel(self)
        BIT1 = QPixmap('BIT2.png')
        label_10.setPixmap(BIT1)
        label_10.setGeometry(QtCore.QRect(40,380,511,331))

        label_11 = QLabel(self)
        BIT2 = QPixmap('BIT3.png')
        label_11.setPixmap(BIT2)


    def Pictures(self):
        label_1 = QLabel(self)
        BIT_1 = QPixmap('BIT2.png')
        label_1.setPixmap(BIT_1)
        label_1.setGeometry(QtCore.QRect(40,380,500,378))

        label_2 = QLabel(self)
        BIT_2 = QPixmap('BIT3.PNG')
        label_2.setPixmap(BIT_2)
        label_2.setGeometry(QtCore.QRect(630,380,540,325))

    def move(self):
        from DS_PROJECT_main2 import MainPage2
        cls = MainPage2()
        cls.exec_()




app = QApplication(sys.argv)
widget = MainPage()
widget.Pictures()
widget.show()
sys.exit(app.exec_())
