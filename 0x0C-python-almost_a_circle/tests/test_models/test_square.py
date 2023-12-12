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
    def test_rect(self):
        ''' test Square'''
        r1 = Square(1, 2)
        r2 = Square(1, 2, 4, 5)
        r3 = Square(2, 1)
        r4 = Square(5, 6, 8, 9)
        r5 = Square(2, 1, 1, 1)
        r6 = Square(3, 4, 5)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 5)

        with self.assertRaises(TypeError):
            Square("five", 5)
        with self.assertRaises(TypeError):
            Square([10], 2)
        with self.assertRaises(TypeError):
            Square((1, 2), 5)
        with self.assertRaises(TypeError):
            Square(1, 2, [3])
        with self.assertRaises(TypeError):
            Square(1, 2, (3, 4))
        with self.assertRaises(TypeError):
            Square(1, 2, {})
        with self.assertRaises(TypeError):
            Square(1, 2, 3.5)
        with self.assertRaises(TypeError):
            Square({}, 5)
        with self.assertRaises(TypeError):
            Square(106, '3')
        with self.assertRaises(TypeError):
            Square(1, [2])
        with self.assertRaises(TypeError):
            Square(1, (2, 3))
        with self.assertRaises(TypeError):
            Square(1, {})
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(TypeError):
            Square(1, 2.5)
        with self.assertRaises(TypeError):
            Square(1, 2, '3')

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
