#By: Barry Guglielmo


# Python 3.7.3
##########################################################################
# This code is written to compile multiple .nt files
# into a single .nt or .txt file that can then be used for
# alignment using MEGA.
#
# USE:
#   1.) Double Click Python Script
#   2.) Enter the name you want to save as
#           Ex. "DEMO.nt" ror .nt format, or "DEMO" for .txt format
#   3.) Click 'Zip Files'
#   4.) Select Folder .nt files are located
#   5.) Enjoy the time you saved!
##########################################################################
#Dependancies
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os

#Function to zip everything together
def zip_nt():
    #folder to direct to
    folder = filedialog.askdirectory()
    #Get the folder of interest entered by the user
    out_file_name = E1.get()
    #change the directory to said folder
    os.chdir(folder)
    #list the files in said folder
    ls = os.listdir()
    #Create the outfile using the name provided by user
    out_file = open(out_file_name, "w+")
    #Go through the file list
    for i in ls:
        #observe only the .nt files of interest
        if '.nt' in i:
            #read the file
            file = open(i)
            #check point for name of seq
            k = 0
            for j in file:
                #check the first line
                if k == 0:
                    #if the name in of the seq does not match the name of the file
                    #change the name of the seq to equal the name of the file, else, stay the same
                    if j != i[:-3]:
                        out_file.write('>'+str(i[:-3])+'\n')
                    else:
                      out_file.write(j)
                    #add 1 to k because we are no longer on the first line
                    k+=1
                #all the other lines after the first
                else: 
                    out_file.write(j)
            #always close a file when you are done
            file.close()
    #close the outfile we created
    out_file.close()
    #close the tk window
    root.destroy()


#Tkinter window to gather info and run program
root = tk.Tk()
#shape of the tk window
root.geometry = ("20x10")
#Label the text field for the outfile
L1 = Label(root, text="Save As: ")
L1.pack()
#Entry space for the outfile name
E1 = Entry(root, bd =10)
E1.pack()
#Submit/Run button labeled compile files
B1 = Button(root, text = "Zip Files", command = zip_nt)
B1.pack()
#the main loop for the window we created
root.mainloop()





