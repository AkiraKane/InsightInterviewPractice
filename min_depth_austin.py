"""
>>> from DataStruct import TreeNode
>>> root = TreeNode(2)
>>> root.left = TreeNode(4)
>>> root.right = TreeNode(7)
>>> root.left.left = TreeNode(5)
>>> root.left.right = TreeNode(8)
>>> min_depth(root)
2
"""


def min_depth(root):
    """ Minimum Depth of Binary Tree """

    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    if root.left and root.right:
        return min(min_depth(root.left), min_depth(root.right)) + 1
    elif root.left:
        return min_depth(root.left) + 1
    else:
        return min_depth(root.right) + 1