# 输入一个文件，将里面的中文文件名改为拼音文件名

import os
import re
import py

import shutil
from pypinyin import pinyin, Style


from PIL import Image

        
def tif2jpg(tif_path, jpg_path):
    # 将tif文件转为jpg文件
    im = Image.open(tif_path)
    im.save(jpg_path)
    
    print(tif_path, '==>', jpg_path)


def to_pinyin(text):
    return ''.join([j for i in pinyin(text, style=Style.NORMAL) for j in i])

intput = r'X:\623Label\2'
output = r'X:\623Label\2rename'

# 遍历input文件夹下的所有文件
for root, dirs, files in os.walk(intput):
    for file in files:
        # 获取文件的绝对路径
        file_path = os.path.join(root, file)
        # 获取文件的扩展名
        file_extension = os.path.splitext(file)[1]
        # 获取文件名
        file_name = os.path.splitext(file)[0]
        # 将文件名改为拼音
        file_name = to_pinyin(file_name)
        new_file_name = file_name + ".jpg"
        # 将文件名改为拼音后的绝对路径
        new_file_path = os.path.join(output, new_file_name)
        
        # 去除文件名中的中文逗号
        new_file_path = new_file_path.replace('，', '_')
        new_file_path = new_file_path.replace(',', '_')
        new_file_path = new_file_path.replace(' ', '_')
        
        # 将文件从原路径移动到新路径
        # shutil.copy(file_path, new_file_path)
        
        tif2jpg(file_path, new_file_path)
        # print(file_path, '==>', new_file_path)
        
        
