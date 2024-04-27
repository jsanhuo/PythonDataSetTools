import os

def compare_folders(folder1, folder2):
    files1 = set([os.path.splitext(file)[0] for file in os.listdir(folder1) if os.path.isfile(os.path.join(folder1, file))])
    files2 = set([os.path.splitext(file)[0] for file in os.listdir(folder2) if os.path.isfile(os.path.join(folder2, file))])

    files_only_in_folder1 = files1 - files2
    files_only_in_folder2 = files2 - files1

    print("Files only in", folder1, ":", files_only_in_folder1)
    print("Files only in", folder2, ":", files_only_in_folder2)


# 两个文件夹的路径
folder1_path = r'D:\PyCode\RT-DETRProject\RTDETR-main\dataset\labels\test_veh'
folder2_path = r'D:\PyCode\RT-DETRProject\RTDETR-main\dataset\images\test_veh'

compare_folders(folder1_path, folder2_path)