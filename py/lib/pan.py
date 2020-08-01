def pan():
    from selenium import webdriver
    import path as p
    import json
    import re
    import time
    from bs4 import BeautifulSoup as bs
    #from pyquery import PyQuery as pq
    from selenium.webdriver.chrome.options import Options
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
    time.sleep(1)
    try:
        element=d.find_element_by_class_name('know-button')
        element.click()
    except:
        pass
    pg=str(d.page_source)
    r=re.findall("<span node-type=\"wzMD72\" class=\"bold\">(.*?)</span>",pg)[0]
    j=re.findall("<span node-type=\"txiw1x01\">(.*?)</span>",pg)[0]
    return (r,j)
if __name__=="__main__":
    print(pan())