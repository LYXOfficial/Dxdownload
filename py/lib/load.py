import sys
from PyQt5.QtWidgets import QDialog , QApplication
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from threading import Thread
from time import sleep
import time
class MainWidget(QSplashScreen):
    def __init__(self,parent=None):
        global pbar
        super(MainWidget,self).__init__(parent)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2.5
        newTop = (screen.height() - size.height()) / 2.5
        self.move(int(newLeft),int(newTop))
        font=QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.setFont(font)
        self.setMinimumSize(200, 75)
        self.setMaximumSize(200, 75)
        pbar = QProgressBar(self)
        pbar.setGeometry(20, 30, 200, 25)
        pbar.setValue(24)
        pbar.setFormat("")
        self.label=QLabel(self)
        self.label.setGeometry(20,10,100,15)
        self.label.setText("加载中...")
    def mousePressEvent(self,event):
        pass
def close():
    for i in range(25,101):
        pbar.setValue(i)
        time.sleep(0.01)
    time.sleep(0.5)
    quit()
def a(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper
@a
def main():
    import time
    app = QApplication(sys.argv)
    main = MainWidget()
    main.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    # import time
    # app = QApplication(sys.argv)
    # main = MainWidget()
    # main.show()
    # QTimer.singleShot(5000,close)
    # sys.exit(app.exec_())
    main()
    time.sleep(5)
    close()