import os
import cv2
import numpy as np
from shapely.geometry import Polygon, Point
import random
imgs_path = r'E:\704data\testhebing\alloil41json'
txt_path = r'E:\704data\testhebing\gasliqout'
save_path = r'E:\704data\testhebing\zd'

labels = os.listdir(txt_path)
count = 0
for label in labels:
    # 将文件名后缀改为_thresh.jpg
    file_name_list = label.split(".")[:-1]
    file_name_str = '.'.join(file_name_list)
    img_path = os.path.join(imgs_path, os.path.splitext(file_name_str)[0] + '.jpg')
    if(not os.path.exists(img_path)):
        # 打印红色的not exist
        print("\033[1;31;40m not exist \033[0m", img_path)
        continue
    img = cv2.imread(img_path)
    with open(os.path.join(txt_path, label), 'r') as f:
        detections = [line.strip().split() for line in f.readlines()]
    # print(img.shape)
    mask = np.full_like(img, (0, 0, 0))  # 创建一个与原始图像大小相同的掩码图像
    sh,sw = img.shape[0],img.shape[1] 
    classList = []
    points = []
    for detection in detections:
        class_id = int(detection[0])
        classList.append(class_id)
        labeldicts = []
        del detection[0]  # 删除第一个元素，保留坐标
        list__ = [detection[i:i + 2] for i in range(0, len(detection), 2)]  # 修改数组，两个一组[x,y]
        for i in list__:
            x = int(float(i[0]) * sw)
            y = int(float(i[1]) * sh)
            labeldicts.append((x, y))
        points.append(labeldicts)

    # 分组
    pre_data = []
    for i in range(len(classList)):
        for j in range(len(classList)):
            if i == j or classList[i] == classList[j]:
                continue
            gasPolygon = None
            oilPolygon = None
            if classList[i] == 0:
                gasPolygon = Polygon(points[i])
                oilPolygon = Polygon(points[j])
            else:
                continue
            # 如果gas的中心点在oil内部，则认为是同一个区域
            gasCenter = gasPolygon.centroid
            if oilPolygon.contains(gasCenter):
                pre_data.append((gasPolygon, oilPolygon))
                break
    for gasPolygon, oilPolygon in pre_data:
        # 获取gas的所有点
        gasPoints = list(gasPolygon.exterior.coords)
        oilPoints = list(oilPolygon.exterior.coords)
        
        # 遍历gas的所有点
        for i in range(len(gasPoints)):
            p = Point(gasPoints[i])
            # 如果p在oil内部，将其移动到oil的外部
            flag = False
            while oilPolygon.contains(p):
                flag = True
                gasPoints[i] = (p.x + random.uniform(-2, 2), p.y + random.uniform(-2, 2))
                p = Point(gasPoints[i])
            
        with open(os.path.join(save_path, label), 'a') as f:
            f.write(str(0) + ' ')
            for i in gasPoints:
                f.write(str(i[0] / sw) + ' ' + str(i[1] / sh) + ' ')
            f.write('\n')
            f.write(str(1) + ' ')
            for i in oilPoints:
                f.write(str(i[0] / sw) + ' ' + str(i[1] / sh) + ' ')
            f.write('\n')
    print("finish:", label)
    count += 1
print("finish all:", count)
    

        