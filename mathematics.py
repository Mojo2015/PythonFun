#Listen here bitch
#I fux shit up with multiples and sheeit

X = 1
Y = 1
Range = int(input("How big you want your multiplication table to be bruh?"+
                  " Enter an integer: "))

print ('{:>4}'.format(' '), end= ' ')

for X in range (1, Range):
    print('{:>4}'.format(X), end=' ')

print()

for X in range(1, Range):
    print('{:>4}'.format(X), end=' ')
    while Y <= Range:
        print('{:>4}'.format(X * Y), end=' ')
        Y+=1
    print()
    Y=1

"""
You fuckin mirin brah?
Thats right sun
go back to SKEWL
"""

print("u mirin' brah?")

