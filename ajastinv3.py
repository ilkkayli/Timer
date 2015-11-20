#!/usr/bin/env python
from PySide.QtCore import *
from PySide.QtGui import *
import sys
#DIR = "C:/Python27/test/ajastin"
#sys.path.insert(0, DIR)
import mainGui2
import time
import winsound
import os   

class Timer(QDialog, mainGui2.Ui_Dialog):
    
    def __init__(self, parent=None):
        super(Timer, self).__init__(parent)
        self.setupUi(self)
        
        self.workerThread = WorkerThread()
 
        self.connect(self.pushButton, SIGNAL("clicked()"), self.initUI) #kaynnistetaan workerThread initUI-metodin kautta Aloita! -nappia painamalla     
        self.connect(self.pushButton_2, SIGNAL("clicked()"), self.closeApp)

        self.connect(self.workerThread, SIGNAL("threadDone()"), self.threadDone) #monitoroi emitoituja signaaleja workerThreadista
    
    def initUI(self):
        self.workerThread.start() 

    def threadDone(self):
        QMessageBox.information(self, "Valmis", "AIKA LOPPUI!")     
        
    def closeApp(self):
        sys.exit()            
               
class WorkerThread(QThread):
    
    def __init__(self, parent=None):
        super(WorkerThread, self).__init__(parent)
    
    def run(self):
        val = form.horizontalSlider.value()
        time.sleep(1)
   
        while val >= 0:
            form.lcdNumber.display(val) #paivita lcd-elementti UI:lla
            time.sleep(60)
            val = val - 1
            form.horizontalSlider.setValue(val) #siirra slider pykalan verran vasemmalle eli takaisinpain

        sound = "1.wav"
        winsound.PlaySound(sound, winsound.SND_FILENAME)
        self.emit(SIGNAL("threadDone()"))  #lahetetaan signaali UI-threadille, etta homma on valmis. Kaytannossa signaalin perusteella avataan infoBox
        
               
app = QApplication(sys.argv)
form = Timer()
form.show()
app.exec_()

