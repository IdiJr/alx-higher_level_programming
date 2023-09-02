#!/usr/bin/python3
""" A python script that takes your GitHub
credentials (username and password) and uses
the GitHub API to display your id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ = '__main__':
    username = sys.argv[1]
    P_A_T = sys.argv[2]
    link = 'https://api.github.com/user'
    auth = HTTPBasicAuth(username, P_A_T)
    r = requests.get(link, auth=auth)
    print(r.json().get('id'))
