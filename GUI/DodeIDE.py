# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DodeIDE.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DodeIDE(object):
    def setupUi(self, DodeIDE):
        DodeIDE.setObjectName("DodeIDE")
        DodeIDE.resize(1052, 835)
        self.centralwidget = QtWidgets.QWidget(DodeIDE)
        self.centralwidget.setObjectName("centralwidget")
        self.CodeTextArea = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.CodeTextArea.setGeometry(QtCore.QRect(30, 30, 891, 481))
        self.CodeTextArea.setObjectName("CodeTextArea")
        self.OutputArea = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.OutputArea.setGeometry(QtCore.QRect(30, 520, 891, 261))
        self.OutputArea.setObjectName("OutputArea")
        self.OpenFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.OpenFileButton.setGeometry(QtCore.QRect(30, 0, 80, 23))
        self.OpenFileButton.setObjectName("OpenFileButton")
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(110, 0, 80, 23))
        self.SaveButton.setObjectName("SaveButton")
        self.CompileButton = QtWidgets.QPushButton(self.centralwidget)
        self.CompileButton.setGeometry(QtCore.QRect(190, 0, 80, 23))
        self.CompileButton.setObjectName("CompileButton")
        DodeIDE.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DodeIDE)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1052, 20))
        self.menubar.setObjectName("menubar")
        DodeIDE.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DodeIDE)
        self.statusbar.setObjectName("statusbar")
        DodeIDE.setStatusBar(self.statusbar)

        self.retranslateUi(DodeIDE)
        QtCore.QMetaObject.connectSlotsByName(DodeIDE)

    def retranslateUi(self, DodeIDE):
        _translate = QtCore.QCoreApplication.translate
        DodeIDE.setWindowTitle(_translate("DodeIDE", "DodeIDE"))
        self.OpenFileButton.setText(_translate("DodeIDE", "OPEN FILE"))
        self.SaveButton.setText(_translate("DodeIDE", "SAVE FILE"))
        self.CompileButton.setText(_translate("DodeIDE", "COMPILE"))



