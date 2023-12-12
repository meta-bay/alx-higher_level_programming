#!/usr/bin/python3
'''
    Tests the base
'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    ''' Base Testing class '''

    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(25)
        self.b5 = Base()

    def testBase(self):
        '''Testing the base class'''
        id = self.b1.id
        self.assertEqual(id, 1)
        id = self.b2.id
        self.assertEqual(id, 2)
        id = self.b3.id
        self.assertEqual(id, 3)
        id = self.b4.id
        self.assertEqual(id, 25)
        id = self.b5.id
        self.assertEqual(id, 4)

    def tearDown(self):
        self.b1.id = None
        self.b2.id = None
        self.b3.id = None
        self.b4.id = None
        self.b5.id = None

if __name__ == '__main__':
    unittest.main()
