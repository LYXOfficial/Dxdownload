import os
import sys
import traceback
def getpath():
    import winreg
    string = r'SOFTWARE\Dxdownload\path'
    handle = winreg.OpenKey(winreg.HKEY_CURRENT_USER, string, 0, (winreg.KEY_WOW64_64KEY + winreg.KEY_READ))
    location, _type = winreg.QueryValueEx(handle, "install_path")
    return location
os.system("pythonw "+getpath()+"\\py\\__main__.py")
