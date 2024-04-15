<<<<<<< HEAD
#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
=======
s function prints a text with 2 new lines after each of these characters: '.' ',' '?' and ':'

def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    variable = 0
    for letter in text:
        if variable == 0:
            if text == " ":
                continue
            else:
                variable = 1
        if variable == 1:
            if letter == "?" or letter == "." or letter == ":":
                print(letter)
                print()
                variable = 0
            else:
                print(letter, end="")
print("\nCode developed by Castro")
>>>>>>> 3a2eaf8046d8ffb5d83c112dbc4ecb8cd4b3b32b
