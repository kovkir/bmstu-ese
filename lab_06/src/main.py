import os
import sys
from math import ceil
from matplotlib import pyplot as plt
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QComboBox, QDialog, QHeaderView, QLineEdit, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp

from parameters import params_table, project_modes
from task1 import Task1

AVERAGE_SALARY = 90


def resource_path(relative_path):
    if getattr(sys, 'frozen', False): # Функция возвращает значение атрибута указанного объекта по имени
        base_path = sys._MEIPASS
    else:
        base_path = os.getcwd()

    return os.path.join(base_path, relative_path)
            

class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = uic.loadUi(resource_path('ui.ui'), self)

        self.ui.sizeEdit.setValidator(QRegExpValidator(QRegExp("[0-9.]*"), self.ui.sizeEdit))

        self.RELY: QComboBox = self.ui.comboBox_1
        self.DATA: QComboBox = self.ui.comboBox_2
        self.CPLX: QComboBox = self.ui.comboBox_3
        self.TIME: QComboBox = self.ui.comboBox_4
        self.STOR: QComboBox = self.ui.comboBox_5
        self.VIRT: QComboBox = self.ui.comboBox_6
        self.TURN: QComboBox = self.ui.comboBox_7
        self.ACAP: QComboBox = self.ui.comboBox_8
        self.AEXP: QComboBox = self.ui.comboBox_9
        self.PCAP: QComboBox = self.ui.comboBox_10
        self.VEXP: QComboBox = self.ui.comboBox_11
        self.LEXP: QComboBox = self.ui.comboBox_12
        self.MODP: QComboBox = self.ui.comboBox_13
        self.TOOL: QComboBox = self.ui.comboBox_14
        self.SCED: QComboBox = self.ui.comboBox_15
        self.SIZE: QLineEdit = self.ui.sizeEdit
        self.project_mode: QComboBox = self.ui.comboBox_16

        self.ui.wbsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.classicTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


    def EAF(self):
        RELY = params_table['RELY'][self.RELY.currentIndex()]
        DATA = params_table['DATA'][self.DATA.currentIndex()]
        CPLX = params_table['CPLX'][self.CPLX.currentIndex()]
        TIME = params_table['TIME'][self.TIME.currentIndex()]
        STOR = params_table['STOR'][self.STOR.currentIndex()]
        VIRT = params_table['VIRT'][self.VIRT.currentIndex()]
        TURN = params_table['TURN'][self.TURN.currentIndex()]
        ACAP = params_table['ACAP'][self.ACAP.currentIndex()]
        AEXP = params_table['AEXP'][self.AEXP.currentIndex()]
        PCAP = params_table['PCAP'][self.PCAP.currentIndex()]
        VEXP = params_table['VEXP'][self.VEXP.currentIndex()]
        LEXP = params_table['LEXP'][self.LEXP.currentIndex()]
        MODP = params_table['MODP'][self.MODP.currentIndex()]
        TOOL = params_table['TOOL'][self.TOOL.currentIndex()]
        SCED = params_table['SCED'][self.SCED.currentIndex()]

        return RELY * DATA * CPLX * TIME * STOR * VIRT * TURN * ACAP * \
               AEXP * PCAP * VEXP * LEXP * MODP * TOOL * SCED


    def PM(self):
        mode = self.project_mode.currentIndex()
        size = float(self.SIZE.text())
        return project_modes['c1'][mode] * self.EAF() * (size ** project_modes['p1'][mode])


    def TM(self):
        mode = self.project_mode.currentIndex()
        return project_modes['c2'][mode] * (self.PM() ** project_modes['p2'][mode])


    def buildGraph(self):
        y = []
        for i in range(5):
            t = float(self.ui.classicTable.item(i, 3).text())
            y.append(ceil(float(self.ui.classicTable.item(i, 1).text()) / t))
            
        x = [i + 1 for i in range(len(y))]

        plt.bar(x, y)
        plt.ylabel('Кол-во сотрудников')
        plt.xlabel('Стадии жизненного цикла')
        plt.show()


    @pyqtSlot(name="on_projectButton_clicked")
    def calculateProject(self):
        try:
            float(self.SIZE.text())
        except:
            msg = QMessageBox()
            msg.setText('Размер конечного продукта –– положительное действительное число!')
            msg.show()
            msg.exec()
            return

        pm = round(self.PM(), 2)
        tm = round(self.TM(), 2)

        # Вычислить человеко-месяцы
        for i in range(9):
            self.ui.wbsTable.setItem(i, 1,
                QTableWidgetItem(str(round(pm * int(self.ui.wbsTable.item(i, 0).text()) / 100.0, 2)))
            )

        # Вычисление затрат
        for i in range(9):
            self.ui.wbsTable.setItem(i, 2,
                QTableWidgetItem(str(round(AVERAGE_SALARY * float(self.ui.wbsTable.item(i, 1).text()), 2)))
            )

        # Вычислить трудозатраты
        for i in range(7):
            self.ui.classicTable.setItem(i, 1,
                QTableWidgetItem(str(round(pm * int(self.ui.classicTable.item(i, 0).text()) / 100.0, 2)))
            )

        # Вычислить время
        for i in range(7):
            self.ui.classicTable.setItem(i, 3,
                QTableWidgetItem(str(round(tm * int(self.ui.classicTable.item(i, 2).text()) / 100.0, 2)))
            )

        self.buildGraph()
        

    @pyqtSlot(name="on_task1Button_clicked")
    def calculateTask1(self):
        mode = 0 # Обычный тип проекта
        size = 25 # кол-во тысяч строк кода в ПО 

        task1 = Task1(mode, size)
        task1.exploreAttributes()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    return app.exec()


if __name__ == '__main__':
    sys.exit(main())
