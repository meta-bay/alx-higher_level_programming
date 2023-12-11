#!/usr/bin/python3
'''
    Test the rectangle class
'''
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    ''' Rectangle class testing class'''

    def setUp(self):
        ''' Set up'''
        Rectangle._Base__nb_objects = 0

    def test_rect(self):
        ''' test rectangle'''
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(20, 10)
        self.assertEqual(r2.id, 2)

    def test_something(self):
        ''' test something '''
        r3 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r3.id, 5)


if __name__ == '__main__':
    unittest.main()
