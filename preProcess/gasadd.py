import os
import cv2
import numpy as np
from shapely.geometry import Polygon, Point
import random
img_path = r'E:\630data\2_1066'
txt_path = r'E:\630data\yolol'
save_path = r'E:\630data\out'

labels = os.listdir(txt_path)

for label in labels:
    img = cv2.imread(os.path.join(img_path, os.path.splitext(label)[0] + '.jpg'))
    with open(os.path.join(txt_path, label), 'r') as f:
        detections = [line.strip().split() for line in f.readlines()]
    # print(img.shape)
    mask = np.full_like(img, (0, 0, 0))  # 创建一个与原始图像大小相同的掩码图像
    sh,sw = img.shape[0],img.shape[1] 
    for detection in detections:
        class_id = int(detection[0])
        labeldicts = []
        del detection[0]  # 删除第一个元素，保留坐标
        list__ = [detection[i:i + 2] for i in range(0, len(detection), 2)]  # 修改数组，两个一组[x,y]
        for i in list__:
            x = int(float(i[0]) * sw)
            y = int(float(i[1]) * sh)
            labeldicts.append((x, y))

        print("length:", len(labeldicts))
        new_points = labeldicts
        flag = True
        while flag:
            flag = False
            threshold_distance = 5
            old_points = new_points.copy()
            polygon = Polygon(old_points)
            py = 2
            polygon_points = list(polygon.exterior.coords)
            new_points = []
            for i in range(len(polygon_points) - 1):
                p1 = Point(polygon_points[i])
                p2 = Point(polygon_points[i + 1])
                distance = p1.distance(p2)
                
                # 如果距离超过阈值,则在两点之间插入新点
                if distance > threshold_distance:
                    flag = True
                    x1, y1 = p1.x, p1.y
                    x2, y2 = p2.x, p2.y
                    new_x = (x1 + x2) / 2 + random.uniform(-py, py)
                    new_y = (y1 + y2) / 2 + random.uniform(-py, py)
                    new_point = Point(new_x, new_y)
                    while polygon.contains(new_point):
                        new_x = (x1 + x2) / 2 + random.uniform(-py, py)
                        new_y = (y1 + y2) / 2 + random.uniform(-py, py)
                        new_point = Point(new_x, new_y)
                    new_points.append(new_point)
                    new_points.append(p2)
                else:
                    new_points.append(p1)
        labeldicts = [(int(i.x), int(i.y)) for i in new_points]
        print("afterlength:", len(labeldicts))
        with open(os.path.join(save_path, label), 'a') as f:
            f.write(str(class_id) + ' ')
            for i in labeldicts:
                f.write(str(i[0] / sw) + ' ' + str(i[1] / sh) + ' ')
            f.write('\n')
