One = int(input("Type a number between 1 and 10: "))
Two = int(input("Type a number between 1 and 10: "))

if (One >= 1) and (One <= 10) :
    if(Two >= 1) and (Two <=10) :
        print("Your secret number is: ", One * Two)
    else:
        print("Incorrect second Value!")
else:
    print("Incorrect first value!")
