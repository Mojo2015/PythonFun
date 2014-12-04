##Example program -- Searching a string for a single keyword --
#If the user inputs any of the "Swear" words, the program will print
#"Quit Cursing!"
#Otherwise it will print "That sounds great!")

Swear = ("curse", "badword", "swear") 
Userinput = str.lower(input("Tell me about your day: "))

if any(Userinput.find(s)>=0 for s in Swear):
     print("Quit Cursing!")
else:
     print("That sounds great!")
