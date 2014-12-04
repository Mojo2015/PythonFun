#Exception Handling 1#
#What's wrong with this code?#

def bacon():
    
    try:
        Value = int(input("Type a number between 1 and 10: "))

    except ValueError:
        print("You must type a number between 1 and 10!")
        bacon()
           
    else:

        if (Value > 0) and (Value <= 10):
            print("You typed: ", Value)
        else:
            print("The value you typed is wrongzo!")
            bacon()


###Program starts running here##
            
bacon() #Tells the program to start with the program you defined until it says
         #return

print("bacon() has completed")
