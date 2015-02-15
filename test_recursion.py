__author__ = 'aouyang1'

import unittest
import RecursionClass as rc

# run nosetests in the terminal


class TestRecursion(unittest.TestCase):

    def test_listsum(self):
        self.assertEqual(rc.listsum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(rc.listsum([]), 0)

    def test_tostring(self):
        self.assertEqual(rc.tostring(9876543210), "9876543210")
        self.assertEqual(rc.tostring(0), "0")