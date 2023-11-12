import cv2
import os


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
