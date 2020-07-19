def getpath():
    import win32api, win32con
    reg_root = win32con.HKEY_CURRENT_USER
    reg_path = r"SOFTWARE\Dxdownload\path"
    reg_flags = win32con.WRITE_OWNER|win32con.KEY_WOW64_64KEY|win32con.KEY_ALL_ACCESS
    key = win32api.RegOpenKeyEx(reg_root, reg_path, 0, reg_flags)
    value, key_type = win32api.RegQueryValueEx(key, 'install_path')
    return value
if __name__=="__main__":
    print(getpath())