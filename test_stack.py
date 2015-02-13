__author__ = 'aouyang1'

import unittest
from DataStruct import StackClass

# run nosetests in the terminal


class TestStack(unittest.TestCase):

    def test_stack(self):
        s = StackClass()

        self.assertEqual(s.is_empty(), True)
        s.push(4)
        s.push('dog')
        self.assertEqual(s.peek(), 'dog')
        s.push(True)
        self.assertEqual(s.size(), 3)
        self.assertEqual(s.is_empty(), False)
        s.push(8.4)
        self.assertEqual(s.pop(), 8.4)
        self.assertEqual(s.pop(), True)
        self.assertEqual(s.size(), 2)
