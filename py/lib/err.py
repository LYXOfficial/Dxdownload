from PyQt5 import QtCore, QtGui, QtWidgets
import path
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import tweet
import sys
import os
import json
retur=0
x=""
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(498, 385)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 4, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 2, 3)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 3, 0, 1, 5)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 4, 1, 1)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        global x
        import sys
        def rr():
            with open(path.getpath()+"\\py\\lib\\tmp.json","w",encoding="ANSI") as f:
                json.dump({'is':1,"text":x},f)
            os.system("python "+path.getpath()+"\\py\\lib\\tweet.py")
            sys.exit(0)
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "错误!"))
        Dialog.setWindowIcon(QIcon(path.getpath()+r"\icon\Dx.ico"))
        self.pushButton.setText(_translate("Dialog", "反馈"))
        self.pushButton.clicked.connect(rr)
        self.label_4.setText(_translate("Dialog", "请将该错误信息反馈给作者，也许能帮助解决此问题"))
        self.label.setPixmap(QPixmap(path.getpath()+"\\icon\\error.ico"))
        self.label_3.setText(_translate("Dialog", "错误信息："))
        self.label_2.setText(_translate("Dialog", "程序出错！\n"))
        self.textBrowser.setText(x)

def error(ex):
    global x
    import sys,os
    x=ex
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    error("测试")
