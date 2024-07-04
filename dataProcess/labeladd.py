import os  
# 指定文件夹路径  
folder_A = r'E:\704data\testhebing\liqout'  
folder_B = r'E:\704data\testhebing\gasout'  
folder_C = r'E:\704data\testhebing\gasliqout'


if not os.path.exists(folder_B):  
    os.makedirs(folder_B)  

for filename in os.listdir(folder_A):  
    if filename.endswith('.txt'):  
        # 构造A文件夹中文件的完整路径  
        source1_path = os.path.join(folder_A, filename)  
        # 读取文件内容  
        with open(source1_path, 'r', encoding='utf-8') as file:  
            content1 = file.read()  
        # 读取B文件内容
        source2_path = os.path.join(folder_B, filename)  
        with open(source2_path, 'r', encoding='utf-8') as file:  
            content2 = file.read()
        
        des_path = os.path.join(folder_C, filename)
        with open(des_path, 'a', encoding='utf-8') as file:
            file.write(content1)  
            file.write(content2)
        
        print(f'Appended "{filename}" content from "{source1_path} and {source2_path}" to "{des_path}".')