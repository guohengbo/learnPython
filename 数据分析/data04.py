'''
本节是数据连接与组合
'''
import pandas as pd

#数据集导入
path = 'E:\LearnPython\数据分析\data.xlsx'
data = pd.read_excel(path)

#连接
    #01 pd.append(data2)在data2的末尾添加数据集data1，data1与data2的列数应该相等
    #本句是 对比看看进球最多和最少分别是哪支队伍吧
shootMax=data.sort_values("进球数").head(1)
shootMin=data.sort_values("进球数").tail(1)
print(shootMax.append(shootMin))
    #02 pd.concat([data1,data2],axis=1)
    # #data1的列最后添加data2，其中data1与data2的行数应该相等sql的union all 
    # 查看全部队伍和进球数的对应关系
allShoot = pd.concat([data["队伍"],data["进球数"]],axis=1)
print(allShoot)