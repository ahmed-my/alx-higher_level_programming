#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = list(a_dictionary.keys())

    for dictionary_value in key_list:
        if value == a_dictionary.get(dictionary_value):
            del a_dictionary[dictionary_value]

    return (a_dictionary)
