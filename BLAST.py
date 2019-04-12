#By: Barry Guglielmo


# Python 3.7.3
##########################################################################
# This code is written to blast a series of aligned sequences
# The output will be:
#           Lab Seq Name : NCBI Blast Name
# This will be saved into a CSV file
# USE:
#   1.) Double Click Python Script
#   2.) Enter the name you want to save as
#           Ex. "DEMO"
#   3.) Click 'BLAST'
#   4.) Select Folder .nt files are located
#   5.) Enjoy the time you saved!
##########################################################################



#Dependancies
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import os
import Bio
from Bio.Blast import NCBIWWW
from Bio import SeqIO


#tk already included in 3.7
#install Bio or biopython (not sure which its called for install)


#Function to zip everything together
def blast():
    #message to tell them to choose local folder to save to
    messagebox.showinfo("Local Folder Chooser", "Please Choose a LOCAL folder to save files to: Files cannot be written to the cloud")
    #folder to save to
    save_folder = filedialog.askdirectory()
    #Message box to tell them to choose the alignment fasta folder
    messagebox.showinfo("Alignment File", "Please Choose The Alignment File : File Must Be FASTA Format")
    #folder to direct to
    fasta = filedialog.askopenfilename()
    #Get the folder of interest entered by the user
    out_file_name = E1.get()
    #Create the outfile using the name provided by user
    out_file = open(out_file_name, "w+")
    #Sequence list
    seqs = []
    old_names = []
    #Go through the file and parse the sequences into a list
    with open(fasta, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            seqs.append(record.seq)
            old_names.append(record.id)
    one = NCBIWWW.qblast("blastn", "nt", seqs[0])
    os.chdir(save_folder)
    with open(E1.get() +'.xml','w') as out_handle:
        out_handle.write(one.read())
    import xml.etree.ElementTree as ET
    tree = ET.parse(E1.get()".xml")
    root = tree.getroot()
    bac = []
    id = []
    i = 0
    for hitnum in root.iter('Hit_id'):
        while i < 1:
            id.append(hitnum.text)
            i+=1
    i=0
    for hitnum in root.iter('Hit_def'):
        while i < 3:
            bac.append(hitnum.text)
            i+=1
###################################################
NEXT IS TO HAVE A DECIDING FACTOR FOR THE NAME TO CHOOSE
ALSO, WE NEED TO LOOP THIS FOR ALL OF THE BUGS IN THE FASTA
###################################################
###################################################
    print(minidom.parse(E1.get()+'.xml'))

    print(one.read())
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
B1 = Button(root, text = "BLAST", command = blast)
B1.pack()
#the main loop for the window we created
root.mainloop()
