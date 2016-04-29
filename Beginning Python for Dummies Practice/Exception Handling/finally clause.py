import sys

try:
    raise ValueError #forces an exception for our purpose#
#if you comment out raise ValueError, the finally clause will
##still run but the program won't crash.

    print("Raising an exception.")
except ValueError: #what to do when the exception arises
    print("ValueError Exception!")
    sys.exit() #application will exit after exception is handled
finally: #This will always execute whether the the exception happens or not
    print("Taking care of the last minute details.")

print("This code will never execute because the program stopped.")
