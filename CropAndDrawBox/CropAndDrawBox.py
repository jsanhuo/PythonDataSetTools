import cv2
import os
from Utils import append_suffix_to_filename,apply_mosaic,getRect

img_extension = [".jpg",".png"]

def crop_and_draw_box(image_name, x, y, width, height, draw_output_path, crop_output_path, mosaic: list):
    image = None
    cur_extension = None
    for extension in img_extension:
        if image is None:
            image_path = image_name + extension
            image = cv2.imread(image_path)
            cur_extension = extension
        else:
            break
    if image is None:
        print("File Not Found!!!",image_name)
        return
    count = len(mosaic)
    i = 0
    while i < count:
        pt1 = mosaic[i] 
        pt2 = mosaic[i+1]
        mx,my,mwidth,mheight = getRect(pt1,pt2)
        apply_mosaic(image,mx,my,mwidth,mheight)
        i = i+2
    cropped_image = image[y : y + height, x : x + width]
    cv2.rectangle(image, (x, y), (x + width, y + height), (0, 0, 255), 2)
    cv2.imwrite(draw_output_path + cur_extension, image)
    cv2.imwrite(crop_output_path + cur_extension, cropped_image)




if __name__ == "__main__":
    dirpath = "D:\dataset\Prealrain"
    imgDirs = ["derain", "deraindetect", "rain", "raindetect"]
    # set image Name
    imgName = "241"
    x = 30
    y = 140
    width = 200
    height = width
    for imgDir in imgDirs:
        path = os.path.join(dirpath, imgDir, imgName)
        draw_output_path = os.path.join(dirpath, imgDir, append_suffix_to_filename(imgName,"_draw"))
        crop_output_path = os.path.join(dirpath, imgDir, append_suffix_to_filename(imgName,"_crop"))
        crop_and_draw_box(path, x, y, width, height, draw_output_path,crop_output_path,None)
