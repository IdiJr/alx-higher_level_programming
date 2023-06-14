#!/usr/bin/python3
"""function that reads stdin line by line and computes metrics"""


if __name__ == "__main__":

    import sys

    size = 0
    status_codes = {}

try:
    counter = 0
    for line in sys.stdin:
        line = line.split()

        size += int(line[8])
        status_code = line[7]

        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1

        counter += 1

        if counter == 10:
            print("File size: {}".format(size))
            for code in sorted(status_codes.keys()):
                print("{}: {}".format(code, status_codes[code]))
            counter = 0

except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(size))
    for key in sorted(statuscd):
        print("{}: {}".format(key, statuscd[key]))
