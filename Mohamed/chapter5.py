Python 3.3.4 (v3.3.4:7ff62415e426, Feb 10 2014, 18:13:51) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> myVar = 5
>>> myVar
5
>>> Text = 0b100
>>> test = 0b100
>>> test
4
>>> test = 0o100
>>> test
64
>>> test = 100
>>> test
100
>>> test
100
>>> text
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    text
NameError: name 'text' is not defined
>>> print(text)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(text)
NameError: name 'text' is not defined
>>> print(text,=)
SyntaxError: invalid syntax
>>> print(text,='penis')
SyntaxError: invalid syntax
>>> text
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    text
NameError: name 'text' is not defined
>>> Text
4
>>> bint(test)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    bint(test)
NameError: name 'bint' is not defined
>>> bin(test)
'0b1100100'
>>> bin(text)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    bin(text)
NameError: name 'text' is not defined
>>> bin(Text)
'0b100'
>>> hex(test)
'0x64'
>>> text = 0x100
>>> test
100
>>> text
256
>>> hex(text)
'0x100'
>>> myComplex = 3 + 4j
>>> myComplex.real
3.0
>>> myComplex.imag
4.0
>>> ord
<built-in function ord>
>>> ord(A"")
SyntaxError: invalid syntax
>>> ord("A")
65
>>> myInt = int("123")
>>> myInt
123
>>> type(,yInt)
SyntaxError: invalid syntax
>>> type(myInt)
<class 'int'>
>>> myStr = str(1234.56)
>>> myStr
'1234.56'
>>> type(myStr)
<class 'str'>
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2014, 11, 17, 23, 27, 15, 202966)
>>> str(datetime.datetime.no().date())
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    str(datetime.datetime.no().date())
AttributeError: type object 'datetime.datetime' has no attribute 'no'
>>> str(datetime.datetime.now().date())
'2014-11-17'
>>> 
