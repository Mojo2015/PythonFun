#ForElse multiplication table##

X = 1
Y = 1

print ('{:>4}'.format(' '), end= ' ')

for X in range(1, 11):
    print('{:>4}'.format(X), end=' ')

print()

for X in range(1, 11):
    print('{:>4}'.format(X), end=' ')
    while Y <= 10:
        print('{:>4}'.format(X * Y), end=' ')
        Y+=1
    print()
    Y=1
