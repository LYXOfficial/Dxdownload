#encoding:utf-8
#关于打开窗口
from PyQt4 import QtCore,QtGui
class Ui_MainWindow(QtGui.QMainWindow):
    def init(self):
        QtGui.QMainWindow.init(self)#初始化窗口体
        self.setupUi(self)#调用UI文件方法
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)#函数进入方法
    ui = Ui_MainWindow()
    ui.show() #调用QT中内函数show方法
    sys.exit(app.exec_())# 函数退出