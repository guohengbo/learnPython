import os
import time
import xlrd

def GetTestDataPath():
    ospath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath,"testdata","TestData.xls")

# # 读取测试数据
# Testdata = xlrd.open_workbook(GetTestDataPath())
# # 选择excle表中的sheet
# table = Testdata.sheets()[1]
# # 从测试数据中读取数据，先行后列，都从0开始
# choice=table.cell(3,0).value
# print(choice)

def GetTestReport():
    now = time.strftime("%Y-%m-%d-%H-%M-%S-", time.localtime(time.time()))
    ospath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath,"testreport", now +"TestReport.xls")

def GetTestLogPath():
    ospath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath,"logs","log.txt")

def GetTestConfig(configname):
    ospath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath,"config",configname)