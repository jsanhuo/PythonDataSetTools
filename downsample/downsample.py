import os
from PIL import Image

def downsample_images(input_folder, output_folder, downsample_factor):
    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的图像文件
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # 打开图像
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)
            
            # 检查图像尺寸是否大于1000x1000，大于1000x1000的图像才进行下采样
            if image.width <= 640 and image.height <= 640:
                # 构建保存路径
                output_path = os.path.join(output_folder, filename)
                # 保存下采样后的图像
                image.save(output_path)
                print(f"Downsampled {filename} and saved to {output_path}")
            else:
                # 将图片下采样到1000x1000以下，保证宽高比
                if image.width > 640:
                    new_width = 640
                    new_height = int(image.height * 640 / image.width)
                else:
                    new_width = int(image.width * 640 / image.height)
                    new_height = 640
                
                image = image.resize((new_width, new_height), Image.ANTIALIAS)
                
                # 构建保存路径
                output_path = os.path.join(output_folder, filename)

                # 保存下采样后的图像
                image.save(output_path)

                print(f"Downsampled {filename} and saved to {output_path}")

# 使用示例
input_folder = r"X:\20240425DetEXP\SR\rid\big"
output_folder = r"X:\20240425DetEXP\SR\rid\input"
downsample_factor = 4  # 设置下采样因子

downsample_images(input_folder, output_folder, downsample_factor)