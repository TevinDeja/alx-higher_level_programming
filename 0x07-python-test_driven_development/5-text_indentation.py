#!/usr/bin/python3
"""Defines a text-indentation function"""


def text_indentation(text):
    """Print text with 2 new lines after ., ? and :"""
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")
        
    for delim in ".?:":
        text = text.replace(delim, delim + "\n\n")
    print(text.strip(), end="")
