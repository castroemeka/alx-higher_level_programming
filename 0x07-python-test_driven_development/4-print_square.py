#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a square-printing function."""


def print_square(size):
    """Print a square with the # character.

    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
=======

#This code prints a square with "#"

def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for number in range(size):
        print(("#" * size + "\n") * size, end="")
print("\nCode developed by Castro")
>>>>>>> 3a2eaf8046d8ffb5d83c112dbc4ecb8cd4b3b32b
