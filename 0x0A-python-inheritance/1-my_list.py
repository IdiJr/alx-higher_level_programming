#!/usr/bin/python3


class MyList(list):
    """Function that prints a sorted list"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
