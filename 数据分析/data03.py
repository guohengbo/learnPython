'''
本节是数据排序与过滤
'''
import pandas as pd

#数据集导入
path = 'E:\LearnPython\数据分析\data.xlsx'
data = pd.read_excel(path)

#排序
    #01 按照某列升序排序
data_asc = data.sort_values("射正率")
print(data_asc)
    #02 多列升序排序(本句是按照进球数降序，越位升序)
data_sort = data.sort_values(["进球数","越位"],ascending=[False,True])
print(data_sort)

#过滤(分组)
    #01 按照某列对数据框data做分组
    #注意：groupby之后的数据并不是DataFrame格式的数据，而是特殊的groupby类型 
data.groupby("球员数")
    #02 分组后返回统计结果
static=data.groupby("球员数").size()
print(static)
    #03 分组后查看某列的特征值
print(data.groupby("进球数")['射正率'].mean())