#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """
        The constructor for the Square class.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        The size getter method.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        The size setter method.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        This method calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        This method prints the square in stdout with the character #.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print('#' * self.__size)
