"""Practicing exception handling
11/30/2014
Beginning Programming With Python for Dummies
"""

##import sys #obtains code from another file#
##
##try:
##    File = open('myfile.txt')
##except IOError as e: #Trying to open nonexistent file generates an IOError exception#
##                print("Error opening file!\r\n" +
##                      "Error Number: {0}\r\n".format(e.errno) + #errno: Provides the operating system error number as an integer
##                      "Error Text: {0}".format(e.strerror)) #strerror: Contains the error information as a human readable string
##else:
##    print("File opened as expected.")
##    File.close();
##
##
###The as clause places the exception information into a variable, e; which is accessible for additional information
##    #The except block contains a print() call that formats the error information into an easily read error message
##    #if myfile.txt existed, the else clause would execute.

##import sys
##
##try:
##    File = open('myfile.txt')
##except IOError as e:
##    for Arg in e.args:
##        print(Arg)
##else:
##    print("File opened as expected.")
##    File.close();
##
###the args property always contains a list of the exception arguments in string format. You can
###use a simple for loop to print each of these arguments
##    #this method will not print the argument name, just the output information.
##

import sys

try:
    File = open('myfile.txt')
except IOError as e:
    for Entry in dir(e):
        if (not Entry.startswith("_")):
            try:
                print(Entry, " = ", e.__getattribute__(Entry))
            except AttributeError:
                print("Attribute ", Entry, " not accessible.")

else:
    print("File opened as expected.")
    File.close();

"""
In the above case you get a list of the attributes associated with the error argument using the dir() function.
The output of the dir() function is a list of strings containing the names of the attributes that you can print.
Only those arguments that don't start with an underscore(_) contain useful information about the exception.
"""

    
    
