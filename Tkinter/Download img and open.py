#Paste an image url, name it, boom it opens!

import random
import urllib.request
import sys
import os
from tkinter import *
import webbrowser


    
def download_web_image(url):
    global name
    global full_name
    name = str(input("what do you want to name it? "))
    full_name = str(name) + "." + str(Define_URL[-3:]) #str(name) will convert it to a string
    urllib.request.urlretrieve(url, full_name)
    print(Define_URL[-3:])
    return name

global Define_URL
Define_URL = str(input("Paste the URL here: "))
download_web_image(Define_URL)

os.startfile(full_name)
import webbrowser
webbrowser.open(full_name)



##def my_gui():
##    my_gui = Tk()
####    my_gui.geometry('800x600+450+300')
##
##    photo = PhotoImage(file=str(full_name)) #+ '.gif')
##    label = Label(my_gui, image=photo)
##    label.pack()
##
##    my_gui.mainloop()
##
##my_gui()








                 
