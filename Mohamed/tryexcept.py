#Exception Handling 1#


def bacon(): #Creating a function so i can make it restart if error
    
    try: #you have to start with try before anticipating an exception, try the following
        Value = int(input("Type a number between 1 and 10: "))

    except ValueError: #if above input has a value error (user inputs a string instead), error.
        print("You must type a number between 1 and 10!")
        bacon() #restarts the function
           
    else: #if no exception do the following

        if (Value > 0) and (Value <= 10): #if the number is between 1-10
            print("You typed: ", Value) #print this
        else:                           #otherwise
            print("The value you typed is wrongzo!") #print this and restart
            bacon()
 

###Program starts running here##
            
bacon() #Tells the program to start with the program you defined until it says
         #return

print("bacon() has completed")
