import os

def delete_files_with_rain(folder_path):
    deleteNames = {"jpg"};
    for deleteName in deleteNames:
        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                if deleteName in file_name:
                    file_path = os.path.join(root, file_name)
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")

# 指定要删除文件的文件夹路径
folder_path = r"X:\20240425DetEXP\DET\real300\de"
# 调用函数删除文件
delete_files_with_rain(folder_path)

folder_path = r"X:\20240425DetEXP\DET\rid\de"
delete_files_with_rain(folder_path)