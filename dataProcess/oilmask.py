
import os
import cv2
import numpy as np
import math
import csv

img_path = r'E:\708\allgas'
txt_path = r'E:\708\allgas'
save_path = r'E:\708\out'

class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

class Line:
    def __init__(self, point1, point2):
        self.Point1 = point1
        self.Point2 = point2

def getAngle(line1, line2):
    dx1 = line1.Point1.X - line1.Point2.X
    dy1 = line1.Point1.Y - line1.Point2.Y
    dx2 = line2.Point1.X - line2.Point2.X
    dy2 = line2.Point1.Y - line2.Point2.Y
    angle1 = math.atan2(dy1, dx1)
    angle1 = int(angle1 * 180 / math.pi)
    # print(angle1)
    angle2 = math.atan2(dy2, dx2)
    angle2 = int(angle2 * 180 / math.pi)
    # print(angle2)
    if angle1 * angle2 >= 0:
        insideAngle = abs(angle1 - angle2)
    else:
        insideAngle = abs(angle1) + abs(angle2)
        if insideAngle > 180:
            insideAngle = 360 - insideAngle
    insideAngle = insideAngle % 180
    return insideAngle

def process():
    labels = os.listdir(txt_path)
    with open(os.path.join(save_path, "circles.csv"), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["文件名", "序号", "喷油角度", "喷油宽度", "喷油高度", "面积"])  # 写入表头
    for label in labels:
        if os.path.splitext(label)[-1] != '.txt':
            continue
        img = cv2.imread(os.path.join(img_path, os.path.splitext(label)[0] + '.jpg'))
        with open(os.path.join(txt_path, label), 'r') as f:
            detections = [line.strip().split() for line in f.readlines()]
        # print(img.shape)
        mask = np.full_like(img, (0, 0, 0))  # 创建一个与原始图像大小相同的掩码图像
        sh,sw = img.shape[0],img.shape[1]
        angle = 0
        num = 1
        for detection in detections:
            class_id = int(detection[0])
            labeldicts = []
            del detection[0]  # 删除第一个元素，保留坐标
            list__ = [detection[i:i + 2] for i in range(0, len(detection), 2)]  # 修改数组，两个一组[x,y]
            for i in list__:
                x = int(float(i[0]) * sw)
                y = int(float(i[1]) * sh)
                labeldicts.append([x, y])
            white_color = (255, 255, 255) # BGR
            if labeldicts[0] != labeldicts[len(labeldicts) - 1]:
                labeldicts[len(labeldicts) - 1] = labeldicts[0]
            po = np.array(labeldicts)
            cv2.fillPoly(mask, [po], white_color)  # 使用对象颜色填充多边形区域
            area=cv2.contourArea(contour=po,oriented=False)

            # 初始化最顶点、最低点、最左点和最右点
            highest_point = (np.inf, np.inf)
            lowest_point = (-np.inf, -np.inf)
            leftmost_point = (np.inf, np.inf)
            rightmost_point = (-np.inf, -np.inf)

            # 更新最顶点、最低点、最左点和最右点
            for point in po:
                x, y = point
                if y < highest_point[1]:
                    highest_point = (x, y)
                if y > lowest_point[1]:
                    lowest_point = (x, y)
                if x < leftmost_point[0]:
                    leftmost_point = (x, y)
                if x > rightmost_point[0]:
                    rightmost_point = (x, y)

            x, y, w, h = cv2.boundingRect(po)
            p1x = p2x = p1y = p2y = 0
            points = []
            if w > h:#横着的
                p1x = int(x + w / 2)
                p1y = y
                p2x = int(x + w / 2)
                p2y = y + h
                # cv2.rectangle(mask, (x, p1y), (p2x, p2y), (0, 0, 255), -1)

                for i in range(p1y, p2y):
                    if cv2.pointPolygonTest(po, (p1x, i), False) == 0:
                        cv2.circle(mask, (p1x, i), 2, (0, 255, 0), 2)
                        points.append((p1x, i))
                    elif (cv2.pointPolygonTest(po, (p1x, i - 1), False) < 0 and cv2.pointPolygonTest(po, (p1x, i), False) > 0) or (cv2.pointPolygonTest(po, (p1x, i - 1), False) > 0 and cv2.pointPolygonTest(po, (p1x, i), False) < 0):
                        cv2.circle(mask, (p1x, i), 2, (0, 255, 0), 2)
                        points.append((p1x, i))

                dd = rightmost_point
                if points[0][0] > sw / 2:
                    dd = rightmost_point
                else:
                    dd = leftmost_point

                cv2.circle(mask, dd, 2, (0, 255, 0), 2)

                cv2.line(mask, dd, points[0], (0, 0, 255), 2)
                cv2.line(mask, dd, points[1], (0, 0, 255), 2)

                L1 = Line(Point(dd[0], dd[1]), Point(points[0][0], points[0][1]))
                L2 = Line(Point(dd[0], dd[1]), Point(points[1][0], points[1][1]))
                angle = getAngle(L1, L2)
                cv2.putText(mask, f"A: {angle}", (dd[0] - 30, dd[1] - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.rectangle(mask, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(mask, f"W: {w}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                cv2.putText(mask, f"H: {h}", (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                cv2.putText(mask, f"N: {num} S:{area}", (x + w - 20, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            else:#竖着的
                p1x = x
                p1y = int(y + h / 2)
                p2x = x + w
                p2y = int(y + h / 2)
                # cv2.rectangle(mask, (x, y), (x + w, y + h), (0, 0, 255), 2)

                for i in range(p1x, p2x):
                    if cv2.pointPolygonTest(po, (i, p1y), False) == 0:
                        cv2.circle(mask, (i, p1y), 2, (0, 255, 0), 2)
                        points.append((i, p1y))
                    elif (cv2.pointPolygonTest(po, (i - 1, p1y), False) < 0 and cv2.pointPolygonTest(po, (i, p1y), False) > 0) or (cv2.pointPolygonTest(po, (i - 1, p1y), False) > 0 and cv2.pointPolygonTest(po, (i, p1y), False) < 0):
                        cv2.circle(mask, (i, p1y), 2, (0, 255, 0), 2)
                        points.append((i, p1y))

                dd = highest_point
                if points[0][1] > sh / 2 and h < sh / 2:
                    dd = lowest_point
                else:
                    dd = highest_point

                cv2.circle(mask, dd, 2, (0, 255, 0), 2)

                cv2.line(mask, dd, points[0], (0, 0, 255), 2)
                cv2.line(mask, dd, points[1], (0, 0, 255), 2)

                L1 = Line(Point(dd[0], dd[1]), Point(points[0][0], points[0][1]))
                L2 = Line(Point(dd[0], dd[1]), Point(points[1][0], points[1][1]))
                angle = getAngle(L1, L2)
                cv2.putText(mask, f"A: {angle}", (dd[0] - 30, dd[1] - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            # cv2.line(mask, (p1x, p1y), (p2x, p2y), (0, 0, 255), 2)

                cv2.rectangle(mask, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(mask, f"W: {w}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                cv2.putText(mask, f"H: {h}", (x + w + 10, y + (h // 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                cv2.putText(mask, f"N: {num} S:{area}", (x + w + 10, y + (h // 2) + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            with open(os.path.join(save_path, "circles.csv"), mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([os.path.splitext(label)[0], num, angle, w, h, area])  # 写入表头
            num += 1
        cv2.imwrite(os.path.join(save_path, os.path.splitext(label)[0] + '.jpg'), mask)

if __name__ == '__main__':
    process()
    print('Done!!')