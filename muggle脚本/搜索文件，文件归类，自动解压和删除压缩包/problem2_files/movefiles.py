#1.把 jpg,png,gif 文件夹中的所有文件移动到 image 文件夹中，然后删除 jpg,png,gif 文件夹 
#2.把 doc,docx,md,ppt 文件夹中的所有文件移动到 document 文件夹中，然后删除
import os
import shutil
 
path='./problem2_files'

#创建文件夹
os.makedirs(path+'/image')
os.makedirs(path+'/document')
 #后缀
image_suffix=['jpg','png','gif']
document_suffix=['doc','docx','md','ppt']
 
 #移动图片
for i in image_suffix:
	cur_path=path+'/'+i		#原来文件夹的路径,eg:./problem2_files/jpg
	files=os.listdir(cur_path)
	for f in files:
		shutil.move(cur_path+'/'+f, path+'/image')
	os.removedirs(cur_path)
	
 #移动文件
for j in document_suffix:
	cur_path=path+'/'+j		#原来文件夹的路径,eg:./problem2_files/doc
	files=os.listdir(cur_path)
	for f in files:
		shutil.move(cur_path+'/'+f, path+'/document')
	os.removedirs(cur_path)