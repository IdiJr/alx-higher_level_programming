#!/usr/bin/python3
"""function that writes a string to a text file"""


def write_file(filename="", text=""):
    """function that counts characters
    Args:
        Arg filename: name of file
        Arg text: text to be counted
    Return: writes into the specified file
    """
    with open(filename, "w", encoding="UTF-8") as FILE:
        written_FILE = FILE.write(text)
        return (written_FILE)
