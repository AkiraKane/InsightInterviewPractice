__author__ = 'aouyang1'

import unittest
from Stack import Stack

# run nosetests in the terminal


class TestStack(unittest.TestCase):

    def test_stack(self):
        s = Stack()

        self.assertEqual(s.isEmpty(), True)
        s.push(4)
        s.push('dog')
        self.assertEqual(s.peek(), 'dog')
        s.push(True)
        self.assertEqual(s.size(), 3)
        self.assertEqual(s.isEmpty(), False)
        s.push(8.4)
        self.assertEqual(s.pop(), 8.4)
        self.assertEqual(s.pop(), True)
        self.assertEqual(s.size(), 2)
