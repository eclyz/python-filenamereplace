import os

for filename in os.listdir("."): //current directory
    print(filename)
    a = filename.replace("jpg", "jpeg") //jpg to jpeg
    os.rename(filename,a)


