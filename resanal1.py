import sys
import os
from resanal import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.cdetls)
     self.ui.pushButton_2.clicked.connect(self.fdetls)
     self.ui.pushButton_3.clicked.connect(self.stutails)
     self.ui.pushButton_4.clicked.connect(self.dflcn)
     self.ui.pushButton_5.clicked.connect(self.gsts)
 
       

  def cdetls(self):
    os.system("python clsdet1.py")

  def fdetls(self):
    os.system("python faculty1.py")

  def dflcn(self):
    os.system("python csvfile1.py")

  def stutails(self):
    os.system("python studentdtls1.py")

  def gsts(self):
    os.system("python genstats1.py")
     
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
