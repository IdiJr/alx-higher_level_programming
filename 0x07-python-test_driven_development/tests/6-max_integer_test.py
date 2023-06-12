#!/usr/bin/python3
"""Unittest for max_integer([...]) 
"""
import unittest


max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class unittest for the max integer function"""


    def test_sorted_list(self):
        sorted_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(sorted_list), 4)

    def test_unsorted_list(self):
        unsorted_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(unsorted_list), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_first(self):
        max_first = [4, 1, 2, 3]
        self.assertEqual(max_integer(max_first), 4)

    def test_strings(self):
        self.assertEqual(max_integer("school"), "s")
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
