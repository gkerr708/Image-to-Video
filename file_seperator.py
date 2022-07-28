import cv2, os, numpy as np, shutil
from time import sleep 
from tqdm import tqdm
from datetime import datetime 
from tqdm import tqdm


mainDirectory = os.path.dirname(os.path.realpath(__file__))
imgFolderDirectory = r"C:\Users\Gavin's XPS 13\Desktop"
imgFolderName = r"2022-07-26"
imgFolder = os.path.join(imgFolderDirectory, imgFolderName)

parentFolderDirectory = r"C:\Users\Gavin's XPS 13\Desktop\vs-code\Image-to-Video"
parentFolderName = rf"{imgFolderName}_organized"
parentFolder = os.path.join(parentFolderDirectory, parentFolderName)


allFiles = os.listdir(imgFolder)

# Gets a list of all of the names that will soon be sub folders
subFolderNames = []
for i, file in enumerate(allFiles):
    subFolderNames.append(file[:9])
subFolderNames = np.unique(np.array(subFolderNames))

# Creates the "parentFolder" 
if not os.path.exists(parentFolder):
    os.makedirs(parentFolder)
else:
    print(f"\nFolder: '{parentFolder}' already exists\n")
    x = input("Would you like to delete this folder and create new? [y/n]: ")
    if x == 'y':
        shutil.rmtree(parentFolder)
        #os.remove(parentFolder) # think this was giving me the permission error
        os.makedirs(parentFolder)
    
# Creats subfolder for each name in the "subFolderNames" list 
for i, subFolderName in enumerate(subFolderNames):
    if not os.path.exists(subFolderName):
        subFolder = os.path.join(parentFolder, subFolderName)
        os.makedirs(subFolder)
    else:
        print(f"\nSub-Folder: '{subFolder}' already exists\n")



print("\nStarting...\n")
pbar = tqdm(total=100)
for i, subFolderName in enumerate(subFolderNames): # This should be really fast :(
    for file in allFiles:
        if file[:9] == subFolderName:
            for imgIndex in range(500):
                pbar.update(100/(len(subFolderNames)*len(allFiles)*500))
                name = f"{file[:9]}_{imgIndex}.bmp"
                try:
                    shutil.copy(os.path.join(imgFolder, name), os.path.join(parentFolder, subFolderName))
                except FileNotFoundError:
                    print(f"\nCouldn't find file: '{name}'\n")
                    pass
pbar.close()

