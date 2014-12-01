"""
This will be the headquarters program where we can select modules
for many of the other apps we make
now that we are leet as fuuu
Created by: Jomomo
Date: 11/30/2014
Purpose: To rule the universe
"""

import time

Name = str(input("What's your name? "))
time.sleep(1)
print("\r\n")
print("Oh hey what's up, ", Name,"? What would you like to do today?", "\r\n")
time.sleep(1)

print("1. How long will it take me to master Python?")

def Selection():

    try:
        MainSelect = int(input("\r\n Enter a number: "))


    except ValueError:
        print("You have to enter an integer")
        Selection()

    else:
        print("You have selected", MainSelect)

        if (MainSelect == 1):
            import Mastery
            Facts()

Selection()


