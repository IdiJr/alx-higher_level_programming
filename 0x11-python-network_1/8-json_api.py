#!/usr/bin/python3
"""
A python script that takes in a letter and send a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        letter = ""
    else:
        letter = sys.argv[1]
    payload = {"q": letter}
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if not response:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
