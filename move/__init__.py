import os
import shutil

def combine_folders(folder_a, folder_b, folder_c, folder_d):
    output_folder = r"D:\RainExp\dataset\test\Test1500"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    input_folder = os.path.join(output_folder, "input")
    target_folder = os.path.join(output_folder, "target")
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # 获取文件夹中的文件列表
    fiels_a_input = os.path.join(folder_a, "input")
    files_a_target = os.path.join(folder_a, "target")

    files_b_input = os.path.join(folder_b, "input")
    files_b_target = os.path.join(folder_b, "target")

    files_c_input = os.path.join(folder_c, "input")
    files_c_target = os.path.join(folder_c, "target")

    files_d_input = os.path.join(folder_d, "input")
    files_d_target = os.path.join(folder_d, "target")

    files_input = [fiels_a_input, files_b_input, files_c_input, files_d_input]
    files_target = [files_a_target, files_b_target, files_c_target, files_d_target]

    for i, files_folder in enumerate(files_input):
        files = [f for f in os.listdir(files_folder) if os.path.isfile(os.path.join(files_folder, f))]
        for j, file_name in enumerate(files):
            new_file_name = f"{i}_{file_name}"
            shutil.copy2(os.path.join(files_folder, file_name), os.path.join(input_folder, new_file_name))

    for i, files_folder in enumerate(files_target):
        files = [f for f in os.listdir(files_folder) if os.path.isfile(os.path.join(files_folder, f))]
        for j, file_name in enumerate(files):
            new_file_name = f"{i}_{file_name}"
            shutil.copy2(os.path.join(files_folder, file_name), os.path.join(target_folder, new_file_name))

    print("文件夹组合完成！")

# 用法示例
combine_folders(r"D:\RainExp\dataset\test\Test1200", r"D:\RainExp\dataset\test\Test100", r"D:\RainExp\dataset\test\Rain100L", r"D:\RainExp\dataset\test\Rain100H")