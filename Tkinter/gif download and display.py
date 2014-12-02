import random
import urllib.request
import sys
from tkinter import *

    
def download_web_image(url):
    global name
    name = str(input("what do you want to name it? "))
    full_name = str(name) + ".gif" #str(name) will convert it to a string
    urllib.request.urlretrieve(url, full_name)
    return name

Define_URL = str(input("Paste the URL here: "))
download_web_image(Define_URL)

def my_gui():
    my_gui = Tk()
##    my_gui.geometry('800x600+450+300')

    photo = PhotoImage(file=str(name) + '.gif')
    label = Label(my_gui, image=photo)
    label.pack()

    my_gui.mainloop()

my_gui()








                 
