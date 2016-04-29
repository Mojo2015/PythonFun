TryAgain = True

while TryAgain:

    try:
        Value = int(input("Type a whole number. "))
    except ValueError:
        print("You must type a whole number!")

        try:
            DoOver = input("Try again (y/n)? ")
        except:
            print("OK, Go screw yourself!")
            TryAgain = False
        else:
            if (str.upper(DoOver) == "N"):
                TryAgain = False

    except KeyboardInterrupt:
        print("You pressed CTRL+C!")
        print("GO to hell and DIE!")
        TryAgain = False
    else:
        print(Value)
        TryAgain = False
