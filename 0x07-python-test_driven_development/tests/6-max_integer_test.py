#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''
        Unittest class
    '''
    def test_positives(self):
        self.assertEqual(max_integer([600, 2, 3, 4]), 600)

    def test_negatives(self):
        self.assertEqual(max_integer([-3, -10, -1]), -1)

    def test_negatives_positives(self):
        self.assertEqual(max_integer([1, -3, 6, -90]), 6)

    def test_zero(self):
        self.assertEqual(max_integer([0]), 0)


if __name__ == "__main__":
    unittest.main()
