import cv2
import os
import json
from shapely.geometry import Polygon, Point, LineString
from shapely.ops import unary_union
def convert_gray(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray

def p_img(image):
    # 读取图像
    _, thresh = cv2.threshold(image, 30, 255, cv2.THRESH_BINARY)
    thresh = cv2.bitwise_not(thresh)
    return thresh

def main():
    floderPath = r"E:\704data\alloil2";
    output_path = r"E:\704data\out";
    i = 0
    p = 0
    for file in os.listdir(floderPath):
        i += 1
        if file.endswith(".jpg") and not file.endswith("_thresh.jpg"):
            image_path = os.path.join(floderPath, file)
            gray = convert_gray(image_path)
            thresh = p_img(gray)
            thresh = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
            # 将文件名后缀改为_thresh.jpg
            file_name_list = file.split(".")[:-1]
            # 将list转为str
            file_name_str = '.'.join(file_name_list)
            file_new_name = file_name_str + "_thresh.jpg"
            cv2.imwrite(os.path.join(output_path, file_new_name), thresh)
            p += 1
    print("total:", i)
    print("processed:", p)

if __name__ == '__main__':
    main()