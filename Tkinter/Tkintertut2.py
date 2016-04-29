import sys
from tkinter import *
from tkinter import colorchooser



###FUNCTIONS###

def function1():
    mtext = ment.get()#gets the value stored in ment
    mlabel = Label(mGui,text=mtext).pack()
    return

def mAbout(): #basic message box displaying text
    messagebox.showinfo(title="About",message="This is my about box bro!")
    return

def mQuit(): #Will open a dialog box, ask the user if they wish to quit, if yes is selected it destroys
    mExit = messagebox.askyesno(title="Quit",message="Do you want to quit?")
    if mExit > 0 : #The response is boolean, 0 and 1
        mGui.destroy()
        return

def mColor(): #will bring up a color panel for users to select a color
    mycolor = colorchooser.askcolor()
    mlabel4 = Label(mGui,text=mycolor).pack()
    return

def mOpen(): #This function will open a file dialog box to choose a file
    myopen = filedialog.askopenfile()
    mlabel5 = Label(mGui,text=myopen).pack() 
    return
    

###/FUNCTIONS###
    

mGui = Tk()
ment = StringVar() #ment defined, see mEntry function

mGui.geometry('500x800+450+300')
mGui.title('Sup Yo')

mlabel = Label(mGui,text='Labels yo').pack()
mbutton = Button(mGui,text = 'CLICK',command = function1, fg = 'red').pack()

mEntry = Entry(mGui,textvariable=ment).pack() #Whatever I enter will be stored in ment using textvariable


#Menu Construction

menubar = Menu(mGui) #creats menubar

filemenu = Menu(menubar,tearoff = 0) #creates a menu bar tearoff = 0 gets rid of the ability to break out the file menu
filemenu.add_command(label = "New") #objects to add to menu bar
filemenu.add_command(label = "Open",command = mOpen)
filemenu.add_command(label = "Save As..")
filemenu.add_command(label = "Color",command = mColor)
filemenu.add_command(label = "Close",command = mQuit)

menubar.add_cascade(label = 'File', menu = filemenu) #makes it cascade

#help menu all menus will go in order following your code, this will be to the right of filemenu
helpmenu = Menu(menubar,tearoff = 0)
helpmenu.add_command(label='help docs')
helpmenu.add_command(label='about',command = mAbout)
menubar.add_cascade(label="Help",menu=helpmenu)

mGui.config(menu = menubar) #places the menu

#setup menu

setupmenu = Menu(menubar,tearoff=0)
setupmenu.add_checkbutton(label = "Auto")
menubar.add_cascade(label="Setup",menu=setupmenu)

#Radio Buttons - Simply use the following, there is a bit of an issue with 3 of them being highlighted from the start
Radio_1 = Radiobutton(mGui,text="Option 1", value = 1, variable = 1).pack()#The variable = is a grouping
Radio_2 = Radiobutton(mGui,text="Option 2", value = 2, variable = 1).pack()#Any button variable = 1 will be grouped
Radio_3 = Radiobutton(mGui,text="Option 3", value = 3, variable = 1).pack()#any button variable = 2 will be grouped
Radio_4 = Radiobutton(mGui,text="Option 4", value = 4, variable = 2).pack()
Radio_5 = Radiobutton(mGui,text="Option 5", value = 5, variable = 2).pack()


#SPIN BOX

spinbox1 = Spinbox(mGui,from_=0,to=10,state=NORMAL).pack()     #A spin box is a value box that you can put a number in or select a number. from_=minimums,to=maximum
                                                                #State=NORMAL is not needed, that's default, DISABLED will gray it out.
                                                                #This is not the usual from statement, it's from_ 



#LIST BOX - Similar to spin box, holds a list of items you can choose from

listbox1 = Listbox(mGui)
listbox1.insert(1, "bacon sandwiches")
listbox1.insert(2, "python is leet")
listbox1.insert(3, "I like chinese food")
listbox1.insert(4, "Well that was fun.")
listbox1.pack()


# Slider - known as a scale in TKinter
##By default a scale will be vertical 0-100, orient = DIRECTION,
##length and width set the size of the slider
##sliderlength - sets the width of the actual slider
##from_ just as the spinbox, from_ sets the length of the scale from_ = min, to = max
###tickinterval = interval of numbering below the scale (run the program to see)
Slider_1 = Scale(mGui, orient = HORIZONTAL,length = 300, width = 20, sliderlength = 15, from_ = 0, to = 50, tickinterval = 5).pack()

# CANVAS - placing a canvas on the window; creating a frame within the window to draw in like paint

#Canvas will default to the background color of gray, make sure to use bg="color" - must use quotes unless using bg code.

##canvas_1 = Canvas(mGui,height = 300, width = 300, bg="white")
##canvas_1.create_line(0,0,300,300) #0,0 = top left, 300,300 = bottom right. will draw a diagonal line
##canvas_1.create_oval(50,200,200,250)

##canvas_1.pack() #Canvas can not be packed until all drawing code for it is inserted first.

"""Photo"""

photo = PhotoImage(file="troll.gif") ##photos must be placed inside a label
label = Label(mGui, image=photo)
label.pack()



mGui.mainloop() #Always at the end of the code, or else the window will close once it is executed

