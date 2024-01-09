#!/usr/bin/python3
"""Defines a text file-reading function"""


def append_write(="", text=""):
    """Appends a string at the end of a text file (UTF8) and returns
    number of characters added.

    If the file doesn’ exist, it should be created.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf8') as file:
        file.write(text)
        return len(text)
