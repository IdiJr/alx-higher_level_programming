#!/usr/bin/python3
"""
Take in a URL, sends request to the URL to display the value of the
X-Request-Id variable found in the header of the response
"""

import sys
import urllib.request

if __name__ == '__main__':
    link = sys.argv[1]
    with urllib.request.urlopen(link) as response:
        print(dict(response.headers).get("X-Request-Id"))
