import os
from PIL import Image
import imghdr
def convert_to_jpg(folder_path):
    # 确保文件夹路径存在
    if not os.path.exists(folder_path):
        print("文件夹路径不存在")
        return

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # 检查文件是否为图像文件
        if os.path.isfile(file_path) and imghdr.what(file_path):
            # 打开图像文件
            image = Image.open(file_path)
            new_file_path = os.path.splitext(file_path)[0] + '.jpg'
            image.convert('RGB').save(new_file_path, 'JPEG')
            print(f"已转换 {file_path} 为 {new_file_path}")

    print("转换完成")

# 指定要转换的文件夹路径
folder_path = r'D:\dataset\mixdatave-up\test_mixrain_696'

# 调用函数进行转换
convert_to_jpg(folder_path)