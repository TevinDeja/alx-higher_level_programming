#!/usr/bin/python3
"""Defines a class Rectangle that inherits from a BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represent a rectangle from  BaseGeometry"""
    def __init__(self, width, height):
        """Intialize a new Rectangle"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
