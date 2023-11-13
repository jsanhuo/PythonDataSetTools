import os

def rename_files(folder_path):
    file_list = os.listdir(folder_path)
    file_list.sort()  # 确保文件按照字母顺序排序

    index = 1
    for file_name in file_list:
        file_extension = os.path.splitext(file_name)[1]  # 获取文件扩展名
        new_file_name = str(index) + file_extension
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)
        os.rename(old_file_path, new_file_path)
        index += 1

# 示例用法
folder_path = './addrain/'  # 替换为目标文件夹路径
rename_files(folder_path)