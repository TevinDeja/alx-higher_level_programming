#!/usr/bin/python3
"""Defines a class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited instance of a class"""
    if isinstance(obj, a_class):
        return True
    try:
        return issubclass(type(obj), a_class)
    except TypeError:
        return False
