'''
利用pandas学习数据分析 
本节是数据导入与查看
'''
import pandas as pd

#数据集导入
path='E:\LearnPython\数据分析\data.xlsx'
data=pd.read_excel(path)

#查看数据集DataFrame
    #01 查看数据集索引、数据类型及内存信息
data.info()
    #02 查看数据库的行数与列数--(16,8)16行8列
print(data.shape)
    #03 查看数据框的前n行
print(data.head(3))
    #04 查看数据框的最后n行
print(data.tail(3)) 
