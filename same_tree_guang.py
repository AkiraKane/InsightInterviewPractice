# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        # first two levels edge cases
        if p is None and q is None:
            return True
        if (p is None) is (q is not None):
            return False

        # check base structure is same
        if (p.left is None) is (q.left is not None):
            return False
        if (p.right is None) is (q.right is not None):
            return False

        # check current node values
        if p.val != q.val:
            return False

        # base case
        if p.left is None and p.right is None:
            return True

        # other cases
        elif p.left is None:
            return self.isSameTree(p.right, q.right)

        elif p.right is None:
            return self.isSameTree(p.left, q.left)
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
