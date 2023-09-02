#!/usr/bin/python3
"""
Takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally
displays the body of the response.
"""

import sys
import requests

if __name__ == '__main__':
    link = sys.argv[1]
    mail = {'email': sys.argv[2]}
    data = mail
    r = requests.post(link, data)
    print(r.text)
