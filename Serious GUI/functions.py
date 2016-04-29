"""
###****functions.py -- Please run program from "gui.py"***####
First 100% Functional GUI
12/3/2014
Johamed 0.1 alpha
"""
from tkinter import *
import sys
from config import * #Need this for our global variables to work#

#Functions **PLEASE COPY TO A MODULE AND IMPORT LATER TO SAVE SPACE**
def mNew():
    messagebox.showinfo(title="Warning",message ="This user has come out of the closet, please upgrade to Chippendales 2.0")
    return
    #just a space filler

def mOpen(): # This function will open a file dialog box to choose a file
    filedialog.askopenfile() # filedialogbox.askopenfile will bring up a file menu, there are many args for this
    #this will bring up the dialog and select a file, but nothing is done with the file yet.
    return

def mRecent():
    messagebox.showinfo(title='Sup',message='sup')
    #space filler
    return

def mSave():
    messagebox.showinfo(title='Sup',message = 'This just does not do a thing yet bruh')
    #space filler
    return

def mSaveas():
    messagebox.showinfo(title='Sup',message = 'This just does not do a thing yet bruh')
    #space filler
    return

def mPrint():
    messagebox.showinfo(title='Sup',message = 'This just does not do a thing yet bruh')
    #space filler
    return

def mQuit():
    mExit = messagebox.askyesno(title='Quit',message = 'Are you sure?') #Must establish a variable for the boolean value (mExit)
    if mExit > 0: #The response is boolean, 0 is false 1 is true, if the user agrees it will return true to mExit and this will read true.
        mGui.destroy() #This will close the program IF the user clicks yes.
        return
