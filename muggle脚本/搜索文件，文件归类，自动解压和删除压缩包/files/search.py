import os
path='./files'

files=os.listdir(path)
for f in files:
	if(not f.endswith('.gif')) and ('project30' in f or 'commercial' in f):
		print(f)