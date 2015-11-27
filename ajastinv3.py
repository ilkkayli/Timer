#!/usr/bin/env python
from PySide.QtCore import *
from PySide.QtGui import *
import sys
import mainGui2
import time
import winsound
import os   

class Timer(QDialog, mainGui2.Ui_Dialog):
    
    def __init__(self, parent=None):
        super(Timer, self).__init__(parent)
        self.setupUi(self)
        
        self.workerThread = WorkerThread() 
        self.connect(self.startButton, SIGNAL("clicked()"), self.initUI) #init the workerThread   
        self.connect(self.quitButton, SIGNAL("clicked()"), self.closeApp)
        
        self.connect(self.workerThread, SIGNAL("updateMinutes(QString)"), self.updateMinutes)
        self.connect(self.workerThread, SIGNAL("updateSeconds(QString)"), self.updateSeconds)
        self.connect(self.workerThread, SIGNAL("updateHorizontalSlider(QString)"), self.updateHorizontalSlider)
        self.connect(self.workerThread, SIGNAL("threadDone()"), self.threadDone) 
    
    def initUI(self):
        self.workerThread.start()
        
    def updateMinutes(self, minutes):
        self.lcdNumberMinutes.display(int(minutes))
                    
    def updateSeconds(self, seconds):
        self.lcdNumberSeconds.display(int(seconds))
        
    def updateHorizontalSlider(self, minutes):
        self.horizontalSlider.setValue(int(minutes))

    def threadDone(self):
        QMessageBox.information(self, "Info", "TIME IS UP!")     
        
    def closeApp(self):
        sys.exit()            
               
class WorkerThread(QThread):
    
    def __init__(self, parent=None):
        super(WorkerThread, self).__init__(parent)
    
    def run(self):
        val_minutes = form.horizontalSlider.value()
        time.sleep(1)
        
        val_minutes = val_minutes - 1
   
        while val_minutes >= 0:
            self.emit(SIGNAL("updateMinutes(QString)"), str(val_minutes)) #update minutes on the LCD display
            self.emit(SIGNAL("updateHorizontalSlider(QString)"), str(val_minutes)) #move slider one step back
            val_seconds = 59
            while val_seconds >= 0:
                self.emit(SIGNAL("updateSeconds(QString)"), str(val_seconds)) #update seconds on the LCD display
                val_seconds = val_seconds - 1
                time.sleep(1)
            val_minutes = val_minutes - 1

        sound = "1.wav"
        winsound.PlaySound(sound, winsound.SND_FILENAME)
        self.emit(SIGNAL("threadDone()"))  
        
               
app = QApplication(sys.argv)
form = Timer()
form.show()
app.exec_()

