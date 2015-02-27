"""
>>> from DataStruct import TreeNode
>>> root = TreeNode(2)
>>> root.left = TreeNode(4)
>>> root.right = TreeNode(7)
>>> root.left.left = TreeNode(5)
>>> root.left.right = TreeNode(8)
>>> root.right.left = TreeNode(1)
>>> has_path_sum(root, 22)
False
>>> has_path_sum(root, 10)
True
"""


def has_path_sum(root, sum):
    """ Path Sum """

    if not root:
        return False

    next_sum = sum - root.val
    if not root.left and not root.right:
        return sum-root.val == 0

    if root.left and root.right:
        return has_path_sum(root.left, next_sum) or \
               has_path_sum(root.right, next_sum)
    elif root.left:
        return has_path_sum(root.left, next_sum)
    else:
        return has_path_sum(root.right, next_sum)