import sys
from faculty import *
from PyQt5 import QtWidgets, QtGui, QtCore

import sqlite3
con = sqlite3.connect('resanal1')

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues) 
   

  def insertvalues(self):
         
     with con:
    
        cur = con.cursor()
        fid = str(self.ui.lineEdit_3.text())
        fname = str(self.ui.lineEdit_4.text())
        cur.execute('INSERT INTO faculty VALUES(?,?)',(fid,fname))
        con.commit()

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
