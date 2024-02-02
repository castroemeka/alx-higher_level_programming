#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
=======

#This code defines a funtion that prints: My name is <first name> <last name>

def say_my_name(first_name, last_name=""):
    #This prints a first name and a subsequent last name.
    # All arguments must be strings.
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print(f'My name is {first_name} {last_name}')
print('\nCode developed by Castro')
>>>>>>> 3a2eaf8046d8ffb5d83c112dbc4ecb8cd4b3b32b
