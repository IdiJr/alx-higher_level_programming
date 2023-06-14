#!/usr/bin/python3
"""function that creates an obj from a JSON file"""
import json


def load_from_json_file(filename):
    """function to create a python obj from a JSON file
    Args:
        Arg filename: json file to create the obj from
    Return: create the obj from file
    """
    with open(filename) as f:
        return json.load(f)
