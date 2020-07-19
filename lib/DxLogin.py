from selenium import webdriver
from path import *
import time
import traceback
import sys
import err
from PyQt5.QtWidgets import *
import json
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
def islogin():
    with open(getpath()+"\\lib\\setting.json") as e:
        file=json.load(e)
    if file["isLogin"]:
        return True
    else:
        return False
def getname():
    with open(getpath()+"\\lib\\setting.json") as e:
        file=json.load(e)
    return file["username"]
def login():
    global d
    try:
        class do(QWidget):
            def __init__(self):
                import sys
                app = QApplication(sys.argv)
                super().__init__()
                reply = QMessageBox.information(self,"登录提示","将弹出浏览器框，请在浏览器中登录，登录成功后会自动登录到程序，按ok开始",QMessageBox.Ok)
        do()
        d=webdriver.Chrome(getpath()+r'\lib\chromedriver.exe')
        d.get(r"https://pan.baidu.com")
        def urlchange():
            if "https://pan.baidu.com/disk/home" in d.current_url:
                return False
            else:
                return True
        while urlchange():
            pass
        d.quit()
        with open(getpath()):
            pass
        class do(QWidget):
            def __init__(self):
                import sys
                app = QApplication(sys.argv)
                super().__init__()
                reply = QMessageBox.information(self,"登录提示","登陆成功",QMessageBox.Ok)
                reply.setWindowIcon(QIcon(getpath()+"\\icon\\Dx.ico"))
        do()
        
    except:
        e=traceback.format_exc()
        if "selenium.common.exceptions.NoSuchWindowException" in e or "TypeError: argument of type 'NoneType' is not iterable" in e:
            class do(QWidget):
                def __init__(self):
                    import sys
                    app = QApplication(sys.argv)
                    super().__init__()
                    reply = QMessageBox.warning(self,"登录提示","由于关闭了浏览器，登陆失败",QMessageBox.Ok)
            do()
        else:
            print(e)
            err.error(e)
    finally:
        try:
            d.quit()
        except:
            pass
if __name__=="__main__":
    login()
