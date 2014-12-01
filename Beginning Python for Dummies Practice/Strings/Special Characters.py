print("Part of this text\r\nis on the next line.")
print("This is an A with a grave accent: \xC0.")
print("This is a drawing character: \u2562.")
print("This is a pilcrow: \266.")
print("This is a division sign: \xF7.")

MyString = "Hello World"
print(MyString[0:12])

String1 = "Hello World"
String2 = "Python is Fun!"

print(String1[0])
print(String1[0:5])
print(String1[:5])
print(String1[6:])

String3 = String1[:6] + String2 [:6]
print(String3)

print(String2[:7]*5)
