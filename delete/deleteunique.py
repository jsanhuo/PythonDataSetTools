# 删除没有对应json文件的图片
import os

path = r"X:\623Label\beiyong2"

for file in os.listdir(path):
    if file.endswith('.jpg'):
        json_file = os.path.join(path, file.replace('.jpg', '.json'))
        if not os.path.exists(json_file):
            os.remove(os.path.join(path, file))
            print(file)
    if file.endswith('.json'):
        jpg_file = os.path.join(path, file.replace('.json', '.jpg'))
        if not os.path.exists(jpg_file):
            os.remove(os.path.join(path, file))
            print(file)