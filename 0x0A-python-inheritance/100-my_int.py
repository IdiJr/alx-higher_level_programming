#!/usr/bin/python3
"""Defines a class that inherits from an int"""


class MyInt(int):
    """Represents a class that inherits from int and overrides the operators"""

    def __eq__(self, other):
        """Overrides the == operator"""
        return self.real != other

    def __ne__(self, other):
        """Overrides the != operator"""
        return self.real == other
