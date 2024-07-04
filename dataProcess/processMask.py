import cv2
import os
import json
import numpy as np
path = r"E:\704data\testhebing\alloil41json"
json_path = r"E:\704data\testhebing\gasliqisat"
result_mask = r"E:\704data\testhebing\mask"
result_or = r"E:\704data\testhebing\or"
# 一个像素代表多大区域
pixel = 1


# 如果result文件夹不存在，则创建一个
if not os.path.exists(result_mask):
    os.makedirs(result_mask)

if not os.path.exists(result_or):
    os.makedirs(result_or)

imgs = []
label = []
imageName = []
# 打开 path 路径下的所有bmp文件
for file in os.listdir(path):
    if file.endswith(".bmp") or file.endswith(".jpg"):
        img = cv2.imread(os.path.join(path, file))
        imageName.append(file)
        imgs.append(img)
        # 读取json文件
        file_name_list = file.split(".")[:-1]
            # 将list转为str
        file_name_str = '.'.join(file_name_list)
        with open(os.path.join(json_path, file_name_str + ".json"), "r") as f:
            data = json.load(f)
            label.append(data)
        
        
def process(img, data, name):
    area = []
    poly = []
    textPoint = []
    objects = data["objects"]
    # 0 gas 1 liq
    classList = []
    for object in objects:
        poly.append(object["segmentation"])
        area.append(object["area"])
        textPoint.append(object["bbox"])
        classList.append(object["category"])
        
    
    
    # 添加一个画板，将底色填充成黑色
    canvas = np.zeros_like(img)
    
    calcArea = []
    index = 0
    for index, points in enumerate(poly):
        lines = []
        # 画出所有的点
        for point in points:
            x = int(point[0])
            y = int(point[1])
            lines.append([x, y])
            # cv2.circle(img, tuple([x,y]), 1, (0, 255, 0), 1)
        # 将点连接成多边形
        lines = [tuple(l) for l in lines]
        
        if classList[index] == "1":
            cv2.polylines(img, [np.array(lines)], True, (0, 255, 0), 1)
            cv2.fillPoly(canvas, [np.array(lines)], (255, 255, 255))
            x  = np.mean([l[0] for l in lines])
            y  = np.mean([l[1] for l in lines])
            curArea = cv2.contourArea(np.array(lines))
            calcArea.append(curArea)
            curArea *= pixel
        elif classList[index] == "0":
            cv2.polylines(img, [np.array(lines)], True, (0, 0, 255), 1)
            # 将这些点在画板上填充成白色
            cv2.polylines(canvas, [np.array(lines)],True, (255, 255, 255), 1)
            # 求出多边形的中心点
            x  = np.mean([l[0] for l in lines])
            y  = np.mean([l[1] for l in lines])
            curArea = cv2.contourArea(np.array(lines))
            calcArea.append(curArea)
            curArea *= pixel
    # 将canvas保存到result文件夹下
    cv2.imwrite(os.path.join(result_mask, name), canvas)
    cv2.imwrite(os.path.join(result_or, name), img)

    
    # 添加一个长方形画板，左边显示原图，右边显示画板
    canvas = np.hstack([img, canvas])
    
    # 添加zoom功能
    
    cv2.namedWindow("canvas", cv2.WINDOW_NORMAL)
    
    # 左边显示原图，右边显示画板
    cv2.imshow("canvas", canvas)



# 在一个窗口中按AD向左向右切换图片
i = 0
while True:
    process(imgs[i], label[i], imageName[i])
    print(imageName[i])
    key = cv2.waitKey(0)
    if key == ord("a"):
        i = (i - 1) % len(imgs)
    elif key == ord("d"):
        i = (i + 1) % len(imgs)
    else:
        break
    
    