import sys
from PyQt5.QtWidgets import QDialog , QApplication
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from path import *
class MainWidget(QDialog):
    def __init__(self,parent=None):
        super(MainWidget,self).__init__(parent)
        font=QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.setFont(font)
        with open(getpath()+r"\py\lib\version.txt","r",encoding="utf-8") as r:
            v=r.read()
        self.setWindowTitle("更新日志")
        self.setMinimumSize(350, 400)
        self.setMaximumSize(350, 400)
        self.tb=QtWidgets.QTextBrowser(self)
        self.ok=QtWidgets.QPushButton(self)
        self.ok.setText("确定")
        self.ok.setGeometry(130,360,75,25)
        self.ok.clicked.connect(lambda:quit())
        self.tb.setText(v)
        self.tb.setGeometry(10,10,330,340)
if __name__ == "__main__": 
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(getpath()+"\\icon\\Dx.ico"))
    main = MainWidget()
    main.show()
    sys.exit(app.exec_())
