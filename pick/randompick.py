import os
import random
import shutil

def pick_and_delete_files(folder_input_path,folder_target_path,val_input,val_target, num_files):
    files = os.listdir(folder_input_path)

    if len(files) < num_files:
        print("文件夹中的文件数量不足。")
        return

    files_to_delete = random.sample(files, num_files)

    # 删除文件
    for file_name in files_to_delete:
        source_path = os.path.join(folder_input_path, file_name)
        target_path = os.path.join(val_input, file_name)
        shutil.move(source_path, target_path)
        # shutil.copy(source_path, target_path)
        
        source_path = os.path.join(folder_target_path, file_name)
        target_path = os.path.join(val_target, file_name)
        shutil.move(source_path, target_path)
        # shutil.copy(source_path, target_path)
        

# 指定文件夹路径和要挑选的文件数量
folder_input_path = r"F:\dataset\yuwu\rain_streak_raindrop_hazy\input"
folder_target_path = r"F:\dataset\yuwu\rain_streak_raindrop_hazy\target"
val_input = r"F:\dataset\yuwu\test_rain_streak_raindrop_hazy\input"
val_target = r"F:\dataset\yuwu\test_rain_streak_raindrop_hazy\target"
num_files = 1000

# 调用函数进行挑选和删除文件
pick_and_delete_files(folder_input_path,folder_target_path,val_input,val_target, num_files)