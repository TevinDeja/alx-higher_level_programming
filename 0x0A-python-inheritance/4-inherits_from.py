#!/usr/bin/python3
"""Defines an inherited class checking function"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class"""
    try:
        return issubclass(type(obj), a_class)
    except TypeError:
        return False
