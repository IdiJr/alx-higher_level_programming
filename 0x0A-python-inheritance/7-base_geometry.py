#!/usr/bin/python3
"""Defines the class BaseGeometry"""

class BaseGeometry:
    """Type class of BaseGeometry"""

    def area(self):
        """"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if the value is an int greater than 0
        Args:
            name: name of the value being checked
            value: value to be checked
        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
