
        ## Input CC Name
        CCompany = input("Enter credit card company: ")
        ## Input how much you owe
        DOutstanding = float(input("Type how much you owe: "))
        ## Time until paid off
        PaidFull = float(input("How many months do you want to take to pay it off:"))
        ## Define what the interest rate is
        Interest = float(input("What is the APR for the card: "))


## Converting Interest into a working number for equation
WorkableInterest = Interest/100
## determining the amount of interest applied monthly based on APR
MonthlyInterest = Interest/12
## getting the interest to add on top of the monthly amount.
NoInterestMonthly = DOutstanding / PaidFull 
## calculating interest on what you owe
AppliedInterest = DOutstanding*WorkableInterest
## calculate overall outstanding to then determine what monthly payment will be in order to pay off over time
MonthlyPayment = AppliedInterest/PaidFull + NoInterestMonthly


    ## Calculation of what the debt at a percentage will come out to over X amount of time.
    print(Interest ,"%", "on", DOutstanding, "Comes out to: $", AppliedInterest)
    ## Display what they would need to pay to have it paid off by the time they want
    print( "if you pay: $", MonthlyPayment, "a month you will have your debt paid off in",PaidFull,"Months")
