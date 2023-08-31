#!/usr/bin/python3
"""
Module containing a function to find a peak in an unsorted list of integers.
"""


def find_peak(list_of_integers):
    """
        Find a peak in a list of unsorted integers.
        Args:
        list_of_integers (list): The list of unsorted integers.
        Returns:
        int: The peak element.
    """
    loi = list_of_integers
    if not loi:
        return None
    low, high = 0, len(loi) - 1
    while low < high:
        middle = (low + high) // 2
        if loi[middle] > loi[middle + 1]:
            high = middle
        else:
            low = middle + 1
    return loi[low]
