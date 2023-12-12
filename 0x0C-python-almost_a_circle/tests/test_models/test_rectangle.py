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
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3, 4, 5)
        r3 = Rectangle(2, 1)
        r4 = Rectangle(5, 6, 7, 8, 9)
        r5 = Rectangle(2, 1, 1, 1)
        r6 = Rectangle(3, 4, 5)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 5)

        with self.assertRaises(TypeError):
            Rectangle("five", 5)
        with self.assertRaises(TypeError):
            Rectangle([10], 2)
        with self.assertRaises(TypeError):
            Rectangle((1, 2), 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, [3])
        with self.assertRaises(TypeError):
            Rectangle(1, 2, (3, 4))
        with self.assertRaises(TypeError):
            Rectangle(1, 2, {})
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3.5)
        with self.assertRaises(TypeError):
            Rectangle({}, 5)
        with self.assertRaises(TypeError):
            Rectangle(1.5, 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, '4')
        with self.assertRaises(TypeError):
            Rectangle(1, 3, 4, [5])
        with self.assertRaises(TypeError):
            Rectangle(1, 3, 4, (5, 2))
        with self.assertRaises(TypeError):
            Rectangle(1, 5, 6, {})
        with self.assertRaises(TypeError):
            Rectangle(1, 5, 6, 7.5)
        with self.assertRaises(TypeError):
            Rectangle(106, '3')
        with self.assertRaises(TypeError):
            Rectangle(1, [2])
        with self.assertRaises(TypeError):
            Rectangle(1, (2, 3))
        with self.assertRaises(TypeError):
            Rectangle(1, {})
        with self.assertRaises(TypeError):
            Rectangle(1, 2.5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, '3')

    def test_something(self):
        ''' test something '''
        r3 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r3.id, 5)


if __name__ == '__main__':
    unittest.main()
