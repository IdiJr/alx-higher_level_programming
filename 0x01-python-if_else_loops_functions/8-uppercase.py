#!/usr/bin/python3
def to_uper(chars):
    if ord(chars) >= 97 and ord(chars) <= 122:
        return (ord(chars) - 32)
    else:
        return ord(chars)

def uppercase(str):
    str_new = ""
    for chars in str:
        str_new += "%c" % to_uper(chars)
        print("{:s}".format(str_new))
