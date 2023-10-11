#!/usr/bin/python3
def number_keys(a_dictionary):
    number = 0
    number_of_keys = list(a_dictionary.keys())

    for i in number_of_keys:
        number += 1

    return (number)
