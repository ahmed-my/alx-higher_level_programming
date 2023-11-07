#!/usr/bin/python3
"""function defines for a text file-reading """


def read_file(filename=""):
    """display the contents of a UTF-8 text file to stdout."""
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
