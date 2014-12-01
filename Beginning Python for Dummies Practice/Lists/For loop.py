##List1 = [0, 1, 2, 3, 4, 5]
##
##for Item in List1:
##    print(Item)

List2 = []
len(List2) #will count the amount of entries in the list
List2.append(1) #This will add an entry to the list
len(List2) #Will now contain 1 entry
List2[0] #Shows that the appended value is in the first position of the list
List2.insert(0,2) #insert requires 2 arguments: first is the index of the
#insertion (element 0), the second argument is the object to be inserted
#into that element (2).

List2

List3 = List2.copy() # Copies list 2 to list 3
List2.extend(List3) #Copies all elements of list 3 to the end of list 2 (consolidation)
List2 #List 2 will now contain the extended portion from list 3

List2.pop() #pop() always removes the end value from the list
List2.remove(1) #This will remove the item at element 1
List2.clear() #Erases every element from the list

len(List2) #Output should be 0 since you used clear()

