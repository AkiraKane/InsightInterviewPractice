"""
>>> from DataStruct import TreeNode
>>> root = TreeNode(1)
>>> root.left = TreeNode(2)
>>> level_order(root)
[[1], [2]]
"""


def level_order(root):
    """ Binary Tree Level Order Traversal """

    if root is None:
        return []

    level_list = []
    level = [root]
    while level:
        temp_level = []
        next_level = []
        for node in level:
            temp_level.append(node.val)
            if node.left:
                next_level.append(node.left)

            if node.right:
                next_level.append(node.right)

        level_list.append(temp_level)
        level = next_level

    return level_list