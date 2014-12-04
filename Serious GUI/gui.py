"""
First 100% Functional GUI
12/3/2014
Johamed 0.1 alpha

"""

##NOTICE: ALL FUNCTIONS ARE DEFINED IN MODULE: function.py
from tkinter import * #Command to import Tkinter library, you can't build a GUI without this line
import sys
from functions import *
from config import *

#Window Specs
##mGui = Tk()           #Naming your GUI and defining it to use the function Tk()
mGui.geometry('500x800+450+300') # sets the window size, heightxwidth+distance from top down+distance from left to right
mGui.title('Johamed 0.1 Alpha') # Names the window

    
### The Following Section Creates The Window Menu ###

#Adding a top menu
menubar = Menu(mGui) # Defines and creates a Menu bar



#Adding File button
filemenu = Menu(menubar, tearoff = 0) #Creates a menubar. Tearoff = 0 gets rid of ability to break menu away as a separate window
filemenu.add_command(label = "New", command = mNew) #Adds a new object label to the filemenu bar
filemenu.add_command(label = "Open", command = mOpen) # Another object, "command" will make it run a function when clicked. mOpen is our function.
filemenu.add_command(label = "Recent Files",command = mRecent)
filemenu.add_separator() #Adds a space between these commands
filemenu.add_command(label = "Save", command = mSave)
filemenu.add_command(label = "Save As..", command = mSaveas)
filemenu.add_separator()
filemenu.add_command(label = "Print Window", command = mPrint)
filemenu.add_separator()
filemenu.add_command(label = "Close", command = mQuit)

#IMPORTANT: IN THE FOLLOWING LINE ALWAYS START WITH YOUR VARIABLE, menubar is the variable you defined above!!!###
menubar.add_cascade(label = 'File', menu = filemenu) #Adds the file option with a cascading dropdown with all of the above options

#Adding Edit Button
edit_menu = Menu(menubar, tearoff = 0) #Creates edit menu
edit_menu.add_command(label = 'Undo')
edit_menu.add_command(label = 'Redo')
edit_menu.add_command(label = 'Cut')
edit_menu.add_command(label = 'Copy')
edit_menu.add_command(label = 'Paste')
edit_menu.add_command(label = 'Select All')

menubar.add_cascade(label = 'Edit', menu = edit_menu) #Adds the Edit menu with a cascading dropdown, as you can see python will render them in order


#Adding Options Button
optionsmenu = Menu(menubar,tearoff = 0)
optionsmenu.add_command(label = 'Configure')
optionsmenu.add_checkbutton(label = 'Test')
menubar.add_cascade(label="Options",menu= optionsmenu)

#Displaying The Menu
mGui.config(menu = menubar) #Physically places the menu on the GUI

#Adding Help Button

#Adding Temporary Pic Of Beautiful Beast
photo = PhotoImage(file="gifhamed.gif") #Imports phoeo
label = Label(mGui, image=photo) #Photo must be placed inside a label.. unfortunately only gifs work until i figure out pillow
label.pack() #mashes the pic into the window










mGui.mainloop()       #This repeats the loop, in windows your window will execute and immediately close without this
