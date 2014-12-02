from tkinter import * #import all tkinter
root = Tk()     #creates instance (root window)
mylabel = Label(root,text="I am a label widget") #label widget. The first parameter defines root as parent container, second configures text.
mybutton = Button(root,text="I am a button") #same as mylabel, bound to root, text
mylabel.pack() #required to position the label and button widgts. Some sort of geometry management is required to display within window
mybutton.pack() #same as above comment
root.mainloop() #keeps window from terminating

#create a frame widget for placing menu
