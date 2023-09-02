#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""

import sys
import requests

if __name__ == '__main__':
    link = sys.argv[1]
    r = requests.get(link)
    print(r.headers.get("X-Request-Id"))
