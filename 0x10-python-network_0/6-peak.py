#!/usr/bin/python3
"""program algorithm for list of integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    list_of_integers.sort(reverse=True)
    return list_of_integers[0]
