#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """ all multiples of 2 in a list."""
    multiples = []
    length = len(my_list)
    for i in range(length):
        if my_list[i] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)
    return (multiples)
