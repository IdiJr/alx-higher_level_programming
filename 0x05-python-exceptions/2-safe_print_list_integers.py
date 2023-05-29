#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    try:
        for index in my_list[:x]:
            if isinstance(index, int):
                print("{:d}".format(index), end="")
                printed += 1
        print()
    except (ValueError, TypeError):
        pass

    return (printed)
