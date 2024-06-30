import os
 
def traverse_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            print(os.path.join(root, file))
 
# 使用示例
traverse_files(r'Z:/')