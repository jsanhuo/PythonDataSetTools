# 删除文件文件夹a中存在在文件夹b的文件

import os

input = r"X:\623Label\2rename_shengyu"
target = r"X:\623Label\ok"

for file in os.listdir(input):
    if file.endswith('.jpg'):
        jpg_file = os.path.join(target, file)
        if os.path.exists(jpg_file):
            os.remove(os.path.join(input, file))
            print(file)