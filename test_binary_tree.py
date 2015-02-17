__author__ = 'aouyang1'


import unittest
from DataStruct import TreeNode


class TestTree(object):

    def test_binary_tree(self):

        root = TreeNode(7)
        root.left = TreeNode(4)
        root.right = TreeNode(6)


