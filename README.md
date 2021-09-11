# Dxdownload
完全免费、开源的百度网盘不限速软件（编写中，暂无法使用）
本软件采用python编写，目前gui写好了，其他没写
注意：本软件的path机制是注册表，请在HKEY_CURRENT_USER\SOFTWARE\创建一个键:Dxdownload,然后创建一个键：path，最后创建一个值:install_path,并设置为dxdownload的__main__.py的路径
已知bug:
1.点击文件夹可能会卡顿或卡死，双击可能出现两个文件夹
需要使用python3.8环境,然后安装pyqt5和win32api，selenium，requests库，大多数环境已经内置（导致程序很大，后面会压缩）
恳请查错!
烂尾一年啦，学习任务紧张，这段时间会更新一点，预计2023年左右写完（超级鸽）【滑稽】
-------------------------------------
2021.9.12更新：
更新0.85版，重写代码与ui，换用bdpcsapi，而不是动态网页爬虫
