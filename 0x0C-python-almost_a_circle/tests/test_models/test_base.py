#!/usr/bin/python3
'''
    Tests the base
'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    ''' Base Testing class '''

    def test_id(self):
        ''' Test id 1'''
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id2(self):
        ''' test id 2'''
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id3(self):
        ''' test id 3'''
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_rand(self):
        ''' test random id'''
        b4 = Base(24)
        self.assertEqual(b4.id, 24)


if __name__ == '__main__':
    unittest.main()
