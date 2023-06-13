#!/usr/bin/python3
"""Function that prints a sorted list"""

class MyList(list):
    """Represents a public instance of type list"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
