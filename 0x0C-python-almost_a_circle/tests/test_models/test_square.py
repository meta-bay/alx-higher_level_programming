#!/usr/bin/python3
"""
    Test Square
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test square """

    def setUp(self):
        """ test """
        Square._Base__nb_objects = 0

    def test_sq(self):
        """ test """
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_sq1(self):
        ''' a test'''
        s2 = Square(4, 4)
        self.assertEqual(s2.area(), 16)

    def test_sq2(self):
        ''' a test '''
        s3 = Square(4, 1, 4)
        self.assertEqual(s3.area(), 16)


if __name__ == '__main__':
    unittest.main()
