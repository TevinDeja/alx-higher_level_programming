#!/usr/bin/python3
"""Defines an object attribute lookup function."""

def lookup(obj):
    """Return a list of an object's available attributes."""
    result = []
    for i in dir(obj):
        if not i.startswith('__'):
            result.append(i)
    return result
