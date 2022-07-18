from tkinter import * 
from tkinter.ttk import *
from tkinter import filedialog
import time
from img_to_vid import vidify
import tkinter.messagebox
import customtkinter as ctk
import os
from PIL import Image, ImageTk 
#to change to .exe type in cmd: pyinstaller --onefile main.py

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

PATH = os.path.dirname(os.path.realpath(__file__))

root = ctk.CTk()
root.geometry("350x160")
root.title('FLD-Generator')

def browseFiles():
    dir = filedialog.askdirectory()
    vidify(dir) 

img = ImageTk.PhotoImage(Image.open(r"test_images\3dBiofibr.png"))
imgLabel = Label(root, image = img)
imgLabel.configure(background='gray')
imgLabel.grid(row=0, column=0, padx=20, pady=20, sticky="n")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1, minsize=200)

#creating file explorer button
image_size = 50
add_folder_image = ImageTk.PhotoImage(Image.open(PATH + "/test_images/add-folder.png").resize((image_size, image_size), Image.ANTIALIAS))

button_1 = ctk.CTkButton(root, image=add_folder_image, text="Select Image Folder ", width=190, height=40,
                                   compound="right", command=browseFiles)
button_1.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

root.mainloop()