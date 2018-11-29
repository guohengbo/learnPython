'''
本节是数据统计与导出
'''
import pandas as pd

#数据集导入
path = 'E:\LearnPython\数据分析\data.xlsx'
data = pd.read_excel(path)

#统计
    #01 data.mean()得到数据框data中每一列的平均值
mean=data.mean()
print(mean)
    #02 data.corr()得到数据框data中每一列与其他列的相关系数
corr=data.corr()
print(corr)
    #03 data.count()得到数据框data中每一列的非空值个数
count=data.count()
print(count)
    #04 data.max/min()得到数据框data中每一列的最大/小值
max=data.max()
print(max)
    #05 data.median()得到数据框data中每一列的中位数
median=data.median()
print(median)
    #06 data.std()得到数据框data中每一列的标准差
std=data.std()
print(std) 
    #07 data.describe()得到数据框data每一列的描述性统计
describe=data.describe()
print(describe)

#导出
data.to_csv("filename")
data.to_excel("filename")
data.to_json("filename")
#实例
dataNew = data[["队伍","黄牌","红牌","罚球"]]
print(dataNew)
out_path='E:\LearnPython\数据分析\out_data.xlsx'
dataNew.to_excel(out_path)