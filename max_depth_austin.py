"""
>>> from DataStruct import TreeNode
>>> root = TreeNode(2)
>>> root.left = TreeNode(4)
>>> root.right = TreeNode(7)
>>> root.left.left = TreeNode(5)
>>> root.left.right = TreeNode(8)
>>> root.right.left = TreeNode(1)
>>> max_depth(root)
3
"""


def max_depth(root):
    """ Maximum Depth of Binary Tree """

    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    if root.left and root.right:
        return max(max_depth(root.left), max_depth(root.right)) + 1
    elif root.left:
        return max_depth(root.left) + 1
    else:
        return max_depth(root.right) + 1