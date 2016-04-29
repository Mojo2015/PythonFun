class CustomValueError(ValueError):
    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}

try:
    raise CustomValueError("Value must be within 1 and 10.")
except CustomValueError as e:
    print("CustomValueError Exception!", e.strerror)


"""
The code begins by creating the CustomValueError class that uses the
ValueError exception class ass the starting point.

The __init__() function provides the means for creating a new instance of
that class. Think of the class as a blueprint and the instance as the building
created from the blueprint.

Notice that the strerror attribute has the value assigned directly to it,
but args receives it as an array. The args member normally contains
an array of all the exception values, so this is standard procedure, even
when args contains just one value as it does now.

The code for using the exception is considerably easier than modifying
ValueError directly. All you do is call raise with the name of the exception
and the arguments you want to pass, all on one line.
"""
    
