#!/usr/bin/python3
'''
    square testing module
'''
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    '''square test class'''

    def setUp(self):
        '''the setup'''
        Square._Base__nb_objects = 0

    def test_sq(self):
        '''the setup'''
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
