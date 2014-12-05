print("1. Red")
print("2. Orange")
print("3. Yellow")
print("4. Green")
print("5. Blue")
print("6. Purple")

Choice = int(input("Select your favorite color: "))
if (Choice == 1):
    print("You chose Red!")
elif(Choice == 2):
    print("You chose Orange!")
elif(Choice == 3 ):
    print("You chose Yellow!")
elif(Choice == 4):
    print("You chose Green!")
elif(Choice == 5 ):
    print("You chose Blue!")
elif(Choice == 6):
    print("You chose Purple!")
else:                       #defines that any other scenario will produce the following message
    print("You made an invalid choice!")
        
