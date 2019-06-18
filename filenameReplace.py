import os

for filename in os.listdir("."):
    print(filename)
    a = filename.replace("jpg", "jpeg")
    os.rename(filename,a)


