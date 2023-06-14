#!/usr/bin/python3
"""function that returns an object represented by JSON"""
import json


def from_json_string(my_str):
    """function to create the python obj reprented by JSON string
    Arg my_str: object to be converted from JSON
    Return: python obj representation
    """
    return json.loads(my_str)
