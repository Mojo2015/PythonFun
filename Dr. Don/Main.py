"""
Doctor Don
For Mom
Version: 0.1.1 Alpha
Last Revision: 12/4/2014
"""

import time
import sys
import random
from tkinter import *
import os

#Set Variables#
curse = ("fuck","piss","asshole", "shit", "bitch", "pussy")
angerLevel = 0
sayInput = ("say", "repeat after me")

myChoice = ['this is random reply 1', 'this is random reply 2', 'this is random reply 3', 'this is random reply 4']

"""Define Functions""" 

#Curse quit
def rudeDoctor():
    
    global a1 #This is a global variable set below when the program runs, you have to call the variable THEN update it.
    a1 += 1 #Adds 1 to the variable a1 every time rudeDoctor() is run. 
    
    
    
    if a1 == 1: #Python see's this as a variable assignment within the context of this function
        print("I will not tolerate this type of language, third warning results in your castration.")
        nextQuestion()
    elif a1 == 2:
        print("This is your second warning, one more time and there will be consequences")
        
        nextQuestion()
    elif a1 == 3:
        print("You have been warned... Goodbye")
        mGui = Tk()
        mGui.call('wm', 'attributes', '.', '-topmost', '1')
        mGui.title("Scumbag!!!")
        photo = PhotoImage(file="rudeDoctor.gif")
        label = Label(mGui, image=photo).pack()
        
        mGui.mainloop()
                           
        time.sleep(1)
        quit()
    
    

#Opening Question - Should not repeat#

def openQuestion():
    
        Input_ = str.lower(input("Tell me all about your problems\n "))
        Output_ = Input_.replace("i'm" , "one is").replace("i am", "one is").replace("im", "one is").replace("i ", "one ")
    
    

        if any(Input_.find(s)>=0 for s in curse):
            rudeDoctor()
        elif Input_ == "quit":
            print("goodbye")
            time.sleep(1)
            quit()
        else:
            print("I understand", Name, "It is very hard when", Output_ +','+
                  "\n","Just remember to eat your banananananas!")
            print("What would you like to talk about?\n")


def nextQuestion():
    userQuit = ''
    while userQuit == "":
        Input_ = str.lower(input(""))
        Output_ = Input_.replace("i ", "one") and Input_.replace("i'm", "one is") and Input_.replace("i am", "one is") and Input_.replace("im", "one is")
        if any(Input_.find(s)>=0 for s in curse):
            
            rudeDoctor()
        elif any(Input_.find(s)>=0 for s in sayInput):
            sayCommand = (Input_.split(' ', 1))
            print(sayCommand[1])
                          
        elif Input_ == "quit":
            print("goodbye")
            time.sleep(1)
            quit()
        else:
            print("I see, well it is very difficult when", Output_ +',', random.choice(myChoice))
        
"""PROGRAM START"""
#Program starts below#

#Define User Name#
global Name
Name = str(input("What's your name!\n"))
global a1
a1 = 0
print("Hello", Name, "!")
print("My name is Dr. Don, I am here to help you.")

openQuestion()
nextQuestion()





