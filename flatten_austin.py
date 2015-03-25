"""
>>> from DataStruct import TreeNode
>>> root = TreeNode(1)
>>> root.left = TreeNode(2)
>>> root.left.left = TreeNode(3)
>>> root.left.right = TreeNode(4)
>>> root.right = TreeNode(5)
>>> root.right.right = TreeNode(6)
>>> flatten(root)
>>> print root.val, root.right.val, root.right.right.val, root.right.right.right.val, root.right.right.right.right.val, root.right.right.right.right.right.val, root.right.right.right.right.right.right
1 2 3 4 5 6 None
"""


def append_right(root):
    temp_right = root.right
    root.right = root.left
    root.left = None
    tail = root.right
    while tail.right is not None:
        tail = tail.right

    tail.right = temp_right


def is_leaf(root):
    return not root.left and not root.right


def flatten(root):
    """ Flatten Binary Tree to Linked List """

    if not root or is_leaf(root):
        return

    if root.left:
        append_right(root)

    flatten(root.right)