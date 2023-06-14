#!/usr/bin/python3
"""function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line
    containing a specific string.
    Args:
        filename: name of file to be appended to.
        search_string(str): the string to insert text after.
        new_string(str): the new string to be inserted into file.
    Return: writes to the specified file.
    """
    txt = ""
    with open(filename) as r:
        for line in r:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
