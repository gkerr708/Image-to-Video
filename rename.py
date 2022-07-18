import os

#path = r"C:\Users\gkerr\Desktop\vs-code\Lab Data\Kerr fiber imaging"
path = r"C:\Users\Gavin's XPS 13\Desktop\Kerr fiber imaging"
files = os.listdir(path)

for index, file in enumerate(files):
    size = len(file)
    newFile = file[:size-18]
    newFile = newFile + ".bmp"
    try:
        os.rename(os.path.join(path, file), os.path.join(path, newFile))
    except:
        print(f"File: {file} has been deleted")
        os.remove(os.path.join(path,file))
