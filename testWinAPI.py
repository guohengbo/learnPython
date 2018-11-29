import win32api,win32con,win32gui
win32api.MessageBox(0,"您好，Win API","百度经验",win32con.MB_YESNO+win32con.MB_ICONQUESTION)

#从顶层窗口向下搜索主窗口，无法搜索子窗口
#FindWindow(lpClassName=None,lpWindowName=None) 窗口类名 窗口标题名
handle = win32api.FindWindow("Notepad", None) 