#!/usr/bin/python3
"""square class"""


class Square:
    """defines the square"""

    def __init__(self, size=0):
        """Initializes a new square
        Args:
            size: The size the square
        """
        self.size = size

    @property
    def size(self):
        """gets the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square with '#' """
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
