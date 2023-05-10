#!/usr/bin/python3
def uppercase(str):
    c = list(str)
    for i in range(len(c)):
        if ord(c[i]) > 96 and ord(c[i]) < 123:
            c[i] = chr(ord(c[i]) - 32)
            print("{}".format(("").join(c)))
