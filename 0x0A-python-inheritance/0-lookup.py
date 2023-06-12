#!/usr/bin/python3


def lookup(obj):
    """
    Return: a list of attributes and methods of an object
    Args:
        obj: The object for which attributes and methods need to be looked up.

    """
    return (dir(obj))
