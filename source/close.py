from webcam import myThread2
from screen import myThread1
import json
from check_internet import myThread5,thread1,thread2
from check_internet import stop
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import os
import sys

class Ui_CloseWindow(object):
    def setupUi(self, CloseWindow,val1,val2,val3,val4,thread3,thread4,thread5):
        self.val1=val1
        self.val2=val2
        self.val3=val3
        self.val4=val4
        self.CloseWindow=CloseWindow
        self.CloseWindow.setObjectName("CloseWindow")
        self.CloseWindow.resize(549, 382)
        self.centralwidget = QtWidgets.QWidget(self.CloseWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stopbutton = QtWidgets.QPushButton(self.centralwidget)
        self.stopbutton.setGeometry(QtCore.QRect(200, 150, 161, 71))
        self.stopbutton.setObjectName("stopbutton")
        self.stopbutton.clicked.connect(self.stop)
        self.textBrowser_stopWindow = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_stopWindow.setGeometry(QtCore.QRect(140, 80, 261, 41))
        self.textBrowser_stopWindow.setObjectName("textBrowser_stopWindow")
        self.CloseWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.CloseWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 549, 22))
        self.menubar.setObjectName("menubar")
        self.CloseWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.CloseWindow)
        self.statusbar.setObjectName("statusbar")
        self.CloseWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CloseWindow)
        QtCore.QMetaObject.connectSlotsByName(CloseWindow)
        self.thread5=thread5
        self.thread3=thread3
        self.thread4=thread4
    
    
    def stop(self):
        stop(self.val1,self.val2)
        if self.val3==True:
            self.thread3.set()
        if self.val4==True:
            self.thread4.set()
        self.thread5.sete()    
        self.CloseWindow.close()

    def retranslateUi(self, CloseWindow):
        _translate = QtCore.QCoreApplication.translate
        CloseWindow.setWindowTitle(_translate("CloseWindow", "Close Window"))
        self.stopbutton.setText(_translate("CloseWindow", "Stop"))
        self.textBrowser_stopWindow.setHtml(_translate("CloseWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Press to stop the proctoring</p></body></html>"))



