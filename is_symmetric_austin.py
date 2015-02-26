"""
>>> from DataStruct import TreeNode
>>> root = TreeNode(1)
>>> root.left = TreeNode(2)
>>> root.right = TreeNode(2)
>>> root.left.left = TreeNode(3)
>>> root.left.right = TreeNode(4)
>>> root.right.left = TreeNode(4)
>>> root.right.right = TreeNode(3)
>>> is_symmetric(root)
True
>>> root = TreeNode(1)
>>> root.left = TreeNode(2)
>>> root.right = TreeNode(2)
>>> root.left.right = TreeNode(3)
>>> root.right.right = TreeNode(3)
>>> is_symmetric(root)
False
"""


def is_symmetric(root):
    """ Symmetric Tree """

    def is_leaf(node):
        return node.left is None and node.right is None

    if not root or is_leaf(root):
        return True

    level = [root]
    while level:
        # fill next level and values of current level
        next_level = []
        node_val = []
        for node in level:
            if node.left:
                next_level.append(node.left)
                node_val.append(node.left.val)
            else:
                node_val.append(None)

            if node.right:
                next_level.append(node.right)
                node_val.append(node.right.val)
            else:
                node_val.append(None)

        #check if node_val list is symmetric
        for n_idx in range(len(node_val)/2):
            if node_val[n_idx] != node_val[len(node_val)-n_idx-1]:
                return False

        # clean level if all None
        level = next_level

    return True