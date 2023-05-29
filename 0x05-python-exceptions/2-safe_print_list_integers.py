#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    try:
        for index in my_lis[:x]:
            if isinstance(item, int):
                print("{:d}".format(index), end="")
                printed += 1
                print()
        except (TypeError):
            pass

        return (printed)
