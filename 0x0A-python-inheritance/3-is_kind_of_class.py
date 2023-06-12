#!/usr/bin/python3
"""Function that check the instance of th object"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of the object or  class.
    Args:
        Arg1: obj
        Arg2: a_class that matches the obj
    Return: True if isinstance of obj or False if not
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
