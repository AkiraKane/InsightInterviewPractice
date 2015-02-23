"""
>>> from DataStruct import TreeNode
>>> root = TreeNode(3)
>>> root.left = TreeNode(9)
>>> root.right = TreeNode(20, left=TreeNode(15), right=TreeNode(7))
>>> zigzag_level_order(root)
[[3], [20, 9], [15, 7]]
"""


def zigzag_level_order(root):
    """ Binary Tree Zigzag Level Order Traversal """

    if not root:
        return []

    # breadth first approach
    level_list = [root]
    tree_list = []
    scan_right = True
    while level_list:
        curr_level = []
        next_level = []

        for node in level_list:
            curr_level.append(node.val)
            if scan_right:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            else:
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)

        scan_right = not scan_right
        next_level.reverse()
        level_list = next_level
        tree_list.append(curr_level)

    return tree_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()