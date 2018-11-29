'''
本节是数据选取与清洗
'''
import pandas as pd

#数据集导入
path = 'E:\LearnPython\数据分析\data.xlsx'
data = pd.read_excel(path)

#数据选取
    #01 选取某列
    #以数组 Series 的形式返回选取的列
print(data["队伍"]) 
    #02 选取多列
dataNew = data[["队伍","黄牌","红牌","罚球"]]
print(dataNew)

#数据清洗
    #01 检查数据中空值出现的情况，并返回布尔值组成的列
isNull = dataNew['罚球'].isnull()
print(isNull)
    #02 检查数据中非空值出现的情况
notNull = dataNew.notnull()
print(notNull)
    #03 移除数据框 DataFrame 中包含空值的行
print(dataNew.dropna()) 
    #04 移除数据框 DataFrame 中包含空值的列
print(dataNew.dropna(axis=1)) 
    #05 将数据框 DataFrame 中的所有空值替换为 x
print(dataNew.fillna(0))