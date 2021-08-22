import sys
from clsdet import *
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
        fld1 = str(self.ui.lineEdit_3.text())
        fld2 = str(self.ui.lineEdit_5.text())
        fld3 = str(self.ui.lineEdit_6.text())
        fld4 = str(self.ui.lineEdit_4.text())        
        fld5 = str(self.ui.lineEdit_7.text())
        fld6 = str(self.ui.lineEdit_8.text())        
        fld7 = str(self.ui.lineEdit_10.text())
        fld8 = str(self.ui.lineEdit_9.text())
        fld9 = str(self.ui.lineEdit_11.text())
        fld10 = str(self.ui.lineEdit_13.text())        
        fld11 = str(self.ui.lineEdit_12.text())
        fld12 = str(self.ui.lineEdit_14.text())
        fld13 = str(self.ui.lineEdit_16.text())
        fld14 = str(self.ui.lineEdit_15.text())
        fld15 = str(self.ui.lineEdit_17	.text())
        fld16 = str(self.ui.lineEdit_19.text())        
        fld17 = str(self.ui.lineEdit_18.text())
        fld18 = str(self.ui.lineEdit_20.text())
        fld19 = str(self.ui.lineEdit_22.text())
        fld20 = str(self.ui.lineEdit_21.text())
        fld21 = str(self.ui.lineEdit_23.text())
        fld22 = str(self.ui.lineEdit_25.text())        
        fld23 = str(self.ui.lineEdit_24.text())
        fld24 = str(self.ui.lineEdit_26.text())
        fld25 = str(self.ui.lineEdit_28.text())
        fld26 = str(self.ui.lineEdit_27.text())
        fld27 = str(self.ui.lineEdit_29.text())
        fld28 = str(self.ui.lineEdit_31.text())        
        fld29 = str(self.ui.lineEdit_30.text())
        fld30 = str(self.ui.lineEdit_32.text())
        fld31 = str(self.ui.lineEdit_34.text())
        fld32 = str(self.ui.lineEdit_33.text())
        fld33 = str(self.ui.lineEdit_35.text())
        fld34 = str(self.ui.lineEdit_37.text())
        fld35 = str(self.ui.lineEdit_36.text())
        fld36 = str(self.ui.lineEdit_38.text())
        cur.execute('INSERT INTO clsdet(year,semester,acayear,sub1,stitle1,facid1) VALUES(?,?,?,?,?,?)', (fld1,fld2,fld3,fld4,fld5,fld6))
        cur.execute('INSERT INTO clsdet(sub2,stitle2,facid2,sub3,stitle3,facid3) VALUES(?,?,?,?,?,?)', (fld7,fld8,fld9,fld10,fld11,fld12))
        cur.execute('INSERT INTO clsdet(sub4,stitle4,facid4,sub5,stitle5,facid5) VALUES(?,?,?,?,?,?)', (fld13,fld14,fld15,fld16,fld17,fld18))
        cur.execute('INSERT INTO clsdet(sub6,stitle6,facid6,sub7,stitle7,facid7) VALUES(?,?,?,?,?,?)', (fld19,fld20,fld21,fld22,fld23,fld24))
        cur.execute('INSERT INTO clsdet(sub8,stitle8,facid8,sub9,stitle9,facid9) VALUES(?,?,?,?,?,?)', (fld25,fld26,fld27,fld28,fld29,fld30))
        cur.execute('INSERT INTO clsdet(sub10,stitle10,facid10,sub11,stitle11,facid11) VALUES(?,?,?,?,?,?)', (fld31,fld32,fld33,fld34,fld35,fld36))
        con.commit()

  
   
'''	
cur.execute('INSERT INTO clsdet VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,)',(fld1,fld2,fld3,fld4,fld5,fld6,fld7,fld8,fld9,fld10,fld11,fld12,fld13,fld14,fld15,fld16,fld17,fld18,fld19,fld20,fld21,fld22,fld23,fld24,fld25,fld26,fld27, fld28,fld29,fld30,fld31,fld32,fld33,fld34,fld35,fld36))
'''
        
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
