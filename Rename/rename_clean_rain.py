import os

def delete_files_with_rain(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if "_clean" in file_name:
                file_path = os.path.join(root, file_name)
                new_file_path = file_path.replace("_clean","_rain")
                os.rename(file_path,new_file_path)
                print(f"rename file: {file_path} ->{new_file_path}")

# 指定要删除文件的文件夹路径
folder_path = r"F:\dataset\raindrop_861\target"

# 调用函数删除文件
delete_files_with_rain(folder_path)