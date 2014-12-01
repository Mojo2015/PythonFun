"""
Nested exception handling
"""

TryAgain = True

while TryAgain:

    try:
        Value = int(input("Type a whole number. "))
    except ValueError:
        print("You must type a whole number!")

        try:
            DoOver - input("Try again (y/n)? ")
        except:
            print("OK, see you next time!")
            TryAgain = False
        else:
            if (str.upper(DoOver) == "N"):
                TryAgain = False

    except KeyboardInterrupt:
        print("You pressed Control+C!")
        print("See you next time!")
        TryAgain = False

    else:
        print(Value)
        TryAgain = False
            
