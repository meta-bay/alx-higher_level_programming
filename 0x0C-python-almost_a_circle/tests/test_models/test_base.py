#!/usr/bin/python3
"""
    Test Base Class
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Inherits from TestCase to test Base """

    def test_id(self):
        """ test """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id2(self):
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id3(self):
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_rand(self):
        b4 = Base(24)
        self.assertEqual(b4.id, 24)


if __name__ == '__main__':
    unittest.main()
