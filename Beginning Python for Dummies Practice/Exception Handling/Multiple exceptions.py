"""
Handling multiple exceptions with a single except clause
11/30/14
Beginning python for dumbasses
"""

"""
#using a single except clause to handle multiple exceptions works
#only when a common source of action fulfills the needs of all the exception
#types. Otherwise you need to handle each exception individually.
"""

##try:
##    Value = int(input("Type a number between 1 and 10: "))
##except (ValueError, KeyboardInterrupt):
##    print("You must type a number between 1 and 10!")
##else:
##
##    if(Value > 0) and (Value <= 10):
##        print("You typed: ", Value)
##    else:
##        print("The value you typed is incorrect!")

try:
    Value1 = int(input("type the first number: "))
    Value2 = int(input("type the second number: "))
    Output = Value1 / Value2
except ValueError: #only integers will pass this
    print("You must type a whole number!")
except KeyboardInterrupt:
    print("You pressed Control+C")
except ArithmeticError: #If you divide by zero, you will get this error first
    #Because python will go in the order of your exceptions.
    print("an undefined math error occurred")
except ZeroDivisionError:
    print("Attempted to divide by zero")
else:
    print(Output)

    
