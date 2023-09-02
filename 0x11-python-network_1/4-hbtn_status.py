#!/usr/bin/python3
"""A python script that fetches https://alx-intranet.hbtn.io/status"""

import requests

if __name__ == '__main__':
    link = "https://intranet.hbtn.io/status"
    r = requests.get(link)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
