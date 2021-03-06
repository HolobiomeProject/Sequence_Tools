#By Barry Guglielmo
# This code is writen with Python 3.6
# The functions in this package serve to aid in manipulating fasta and MultiFASTA files

#Dependancies
import os
import pandas as pd
from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

#Function to Combine all Fasta in file
def multifasta(file_type, change_contig_name = True):
    '''Concatinate Multiple FASTAs to a Multifasta\n(to concat multiple multifastas set change_name = False)'''
    #folder to direct to
    folder = filedialog.askdirectory()
    #Get the folder of interest entered by the user
    out_file_name = str(datetime.now().strftime("%y-%m-%d-%H-%M"))+'-multifasta.txt'
    #change the directory to said folder
    os.chdir(folder)
    #list the files in said folder
    ls = os.listdir()
    #Create the outfile using the name provided by user
    out_file = open(out_file_name, "w+")
    #Go through the file list
    first = True
    for i in ls:
        #observe only the .nt files of interest
        if str(file_type) in i:
            #read the file
            file = open(i)
            #check point for name of seq
            k = 0
            for j in file:
                #check the first line
                if k == 0:
                    #if the name in of the seq does not match the name of the file
                    #change the name of the seq to equal the name of the file, else, stay the same
                    if j != i[:-len(file_type)] and change_contig_name == True and first ==False:
                        out_file.write('\n>'+str(i[:-(len(file_type))])+'\n')
                    elif j != i[:-len(file_type)] and change_contig_name == True and first ==True:
                        out_file.write('>'+str(i[:-(len(file_type))])+'\n')
                        first = False

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
    messagebox.showinfo("Complete", "Your MultiFASTA is Complete :)\nName of File:  "+out_file_name)

def prefix(prefix, file_type, contigs_too = False):
    '''Add Prefix to Files of Interest'''
    folder = filedialog.askdirectory()
    #change the directory to said folder
    os.chdir(folder)
    #list the files in said folder
    ls = os.listdir()
    os.mkdir(prefix)
    pf = folder+'/'+prefix
    #Go through the file list
    for i in ls:
        #observe only the .nt files of interest
        if str(file_type) in i:
            os.chdir(pf)
            #Get the folder of interest entered by the user
            out_file_name = str(prefix)+i
            #Create the outfile using the name provided by user
            out_file = open(out_file_name, "w+")
            #read the file
            os.chdir(folder)
            file = open(i)
            #check point for name of seq
            for j in file:
                out_file.write(j)
            #always close a file when you are done
            file.close()
            #close the outfile we created
            out_file.close()
    messagebox.showinfo("Complete", "Your Prefix is Complete :)\nName of Folder:  "+prefix)

def change_f_type(starting_file_type, ending_file_type):
    '''Change File Type (Note: does not change format)'''
    folder = filedialog.askdirectory()
    #change the directory to said folder
    os.chdir(folder)
    #list the files in said folder
    ls = os.listdir()
    os.mkdir(ending_file_type[1:])
    pf = folder+'/'+ending_file_type[1:]
    for i in ls:
        #observe only the .nt files of interest
        if str(starting_file_type) in i:
            os.chdir(pf)
            #Get the folder of interest entered by the user
            out_file_name = str(i[:-len(starting_file_type)])+ending_file_type
            #Create the outfile using the name provided by user
            out_file = open(out_file_name, "w+")
            #read the file
            os.chdir(folder)
            file = open(i)
            for j in file:
                out_file.write(j)
            #always close a file when you are done
            file.close()
            #close the outfile we created
            out_file.close()
    messagebox.showinfo("Complete", "Your File Type Change is Complete :)\nName of Folder:  "+ ending_file_type[1:])

def multifasta_map_name(df, c1_file_names, c2_change_to_names, lg_out_file_name = 'A_Name_Change_Multifasta', file_type = '.fasta', change_contig_name =True):
    '''Change file name to dif name and concatinate'''
    folder = filedialog.askdirectory()
    #change the directory to said folder
    os.chdir(folder)
    #list the files in said folder
    ls = os.listdir()
    lg = open(lg_out_file_name+file_type, "w+")
    os.mkdir('Name_Change')
    pf = folder+'/'+'Name_Change'
    first = True
    for i in ls:
        #observe only the .nt files of interest
        if str(file_type) in i:
            #read the file
            os.chdir(folder)
            file = open(i)
            to = df.loc[df[c1_file_names]== i[:-len(file_type)]]
            to.reset_index(drop=True, inplace=True)
            #check point for name of seq
            os.chdir(pf)
            k = 0
            if len(to[c2_change_to_names]) == 1:
                out_file_name = str(to[c2_change_to_names][0])+file_type
                out_file = open(out_file_name, "w+")
                for j in file:
                    if k==0 and first == True:
                        out_file.write('>'+out_file_name[:-len(file_type)]+'\n')
                        lg.write('>'+out_file_name[:-len(file_type)]+'\n')
                        k+=1
                        first = False
                    elif k==0 and first == False:
                        out_file.write('>'+out_file_name[:-len(file_type)]+'\n')
                        lg.write('\n>'+out_file_name[:-len(file_type)]+'\n')
                        k+=1
                    else:
                        out_file.write(j)
                        lg.write(j)
                out_file.close()
            else:
                print('Error: '+str(i[:-len(file_type)])+' : '+str(len(to)))
    lg.close()
    messagebox.showinfo("Complete", "Your MultiFASTA is Complete :)\nFiles found in Name_Change Folder\nMultifasta = %s%s"%(lg_out_file_name, file_type))
