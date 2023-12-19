#!/usr/bin/python3
"""Defines a Square with private size and area method
"""

class Square:
    """Represents a square with private size
    
    Attributes:
        __size (int): The size of the square
        
    """

    def __init__(self, size=0):
        """Initializes a new Square
        
        Args:
            size (int, optional): The size of the square. Defaults to 0.
        
        Raises:
            TypeError: If size is not an int 
            ValueError: If size is less than 0
        
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
    def area(self):
        """Calculates the Square area
        
        Returns:
            The area of the square
        
        """
        return self.__size ** 2
