#!/usr/bin/python3
"""
Takes in the URL, sends a request to the URL and displays the body
of the response (decoded in utf-8)
"""
import sys
import urllib.error
import urllib.request

if __name__ == '__main__':
    link = sys.argv[1]
    try:
        with urllib.request.urlopen(link) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
