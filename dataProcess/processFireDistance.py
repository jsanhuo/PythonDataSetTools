import cv2
import os
import json
import numpy as np
import csv
path = r"E:\712\ranshaorest"
result_path = r"E:\712\result"
result_mask_path = r"E:\712\result_mask"
result_fire_path = r"E:\712\result_fire"
csv_path = r"E:\712\result.csv"

# 一个像素代表多大区域
pixel = 1

csv_file = open(csv_path, 'w', newline='')
writer = csv.writer(csv_file)
writer.writerow(["文件名", "总面积", "火焰浮起长度"])

# 如果result文件夹不存在，则创建一个
if not os.path.exists(result_path):
    os.makedirs(result_path)

if not os.path.exists(result_mask_path):
    os.makedirs(result_mask_path)

if not os.path.exists(result_fire_path):
    os.makedirs(result_fire_path)

imgs = []
label = []
imageName = []
# 打开 path 路径下的所有bmp文件
for file in os.listdir(path):
    if file.endswith(".jpg"):
        img = cv2.imread(os.path.join(path, file))
        imageName.append(file)
        imgs.append(img)
        # 读取json文件
        with open(os.path.join(path, file.split(".")[0] + ".json"), "r") as f:
            data = json.load(f)
            label.append(data)
        
        
def process(img, data, name):
    area = []
    poly = []
    textPoint = []
    objects = data["objects"]
    classList = []
    or_img = np.copy(img)
    for object in objects:
        poly.append(object["segmentation"])
        area.append(object["area"])
        textPoint.append(object["bbox"])
        classList.append(object["category"])
        
    canvas = np.zeros_like(img)
    
    # 将图片转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 将灰度图转换为二值图
    ret, binary = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
    # 找到灰度图中最上面的点
    points = np.argwhere(binary == 255)
    # 找到最上面的点
    img_minY = np.inf
    for point in points:
        if point[0] < img_minY:
            img_minY = point[0]
    
    sum_area = 0
    distance = 0
    fire_minY = np.inf
    for points in poly:
        lines = []
        
        # 画出所有的点
        for point in points:
            x = int(point[0])
            y = int(point[1])
            if y < fire_minY:
                fire_minY = y
            lines.append([x, y])
            # cv2.circle(img, tuple([x,y]), 1, (0, 255, 0), 1)
        # 将点连接成多边形
        lines = [tuple(l) for l in lines]
        # 计算这个多边形的面积
        curArea = cv2.contourArea(np.array(lines))
        curArea *= pixel
        sum_area += curArea
        
        cv2.fillPoly(img, [np.array(lines)], (0, 255, 0), 1)
        cv2.fillPoly(canvas, [np.array(lines)], (255, 255, 255), 1)
        x  = np.mean([l[0] for l in lines])
        y  = np.mean([l[1] for l in lines])
        cv2.putText(img, str(curArea), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    
    # 建立一个新的画布，复制img到这个画布上
    fire_img = np.copy(or_img)
    # 当canvas中的点不为255时，img的点为0
    fire_img[canvas != 255] = 0
    
    
    img_minY += 10
    
    # 在img的minY上画一条直线
    if fire_minY != np.inf:
        cv2.line(img, (0, fire_minY), (img.shape[1], fire_minY), (0, 0, 255), 2)
    # 在img的img_minY上画一条直线
    if img_minY != np.inf:
        cv2.line(img, (0, img_minY), (img.shape[1], img_minY), (255, 0, 0), 2)
    
    if fire_minY != np.inf and img_minY != np.inf:
        # 在x = 50 的线上连接minY和fire_minY
        cv2.line(img, (50, img_minY), (50, fire_minY), (0, 255, 255), 2)
        # 计算两个线之间的距离
        distance = fire_minY - img_minY
        distance *= pixel
        cv2.putText(img, str(distance), (50, int((fire_minY + img_minY) / 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    cv2.imwrite(os.path.join(result_path, name), img)
    cv2.imwrite(os.path.join(result_mask_path, name), canvas)
    cv2.imwrite(os.path.join(result_fire_path, name), fire_img)

    writer.writerow([name, sum_area, distance])



for i in range(len(imgs)):
    print("process: ",imageName[i])
    process(imgs[i], label[i], imageName[i])

# 关闭文件
csv_file.close()