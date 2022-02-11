import os

# get list of file/folder in certain path (os.listdir)
# find whether certain string in file name (file.find)
# replace and rename the file (file.replace, os.rename)

path = "C:\\Users\scakwoo\Desktop\[SVL003863] Go Mobile Octo Card\Documents\Testing\Vedi"

file_list = os.listdir(path)
print(file_list)
old_text = input("Old name to be replaced")
new_text = input("New name")

for file in file_list:
    print(file)
    existing = file.find(old_text)
    # print(existing)
    if existing > -1:
        os.rename(os.path.join(path, file), os.path.join(path, file.replace(old_text, new_text)))

