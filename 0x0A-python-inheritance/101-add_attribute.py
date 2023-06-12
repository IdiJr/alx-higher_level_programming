#!/usr/bin/python3
"""function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attribute, value):
    """ Adds a new attribute to an object if it's possible.
    Args:
        obj: The object to which the attribute should be added.
        attribute: The name of the attribute.
        value: The value of the attribute to be set.
    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
