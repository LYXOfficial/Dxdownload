# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\python\pyqt\tweet.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import path
import time
import os,sys
import mail
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        Dialog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 4)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 3, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.lineEdit.setText("Dxdownload")
    def retranslateUi(self, Dialog):
        def t():
            title="程序"+self.lineEdit.text()+"问题反馈"
            print(title)
            pmwq="联系方式:"+self.lineEdit_2.text()
            print(pmwq)
            what=self.textEdit.toPlainText()
            print(what)
            if title=="" or pmwq=="" or what=="":
                class do(QWidget):
                    def restart():
                        python = sys.executable
                        os.execl(python, python, * sys.argv)
                    def __init__(self):
                        import sys
                        app = QApplication(sys.argv)
                        super().__init__()
                        reply = QMessageBox.information(self,"不能提交","不能有空项",QMessageBox.Ok)
                        do.restart()
                do()
            else:
                mail.mail(t=title,c="问题:\n"+what+"\n"+pmwq)
                class do(QWidget):
                    def __init__(self):
                        import sys
                        app = QApplication(sys.argv)
                        super().__init__()
                        reply = QMessageBox.information(self,"反馈成功","谢谢!       ",QMessageBox.Ok)
                        quit()
                do()
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "反馈"))
        Dialog.setWindowIcon(QIcon(path.getpath()+r"\icon\Dx.ico"))
        self.label_3.setText(_translate("Dialog", "程序名"))
        self.label_4.setText(_translate("Dialog", "问题"))
        self.label_5.setText(_translate("Dialog", "联系方式"))
        self.label_2.setText(_translate("Dialog", "程序遇到问题了吗？请反馈吧！"))
        self.pushButton.setText(_translate("Dialog", "反馈"))
        self.pushButton.clicked.connect(t)
        self.label.setText(_translate("Dialog", "反馈"))

def tweet():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())