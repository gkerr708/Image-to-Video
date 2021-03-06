import cv2, os
from time import sleep 
from tqdm import tqdm
from datetime import datetime 

def vidify(image_folder, fps = 1, save_location = 'default', save_file = None): # I think save location should just be a folder 

    data_and_time = datetime.now()
    t1 = data_and_time.strftime("%H-%M-%S") # returns the time as a string 
    d1 = data_and_time.strftime("%Y-%m-%d") # returns the data as a string

    program_dir = os.path.dirname(os.path.realpath(__file__)) # stores the filepate where the main python files are being stored

    # Change image_folder to the directory of the image folder
    #image_folder = r"C:\Users\gkerr\Desktop\vs-code\Lab Data\image_processing\Kerr fiber imaging"  
    if save_location == 'default':
        video_folder = fr"{program_dir}\{d1}_{t1}_vid"
    else:
        video_folder = os.path.join(save_location, save_file)
    old_file = fr"{program_dir}\video.avi" 
    video_name = r"video.avi"

    if not os.path.exists(video_folder):
        os.makedirs(video_folder)
    else:
        print("\nvideo path already exists\n")


    images = [img for img in os.listdir(image_folder) if img.endswith(".bmp")] # take all of the images which ends with ".bmp" and appends them to a list
    images_50 = [img for img in os.listdir(image_folder) if img.startswith("50")] # creates a seperate list for each of the 4 concentrations
    images_45 = [img for img in os.listdir(image_folder) if img.startswith("45")]
    images_40 = [img for img in os.listdir(image_folder) if img.startswith("40")]
    images_35 = [img for img in os.listdir(image_folder) if img.startswith("35")]

    speeds  = ['400', '200', '100', '050'] # creates a list of the 4 different speeds used in the trials 
    concentrations = [images_50, images_45, images_40, images_35] # creates a list where each element in the list is of list of images for each concentration
    trials = ['01', '02', '03', '04', '05', '06', '07'] # creates a list which allows the program to further seperate everything 

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    list1 = []

    try:
        os.remove(old_file)
        print("\n\nThere was an old file that needed to be removed\n")
    except:
        pass

    pbar = tqdm(total = 100)

    for i, concentration in enumerate(concentrations):

        for ii, speed in enumerate(speeds):
            list1.append([x for x in concentration if speed in x])
            list1 = [j for sub in list1 for j in sub] #this changes the list form 2D to 1D 

            for iiii, trial in enumerate(trials):
                pbar.update(100/(len(concentrations)*len(speeds)*len(trials)))

                list2 = [y for y in list1 if y.endswith(f"{trial}.bmp")] ####### INCOMPLETE
                
                video = cv2.VideoWriter(video_name, 0, fps, (width,height))
                for iii, img in enumerate(list2):
                    video.write(cv2.imread(os.path.join(image_folder, img)))
                cv2.destroyAllWindows()
                video.release()

                x = concentration[0]
                x = x[:2] #this just gives the first two values of the first filename in the list. This is the concentration
                new_file = fr"{video_folder}\{x}_{speed}_{trial}.avi"

                try:
                    os.rename(old_file, new_file)
                    if os.path.getsize(new_file)<1000000:
                        os.remove(new_file)
                except FileExistsError:
                    print("shit got fucked up ")

                list2 = []
            list1 = []