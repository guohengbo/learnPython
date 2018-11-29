#空列表
a=list()

a=['wuchao','jinxin','xiaohu','sanpang','ligang',['wuchao','jinxin']]

#添加 append insert
a.append('xuepeng') #默认插到最后一个位置
a.insert(1,'xuepeng1') #将数据插入到任意一个位置

#修改
a[1]='haidilao'
a[1:3]=['a','b'] #不含3

#删除 remove pop del
a.remove(a[0])
b=a.pop(1)
del a[0]
a.remove(['wuchao','jinxin'])
del a

#count:计算某元素出现次数
t=['to', 'be', 'or', 'not', 'to', 'be'].count('to')

#extend
m = [1, 2, 3]
n = [4, 5, 6]
m.extend(n)  #把n追加到m后面

# index # 根据内容找位置
a = ['wuchao', 'jinxin', 'xiaohu','ligang', 'sanpang', 'ligang', ['wuchao', 'jinxin']]
first_lg_index = a.index("ligang") #3
little_list = a[first_lg_index+1:] #4:到最后
second_lg_index = little_list.index("ligang")#1
second_lg_index_in_big_list = first_lg_index + second_lg_index +1 #3+1+1=5

# reverse
a = ['wuchao', 'jinxin', 'xiaohu','ligang', 'sanpang', 'ligang']
a.reverse()

x = [4, 6, 2, 1, 7, 9]
x.sort(reverse=True)#从大到小排序  false为小到大

a = ['wuchao', 'jinxin', 'Xiaohu','Ligang', 'sanpang', 'ligang']
a.sort()  #按照首字母排序

