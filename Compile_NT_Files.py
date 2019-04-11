#By: Barry Guglielmo


# Python 3.7.3
# This code is written to take zip multiple .nt files
# into a single .nt file that can then be used for
# alignment using MEGA.
#
# USE:
#   1.) Double Click Python Script
#   2.) Enter the name you want to save as
#           Ex. "DEMO.nt"
#   3.) Click 'Zip Files'
#   4.) Select Folder .nt files are located
#   5.) Enjoy the time you saved!


import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os

#Function to zip everything together
def zip_nt():
    folder = filedialog.askdirectory()
    out_file_name = E1.get()
    os.chdir(folder)
    ls = os.listdir()
    out_file = open(out_file_name, "w+")
    for i in ls:
        if '.nt' in i:
            file = open(i)
            k = 0
            for j in file:
                if k == 0:
                    if j != i[:-3]:
                        out_file.write('>'+str(i[:-3])+'\n')
                    else:
                      out_file.write(j)
                    k+=1
                else: 
                    out_file.write(j)
            file.close()
    out_file.close()
    root.destroy()


#Tkinter window to gather info and run program
root = tk.Tk()
root.geometry = ("20x10")
L1 = Label(root, text="Save As: ")
L1.pack()
E1 = Entry(root, bd =10)
E1.pack()
out_file_name = E1.get()
B1 = Button(root, text = "Zip Files", command = zip_nt)
B1.pack()
root.mainloop()





