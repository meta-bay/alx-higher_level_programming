#!/usr/bin/python3
"""square class"""


class Square:
    """defines the square"""

    def __init__(self, size=0):
        """Initializes a new square
        Args:
            size: The size the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area"""
        return (self.__size * self.__size)
