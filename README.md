# Dxdownload
完全免费、开源的百度网盘不限速软件（编写中，暂无法使用）
本软件采用python编写，目前gui写好了，其他没写
注意：本软件的path机制是注册表，请在HKEY_CURRENT_USER\SOFTWARE\创建一个键:Dxdownload,然后创建一个值:path,并设置为dxdownload的__main__.py的路径
已知bug:
1.浏览器登录经常闪退报错
2.错误页面点击反馈页面卡死
3.主界面登录窗口也会卡死
4.无法进行登录，查找文件：请检查电脑是否有chrome，软件自带的chromedriver版本为78，如与chrome版本不符，请更换
需要使用python3.8环境,然后安装pyqt5和win32api，selenium，bs4库
恳请查错!
烂尾一年啦，学习任务紧张，这段时间会更新一点，预计2023年左右写完（超级拖更）【滑稽】
