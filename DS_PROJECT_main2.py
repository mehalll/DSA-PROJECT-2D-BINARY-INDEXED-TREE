import sys
from PyQt5.QtCore import pyqtSlot, QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets, QtGui

class MainPage2(QDialog):
    def __init__(self):
        super(MainPage2, self).__init__()
        loadUi('DS_PROJECT_2.ui',self)
        self.pushButton.clicked.connect(self.Get_Parent_input)
        self.pushButton_2.clicked.connect(self.Get_Next_Input)
        self.pushButton_4.clicked.connect(self.Get_PrefixSum_Input)
        self.pushButton_3.clicked.connect(self.Get_SumOfRange_Input)

    def Get_Parent_input(self):
        user_input = self.plainTextEdit.toPlainText()
        a = BIT([3,5,7,13,57,9])
        b = print(a.GetParent(user_input))
        self.textEdit.setText(b)

    def Get_Next_Input(self):
        user_input = self.plainTextEdit_2.toPlainText()
        a = BIT([3,5,7,13,57,9])
        b = print(a.GetNext(user_input))
        self.textEdit.setText(b)

    def Get_PrefixSum_Input(self):
        user_input = self.plainTextEdit_5.toPlainText()
        a = BIT([3,5,7,13,57,9])
        b = a.PrefixSum(user_input)
        self.textEdit_4.setText(b)

    def Get_SumOfRange_Input(self):
        user_input_1 = self.plainTextEdit_3.toPlainText()
        user_input_2 = self.plainTextEdit_4.toPlainText()
        a = BIT([3,5,7,13,57,9])
        b = a.SumOfRange(user_input_1,user_input_2)
        self.textEdit_3.setText(b)


import numpy as np

class BIT :
    def __init__(self,array):
        # self.array = np.array([[0 for i in range(len(array))], [0 for j in range(len(array))]])
        self.array = np.array([0 for i in range(len(array))])
        self.BIT = np.array([0 for j in range(len(array) + 1)])
        # self.tree = np.array([[0 for x in range(len(array) + 1)], [0 for y in range(len(array) + 1)]])
        # self.array = [0 for i in range(len(array) for j in range(len(array)]

        for i in range(len(array)):
            self.UpdateValue(i,array[i])

    def UpdateValue(self, position, value):
        current , self.array[position] = self.array[position] ,value
        value -= current
        position += 1
        while (position <= len(self.array)):
            self.BIT[position] += value
            position = self.GetNext(position)

    def GetParent(self,child_element):
        # in the arugument of this function , we have to pass the name of the child in order to know the parent
        # it will return the parent
        return (child_element - (child_element & -child_element))

    def GetNext(self,position):
        return (position + (position & -position))

    def PrefixSum(self,position):
        position += 1
        total = 0
        while (position > 0):
            total += self.BIT[position]
            position = self.GetParent(position)

        return total

    def SumOfRange(self,start,end):
        res = self.PrefixSum(max(start,end) - self.PrefixSum(min(start,end) - 1))
        return res

    def PrintArray(self):
        print("THE ARRAY =====>>> \t\t\t\t",self.array)


    def PrintTree(self):
        print("THE BINARY INDEXED TREE ====>>>",self.BIT)
        print("\n")

def test():

    cls = BIT([10,2,4,-5,6,8,1])
    cls.PrintArray()
    cls.PrintTree()
    cls.UpdateValue(3,23)
    print("\n")
    print("AFTER UPDATING THE VALUE ")
    print("\n")
    cls.PrintArray()
    cls.PrintTree()
    print("THE PARENT IS : ",cls.GetParent(5))
    print("THE NEXT VALUE IS : ",cls.GetNext(2))
    print("THE SUM OF THE PREFIX IS : ",cls.PrefixSum(5))
    print("THE SUM OF THE GIVEN RANGE IS : ",cls.SumOfRange(1,5))

#test()

