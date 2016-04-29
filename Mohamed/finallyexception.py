import sys

try:
    #raise ValueError
    print("Raising an exception.")
except ValueError:
    print("ValueError Exception!")
    sys.exit()
finally:
    print("Taking care of last minute details.")

print("This code will self destruct becuase you are a loser.")
