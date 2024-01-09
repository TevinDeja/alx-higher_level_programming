#!/usr/bin/python3
"""Defines a text file-reading function"""


def read_file(filename=""):
    """Open the file in read mode and UTF-8 encoding"""
    with open(filename, 'r', encoding='utf-8') as f:
        contents = f.read()
        print(contents)
