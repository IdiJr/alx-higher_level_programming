#!/usr/bin/python3
"""function that checks if the object is an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):

    """function to check is obj is inherited in a class
    Args:
        Arg1: obj
        Arg2: a_class that matches the obj
    Return: True if obj is an instance of a class that inherited or False if not
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
