LetterNum = 1

Input = str.lower(input("What's up yo? "))
for Letter in Input:
    if Letter == "w":
        pass
        print ("Encountered w, not processed.")
    print("Letter ", LetterNum, " is ", Letter)
    LetterNum += 1

else:
    print("Wow, you're lots of fun.. phaggot...")
