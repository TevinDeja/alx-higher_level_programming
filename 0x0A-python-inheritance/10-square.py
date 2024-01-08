#!/usr/bin/python3
"""Defines a Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represent a square"""
    def __init__(self, size):
        """Initialize a square"""
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
