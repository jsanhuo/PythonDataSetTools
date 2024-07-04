import cv2
import os
import json
import numpy as np
path = "./testgl"
result = "./result"
# 一个像素代表多大区域
pixel = 1


# 如果result文件夹不存在，则创建一个
if not os.path.exists(result):
    os.makedirs(result)

imgs = []
label = []
imageName = []
# 打开 path 路径下的所有bmp文件
for file in os.listdir(path):
    if file.endswith(".bmp"):
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
    
    for object in objects:
        poly.append(object["segmentation"])
        area.append(object["area"])
        textPoint.append(object["bbox"])
        classList.append(object["category"])
    
    # 添加一个画板，将底色填充成黑色
    canvas = np.zeros_like(img)
    
    calcArea = []
    index = 0
    gas = {
        "points": [],
        "area": []
    }
    spray = {
        "points": [],
        "area": []
    }
    
    for points in poly:
        lines = []
        # 画出所有的点
        for point in points:
            x = int(point[0])
            y = int(point[1])
            lines.append([x, y])
            # cv2.circle(img, tuple([x,y]), 1, (0, 255, 0), 1)
        # 将点连接成多边形
        lines = [tuple(l) for l in lines]
        # 计算这个多边形的面积
        curArea = cv2.contourArea(np.array(lines))
        curArea *= pixel
        calcArea.append(curArea)
        
        
        
        if(classList[index] == "spray"):
            spray["points"].append(lines)
            spray["area"].append(curArea)
        elif(classList[index] == "gas"):
            gas["points"].append(lines)
            gas["area"].append(curArea)
            
        index += 1
        

    
    
    # 画gas
    for i in range(len(gas["points"])):
        cv2.fillPoly(img, [np.array(gas["points"][i])], (0, 255, 0), 1)
        cv2.polylines(canvas, [np.array(gas["points"][i])], True, (255, 255, 255), 1)
        x  = np.mean([l[0] for l in gas["points"][i]])
        y  = np.mean([l[1] for l in gas["points"][i]])
        # cv2.putText(img, str(gas["area"][i]), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    
    
    # 画spray
    for i in range(len(spray["points"])):
        cv2.fillPoly(img, [np.array(spray["points"][i])], (0, 0, 255), 1)
        cv2.fillPoly(canvas, [np.array(spray["points"][i])], (255, 255, 255))
        x  = np.mean([l[0] for l in spray["points"][i]])
        y  = np.mean([l[1] for l in spray["points"][i]])
        # cv2.putText(img, str(spray["area"][i]), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    
    
    maxGas = max(gas["area"]) 
    maxSpray = max(spray["area"])
    
    # 在图片右下角上显示最大的gas和spray
    cv2.putText(img, "maxGas: " + str(maxGas), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    cv2.putText(img, "maxSpray: " + str(maxSpray), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    
    
    
    # 将canvas保存到result文件夹下
    cv2.imwrite(os.path.join(result, name), canvas)
    
    # 添加一个长方形画板，左边显示原图，右边显示画板
    canvas = np.hstack([img, canvas])
    
    
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
    
    