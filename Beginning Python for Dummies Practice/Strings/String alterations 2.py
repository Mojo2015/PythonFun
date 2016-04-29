#Special Characters 2#

MyString = "   Hello World   "

print(MyString.upper())
print(MyString.strip()) ##Will remove extra spaces used in your string
print(MyString.strip().center(21, "&"))
print(MyString.center(70, "*"))
print(MyString.isdigit())
print(MyString.istitle())
print(max(MyString))

print(MyString.split())
print(MyString.split()[0])
