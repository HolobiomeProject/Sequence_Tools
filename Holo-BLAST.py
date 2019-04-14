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
#   4.) Wait for all BLAST searches to complete
#   5.) Enjoy the time you saved!
##########################################################################



#Dependancies
import os
import Bio
import pandas as pd
import tkinter as tk
from tkinter import *
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from tkinter import messagebox
from tkinter import filedialog
import xml.etree.ElementTree as ET

#tk already included in 3.7
#install Bio or biopython (not sure which its called for install)


#Function to Blast all sequences in a fasta file
def blast():
    #message to tell them to choose local folder to save to
    messagebox.showinfo("Local Folder Chooser", "Please Choose a LOCAL folder to save files to: Files cannot be written to the cloud")
    #folder to save to
    save_folder = filedialog.askdirectory()
    #Message box to tell them to choose the alignment fasta folder
    messagebox.showinfo("Alignment File Chooser", "Please Choose The Alignment File : File Must Be FASTA Format")
    #folder to direct to
    fasta = filedialog.askopenfilename()
    #Get the folder of interest entered by the user
    out_file_name = E1.get()
    #Create the outfile using the name provided by user
    out_file = open(out_file_name, "w+")
    #lists to be made into dataframe and output to csv
    #sequences
    seqs = []
    #holobiome names
    old_names = []
    #blast names (list of lists)
    bac = []
    #id in ncbi (list of lists)
    id = []
    #percent id (list of lists)
    pct = []
    #Go through the file and parse the sequences into a list
    with open(fasta, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            seqs.append(record.seq)
            old_names.append(record.id)
    #change directory to save folder
    os.chdir(save_folder)
    #main loop
    for j in range(0,len(seqs)):
        #list of names for this bug of interest
        names = []
        #list of ids for this bug of interest
        idd = []
        #blast the sequence
        one = NCBIWWW.qblast("blastn", "nt", seqs[j])
        #save the xml file
        with open(E1.get() +'.xml','w') as out_handle:
            out_handle.write(one.read())
        #parse the xml files
        tree = ET.parse(E1.get()+".xml")
        rootxml = tree.getroot()
        ################################################
        ################################################
        #iterate through xml file and get necessary info
        ################################################
        ################################################
        #get names of bacteria
        for bname in rootxml.iter('Hit_def'):
            #get first 10 names
            names.append(bname.text)
        #get ids
        for bname in rootxml.iter('Hit_id'):
            #get first 10 ids
            idd.append(bname.text)
        #get pct
        hsp_id = []
        hsp_alig = []
        for bname in rootxml.iter('Hsp_identity'):
            #add names to names list
            hsp_id.append(bname.text)
        for bname in rootxml.iter('Hsp_align-len'):
            #add names to names list
            hsp_alig.append(bname.text)
        #multiply values in pct by 100 to get percent (ex(91.35))
        mypct = []
        for i in range(0,len(hsp_id)):
            mypct.append((int(hsp_id[i])/int(hsp_alig[i]))*100)
        #add to list of lists of percents
        pct.append(mypct)
        #add list of names to the list of lists of names
        bac.append(names)
        #add list of idds to the list of idds
        id.append(idd)
        #delete the xml because we do not need it
        os.remove(E1.get()+'.xml')

    #Combine all list of lists into final form
    # print(id)
    # print (bac)
    # print(pct)
    flat = []
    for i in range(0, len(bac)):
        short = []
        for j in range(0, len(bac[i])):
            short.append(bac[i][j])
            short.append(pct[i][j])
            short.append(id[i][j])
        flat.append(short)
    #add the old names to it
    final = []
    for i in range(0, len(old_names)):
        k = [old_names[i]]+flat[i]
        final.append(k)
    final_df = pd.DataFrame(final)
    final_df = final_df.iloc[:,0:31]
    final_df.columns = ['Holobiome_Name', 'Bacteria Match 1', 'Percent ID 1', 'NCBI ID 1','Bacteria Match 2', 'Percent ID 2', 'NCBI ID 2','Bacteria Match 3', 'Percent ID 3', 'NCBI ID 3','Bacteria Match 4', 'Percent ID 4', 'NCBI ID 4','Bacteria Match 5', 'Percent ID 5', 'NCBI ID 5','Bacteria Match 6', 'Percent ID 6', 'NCBI ID 6','Bacteria Match 7', 'Percent ID 7', 'NCBI ID 7','Bacteria Match 8', 'Percent ID 8', 'NCBI ID 8','Bacteria Match 9', 'Percent ID 9', 'NCBI ID 9','Bacteria Match 10','Percent ID 10', 'NCBI ID 10']
    final_df.to_csv(E1.get()+'.csv',index = False)
    #final_df.to_csv(E1.get()+'.csv',index = False)
###################################################
# NEXT IS TO HAVE A DECIDING FACTOR FOR THE NAME TO CHOOSE
# ALSO, WE NEED TO LOOP THIS FOR ALL OF THE BUGS IN THE FASTA
###################################################
###################################################
    root.destroy()


#Tkinter window to gather info and run program
root = tk.Tk()
#shape of the tk window
root.geometry = ("100x50")
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
