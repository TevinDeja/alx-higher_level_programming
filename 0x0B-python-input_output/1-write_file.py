#!/usr/bin/python3
"""Defines a text file-reading function"""


def write_file(filename="", text=""):
        """Writes a string to a text file (UTF8) and the number of characters
        Args:
            filename (str): The name of the file to write to.
            text (str): The text to write to the file.
        Returns:
               int: The number of characters written to the file.
        """
        with open(filename, 'w', encoding='utf8') as f:
        chars_written = f.write(text)
        return chars_written
