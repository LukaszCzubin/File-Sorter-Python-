import os
import shutil

Original_Folder = "C:\\Users\\lukas\\Desktop\\Pliki"

print(os.listdir(Original_Folder))

file_types = {
    ".jpg":"Obrazy",
    ".png":"Obrazy png",
    ".txt":"Pliki tekstowe"
}

for file in os.listdir(Original_Folder):
    file_extension = os.path.splitext(file)[1]
    file_path = os.path.join(Original_Folder, file)
    if file_extension in file_types:
        new_path = os.path.join(Original_Folder, file_types[file_extension])
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        shutil.move(file_path, new_path)
        print(f"Przeniesiono plik {file} do folderu {file_types[file_extension]}")



    

