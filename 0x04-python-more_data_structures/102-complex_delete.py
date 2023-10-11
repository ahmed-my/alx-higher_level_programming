#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = list(a_dictionary.keys())

    for value in key_list:
        if value == a_dictionary.get(value):
            del a_dictionary[value]

    return (a_dictionary)
