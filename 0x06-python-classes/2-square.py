#!/usr/bin/python3
'''square module'''

class Square:
    """Represent square with private size attribute
    
    Attributes:
        __size (int): size of the square
    
    """

    def __init__(self, size=0):
        """Initialize square with optional size
        
        Args:
            size (int, optional): size of square side. Defaults to 0.
        
        Raises:
            TypeError: If size is not int
            ValueError: If size is less than 0
         
        """
        self.__size = size
        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
