import os

def delete_non_jpg_files(folder_path):
    # 确保文件夹路径存在
    if not os.path.exists(folder_path):
        print("文件夹路径不存在")
        return

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # 检查文件是否为文件夹
        if os.path.isdir(file_path):
            # 递归调用，处理子文件夹
            delete_non_jpg_files(file_path)
        else:
            # 检查文件是否为非 JPG 文件且不是 TXT 文件
            if not filename.lower().endswith('.jpg') and not filename.lower().endswith('.txt'):
                # 删除非 JPG 文件
                os.remove(file_path)
                print(f"已删除文件: {file_path}")

    print("删除完成")

# 指定要删除文件的文件夹路径
folder_path = r'D:\dataset\mixdatave-up\test_mixderain_696'

# 调用函数删除非 JPG 文件但排除 TXT 文件
delete_non_jpg_files(folder_path)