from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time 


def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpeg')])
    if file_path is not None:
        pass



master = Tk()

w = Canvas(master, width=100, height=100)
w.grid(row = 0, column = 0)

var1 = IntVar()
Checkbutton(master, text='check button 1', variable=var1).grid(row = 1, column = 0)
var2 = IntVar()
Checkbutton(master, text='check button 2', variable=var2).grid(row = 1, column = 1)

Label(master, text='First Name').grid(row = 2, column = 0)
Label(master, text='Last Name').grid(row = 2, column = 1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row = 3, column = 0)
e2.grid(row = 3, column = 1)

w = Canvas(master, width=100, height=100)
w.grid(row = 4, column = 0)

file_button = Button(master, text='Import File', width = 25, command = lambda:open_file())

exit_button = Button(master, text='Exit', width=25, command=master.destroy)
exit_button.grid(row = 5, column = 0)

mainloop()