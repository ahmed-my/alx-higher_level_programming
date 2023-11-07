#!/usr/bin/python3
"""function that defines file-writing."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        file_data = f.write(text)
        return file_data
