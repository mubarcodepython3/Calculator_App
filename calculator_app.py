# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator_app.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form): #membuat setUp dari ui 
        Form.setObjectName("Form")
        Form.resize(543, 379)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 120, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 170, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 250, 71, 16))
        self.label_3.setObjectName("label_3")
        #textbox1
        self.textbox1 = QtWidgets.QLineEdit(Form)
        self.textbox1.setGeometry(QtCore.QRect(140, 120, 331, 24))
        self.textbox1.setObjectName("textbox1")
        #textbox2
        self.textbox2 = QtWidgets.QLineEdit(Form)
        self.textbox2.setGeometry(QtCore.QRect(140, 170, 331, 24))
        self.textbox2.setObjectName("textbox2")
        #textbox3
        self.textbox3 = QtWidgets.QLineEdit(Form)
        self.textbox3.setGeometry(QtCore.QRect(140, 250, 231, 24))
        self.textbox3.setObjectName("textbox3")
        #buttontambah
        self.tambah = QtWidgets.QPushButton(Form)
        self.tambah.setGeometry(QtCore.QRect(240, 210, 51, 21))
        self.tambah.setObjectName("tambah")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(50, 40, 441, 31))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(130, 10, 191, 16))
        self.label_4.setObjectName("label_4")
        self.kali = QtWidgets.QPushButton(Form)
        self.kali.setGeometry(QtCore.QRect(300, 210, 51, 21))
        #buttonkali
        self.kali.setObjectName("kali")
        self.bagi = QtWidgets.QPushButton(Form)
        self.bagi.setGeometry(QtCore.QRect(360, 210, 51, 21))
        #buttonbagi
        self.bagi.setObjectName("bagi")
        self.kurang = QtWidgets.QPushButton(Form)
        self.kurang.setGeometry(QtCore.QRect(420, 210, 51, 21))
        #buttonkurang
        self.kurang.setObjectName("kurang")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(50, 80, 441, 241))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        #buttonbersihkan
        self.bersihkan = QtWidgets.QPushButton(self.frame)
        self.bersihkan.setGeometry(QtCore.QRect(340, 170, 88, 27))
        self.bersihkan.setObjectName("bersihkan")
        self.frame.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.textbox1.raise_()
        self.textbox2.raise_()
        self.textbox3.raise_()
        self.tambah.raise_()
        self.frame_2.raise_()
        self.kali.raise_()
        self.bagi.raise_()
        self.kurang.raise_()
        self.retranslateUi(Form)
        self.tambah.clicked.connect(self.on_add)
        self.kali.clicked.connect(self.on_sum)
        self.bagi.clicked.connect(self.on_divide)
        self.kurang.clicked.connect(self.on_minus)
        self.bersihkan.clicked.connect(self.textbox1.clear)
        self.bersihkan.clicked.connect(self.textbox2.clear)
        self.bersihkan.clicked.connect(self.textbox3.clear)
        self.bagi.clicked.connect(self.textbox1.show)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form): #membuat label
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Variabel1 : "))
        self.label_2.setText(_translate("Form", "Variabel2 : "))
        self.label_3.setText(_translate("Form", "Result : "))
        self.tambah.setText(_translate("Form", "+"))
        self.label_4.setText(_translate("Form", "SIMPLE CALCULATOR PYTHON"))
        self.kali.setText(_translate("Form", "*"))
        self.bagi.setText(_translate("Form", "/"))
        self.kurang.setText(_translate("Form", "-"))
        self.bersihkan.setText(_translate("Form", "CLEAR")) 
    #function rumus calculator
    def on_add(self): #function tambah
        ValueOne = self.textbox1.text()
        ValueTwo = self.textbox2.text()
        ResultIs = int(ValueOne) + int(ValueTwo)
        self.textbox3.setText(str(ResultIs))
    def on_sum(self): #function kali
        ValueOne = self.textbox1.text()
        ValueTwo = self.textbox2.text()
        ResultIs = int(ValueOne) * int(ValueTwo)
        self.textbox3.setText(str(ResultIs))
    def on_divide(self): #function bagi
        ValueOne = self.textbox1.text()
        ValueTwo = self.textbox2.text()
        ResultIs = int(ValueOne) / int(ValueTwo)
        self.textbox3.setText(str(ResultIs))
    def on_minus(self): #function kurang
        ValueOne = self.textbox1.text()
        Valuetwo = self.textbox2.text()
        ResultIs = int(ValueOne) - int(Valuetwo)
        self.textbox3.setText(str(ResultIs))


