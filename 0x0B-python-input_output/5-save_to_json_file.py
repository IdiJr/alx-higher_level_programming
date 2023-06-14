#!/usr/bin/python3
"""function that writes an object using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes a python obj to a text file using JSON rep.
    Args:
        Arg my_obj: object to be converted from JSON.
        Arg filename: file to be written
    Return: writes the file
    """
    with open(filename, "w") as FILE:
        json.dump(my_obj, FILE)
