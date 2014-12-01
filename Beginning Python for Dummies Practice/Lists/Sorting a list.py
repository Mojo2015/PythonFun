Colors = ["Red", "Orange", "Yellow", "Green", "Blue"] #Creates a list to the variable Color

for Item in Colors: 
    print(Item, end=" ") #This will print the list in the order they occur, end=" " makes sure the list prints to one line

print()

Colors.sort() #Simple, sorts the list in alphabetical order
Colors.reverse() #This will sort them in reverse alphabetical order, you need the sort command above it first

for Item in Colors:
    print(Item, end=" ") #The items will be in order.

print()
