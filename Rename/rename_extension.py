import os
def rename_files(directory, new_extension):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            name, extension = os.path.splitext(filename)
            if extension != new_extension:
                new_filename = name + new_extension
                src = os.path.join(directory, filename)
                dst = os.path.join(directory, new_filename)
                os.rename(src, dst)
                print(f"Renamed file: {filename} -> {new_filename}")

directory = r'D:\dataset\mixdatave-up\test_mixderain_696'
new_extension = '.jpg'

rename_files(directory, new_extension)