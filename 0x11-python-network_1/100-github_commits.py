#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails”
"""

import sys
import requests

if __name__ == '__main__':
    repository_name = sys.argv[1]
    user_name = sys.argv[2]
    link = "https://api.github.com/repos/{}/{}/commits".format(
        user_name, repository_name)
    r = requests.get(link)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
