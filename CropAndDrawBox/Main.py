import cv2
import os
from Utils import *
from CropAndDrawBox import *
refPt = []
cropping = False
aspectRatio = 1

def click_and_crop(event, x, y, flags, param):
    global refPt, cropping

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True

    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False
        p1,p2 = adjust_rectangle_aspect_ratio(refPt[0][0],refPt[0][1],refPt[1][0],refPt[1][1],aspectRatio)
        refPt.clear()
        refPt.append(p1)
        refPt.append(p2)
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)
    elif event == cv2.EVENT_RBUTTONDOWN:
        pass
    elif event == cv2.EVENT_RBUTTONUP:
        pass

if __name__ == "__main__":
    dirpath = "D:\dataset\Prealrain"
    imgDirs = ["derain", "deraindetect", "rain", "raindetect"]
    imgName = "241"
    imgPath = os.path.join(dirpath,imgDirs[1],imgName)
    print(imgPath)
    image,extension = openImg(imgPath)
    assert image is not None
    clone = image.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)
    # 显示图片
    while True:
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF
        # 按 "r" 键重置选择
        if key == ord("r"):
            image = clone.copy()
        # 按 "c" 键完成选择
        elif key == ord("c"):
            x = min(refPt[0][0], refPt[1][0])
            y = min(refPt[0][1], refPt[1][1])
            width = abs(refPt[0][0] - refPt[1][0])
            height = abs(refPt[0][1] - refPt[1][1])
            for imgDir in imgDirs:
                path = os.path.join(dirpath, imgDir, imgName)
                draw_output_path = os.path.join(dirpath, imgDir, append_suffix_to_filename(imgName,"_draw"))
                crop_output_path = os.path.join(dirpath, imgDir, append_suffix_to_filename(imgName,"_crop"))
                crop_and_draw_box(path, x, y, width, height, draw_output_path,crop_output_path)
            break
    cv2.destroyAllWindows()
    
    
