#!/usr/bin/python3
'''
    Test the rectangle class
'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_to_json_string_rectangle_type(self):
        ''' test to json string rectangle type '''
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rect_one_dict(self):
        ''' test to json string rectangle on dict'''
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_sq_two_dicts(self):
        ''' test to json string square two dictionaries'''
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)


if __name__ == '__main__':
    unittest.main()
