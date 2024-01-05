#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds 2 integers a and b.
    a and b must be integers or floats, otherwise raise a TypeError.
    a and b are first casted to integers if they are floats.
    Returns an integer: the addition of a and b.
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
