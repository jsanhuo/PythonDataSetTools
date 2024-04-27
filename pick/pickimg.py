import os
import shutil
depths = ['S80','S85','S90','S95','S100']
hazes = ['a04','a05','a06']
def pick_files(folder_clear, folder_haze,folder_clear_pick,folder_haze_pick):
    for filename in os.listdir(folder_clear):
        if filename.endswith('.png'): 
            for depth in depths:
                for haze in hazes:
                    new_filename = filename.replace('.png', '_'+str(depth)+"_"+str(haze)+".png")
                    clear_source_path = os.path.join(folder_clear, filename)
                    clear_target_path = os.path.join(folder_clear_pick, new_filename)
                    shutil.copyfile(clear_source_path, clear_target_path)
                    print(clear_source_path,"->",clear_target_path)
                    haze_source_path = os.path.join(folder_haze, new_filename)
                    haze_target_path = os.path.join(folder_haze_pick, new_filename)
                    shutil.copyfile(haze_source_path, haze_target_path)
                    print(haze_source_path,"->",haze_target_path)


# 文件夹a和文件夹a1路径
clear = r"F:\dataset\data\gt"
haze = r"F:\dataset\data\in"

# 文件夹b和文件夹b1路径
clear_pick = r"F:\dataset\yuwu\yu\train\input"
haze_pick = r"F:\dataset\yuwu\yu\train\target"

pick_files(clear,haze,clear_pick,haze_pick)