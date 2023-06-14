#!/usr/bin/python3
"""function that writes a file"""


def append_write(filename="", text=""):
    """function to count the number of characters
    Args:
        Arg filename: name of file
        Arg text: text to append
    Return: the number of characters added
    """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
