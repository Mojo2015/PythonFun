###continue Clause example###

#assigning a variable, I believe LetterNum is a built in feature, I
#am struggling to understand how it works.

import time

def Repeat():
    print("\n")
    print ("Want to play again bro? Yes or No")
    print ("\n")
    Retry = str.lower(input("Yes or No: "))

    if (Retry == "yes"):
        Gaines()
    else:
        print ("Whatever beta, kill yourself")

def Gaines():
    
    LetterNum = 1
    BadLetter = 0
    



    InputData = str.lower(input("Enter some information here bro: "))

    for Letter in InputData:
        if Letter == "w":
            BadLetter += 1
            continue
            print("Encountered w, not processed.")
        print ("Letter ", LetterNum, " is ", Letter)
        LetterNum += 1

    print("Also, there were", BadLetter, "unacceptable Letters")

    if (BadLetter >= 5):
        print("Kill yourself.. immediately")
        time.sleep(2)
        print("\n")
        print("alright have a nice day")

    Repeat()

Gaines()




        
