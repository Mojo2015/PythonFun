import sys
from tkinter import *
def function1():
    mlabel = Label(mGui,text='Hello World').pack
mGui = Tk()

mGui.geometry('450x450+500+300')#width,height,pixels from top left, pixels from top right
mGui.title('I Pwn All') #titles the window

mlabel2 = Label(text='Label')
mlabel2.pack
##mlabel = Label(text='Second Label',fg='white',bg = 'black').place(x=225,y=225) #places object based on coordinates

##mlabel = Label(text='Third Label',fg='white',bg = 'black').grid(row = 0, column = 0,sticky=W)

#places it on screen using a grid of rows and colums
#sticky=W is moving it to the left
#other wise it would center with the label below it

##mlabel = Label(text='Third Label again',fg='white',bg = 'black').grid(row = 1, column = 0)

#mybutton = Button(mGui,text = 'YES',command = function1).pack() #creates a button, can use grid or place for this as well
mGui.mainloop() 
