#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of
the response (decoded in utf-8)
"""
import sys
import urllib.parse
import urllib.request

if __name__ == '__main__':
    link = sys.argv[1]
    mail = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(mail)
    data = data.encode('ascii')
    req = urllib.request.Request(link, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
