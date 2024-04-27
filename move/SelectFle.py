import os
import shutil

# 定义源文件夹路径
folder1_path = r'C:\Users\JiaoYan\Documents\WeChat Files\wxid_zzzv5l5ji05k22\FileStorage\File\2024-02\ophaze'
folder2_path = r'F:\dataset\WTC-realhaze'
folder3_path = r'F:\dataset\WTC-realhaze-out'

# 创建目标文件夹
output_folder1 = r'F:\dataset\ophaze-or'
output_folder2 = r'F:\dataset\ophaze-out'
os.makedirs(output_folder1, exist_ok=True)
os.makedirs(output_folder2, exist_ok=True)

# 获取文件夹1中的文件列表
folder1_files = os.listdir(folder1_path)

# 从文件夹2中选择相应的文件并复制到目标文件夹1
for file in folder1_files:
    source_file = os.path.join(folder2_path, file)
    if os.path.isfile(source_file):
        shutil.copy(source_file, output_folder1)

# 从文件夹3中选择相应的文件并复制到目标文件夹2
for file in folder1_files:
    source_file = os.path.join(folder3_path, file)
    if os.path.isfile(source_file):
        shutil.copy(source_file, output_folder2)