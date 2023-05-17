#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    weight = 0
    n_weight = 0

    for tup in my_list:
        weight += tup[0] * tup[1]
        n_weight += tup[1]

    return (weight / n_weight)
