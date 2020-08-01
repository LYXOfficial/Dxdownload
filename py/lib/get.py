d=0
_in=[]
_file=[]
_type=[]
date=[]
big=[]
from selenium import webdriver
import path as p
import re
import json
import time
from bs4 import BeautifulSoup as bs
#from pyquery import PyQuery as pq
from selenium.webdriver.chrome.options import Options
from threading import Thread
def getmy():
    global d,_file,_type,date,big
    def getin():
        chrome_options =Options()
        chrome_options.add_argument('--headless')
        d = webdriver.Chrome(p.getpath()+"\\py\\lib\\chromedriver.exe",options=chrome_options)
        #d=webdriver.Chrome(p.getpath()+"\\py\\lib\\chromedriver.exe")
        d.get("http://pan.baidu.com")
        d.delete_all_cookies()
        with open(p.getpath()+"\\py\\lib\\setting.json") as f:
            j=json.load(f)
        c=j["cookie"]
        for i in range(len(c)):
            x=c[i]
            if "expiry" in x:
                x.pop("expiry")
            c[i]=x
            d.add_cookie(c[i])
        d.get(r"http://pan.baidu.com/disk/home?#/all?path=%2F&vmode=list")
        while True:
            try:
                element=d.find_element_by_class_name('know-button')
                element.click()
                break
            except:
                pass
    def a(f):
        def wrapper(*args, **kwargs):
            thr = Thread(target=f, args=args, kwargs=kwargs)
            thr.start()

        return wrapper
    def sfolder():
        global d,_file,_type,date,big,in_
        def fin(n):
            element=d.find_element_by_link_text(n)
            element.click()
        def exit():
            element=d.find_element_by_link_text("返回上一级")
            element.click()
    #return {"file":_file,"type":_type,"date":date,"big":big,"disk":(r,j)}
if __name__=="__main__":
    print(getmy())