import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox
from numpy.lib.shape_base import vsplit
import vehicleBite
import pandas as pd
import speak as speak
import time

class mainWindow(QDialog):
    Vehicle = vehicleBite.vehicleBite()
    VehicleList = []
    attributes = ["Title","City","Country","Model","Meter Reading","Fuel Type","Engine Capacity","Auto/Manuel","Price","Identity","Contact"]
    searchAlgorithms = ["Select Algorithm","Insertion Sort","Selection Sort","Merge Sort"]
    def __init__(self):
        super(mainWindow,self).__init__()
        loadUi("design2.ui",self)
        self.loadData()
        
        # speak.speak("Welcome to the best platform to buy a vehicle..!. I hope it will help you.")
        
        self.exit.clicked.connect(self.Exit)
        self.sortButton.clicked.connect(self.sort)
        self.sort_attributeCombo.addItems(self.attributes)
        self.sort_AlgoCombo.addItems(self.searchAlgorithms)
    def loadData(self):
        
        df = self.Vehicle.load()
        self.VehicleList = df.values.tolist()
        self.enterInTable(self.VehicleList)

    def Exit(self):
        speak.speak("The system has been closed. Thanks for choosing our platform...!")
        sys.exit()
    def sort(self):
        att = self.sort_attributeCombo.currentText()
        algo = self.sort_AlgoCombo.currentText()
        mode = self.sort_ModeCombo.currentText()
        attIndex = 0
        algoIndex = 0
        isSorted = False

        i = 0
        for a in self.attributes:
            if a == str(att):
                attIndex = i
            i = i+1
        i = 0
        for a in self.searchAlgorithms:
            if a == algo:
                # print(a,algo)
                algoIndex = i
            i = i+1
        # print(att,algo,algoIndex)
        Time = time.time_ns()
        if self.searchAlgorithms[algoIndex] == "Insertion Sort":
            self.VehicleList = self.Vehicle.insertionSort(self.VehicleList,attIndex,mode)
            isSorted = True
        elif self.searchAlgorithms[algoIndex] == "Selection Sort":
            self.VehicleList = self.Vehicle.selectionSort(self.VehicleList,attIndex,mode)
            isSorted = True
        elif self.searchAlgorithms[algoIndex] == "Merge Sort":
            if mode == "Ascending":
                self.Vehicle.mergeSort(self.VehicleList,0,len(self.VehicleList)-1,attIndex)
                isSorted = True
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Descending order is temporarily stopped in Merge Sort')
                msg.setWindowTitle("Error")
                msg.exec_()

        else :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('ALGORITHM is not selected properly...!')
            msg.setWindowTitle("Error")
            msg.exec_()

        Time = "{:.2e}".format(time.time_ns()-Time)
        if isSorted:
            self.sort_algoName_2.setText(self.searchAlgorithms[algoIndex])
            self.sort_TimeTaken_2.setText(str(Time) + " ns")
            self.sort_noOfEntities_2.setText(str(len(self.VehicleList)))
            self.sort_SelectedAttribute_2.setText(self.attributes[attIndex])
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

