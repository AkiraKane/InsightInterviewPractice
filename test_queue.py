__author__ = 'aouyang1'

import unittest
from DataStruct import QueueClass

# run nosetests in the terminal


class TestQueue(unittest.TestCase):

    def test_queue(self):
        q = QueueClass()

        q.enqueue(4)
        q.enqueue('dog')
        q.enqueue(True)
        self.assertEqual(q.size(), 3)
        self.assertEqual(q.is_empty(), False)
        q.enqueue(8.4)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.dequeue(), 'dog')
        self.assertEqual(q.size(), 2)
