def getmy():
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
    # from selenium.webdriver.chrome.options import Options
    # chrome_options =Options()
    # chrome_options.add_argument('--headless')
    # d = webdriver.Chrome(p.getpath()+"\\py\\lib\\chromedriver.exe",options=chrome_options)
    d=webdriver.Chrome(p.getpath()+"\\py\\lib\\chromedriver.exe")
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
    pg=d.page_source
    pg=bs(pg,"lxml")
    s=pg.find_all("div",class_="text")
    for i in range(len(s))[::-1]:
        try:
            s[i]=s[i].a.text.strip()
        except:
            s.pop(i)
    _file=s
    s_2=pg.find_all("div",class_="fa9Dod")
    for i in range(len(s_2))[::-1]:
        s_2[i]=re.findall("<div class=\"fa9Dod\" style=\"width:16%\">([\s\S]*)</div>",str(s_2[i]))[0]
    big=s_2
    s_3=pg.find_all("div",class_="urzlm4Zg")
    for i in range(len(s_2))[::-1]:
        s_3[i]=re.findall("<div class=\"urzlm4Zg\" style=\"width:23%\">([\s\S]*)</div>",str(s_3[i]))[0]
    date=s_3
    for i in _file:
        sp=i.split(".")
        if len(sp)==1:
            _type.append("文件夹")
        else:
            _type.append(sp[len(sp)-1]+"文件")
    return {"file":_file,"type":_type,"date":date,"big":big}
if __name__=="__main__":
    print(getmy())