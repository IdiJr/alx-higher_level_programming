#!/usr/bin/python3
"""Function that checks if the object is
exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """function to check is obj is the same class
    Arguments:
        Arg1: obj
        Arg2: a_class that matches the obj
    Return:
    True for isinstance of obj or False if not
    """

    if type(obj) == a_class:
        return True
    else:
        return False
