import cv2
import os
import random

def getRect(pt1,pt2):
    x = min(pt1[0], pt2[0])
    y = min(pt1[1], pt2[1])
    width = abs(pt1[0] - pt2[0])
    height = abs(pt1[1] - pt2[1])
    return x, y, width, height

def apply_mosaic(image, x, y, width, height, block_size=5):
    roi = image[y:y+height, x:x+width]
    small_roi = cv2.resize(roi, (block_size, block_size), interpolation=cv2.INTER_LINEAR)
    flat_roi = small_roi.reshape(-1, 3)
    random.shuffle(flat_roi)
    shuffled_roi = flat_roi.reshape(small_roi.shape)
    mosaic_roi = cv2.resize(shuffled_roi, (width, height), interpolation=cv2.INTER_NEAREST)
    image[y:y+height, x:x+width] = mosaic_roi
    return image

def adjust_rectangle_aspect_ratio(x1, y1, x2, y2, target_aspect_ratio):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    if height == 0 or width == 0:
        return (int(x1), int(y1)), (int(x2), int(y2)) 
    current_aspect_ratio = width / height
    if current_aspect_ratio > target_aspect_ratio:
        # 宽度过大，根据目标宽高比调整高度
        target_height = width / target_aspect_ratio
        if y2 > y1:
            y2 = y1 + target_height
        else:
            y2 = y1 - target_height
    else:
        # 高度过大，根据目标宽高比调整宽度
        target_width = height * target_aspect_ratio
        if x2 > x1:
            x2 = x1 + target_width
        else:
            x2 = x1 - target_width

    return (int(x1), int(y1)), (int(x2), int(y2))

def openImg(imgPath):
    img_extension = [".jpg",".png"]
    cur_extension = ""
    image = None
    for extension in img_extension:
        if image is None:
            image_path = imgPath + extension
            image = cv2.imread(image_path)
            cur_extension = extension
        else:
            break
    return image,cur_extension

def append_suffix_to_filename(filename, suffix):
    name, extension = os.path.splitext(filename)
    new_filename = name + suffix + extension
    return new_filename
