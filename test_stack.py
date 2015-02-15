__author__ = 'aouyang1'

import unittest
from DataStruct import StackClass, sort_stack

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

    def test_min(self):
        s = StackClass()
        num_list = [1, 2, 3, 4, 5]
        for val in num_list:
            s.push(val)

        self.assertEqual(s.min(), 1)

        s = StackClass()
        num_list = [5, 4, 3, 2, 1, 2, 3, 4, 5]
        for val in num_list:
            s.push(val)

        self.assertEqual(s.min(), 1)

        s.pop()
        self.assertEqual(s.min(), 1)

        s.pop()
        self.assertEqual(s.min(), 1)

        s.pop()
        self.assertEqual(s.min(), 1)

        s.pop()
        self.assertEqual(s.min(), 1)

        s.pop()
        self.assertEqual(s.min(), 2)

        s.pop()
        self.assertEqual(s.min(), 3)

    def test_sort_stack(self):
        s1 = StackClass()
        num_list = [5, 7, 2, 4, 9, 1, 3, 6]
        for val in num_list:
            s1.push(val)

        s1 = sort_stack(s1=s1)

        num_list = sorted(num_list, reverse=True)

        for val in num_list:
            self.assertEqual(s1.pop(), val)
