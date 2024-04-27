import os

def save_png_filenames(folder_path, output_file):
    # 确保文件夹路径存在
    if not os.path.exists(folder_path):
        print("文件夹路径不存在")
        return

    # 遍历文件夹中的所有文件
    png_filenames = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # 检查文件是否为 PNG 文件
        if os.path.isfile(file_path) and (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')):
            # 获取文件名的部分，不包含文件后缀
            png_filenames.append(filename)

    # 将 PNG 文件名保存到 TXT 文件中
    if png_filenames:
        with open(output_file, 'w') as f:
            for filename in png_filenames:
                f.write("rainy\\"+filename + '\n')
        print(f"已保存 PNG 文件名到 {output_file}")
    else:
        print("文件夹中没有 PNG 文件")

# 指定要操作的文件夹路径
folder_path = r'F:\dataset\PromptIRData\Derain\rainy'

# 指定保存 PNG 文件名的 TXT 文件路径
output_file = r'C:\Users\JiaoYan\Documents\gitDC\PromptIR\data_dir\rainy\rainTrain.txt'

# 调用函数保存 PNG 文件名到 TXT 文件
save_png_filenames(folder_path, output_file)