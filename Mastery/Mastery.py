"""
Review of what I know + Useful program
11/30/2014
"""
import time

def Facts():
    print("""
            How long will it take to master programming
            Popular belief is 10,000 hours
            Let's get an understanding of hours.""")
    print("\r\n")
    time.sleep(1)

    HourDay = 1 * 24
    HourWeek = HourDay * 7
    HourMonth = HourDay * 30
    HourYear = HourDay * 365
    Mastery = 10000 / 24

    print("There are", HourDay, "Hours in a day")
    print("There are", HourWeek, "Hours in a week")
    print("There are", HourMonth, "Hours in a 30 day month")
    print("There are", HourYear, "Hours in a 365 day year", "\r\n")
    print("Now we understand our time constraints")
    print("""If you studied 24 hours per day with no breaks
        it would take""", Mastery, "days to truly master programming.", "\r\n")

Facts()

def TenThousand():

    Days = 0
    ZeroHour = 0

    try:
        
        MyMastery = int(input("How many hours a day will you study? "))
        print("\r\n")

    except ValueError:
        print("Enter an integer buddy... ")
        TenThousand()

   

    else:
        if (MyMastery > 24 or MyMastery <= 0):
            print("Strong understanding of hours per day bro. ")
            TenThousand()

        else:
            print("OK.. so you will study ", MyMastery, "hours per day")

    while(ZeroHour <= 10000):
        ZeroHour += MyMastery
        Days += 1

        if (ZeroHour >= 10000):
            print("It will take you", Days, "Days to master this language.")
            print("\r\n")
            print("Yep, that's", Days/365, "years bb")
            print("That's", Days/30, "months bb")
            time.sleep(2)
            print("\r\n", "You can DO THIS BRUH")
            print("\r\n")
            time.sleep(2)
            Retry = str.upper(input("Would you like to retry? (Y/N): "))
            if (Retry == "Y"):
                TenThousand()
            else:
                quit()

TenThousand()




