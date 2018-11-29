import os
path='E:\LearnPython'

file=os.listdir(path)
for f in file:
    if 'Python' in f:
        print("文件夹有:"+f)
    if f.endswith('.py'):
        print("文件有:"+f)

