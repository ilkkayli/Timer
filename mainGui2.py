# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui'
#
# Created: Fri Nov 27 10:16:35 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(436, 196)
        Dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        Dialog.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lcdNumberMinutes = QtGui.QLCDNumber(Dialog)
        self.lcdNumberMinutes.setGeometry(QtCore.QRect(40, 20, 161, 161))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.lcdNumberMinutes.setFont(font)
        self.lcdNumberMinutes.setDigitCount(2)
        self.lcdNumberMinutes.setObjectName("lcdNumberMinutes")
        self.startButton = QtGui.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(310, 100, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startButton.setFont(font)
        self.startButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.startButton.setObjectName("startButton")
        self.horizontalSlider = QtGui.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(310, 50, 91, 31))
        self.horizontalSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalSlider.setMaximum(60)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.quitButton = QtGui.QPushButton(Dialog)
        self.quitButton.setGeometry(QtCore.QRect(310, 150, 91, 31))
        self.quitButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.quitButton.setObjectName("quitButton")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(310, 20, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.lcdNumberSeconds = QtGui.QLCDNumber(Dialog)
        self.lcdNumberSeconds.setGeometry(QtCore.QRect(220, 20, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.lcdNumberSeconds.setFont(font)
        self.lcdNumberSeconds.setDigitCount(2)
        self.lcdNumberSeconds.setObjectName("lcdNumberSeconds")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL("sliderMoved(int)"), self.lcdNumberMinutes.display)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Ajastin", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("Dialog", "Start!", None, QtGui.QApplication.UnicodeUTF8))
        self.quitButton.setText(QtGui.QApplication.translate("Dialog", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Set Minutes", None, QtGui.QApplication.UnicodeUTF8))

