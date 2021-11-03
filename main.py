import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from numpy.lib.shape_base import vsplit
import vehicleBite
import pandas as pd

class mainWindow(QDialog):
    Vehicle = vehicleBite.vehicleBite()
    VehicleList = []
    
    def __init__(self):
        super(mainWindow,self).__init__()
        loadUi("design2.ui",self)
        self.loadData()

    def loadData(self):
        
        df = self.Vehicle.load()
        self.VehicleList = df.values.tolist()
        self.enterInTable(self.VehicleList)

    def enterInTable(self,list):
        row = 0
        self.table.setColumnWidth(0,250)
        self.table.setColumnCount(11)
        
        
        self.table.setRowCount(len(list))
        for vehicle in list:
            
            self.table.setItem(row,0,QtWidgets.QTableWidgetItem(vehicle[0]))
            self.table.setItem(row,1,QtWidgets.QTableWidgetItem(vehicle[1]))
            self.table.setItem(row,2,QtWidgets.QTableWidgetItem(vehicle[2]))
            self.table.setItem(row,3,QtWidgets.QTableWidgetItem(str(vehicle[3])))
            self.table.setItem(row,4,QtWidgets.QTableWidgetItem(vehicle[4]))
            self.table.setItem(row,5,QtWidgets.QTableWidgetItem(vehicle[5]))
            self.table.setItem(row,6,QtWidgets.QTableWidgetItem(vehicle[6]))
            self.table.setItem(row,7,QtWidgets.QTableWidgetItem(vehicle[7]))
            self.table.setItem(row,8,QtWidgets.QTableWidgetItem(vehicle[8]))
            self.table.setItem(row,9,QtWidgets.QTableWidgetItem(str(vehicle[9])))
            self.table.setItem(row,10,QtWidgets.QTableWidgetItem(vehicle[10]))
            row = row+1
        



        





app = QApplication(sys.argv)
mainwindow = mainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setMinimumHeight(800)
widget.setMinimumWidth(1280)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("End")

