# -*- encoding: utf-8 -*-
import sys
def getpath():
    import winreg
    string = r'SOFTWARE\Dxdownload\path'
    handle = winreg.OpenKey(winreg.HKEY_CURRENT_USER, string, 0, (winreg.KEY_WOW64_64KEY + winreg.KEY_READ))
    location, _type = winreg.QueryValueEx(handle, "install_path")
    return location
sys.path.append(getpath()+"\\py\\lib")
from ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from path import *
import DxLogin as dl
import traceback
import err
import tweet
import os,time
import json
import get
from thread import a
try:
    class Dx(Ui_MainWindow,QMainWindow):
        @a
        def rec(self):
            # import load
            # load._main_()
            get.start()
            alls=get.getmy()
            self.plabel.setText(alls["disk"][0]+"/"+alls["disk"][1])
            m=alls["disk"][0]
            ma=alls["disk"][1]
            m=float(m[0:len(m)-1])
            ma=float(ma[0:len(ma)-1])
            self.progress.setMaximum(round(ma))
            self.progress.setValue(round(m))
            print(alls)
            sroot=QTreeWidgetItem()
            with open(getpath()+"\\py\\lib\\setting.json") as f:
                j=json.load(f)
            o=j["username"]
            sroot.setText(0,o+"的网盘")
            sroot.setIcon(0,QIcon(getpath()+"\\icon\\disk.ico"))
            for i in range(len(alls["file"])):
                exec("self.child{}=QTreeWidgetItem(sroot)".format(i))
                exec("self.child{}.setText(0,alls[\"file\"][{}])".format(i,i))
                exec("self.child{}.setText(1,alls[\"big\"][{}])".format(i,i))
                exec("self.child{}.setText(2,alls[\"date\"][{}])".format(i,i))
                exec("self.child{}.setText(3,alls[\"type\"][{}])".format(i,i))
                types={"zips":("zip文件","rar文件","7z文件"),"musics":("mp3文件","mp2文件","wav文件","flac文件"),"docs":("doc文件","docx文件",'rtf文件'),"excels":("xls文件","xlsx文件"),"ppts":("ppt文件","pptx文件"),"pics":("gif文件","png文件","jpg文件","jpeg文件","raw文件","tif文件","tiff文件","ico文件","pic文件","wmf文件","bmp文件","pdf文件"),"videos":("mp4文件","wmv文件","flv文件","avi文件","mov文件","3gp文件","rm文件","rmvb文件","mpeg文件"),"apps":["exe文件","app文件","apk文件"],"isos":("iso文件","img文件"),"txts":("txt文件","md文件","json文件","ini文件"),"scripts":("bat文件","cmd文件","vbs文件","js文件","reg文件")}
                a=alls["type"][i]
                a=a.lower()
                exec("self.child{}.setIcon(0,QIcon(getpath()+\"\\icon\\nfound.ico\"))".format(i))
                if a in types["zips"]:
                    exec("self.child{}.setIcon(0,QIcon(getpath()+\"\\icon\\zip.ico\"))".format(i))
                if a in types["musics"]:
                    exec("self.child{}.setIcon(0,QIcon(getpath()+\"\\icon\\media.ico\"))".format(i))
                if a in types["docs"]:
                    exec("self.child{}.setIcon(0,QIcon(getpath()+\"\\icon\\word.ico\"))".format(i))
                if a in types["ppts"]:
                    exec("self.child{}.setIcon(0,QIcon(getpath()+\"\\icon\\ppt.ico\"))".format(i))
                if a in types["pics"]:
                    exec("self.child{}.setIcon(0,QIcon(getpath()+\"\\icon\\pic.ico\"))".format(i))
                if a in types["videos"]:
                    exec("self.child{}.setIcon(0,QIcon(getpath()+\"\\icon\\video.ico\"))".format(i))
                if a in types["apps"]:
                    exec("self.child{}.setIcon(0,QIcon(getpath()+\"\\icon\\app.ico\"))".format(i))
                if a in types["isos"]:
                    exec("self.child{}.setIcon(0,QIcon(getpath()+\"\\icon\\iso.ico\"))".format(i))
                if a in types["txts"]:
                    exec("self.child{}.setIcon(0,QIcon(getpath()+\"\\icon\\txt.ico\"))".format(i))
                if a in types["scripts"]:
                    exec("self.child{}.setIcon(0,QIcon(getpath()+\"\\icon\\script.ico\"))".format(i))
                if a=="文件夹":
                    exec("self.child{}.setIcon(0,QIcon(getpath()+\"\\icon\\folder.ico\"))".format(i))
                exec("self.child{}.setCheckState(0, not Qt.CheckState)".format(i))
            self.treeWidget.addTopLevelItem(sroot)
            self.treeWidget.expandAll()
            # load.close()
        @a
        def tw(self):
            with open(getpath()+"\\py\\lib\\tmp.json") as f:
                j=json.load(f)
                j["text"]=""
            with open(getpath()+"\\py\\lib\\tmp.json","w") as f:
                json.dump(j,f)
            os.system(getpath()+"\\python38\\pythonw.exe "+getpath()+"\\py\\lib\\tweet.py")
        def ex(self):
            with open(getpath()+"\\py\\lib\\setting.json","r") as f:
                j=json.load(f)
                j["isLogin"]=0
                j["cookie"]=""
                j["username"]=""
            with open(getpath()+"\\py\\lib\\setting.json","w") as f:
                json.dump(j,f)
        @a
        def lo(self):
            os.system(getpath()+"\\python38\\pythonw.exe "+getpath()+"\\py\\lib\\DxLogin.py")
            if dl.islogin():
                self.label_2.setText (dl.getname())
                self.pushButton_10.setVisible(True)
                self.pushButton_10.setText("退出登录")
            else:
                self.label_2.setText( "未登录")
                self.pushButton_10.setVisible(False)
            if dl.islogin():
                self.pushButton.setText( "切换账号")
            else:
                self.pushButton.setText("账号登录")
        def twi(self):
            with open(getpath()+"\\py\\lib\\setting.json","r") as j:
                b=json.load(j)
                b["maindownload"]=self.lineEdit_2.text()
            with open(getpath()+"\\py\\lib\\setting.json","w") as j:
                json.dump(b,j)
        def browse(self):
            Folderpath = QFileDialog.getExistingDirectory()
            self.lineEdit_2.setText(Folderpath)
        def cr(self):
            def msg5(self):
                QMessageBox.about(self,"版权声明","Dxdownload V0.0.1beta\n该软件使用PyQt5和Python3编写。\n完全免费开源,无任何捐赠。\n由于该软件破解了百度网盘的官方机制,\n仅可用于学习交流使用,\n不步PanDownload后尘，谨慎使用并尽量支持正版!")
            msg5(self)
        def version(self):
            os.system(getpath()+"\\python38\\pythonw.exe "+getpath()+r"\py\lib\version.py")
        def zt(self):
            if dl.islogin():
                self.label_2.setText(dl.getname())
                self.pushButton_10.setVisible(True)
                self.pushButton_10.setText("退出登录")
            else:
                self.label_2.setText("未登录")
                self.pushButton_10.setVisible(False)
            if dl.islogin():
                self.pushButton.setText("切换账号")
            else:
                self.pushButton.setText("账号登录")
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.reload.clicked.connect(lambda:a(rec))
            self.zt()
            if dl.islogin():
                self.rec()
            else:
                sroot=QTreeWidgetItem()
                sroot.setText(0,"未登录")
                sroot.setIcon(0,QIcon(getpath()+"\\icon\\nfound.ico"))
                self.treeWidget.addTopLevelItem(sroot)
            with open(getpath()+"\\py\\lib\\setting.json","r") as j:
                b=json.load(j)
                b=b["maindownload"]
            self.lineEdit_2.setText(b)
            self.pushButton_2.clicked.connect(lambda:self.browse())
            self.pushButton_3.clicked.connect(lambda:self.version())
            self.pushButton_4.clicked.connect(lambda:self.cr())
            self.lineEdit_2.textChanged.connect(lambda:self.twi())
            self.tweetb.clicked.connect(self.tw)
            self.pushButton_10.clicked.connect(lambda:self.ex())
            self.pushButton.clicked.connect(lambda :self.lo())
            self.show()
    if __name__=="__main__":
        app = QApplication(sys.argv)
        window=Dx()
        sys.exit(app.exec_())
except SystemExit:
    pass
except:
    e=traceback.format_exc()
    print(e)
    err.error(e)