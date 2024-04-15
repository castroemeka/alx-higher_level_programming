#!/usr/bin/python3
<<<<<<< HEAD
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
=======

#This function adds two integers.

def add_integer(a, b = 98):
    #This prototype will return (a + b)
    #a and b must be typecasted into int before addition
    #if a or b or both is not int, raise a typeError
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
print("\nCode developed by Castro")
>>>>>>> 3a2eaf8046d8ffb5d83c112dbc4ecb8cd4b3b32b
