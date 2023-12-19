#!/usr/bin/python3
"""Defines a class Square with size attribute
"""

class Square:
    """Represent a square with private size attribute

    Attributes:
        __size (int): The size of the square (instantiated)

    """

    def __init__(self, size):
        """
        Instantiate a Square with size

        Args:
            size (int): The size of the square

        Returns: None

        """
        self.__size = size
