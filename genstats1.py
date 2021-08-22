import sys
import os
from genstats import *
from PyQt5 import QtWidgets, QtGui, QtCore
class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.divstats)
     self.ui.pushButton_2.clicked.connect(self.subws)
     self.ui.pushButton_3.clicked.connect(self.topfive)   
  def topfive(self):
    os.system("python samp1.py")

  def divstats(self):
    os.system("python samp2.py")

  def subws(self):
    os.system("python samp3.py")

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
