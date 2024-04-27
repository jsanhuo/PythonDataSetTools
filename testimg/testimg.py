# 使用opencv尝试打开文件夹中所有图片，打不开的图片打印文件名
import cv2
import os

path2 = r'F:\dataset\spa\spaPick\input'
path1 = r'F:\dataset\spa\spaPick\target'

for file in os.listdir(path1):
    if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
        img = cv2.imread(os.path.join(path1, file))
        img2 = cv2.imread(os.path.join(path2, file))
        if img is None or img2 is None:
            print(file)
            # 删除该文件
            try:
                os.remove(os.path.join(path1, file))
            except:
                print(os.path.join(path1, file))
            try:
                os.remove(os.path.join(path2, file))
            except:
                print(os.path.join(path2, file))    
                
            