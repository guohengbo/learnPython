import os
import shutil
import time

path='./image'
out_path='./output'
files=os.listdir(path)
zip_count=0
files_count=len(files)
while True:
    if(files_count>=5):
        zip_count=zip_count+1
        zip_name=out_path+'/archive'+str(zip_count)
        shutil.make_archive(zip_name, 'zip', path)
        for f in files:
            os.remove(path + '/' + f)
     # 休眠1秒，达到每1秒监测一次的效果
    time.sleep(1)