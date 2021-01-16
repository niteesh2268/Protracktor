from data_usage_per_app import myThread3
from window_activity import myThread4
import json
from check_internet import myThread5
from check_internet import stop
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import os
from close import Ui_CloseWindow
import sys
from PIL import Image
from read_config import write_config
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 519)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 831, 471))
        self.tabWidget.setMouseTracking(True)
        self.tabWidget.setTabletTracking(True)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName("tabWidget")
        self.Local_Proctoring_tab = QtWidgets.QWidget()
        self.Local_Proctoring_tab.setMouseTracking(True)
        self.Local_Proctoring_tab.setTabletTracking(True)
        self.Local_Proctoring_tab.setStyleSheet("")
        self.Local_Proctoring_tab.setObjectName("Local_Proctoring_tab")
        self.textBrowser_LocalProctor = QtWidgets.QTextBrowser(self.Local_Proctoring_tab)
        self.textBrowser_LocalProctor.setGeometry(QtCore.QRect(90, 30, 601, 91))
        self.textBrowser_LocalProctor.setObjectName("textBrowser_LocalProctor")
        self.plainTextEdit_CourseCodeInput = QtWidgets.QPlainTextEdit(self.Local_Proctoring_tab)
        self.plainTextEdit_CourseCodeInput.setGeometry(QtCore.QRect(270, 140, 191, 41))
        self.plainTextEdit_CourseCodeInput.setObjectName("plainTextEdit_CourseCodeInput")
        self.textBrowser_CourseCode = QtWidgets.QTextBrowser(self.Local_Proctoring_tab)
        self.textBrowser_CourseCode.setGeometry(QtCore.QRect(90, 140, 181, 41))
        self.textBrowser_CourseCode.setObjectName("textBrowser_CourseCode")
        self.commandLinkButton_Next = QtWidgets.QCommandLinkButton(self.Local_Proctoring_tab)
        self.commandLinkButton_Next.setGeometry(QtCore.QRect(470, 140, 81, 41))
        self.commandLinkButton_Next.setObjectName("commandLinkButton_Next")
        self.tabWidget.addTab(self.Local_Proctoring_tab, "")
        self.Zen_mode_tab = QtWidgets.QWidget()
        self.Zen_mode_tab.setObjectName("Zen_mode_tab")
        self.pushButton_2 = QtWidgets.QPushButton(self.Zen_mode_tab)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 260, 161, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox_Webcam = QtWidgets.QCheckBox(self.Zen_mode_tab)
        self.checkBox_Webcam.setGeometry(QtCore.QRect(80, 160, 161, 41))
        self.checkBox_Webcam.setObjectName("checkBox_Webcam")
        self.checkBox_DataUsage = QtWidgets.QCheckBox(self.Zen_mode_tab)
        self.checkBox_DataUsage.setGeometry(QtCore.QRect(590, 160, 161, 41))
        self.checkBox_DataUsage.setObjectName("checkBox_DataUsage")
        self.checkBox_Activity = QtWidgets.QCheckBox(self.Zen_mode_tab)
        self.checkBox_Activity.setGeometry(QtCore.QRect(440, 160, 161, 41))
        self.checkBox_Activity.setObjectName("checkBox_Activity")
        self.checkBox_ScreenRecording = QtWidgets.QCheckBox(self.Zen_mode_tab)
        self.checkBox_ScreenRecording.setGeometry(QtCore.QRect(270, 160, 161, 41))
        self.checkBox_ScreenRecording.setObjectName("checkBox_ScreenRecording")
        self.textBrowser_ZenMode = QtWidgets.QTextBrowser(self.Zen_mode_tab)
        self.textBrowser_ZenMode.setGeometry(QtCore.QRect(60, 60, 661, 61))
        self.textBrowser_ZenMode.setObjectName("textBrowser_ZenMode")
        self.tabWidget.addTab(self.Zen_mode_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 22))
        self.menubar.setObjectName("menubar")
        self.menuProctoring = QtWidgets.QMenu(self.menubar)
        self.menuProctoring.setObjectName("menuProctoring")
        self.menuResults = QtWidgets.QMenu(self.menuProctoring)
        self.menuResults.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuResults.setTabletTracking(True)
        self.menuResults.setSeparatorsCollapsible(True)
        self.menuResults.setToolTipsVisible(True)
        self.menuResults.setObjectName("menuResults")
        self.menugraphs = QtWidgets.QMenu(self.menuProctoring)
        self.menugraphs.setObjectName("menugraphs")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionasa = QtWidgets.QAction(MainWindow)
        self.actionasa.setObjectName("actionasa")
        self.actionData_Usage = QtWidgets.QAction(MainWindow)
        self.actionData_Usage.setCheckable(False)
        self.actionData_Usage.setObjectName("actionData_Usage")
        self.actionActivity_Monitor = QtWidgets.QAction(MainWindow)
        self.actionActivity_Monitor.setObjectName("actionActivity_Monitor")
        self.actionVIdeo_Recordings = QtWidgets.QAction(MainWindow)
        self.actionVIdeo_Recordings.setObjectName("actionVIdeo_Recordings")
        self.actionScreen_Recordings = QtWidgets.QAction(MainWindow)
        self.actionScreen_Recordings.setObjectName("actionScreen_Recordings")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionLatest_activity_tracker = QtWidgets.QAction(MainWindow)
        self.actionLatest_activity_tracker.setObjectName("actionLatest_activity_tracker")
        self.actionLatest_Data_Usage = QtWidgets.QAction(MainWindow)
        self.actionLatest_Data_Usage.setObjectName("actionLatest_Data_Usage")
        self.actionopen_readme_txt = QtWidgets.QAction(MainWindow)
        self.actionopen_readme_txt.setObjectName("actionopen_readme_txt")
        self.menuResults.addAction(self.actionData_Usage)
        self.menuResults.addAction(self.actionActivity_Monitor)
        self.menuResults.addAction(self.actionVIdeo_Recordings)
        self.menuResults.addAction(self.actionScreen_Recordings)
        self.menugraphs.addSeparator()
        self.menugraphs.addAction(self.actionLatest_activity_tracker)
        self.menugraphs.addAction(self.actionLatest_Data_Usage)
        self.menuProctoring.addSeparator()
        self.menuProctoring.addAction(self.menuResults.menuAction())
        self.menuHelp.addAction(self.actionopen_readme_txt)
        self.menubar.addAction(self.menuProctoring.menuAction())
        self.menuProctoring.addAction(self.menugraphs.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.commandLinkButton_Next.clicked.connect(self.next)
        self.pushButton_2.clicked.connect(self.start)
        self.actionData_Usage.triggered.connect(lambda: self.open('../results/DataUsage'))
        self.actionActivity_Monitor.triggered.connect(lambda: self.open('../results/ActivityTracker'))
        self.actionScreen_Recordings.triggered.connect(lambda: self.open('../results/ScreenRecordings'))
        self.actionVIdeo_Recordings.triggered.connect(lambda: self.open('../results/WebcamRecordings'))
        self.actionopen_readme_txt.triggered.connect(lambda: self.open_doc())
        self.actionLatest_activity_tracker.triggered.connect(lambda: self.open_graph('../results/ActivityTracker/usage_graph'))
        self.actionLatest_Data_Usage.triggered.connect(lambda: self.open_graph('../results/DataUsage'))        
    def open_doc(self):
        #print("hi")
        os.system("gedit ../readme")
        #print("hi")
             
    def open_graph(self,path):
        import glob
        files = glob.glob(path+"/*.png")
        files.sort(key=os.path.getmtime, reverse=True)
        if files!=[]:
            im = Image.open(files[0])  
            im.show()  
    
    
    def open(self,path):
        os.system('xdg-open "%s"' % path)
    def start(self):
        try:
            os.mkdir('../results')
        except FileExistsError:
            pass
        try:
            os.mkdir('../results/ActivityTracker')
        except FileExistsError:
            pass
        try:
            os.mkdir('../results/WebcamRecordings')
        except FileExistsError:
            pass
        try:
            os.mkdir('../results/ScreenRecordings')
        except FileExistsError:
            pass
        try:
            os.mkdir('../results/DataUsage')
        except FileExistsError:
            pass
        write_config(self.course_name)
        MainWindow.close()
        val1=self.checkBox_ScreenRecording.isChecked()
        val2=self.checkBox_Webcam.isChecked()
        val3=self.checkBox_DataUsage.isChecked()
        val4=self.checkBox_Activity.isChecked()
        thread5=myThread5(val1,val2,self.course_name)
        thread5.start() 
        thread3=myThread3()
        thread4=myThread4()   
        if val3==True:
            thread3.start()
        if val4==True:
            thread4.start()
        self.ui = Ui_CloseWindow()
        self.ui.setupUi(MainWindow,val1,val2,val3,val4,thread3,thread4,thread5)
        MainWindow.show()
        
    def next(self):
        self.course_name=self.plainTextEdit_CourseCodeInput.toPlainText()
        self.tabWidget.setCurrentIndex(1)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>artf</p></body></html>"))
        self.textBrowser_LocalProctor.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Local Proctoring Mode</span> : Focus on the exam we will monitor</p></body></html>"))
        self.plainTextEdit_CourseCodeInput.setPlaceholderText(_translate("MainWindow", "This will be used to name the files(videos, logs)"))
        self.textBrowser_CourseCode.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline;\">Course Code: </span></p></body></html>"))
        self.commandLinkButton_Next.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Local_Proctoring_tab), _translate("MainWindow", "Local Proctoring"))
        self.pushButton_2.setText(_translate("MainWindow", "Start"))
        self.checkBox_Webcam.setText(_translate("MainWindow", "Webcam Recording"))
        self.checkBox_DataUsage.setText(_translate("MainWindow", "Data Usage per App"))
        self.checkBox_Activity.setText(_translate("MainWindow", "Activity Manager"))
        self.checkBox_ScreenRecording.setText(_translate("MainWindow", "Screen Recording"))
        self.textBrowser_ZenMode.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Local Proctoring Mode</span> : Focus on your Exam!</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Zen_mode_tab), _translate("MainWindow", "Let's Start"))
        self.menuProctoring.setTitle(_translate("MainWindow", "Proctoring"))
        self.menuResults.setTitle(_translate("MainWindow", "Results"))
        self.menugraphs.setTitle(_translate("MainWindow", "graphs"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionasa.setText(_translate("MainWindow", "asa."))
        self.actionData_Usage.setText(_translate("MainWindow", "Data Usage"))
        self.actionActivity_Monitor.setText(_translate("MainWindow", "Activity Monitor"))
        self.actionVIdeo_Recordings.setText(_translate("MainWindow", "VIdeo Recordings"))
        self.actionScreen_Recordings.setText(_translate("MainWindow", "Screen Recordings"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionLatest_activity_tracker.setText(_translate("MainWindow", "Latest activity tracker"))
        self.actionLatest_Data_Usage.setText(_translate("MainWindow", "Latest Data Usage"))
        self.actionopen_readme_txt.setText(_translate("MainWindow", "open readme.txt"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())